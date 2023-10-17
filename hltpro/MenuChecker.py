#!/usr/bin/env python3

import os
import sys
import argparse
from MenuAnalyzer import MenuAnalyzer
from termcolor import colored

def get_parser():
    parser = argparse.ArgumentParser(description = "Argument parser for command line input options")
    parser.add_argument('menu', type = str, help = 'HLT menu location in ORCOFF') # HLT menu (name of ConfDB configuration)
    parser.add_argument("--menuType",   dest = "menuType",   type = str, default = None,              help = "Force a specific menu type", choices = ["collisions", "collisionsHI", "circulating", "cosmics"]) 
    parser.add_argument("--doAnalysis", dest = "doAnalysis", type = str, default = None, nargs = "*", help = "Specify a specific check to so (default: do all)") 
    #parser.add_argument("--verbose", "-v",  dest = "verbose",    action="store_true",                     help = "Verbose mode (print out ALL checks)") # FIXME: never used anywhere
    return parser

def main():
    # get options passed on the command line
    parser = get_parser()
    args = parser.parse_args()
    
    # run analyzer
    analyzer = MenuAnalyzer(args.menu, args.menuType)

    if not args.doAnalysis:
        analyzer.AddAllAnalyses()
    else:
        for a in args.doAnalysis: analyzer.AddAnalysis(a)
    analyzer.Analyze()

    # check the results
    if not analyzer.expressType=='':
        print("\nEXPRESS Reconstruction will be: %s" % analyzer.expressType)
    else:
        print("WARNING: Cannot determine express reconstruction")

    print("\n")
    failed=[]
    format = "ANALYSIS%26s  %s"
    pass_txt = colored("SUCCEEDED",'green')
    fail_txt = colored("FAILED",'red')
    for analysis,result in analyzer.Results.items():
        if isinstance(result,list): # list output
            if len(result) == 0:
                print(format % (analysis,pass_txt,))
            else:
                print(format % (analysis,fail_txt,))
                failed.append(analysis)
        else:
            if result==0:
                print(format % (analysis,pass_txt,))
            else:
                print(format % (analysis,fail_txt,))
                failed.append(analysis)

    if len(failed)!=0: print("\nLIST OF FAILED ANALYSES:")
    for analysis in failed:
        print(colored(analyzer.ProblemDescriptions[analysis]+":  ",'red'))
        for line in analyzer.Results[analysis]: print(colored(line,'yellow'))
        print("")

if __name__=='__main__':
    main()
