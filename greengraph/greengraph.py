#!/usr/bin/env python
import matplotlib.pyplot as plt
from graph import Greengraph
from argparse import ArgumentParser

def runGreengraph():
    parser = ArgumentParser(description = "Generates a graph of the proportion of green pixels in a series of satellite images between two points")
    parser.add_argument('--from', dest='start', default='New York', help='Starting location, defaults to New York') # Python doesn't like 'arguments.from'
    parser.add_argument('--to', dest='end', default='Chicago', help='End location, defaults to Chicago')
    parser.add_argument('--steps', default=20, help='Number of steps between start and end locations, default 20')
    parser.add_argument('--out', help='Filename to save plot to. Displays plot on screen instead if not specified')
    parser.add_argument('--format', default=None, help='Optionally force an output format, overriding extension in --out')
    arguments=parser.parse_args()
    
    mygraph=Greengraph(arguments.start,arguments.end) 
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    
    if arguments.out:
        plt.savefig(arguments.out,format=arguments.format)
    else:
        plt.show()

if __name__ == "__main__":
    runGreengraph()