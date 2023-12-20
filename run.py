#!/usr/bin/env python3

import re
from argparse import ArgumentParser
from subprocess import Popen

RE_CMDLINE_APPEND = re.compile(r"-append '.+'")

def iter_lines(filename):
    with open(filename, "r") as fh:
        for line in fh:
            if line.startswith("#"):
                continue

            yield line.strip().strip("\\")

def print_wrap(txt):
    s = 0
    for e in range(0, len(txt), 120):
        e+=120
        print("{}{}".format(txt[s:e], "" if e >= len(txt) else "\\"))
        s = e


def main():
    parser = ArgumentParser()
    parser.add_argument("topology", help="The NUMA topology file to use")
    parser.add_argument("--script", default="qemu.sh", help="The QEMU script to run")
    parser.add_argument("--cmdline", default="", help="Extra cmdline arguments")

    args = parser.parse_args()

    topology_file = args.topology
    script_file = args.script
    cmdline = args.cmdline

    topology = " ".join(line for line in iter_lines(topology_file))

    script_lines = []
    for line in iter_lines(script_file):
        if cmdline and RE_CMDLINE_APPEND.match(line):
            # Index of last quote
            idx = len(line) - 1 - line[::-1].find("'")
            line = line[0:idx] + " {}'".format(cmdline)

        script_lines.append(line)


    script = " ".join(script_lines)

    cmd = "{} {}".format(script, topology)
    print_wrap(cmd)

    with Popen(cmd, shell=True) as proc:
        proc.wait()

if __name__ == "__main__":
    main()
