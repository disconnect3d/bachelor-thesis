#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division, print_function

import sys
import os
import csv
import pylab as plt

from collections import OrderedDict
from glob import glob


if __name__ == '__main__':
    if len(sys.argv) not in (3, 4, 5, 6):
        print("Usage: {} <input_dir> <output_dir> [<input_file_filter>] [<plot_only_y_series>] [<postfix>]".format(sys.argv[0]))
        print("Plots data files from <input_dir> and outputs png files into <output_dir>")
        print("<input_file_filter> - optional - plot only files filtered by specified unix wildcard (e.g. '*.out')")
        print("<plot_only_y_series> - optional - specify indexes of y series to plot (e.g. \"0 1 2\"); default - all")
        print("<postfix> - optional - output filename postfix (before extension)")
        sys.exit(0)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    input_dir_filter = sys.argv[3] if len(sys.argv) >= 4 else '*.out'
    plot_only_y_series = list(map(int, sys.argv[4].split(' '))) if len(sys.argv) >= 5 else []
    output_postfix = sys.argv[5] if len(sys.argv) == 6 else ''

    glob_filter = os.path.join(input_dir, input_dir_filter)
    print("Searching for inputs using '{}' glob filter".format(glob_filter))
    # iterate over files in `input_dir` and parse all csv files
    for filepath in glob(glob_filter):
        print("Parsing {}".format(filepath))
        with open(filepath) as fp:
            rows = csv.reader(fp, delimiter=';')
            title = next(rows)
            axes_labels = next(rows)

            x_data = []
            y_data_series = OrderedDict()
            for row in rows:
                x, y_data = float(row[0]), map(float, row[1:])
                x_data.append(x)
                for index, y in enumerate(y_data):
                    y_data_series.setdefault(index, []).append(y)

        # filtering... if it was passed
        if plot_only_y_series:
            for y_data_serie_index in y_data_series.keys():
                if y_data_serie_index not in plot_only_y_series:
                    y_data_series.pop(y_data_serie_index) 
                    axes_labels.pop(y_data_serie_index+1)

        fig, ax = plt.subplots()
        ax.set_xscale('symlog', basex=2)
        plt.grid(True)
        for key in y_data_series:
            plt.plot(x_data, y_data_series[key], '-', label=axes_labels[key+1])
        plt.legend(loc='best')
        plt.title(title[0][:-1])
        plt.xlabel(u"n - liczba elementów")
        plt.ylabel(u"czas wykonania [ms] / liczba elementów")
        fig = plt.gcf()
        fig.set_size_inches(6, 5)
        #plt.gca().tight_layout()
        from matplotlib import rcParams
        rcParams.update({'figure.autolayout': True})
        plt.savefig(os.path.join(output_dir, "{}{}.png".format(os.path.splitext(os.path.basename(filepath))[0], output_postfix)), dpi=300, bbox_inches='tight')
        #plt.show()
