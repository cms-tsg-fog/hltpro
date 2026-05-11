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

def print_diff(diffs):
    for diff in diffs:
        print(diff["path"],diff["count1"],diff["count2"],diff["diff"],diff["rel_diff"])

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='compares two hilton rate outputs stripping versions')
    parser.add_argument('input1',help="rate input 1")
    parser.add_argument('input2',help="rate input 2")
    parser.add_argument('--max_delta',default=0,type=int,help="min diff to print")
    args = parser.parse_args()

    max_diff = args.max_delta
    
    rate_data1=make_rate_data(args.input1);
    rate_data2=make_rate_data(args.input2);

    diffs = []

    for path in rate_data1.keys():
        if path not in rate_data2.keys():
            print("path",path,"not in input2")
        else:
            if rate_data1[path][0] == rate_data1[path][1]: #unprescaled
                count1= int(rate_data1[path][2])  
                count2= int(rate_data2[path][2])
                nr_diff = count1-count2
                rel_diff = (count1-count2)/count2 if count2!=0 else None
                entry = {"path" : path,"count1": count1,"count2" : count2,"diff" : nr_diff,"rel_diff" :rel_diff}
                diffs.append(entry)
                if abs(nr_diff)>max_diff:
                    print("path",path,"miss match",rate_data1[path],rate_data2[path])
    
    for path in rate_data2.keys():
        if path not in rate_data1.keys():
            print("path",path,"not in input1")




    diffs.sort(key=lambda x : abs(x["diff"]))
      
