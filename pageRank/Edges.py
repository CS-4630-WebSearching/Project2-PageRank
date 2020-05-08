#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:30:36 2020

@author: federicowang

graph = defaultdict(list)
def addEdge(graph,u,v): 
    graph[u].append(v) 
  
# definition of function 
def generate_edges(graph): 
    edges = [] 
  
    # for each node in graph 
    for node in graph: 
          
        # for each neighbour node of a single node 
        for neighbour in graph[node]: 
              
            # if edge exists then append 
            edges.append((node, neighbour)) 
    return edges
"""
'''
with open("Data/0.txt", "r") as a_file:
    i = 0
    for line in a_file:
        i+=1
    print(i)
'''
'''
import os

def check_if_string_in_file(filename, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(filename, "r") as a_file:
        # Read all lines in the file one by one
        for line in a_file:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
            else:
                return False
    return False

for filename in os.listdir("Data"):
    if filename.endswith(".txt"): 
        filename = "Data/" + filename
        x = check_if_string_in_file(filename, "patrickarango")
        if x is True:
            print(x)
            print(filename)
            break
    else:
        continue

'''
import os

def getTuples(file_name, directory_name):
    List = []
    with open(file_name, "r") as a_file:
        i = 0
        for line in a_file:
            if i == 0:
                x = line.split()
                List.append(x[1])
                i += 1
            elif i == 1:
                i += 1
                continue
            else:
                List.append(line.rstrip())
    
    list_tuple = []
    for filename in os.listdir(directory_name):
        if filename.endswith(".txt"): 
            filename = directory_name + "/" + filename
            with open(filename, "r") as a_file:
                i = 0
                for line in a_file:
                    if i == 0:
                        x = line.split()
                        if x[1] not in List:
                            break
                        i += 1
                    elif i == 1:
                        i += 1
                        continue
                    else:
                        list_tuple.append((line.rstrip(), x[1]))
    
    return list_tuple

