#!/usr/bin/env python2
# encoding: utf-8

import os
import re

import lconfig


def __buildcmd(ls):
    port = "22"
    if len(ls) == 6:
        port = ls[5]
    cmd = 'sshpass -p%s ssh -p%s %s@%s' % (ls[4], port, ls[3], ls[0])
    print(cmd)
    return cmd


def help():
    try:
        fp = open(lconfig.HELPFILE, 'r')
        for line in fp.readlines():
            print(line.strip())
        fp.close()
    except Exception:
        return False

    return True


def list():
    # shortname hostname ip username password
    try:
        fp = open(lconfig.HOSTFILE, 'r')

        print('<IP>\t\t\t<Hostname>\t\t\t<ShortName>\t\t\t<Username>\t\t\t<Passwd>\t\t\t<Port>\n')

        cnt = 0
        sep = '\t\t\t'
        for line in fp.readlines():
            ls = line.strip().split(' ')
            if ls[0].strip()[0] == '#':
                continue

            out = ls[0] + sep + ls[1] + sep + ls[2] + sep + ls[3] + sep + ls[4]
            if len(ls) == 6:
                out = out + sep + ls[5]
            else:
                out = out + sep + "22"
            cnt += 1

        print('=======================')
        print('## Total:  %d records.' % cnt)
        fp.close()
    except Exception:
        return False

    return True


def add(value):
    # user:pwd@192.168.0.1:hostname:shortname:port
    # Check format
    re_ip = re.compile(
        '((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))')
    re_name = re.compile('[a-z|A-Z|0-9|_|-|@|.]{3,16}')

    try:
        ls = value.split(':')
        ls[1:2] = ls[1].split('@')

        bo = re_ip.match(ls[2]) is not None and \
             re_name.match(ls[1]) is not None and \
             re_name.match(ls[3]) is not None and \
             re_name.match(ls[4]) is not None

        if not bo:
            return False
    except Exception:
        return False

    fp = open(lconfig.HOSTFILE, 'r')

    for line in fp.readlines():
        ls = line.strip().split(' ')
        if ls[0].strip()[0] == '#' or line == '':
            continue

        if ls[0] == value or ls[1] == value or ls[2] == value:
            print(
                'There is duplicated hostsname or IP or shortname.\nWe suggest that the hostname / IP / shortname should be unique.')
            fp.close()
            return False

    fp.close()
    # Parse & Add
    port = "22"
    if len(ls) == 6:
        port = ls[5]
    try:
        os.system('mkdir -p ~/.lssh')
        fp = open(lconfig.HOSTFILE, 'a')

        content = ls[2] + ' ' + ls[3] + ' ' + ls[4] + ' ' + ls[0] + ' ' + ls[1] + ' ' + port + '\n'

        fp.write(content)
        fp.close()
    except Exception:
        return False

    print('Add hosts successfully.')
    return True


def delete(value):
    try:
        fp = open(lconfig.HOSTFILE, 'r')

        ans = []
        for line in fp.readlines():
            ls = line.strip().split(' ')
            if ls[0].strip()[0] == '#' or line == '':
                continue

            if ls[0] == value or ls[1] == value or ls[2] == value:
                continue

            ans.append(line.strip())

        fp.close()
        ############
        fp = open(lconfig.HOSTFILE, 'w')

        for line in ans:
            fp.write(line + '\n')

        fp.close()
    except Exception:
        return False

    print('Delete hosts successfully.')
    return True


def connect(value):
    try:
        fp = open(lconfig.HOSTFILE, 'r')

        for line in fp.readlines():
            ls = line.strip().split(' ')
            if ls[0].strip()[0] == '#' or line == '':
                continue

            if ls[0] == value or ls[1] == value or ls[2] == value:
                cmd = __buildcmd(ls)
                os.system(cmd)

        fp.close()
    except Exception:
        return False

    return True
