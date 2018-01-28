"""
dump_simulator.py

Generates a random string file of a specified length.

Usage:  python dump-simulator.py

Options:    --size  Size of resulting dump in Kb.  Default=100
            --out   Filename of resulting simulated dump file. Default=simulated.dump

"""

import sys
import os
import click
import string
import random

@click.command()
@click.option("--size", help="Size of resulting dump in Kb.", default='100')
@click.option("--out", help="Filename of resulting simulated dump file.", default='simulated.dump')
def execute(size, out):
    writeDump(createDump(size), out)

def writeDump(dumpContent, fileNameOut):
    outFile = open(fileNameOut, 'w')
    outFile.write(dumpContent)
    outFile.close()

def createDump(sizeInK):
    sizeInBytes=sizeInK * 1024
    return ''.join(random.choice(string.printable) for _ in range(sizeInBytes))

if __name__ == "__main__":
    execute()
