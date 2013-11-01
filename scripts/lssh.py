#!/usr/bin/env python2
# encoding: utf-8

import sys
from getopt import getopt

import lfunctions


def is_unique(element, lst):
    if element in lst:
        return len(lst) == 1 
    return True

def parse_args(options, args):
    ### Filter wrong commands
    opt = ['-h', '-a', '-d', '-l']
    keys = [entry[0] for entry in options]

    if len(keys) > 0 and len(args) > 0:
        return False

    bo = is_unique('-h', keys) and is_unique('-l', keys)
    if not bo:
        return False

    if 0 != len(set(keys).difference(set(opt))):
        return False
    if len(list(set(keys))) != len(keys):
        return False

    ### Begin parsing
    for name, value in options:
        if name in ['-h']:
            result = lfunctions.help()
            return result
        elif name in ['-l']:
            result = lfunctions.list()
            return result
        elif name in ['-a']:
            result = lfunctions.add(value)
            return result
        elif name in ['-d']:
            result = lfunctions.delete(value)
            return result

    return True

def main():
    options, args = getopt(sys.argv[1:], 'hla:d:', [])
    
    result = parse_args(options, args)

    if result and len(args) == 1:
        lfunctions.connect(args[0])
    elif not result:
            print '$ Error! Please follow the help information.\n'
            lfunctions.help()

##################
if __name__ == '__main__':
    main()
