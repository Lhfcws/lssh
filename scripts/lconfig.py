#!/usr/bin/env python2
# encoding: utf-8

import commands

# Config
__root = commands.getstatusoutput('echo ~')
HELPFILE = __root[1] + '/.lssh/.help'
HOSTFILE = __root[1] + '/.lssh/hosts'
