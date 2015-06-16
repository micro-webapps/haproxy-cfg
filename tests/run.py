#!/usr/bin/env python3

import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def runtest(d):
    print(bcolors.OKGREEN + "*** " + d + ": STARTING" + bcolors.ENDC)
    ret = os.system("rm -f ./" + d + "/*.conf")

    cmd = 'export `cat {0}`; ../haproxy-cfg {1} {2} --debug; diff -u {3}/webconf.result {4}/*.conf'.format(d + "/test.env", d, d + "/haproxy.conf", d, d)
    #print("Executing:", cmd)
    ret = os.system(cmd)
    if ret != 0:
        print(bcolors.FAIL + "*** " + d + ": FAILED" + bcolors.ENDC)
        if len(sys.argv) == 2:
            os.system("mv {0}/*.conf {1}/webconf.result ".format(d, d))
        else:
            sys.exit(1)
    else:
        print(bcolors.OKGREEN + "*** " + d + ": PASSED" + bcolors.ENDC)
        ret = os.system("rm -f ./" + d + "/*.conf")

tests = os.listdir(".")
tests.sort()
for d in tests:
    if os.path.isdir(d):
        runtest(d)
    