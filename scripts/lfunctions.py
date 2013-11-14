#!/usr/bin/env python2
# encoding: utf-8

import lconfig
import re
import os


def __buildcmd(ls):
    return 'sshpass -p%s ssh %s@%s'%(ls[4], ls[3], ls[0]) 

def help():
    try:
        fp = open(lconfig.HELPFILE, 'r')
        for line in fp.readlines():
            print line.strip()
        fp.close()
    except:
        return False

    return True

def list():
    # shortname hostname ip username password
    try:
        fp = open(lconfig.HOSTFILE, 'r')
    
        print '<IP>\t\t\t<Hostname>\t\t\t<ShortName>\t\t\t<Username>\t\t\t<Passwd>\n'

        cnt = 0
        sep = '\t\t\t'
        for line in fp.readlines():
            ls = line.strip().split(' ')
            if ls[0].strip()[0] == '#':
                continue

            print ls[0] + sep + ls[1] + sep + ls[2] + sep + ls[3] + sep + ls[4]
            cnt += 1
    
        print '======================='
        print '## Total:  %d records.'%cnt
        fp.close()
    except:
        return False

    return True

def add(value):
    # user:pwd@192.168.0.1:hostname:shortname
    # Check format
    re_ip = re.compile('((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))')
    re_name = re.compile('[a-z|A-Z|0-9|_|-|@|.]{3,16}')
    
    try:
        ls = value.split(':')
        ls[1:2] = ls[1].split('@')

        bo = re_ip.match(ls[2]) != None and \
            re_name.match(ls[1]) != None and \
            re_name.match(ls[3]) != None and \
            re_name.match(ls[4]) != None

        if not bo:
            return False
    except:
        return False

    fp = open(lconfig.HOSTFILE, 'r')

    for line in fp.readlines():
        ls = line.strip().split(' ')
        if ls[0].strip()[0] == '#' or line == '':
            continue
        
        if ls[0] == value or ls[1] == value or ls[2] == value:
            print 'There is duplicated hostsname or IP or shortname.\nWe suggest that the hostname / IP / shortname should be unique.'
            fp.close()
            return False

    fp.close()
    # Parse & Add
    try:
        os.system('mkdir -p ~/.lssh')
        fp = open(lconfig.HOSTFILE, 'a')

        content = ls[2] + ' ' + ls[3] + ' ' + ls[4] + ' ' + ls[0] + ' ' + ls[1] + '\n'

        fp.write(content)
        fp.close()
    except:
        return False

    print 'Add hosts successfully.'
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
    except:
        return False

    print 'Delete hosts successfully.'
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
    except:
        return False

    return True
