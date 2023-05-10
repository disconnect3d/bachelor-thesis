#!/usr/bin/env python
# example of perf csv:
"""
$ sudo perf stat -x';' -d ./builds/builds/matrix_sum-O3 1 10000
result value used against compier optimization - ignore this: 140200051990608
0.852883
failed to read counter stalled-cycles-frontend
failed to read counter stalled-cycles-backend
2007,007973;;task-clock;2007007973;100,00
51;;context-switches;2007007973;100,00
0;;cpu-migrations;2007007973;100,00
130;;page-faults;2007007973;100,00
7076083831;;cycles;998268053;49,75
<not supported>;;stalled-cycles-frontend;0;100,00
<not supported>;;stalled-cycles-backend;0;100,00
30785000047;;instructions;1250355406;62,31
9449746508;;branches;1502468647;74,87
24119057;;branch-misses;1502826734;74,89
2476214188;;L1-dcache-loads;1480640364;73,92
100881644;;L1-dcache-load-misses;503921712;25,11
156087;;LLC-loads;499826133;24,91
7587;;LLC-load-misses;747993084;37,27
"""

import os
import csv
import glob
from utils import mkdir, safe_call

BIN_PATH = './builds/builds/matrix_sum-O3'

PERF_REPEAT = 20
PERF_DELIMITER = ';'
PERF_CMD_FMT = 'perf stat -r ' + str(PERF_REPEAT) + ' -x"' + PERF_DELIMITER + '" -d ' + BIN_PATH + ' {launch_type} {n}'

launch_types = [0, 1]


data_sizes = set([20, 22, 23, 24, 25, 26])

data = {}
for launch_type in launch_types:
    for power in data_sizes:
        n = 2**power
        cmd = PERF_CMD_FMT.format(n=n, launch_type=launch_type)
        out = safe_call(cmd, verbose=True, pipe_err_to_out=True)
        rows = csv.reader(str(out).splitlines(), delimiter=PERF_DELIMITER)
        #print(out)
        for row in rows:
            #print(row)
            if len(row) == 1:
                try:
                    timing = float(row[0])
                except Exception as e:
                    continue
                data.setdefault((power, launch_type), dict())
                if 'timing' not in data[(power, launch_type)]:
                    data[(power, launch_type)]['timing'] = timing
                else:
                    data[(power, launch_type)]['timing'] += timing
                #print("Timing:", timing, data[(power, launch_type)]['timing'])
                continue

            elif len(row) < 5:
                continue
            elif len(row) == 5:
                value, _, name, full_value, percentage = row
            elif len(row) == 6:
                value, _, name, _, full_value, percentage = row
    
            data.setdefault((power, launch_type), dict())[name] = (value, full_value, percentage)

#### Just for your information
# data[(power, launch_type)].keys():
# ['stalled-cycles-frontend', 'branches', 'context-switches', 'cpu-migrations', 'LLC-load-misses', 'branch-misses', 'task-clock', 'LLC-loads', 'stalled-cycles-backend', 'L1-dcache-loads', 'instructions', 'cycles', 'L1-dcache-load-misses', 'page-faults', 'timing']
#print (data[10000][0].keys())

# OUTPUTING LATEX TABLE :)


calc_and_round_percentage = lambda d, v1, v2: round(100.0 * float(d[v1][0]) / float(d[v2][0]), 2)
# latex cols are defined as lambdas which take 'n' as parameter
latex_table_cols = [
    lambda power, t: '$2^{' + str(power) + '}$ -- ' + ('rows' if not t else 'cols'),
    lambda power, t: round(data[(power, t)]['timing'] / PERF_REPEAT, 2),
    lambda power, t: data[(power, t)]['instructions'][0],
    #lambda power, t: data[(power, t)]['cycles'][0],
    #lambda power, t: data[(power, t)]['page-faults'][0],
    lambda power, t: calc_and_round_percentage(data[(power, t)], 'branch-misses', 'branches'),
    lambda power, t: calc_and_round_percentage(data[(power, t)], 'L1-dcache-load-misses', 'L1-dcache-loads'),
    lambda power, t: calc_and_round_percentage(data[(power, t)], 'LLC-load-misses', 'LLC-loads')
]
latex_item_delimiter = ' & '
latex_newline = '\n\\\\ \\hline\n'

latex_table = latex_newline.join(
    latex_item_delimiter.join(
        str(value(power, launch_type)) for value in latex_table_cols
    ) for power, launch_type in sorted(data.keys())
)

print(latex_table)
