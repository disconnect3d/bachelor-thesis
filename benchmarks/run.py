#!/usr/bin/env python
"""
This script builds, run and save outputs of particular benchmarks into csvs.
Written by Dominik Czarnota.
"""

from __future__ import print_function
import os
import sys
import subprocess
import shlex
import errno
import datetime

from collections import OrderedDict
from math import sqrt

from utils import mkdir, safe_call
from config import (SRC_DIR, BUILDS_DIR, OUTPUTS_DIR, CURRENT_PATH,
                    OUTPUTS_DELIMITER)

# tqdm is a 'progress bar' module. using it if it is available
# (you can install it through `pip install tqdm` or `python -m pip install tqdm`)
try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable):
        return iterable

def values():
    values_for_power = 6
    vals = []
    for i in range(10, 27):
        vals.append(2**i)
        diff = (2**(i+1) - 2**(i)) / values_for_power
        value = 2**i
        for j in range(values_for_power):
            value += diff
            vals.append(value)
    vals = list(set([int(sqrt(v))**2 for v in vals]))
    vals.sort()
    return vals

nval = values()

# This dict defines executables which will be run and arguments that will be passed
#    * first argument -- type_flags
#    * second argument -- data_sizes
#
# The actualy binary path that is used, is <bench_name><opt_flag> where:
#    * bench_name -- is just name taken from this dict keys
#    * opt_flag -- optimization flag taken from `opt_flags` variable
benchmark2data = OrderedDict()
benchmark2data["matrix_sum"] = {
    "data_sizes": nval,
    "type_flags": {
        0: "row traversal",
        1: "col traversal"
    }
}

benchmark2data["filtered_sum"] = {
    "data_sizes": nval,
    "type_flags": {
        0: "sorted",
        1: "unsorted"
    },
}

benchmark2data["data_alignment"] = {
    "data_sizes": nval,
    "type_flags": {
        0: "padded",
        1: "packed"
    }
}

benchmark2data["aos_vs_soa"] = {
    "data_sizes": nval,
    "type_flags": {
        0: "aos",
        1: "soa"
    }
}

benchmark2data["compact_aos_vs_soa"] = {
    "data_sizes": nval,
    "type_flags": {
        0: "aos",
        1: "soa"
    }
}

benchmark2data["random_access_aos_vs_soa"] = {
    "data_sizes": nval,
    "type_flags": {
        0: "aos",
        1: "soa"
    }
}

benchmark2data["parallel_count"] = {
    "data_sizes": nval,
    "type_flags": {
        0: "near",
        1: "far"
    },
    "third_arg": {
        i: "{} thread(s)".format(i) for i in range(1, 9)
    }
}

opt_flags = ("-O3", "-O2", "-O1", "-O0")

benchs_to_do = benchmark2data.keys()
if '-h' in sys.argv or '--help' in sys.argv:
    print("Options:")
    print("-v | --verbose   -- verbose")
    print("--build          -- only builds benchmarks")
    print("--run            -- only runs benchmarks")
    print("--benchs=<...>   -- launch only specified benchmark (delimited by ,)")
    print("--opts=<...>     -- launch only specified optimizations (delimited by ,). Choices: -O3, -O2, -O1, -O0")
    print("Possible benchmarks: ", ','.join(benchs_to_do))
    sys.exit(0)

verbose = '-v' in sys.argv or '--verbose' in sys.argv
# if no flags are passed all operations are performed
build = '--build' in sys.argv or '--run' not in sys.argv
run = '--run' in sys.argv or '--build' not in sys.argv


for arg in sys.argv:
    if arg.startswith('--benchs='):
        benchs_to_do = arg[9:].split(',')
    if arg.startswith('--opts='):
        opt_flags = arg[7:].split(',')
    

print("Will launch benchmarks: ", ','.join(benchs_to_do))
            


mkdir(OUTPUTS_DIR)
mkdir(BUILDS_DIR)
os.chdir(BUILDS_DIR)

SRC_FULL_PATH = os.path.join(CURRENT_PATH, SRC_DIR)
BIN_FULL_PATH = os.path.join(CURRENT_PATH, BUILDS_DIR, 'builds')  # the 'builds' is hardcoded in cmakelists
OUTPUTS_FULL_PATH = os.path.join(CURRENT_PATH, OUTPUTS_DIR)


if build:
    for opt_flag in opt_flags:
        safe_call("cmake -D USER_OPT_FLAG={} {}".format(opt_flag, SRC_FULL_PATH))
        safe_call("make")

if run:
    time_stats = {}
    for benchmark in benchs_to_do:
        time_stats[benchmark] = {'start': datetime.datetime.now()}
        data = benchmark2data[benchmark]
        print(">>>>>>>>>", benchmark)
        output_filepath = os.path.join(OUTPUTS_FULL_PATH, "{}.out".format(benchmark))

        with open(output_filepath, 'w') as of:
            of.write("data size" + OUTPUTS_DELIMITER)
            of.write(
                OUTPUTS_DELIMITER.join(
                    "{} {}{}".format(type_, opt, " " + third_arg)
                    for type_ in data['type_flags'].values()
                    for third_arg in (data['third_arg'].values() if 'third_arg' in data else [""])
                    for fourth_arg in (data['fourth_arg'].values() if 'fourth_arg' in data else [""])
                    for opt in opt_flags
                ) + "\n"
            )

            for n in tqdm(data['data_sizes']):
                of.write(str(n) + OUTPUTS_DELIMITER)
                outputs = []

                for type_flag in data['type_flags'].keys():
                    for third_arg in data['third_arg'].keys() if 'third_arg' in data else [""]:
                        for fourth_arg in data['fourth_arg'].keys() if 'fourth_arg' in data else [""]:
                            for opt_flag in opt_flags:
                                bin_path = os.path.join(BIN_FULL_PATH, "{}{}".format(benchmark, opt_flag))

                                command = "{bin} {type} {n} {third_arg} {fourth_arg}".format(bin=bin_path, type=type_flag, n=n, third_arg=third_arg, fourth_arg=fourth_arg)
                                print(command)
                                out = safe_call(command, verbose=verbose, pipe_err_to_out=not verbose)

                                # removing newline
                                out = out.splitlines()[-1]
                                outputs.append(out)

                #print(outputs)
                of.write(OUTPUTS_DELIMITER.join(map(str, outputs)))
                of.write("\n")
                of.flush()
        time_stats[benchmark]['end'] = datetime.datetime.now()

    for bench, timings in time_stats.items():
        start = timings['start']
        end = timings['end']
        print (bench, '\t\t', start, '\t', end, '\t', end-start)

