#!/usr/bin/env python
import matplotlib.pyplot as plt
from graph import Greengraph
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description = "Generates a graph of the proportion of green pixels in a series of satellite images between two points")
    parser.add_argument('--from', '-f', dest='start', default='New York') # Python doesn't like 'arguments.from'
    parser.add_argument('--to','-t', default='Chicago')
    parser.add_argument('--steps','-s',default=20)
    parser.add_argument('--out','-o') # Not yet implemented
    arguments=parser.parse_args()
    mygraph=Greengraph(arguments.start,arguments.to) 
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    plt.show()

# mygraph=Greengraph('New York','Chicago')
# data = mygraph.green_between(20)
# plt.plot(data)
# plt.show()