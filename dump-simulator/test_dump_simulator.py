"""
test_dump_simulator.py

Unit tests for dump-simulator.

Usage:  pytest
"""

#import dump-sumulator as dump
import tempfile
import dump_simulator
import string

def test_createDump():
    content = dump_simulator.createDump(1)
    assert len(content) == 1024

def test_writeDump():
    tFile = tempfile.NamedTemporaryFile()
    tFileName = tFile.name
    tFile.close()

    dump_simulator.writeDump('Hi There', tFileName)
    outFile = open(tFileName, 'r')
    content = outFile.read()
    outFile.close()

    assert 'Hi There' == content
