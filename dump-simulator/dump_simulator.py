"""
dump_simulator.py

Generates a random string file of a specified length and optionally cause exception.

Usage:  python dump-simulator.py

Options:    --size      Size of resulting dump in Kb.  Default=100
            --out       Filename of resulting simulated dump file. Default=simulated.dump
            --message   Exception message. No exception thrown if no message provided.

"""

import sys
import os
import click
import string
import random
import exceptions
import time

@click.command()
@click.option("--size", help="Size of resulting dump in Kb.", default='100')
@click.option("--out", help="Filename of resulting simulated dump file.", default='simulated.dump')
@click.option("--message", help="Exception message. No exception thrown if no message provided.", default=None)
@click.option("--delay", help="Delay in seconds before requested exception thrown", default='10')
def execute(size, out, message, delay):
    writeDump(createDump(int(size)), out)
    if message is not None:
        time.sleep(int(delay))
        raise exceptions.Exception(message)

def writeDump(dumpContent, fileNameOut):
    outFile = open(fileNameOut, 'w')
    outFile.write(dumpContent)
    outFile.close()

def createDump(sizeInK):
    sizeInBytes=sizeInK * 1024
    return ''.join(random.choice(string.printable) for _ in range(sizeInBytes))

if __name__ == "__main__":
    execute()
