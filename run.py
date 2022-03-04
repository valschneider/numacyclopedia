#!/usr/bin/env python3

from argparse import ArgumentParser
from subprocess import Popen

def main():
    parser = ArgumentParser()
    parser.add_argument("topology", help="The NUMA topology file to use")
    parser.add_argument("--script", default="qemu.sh", help="The QEMU script to run")

    args = parser.parse_args()

    topology_file = args.topology
    script_file = args.script

    with open(topology_file, "r") as fh:
        topology = " ".join([line.strip().strip("\\") for line in fh if not line.startswith("#")])

    with open(script_file, "r") as fh:
        script = " ".join([line.strip().strip("\\") for line in fh if not line.startswith("#")])

    cmd = "{} {}".format(script, topology)

    with Popen(cmd, shell=True) as proc:
        proc.wait()

if __name__ == "__main__":
    main()
