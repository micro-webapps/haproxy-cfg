#!/usr/bin/env python3

from __future__ import print_function
import sys
import os

from webconftests import runtests

class TestImplementation:
    def pre_start(self):
        os.chdir("webconftests")

    def skip_test(self, d):
        skipped = []
        skipped.append("002")
        skipped.append("003")
        skipped.append("004")
        skipped.append("005")
        skipped.append("008")
        skipped.append("012")
        skipped.append("013")
        skipped.append("014")
        skipped.append("015")
        skipped.append("018")
        skipped.append("019")
        skipped.append("020")

        return d in skipped

    def stop(self):
        os.system("rm -rf */certs")
        os.system("rm -rf __pycache__")

    def generate_cfg(self, d):
        cmd = 'export `cat {0}`; ../../haproxy-cfg {1} {2} --debug; diff -u ../results/{3}/webconf.result {4}/haproxy.conf'.format(d + "/test.env", d, d + "/haproxy.conf", d, d)
        return os.system(cmd)

    def start_server(self, d):
        os.system("killall haproxy >/dev/null 2>&1")
        os.system("haproxy -f " + d + "/haproxy.conf > ./" + d + "/haproxy.output 2>&1 &")

    def stop_server(self, d):
        os.system("killall haproxy >/dev/null 2>&1")

impl = TestImplementation()
runtests(impl)
