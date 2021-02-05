### L1_prescale_xml2csv.py
# Author: Thiago R. F. P. Tomei
# Date: 2018-06-22
# Version: v2

# This script takes two XMLs as input: the RunSettings key (i.e. the L1 prescales)
# and the L1Menu. It outputs into stdout the same information as the XML but in CSV
# format. We pad out unused bits with empty names and columns of zeros.
# This can then be pasted back into the GoogleDocs for book-keeping.
# Mostly useful for when the L1 menu changes.
# The logic is: L1 Menu maps numbersToNames, RunSettings key maps namesToColumns
# Changed to be compatible with python3
# Now adding warnings in stderr for L1 bits missing either in the RunSeetings key
# or in the L1Menu XML itself.

from __future__ import print_function
import xml.etree.ElementTree as ET
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


L1PrescalesName = "90mbetastartL1.xml"
L1MenuName = "L1Menu_Special2018_v1_1_0-d1.xml"

numbersToNames = dict()
namesToColumns = dict()

# L1 Prescales
L1PrescalesTree = ET.parse(L1PrescalesName)
L1Prescales = L1PrescalesTree.getroot()
columnsrow = L1Prescales[0][1][0].text.split(",")
columnNames = [x.split(":")[1] for x in columnsrow[1:]]
nColumns = len(columnNames)
defaultColumn = int(L1Prescales[0][0].text)

# Using XPath, find everything named "row" in the tree
listOfPrescales = L1Prescales.findall(".//row")
for row in listOfPrescales:
    row2 = row.text.split(",")
    # We strip whitespace at the beginning and end of the bitName
    bitName = row2[0].strip()
    prescaleRow = [int(ps) for ps in row2[1:]]
    namesToColumns[bitName] = prescaleRow

# L1 Menu
L1MenuTree = ET.parse(L1MenuName)
L1Menu = L1MenuTree.getroot()
listOfAlgos = L1Menu.findall("algorithm")
for algo in listOfAlgos:
    bitNumber = int(algo.find("index").text)
    bitName = algo.find("name").text
    numbersToNames[bitNumber] = bitName

# We need to prepend the column names with a single quote to ensure that GoogleDocs
# doesn't transform strings like "2.0E34" into numbers...
maxAlgo = max(numbersToNames.keys())
print("Default" + "," + columnNames[defaultColumn])
print("Bit" + "," + "Algo name" + "," + (",".join(["'" + cn for cn in columnNames])))

# We print into stdout
for bit in range(0, maxAlgo + 1):
    if bit in numbersToNames.keys():  # This bit is defined in the L1 menu
        bitName = numbersToNames[bit]
        if bitName in namesToColumns:  # We have prescales for this bit
            prescaleRow = namesToColumns[bitName]
            del namesToColumns[bitName]
            print(
                str(bit)
                + ","
                + bitName
                + ","
                + (",".join([str(ps) for ps in prescaleRow]))
            )
        else:  # We don't have prescales for this bit. Put 0 for the time being
            eprint(
                bcolors.WARNING
                + bitName
                + bcolors.ENDC
                + " is not defined in the original XML"
            )
            print(str(bit) + "," + bitName + "," + (",".join(["0"] * nColumns)))
    else:  # L1 doesn't define this bit. Put 0
        print(str(bit) + "," + " " + "," + (",".join(["0"] * nColumns)))

# Let's see if there is some bit that we wanted to add, but couldn't
if namesToColumns:
    for bitName in namesToColumns:
        eprint(
            bcolors.FAIL + bitName + bcolors.ENDC + " was not found in the new L1 XML!"
        )
