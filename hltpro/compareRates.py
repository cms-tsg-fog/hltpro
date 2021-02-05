#!/usr/bin/env python

import argparse

def rm_hlt_version(name):
    version_start = name.rfind("_v")
    if version_start == -1: 
        return name
    else:
        return name[:version_start+2] 


def make_rate_data(filename):
    rate_data = {}    
    with open(filename) as f:
        for line in f.readlines():
            line_split = line.split()
            if len(line_split)==4:
                rate_data[rm_hlt_version(line_split[0])]=line_split[1:]
    return rate_data

def main(args):
    
    rate_data1=make_rate_data(args.input1);
    rate_data2=make_rate_data(args.input2);

    for path in rate_data1.keys():
        if path not in rate_data2.keys():
            print "path",path,"not in input2"
        else:
            if rate_data1[path][0] == rate_data1[path][1]: #unprescaled
                if rate_data1[path][2] != rate_data2[path][2]:
                    print "path",path,"miss match",rate_data1[path],rate_data2[path]
    
    for path in rate_data2.keys():
        if path not in rate_data1.keys():
            print "path",path,"not in input1"



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='compares two hilton rate outputs stripping versions')
    parser.add_argument('input1',help="rate input 1")
    parser.add_argument('input2',help="rate input 2")
    args = parser.parse_args()
    main(args)

