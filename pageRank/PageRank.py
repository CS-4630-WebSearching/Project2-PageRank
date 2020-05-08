import os
import random
from operator import itemgetter
import networkx as nx
import csv
from Edges import getTuples

def pageRank(edges):
    # Create directed graph G from list of edges
    G = nx.DiGraph()
    G.add_edges_from(edges)
    nodes = list(G.nodes())

    # Choose random source node
    r = random.choice(nodes)

    # Initialize all pagerank values to 0
    dict_rw = {}
    for node in nodes:
        dict_rw.update({node : 0})
    
    # Increment source node's pagerank value
    dict_rw[r] += 1

    # Do 10000000 iterations
    for i in range(10000000):
        # Get list of successors of chosen node
        neighbor = list(G.successors(r))

        # If no successors, chose another random node from graph
        if (len(neighbor) == 0):
            r = random.choice(nodes)
            dict_rw[r] += 1
        # Choose random node from list of successors
        else:
            r = random.choice(neighbor)
            dict_rw[r] += 1

    return sorted(dict_rw.items(), key=itemgetter(1), reverse=True)


def writeToFile(values):
    with open('results.csv', mode='w', newline='') as csv_file:
        file_write = csv.writer(csv_file)
        file_write.writerow(['username', 'pagerank value'])

        for line in values:
            file_write.writerow([line[0], line[1]])
        
    print("results.csv created.")


edges = getTuples("Data\\0.txt", "Data")
values = pageRank(edges)
writeToFile(values)


