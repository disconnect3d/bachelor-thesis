#!/usr/bin/env python

import csv
import os
import glob
from utils import mkdir

from config import OUTPUTS_DIR, PLOT_OUTPUTS_DIR, ONE_TIMING_DELIMITER, OUTPUTS_DELIMITER

print("Creating plot directory:", PLOT_OUTPUTS_DIR)
mkdir(PLOT_OUTPUTS_DIR)
print("Created.")

for filepath in glob.glob(os.path.join(OUTPUTS_DIR, '*.out')):
    print("Working on ", filepath)
    with open(filepath, 'r') as fp:
        rows = csv.reader(fp, delimiter=OUTPUTS_DELIMITER)
        with open(os.path.join(PLOT_OUTPUTS_DIR, os.path.basename(filepath)), 'w') as ofp:
            ofp.write(OUTPUTS_DELIMITER.join(next(rows)) + '\n')

            for row in rows:
                n = row[0]

                out_row = [n]
                for col in row[1:]: 
                    try:
                        floats = map(float, (i for i in col.split(ONE_TIMING_DELIMITER) if i != ''))
                        if not floats:
                            continue

                        avg = sum(i*1000 for i in floats)/float(len(floats))
                        out_row.append(str(avg))
                    except Exception as e:
                        print("f = ", floats)
                        print(e, '\n', col)
                ofp.write(OUTPUTS_DELIMITER.join(out_row) + '\n')

