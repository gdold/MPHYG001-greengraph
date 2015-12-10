#!/usr/bin/env python
import matplotlib.pyplot as plt
from graph import Greengraph
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description = "Generates a graph of the proportion of green pixels in a series of satellite images between two points")
    parser.add_argument('--from', '-f', dest='start', required=True, help='Starting location') # Python doesn't like 'arguments.from'
    parser.add_argument('--to', '-t', required=True, help='End location')
    parser.add_argument('--steps', '-s', default=20, help='Number of steps between start and end locations')
    parser.add_argument('--out', '-o', help='Filename to save plot to. Displays plot on screen instead if not specified')
    parser.add_argument('--format', default=None, help='Optionally force an output format, overriding extension in --out')
    arguments=parser.parse_args()
    mygraph=Greengraph(arguments.start,arguments.to) 
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    if arguments.out:
        plt.savefig(arguments.out,format=arguments.format)
    else:
        plt.show()

# mygraph=Greengraph('New York','Chicago')
# data = mygraph.green_between(20)
# plt.plot(data)
# plt.show()