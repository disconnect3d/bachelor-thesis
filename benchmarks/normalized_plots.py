#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script takes outputs from "outputs to plot",
parses them and outputs "relative performance plot" for -O3 optimization.

The user has to specify for specific benchmark which of the data serie will be the "normalization base" (not sure if that's correct name).
"""
from __future__ import print_function

import os
import glob
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from utils import mkdir
from config import PLOT_OUTPUTS_DIR, OUTPUTS_EXT, NORMALIZED_PLOTS_DIR, OUTPUTS_DELIMITER

# making the plot size 2 times longer for x axis
size = plt.rcParams['figure.figsize']
plt.rcParams['figure.figsize'] = (size[0]*2, size[1])

mkdir(NORMALIZED_PLOTS_DIR)

matplotlib.rcParams.update({'font.size': 18})

default_x_header = u'data size'
benchmark2data = {
    'aos_vs_soa': {
        'title': u'AoS vs SoA - przyspieszenie względne',
        'xaxis': u'n - liczba elementów',
        'yaxis': lambda norm_header, rest_headers: u'Przyspieszenie',
        'normalize_to_column': u'aos -O3 ',
        'normalize_columns': [u'soa -O3 '],
        'plot_name_fmt': '{}_normalized.pdf'
    },
    'compact_aos_vs_soa': {
        'title': u'AoS vs SoA - mniejsze struktury - przyspieszenie względne',
        'xaxis': u'n - liczba elementów',
        'yaxis': lambda norm_header, rest_headers: u'Przyspieszenie',
        'normalize_to_column': u'aos -O3 ',
        'normalize_columns': [u'soa -O3 '],
        'plot_name_fmt': '{}_normalized.pdf'
    },
    'random_access_aos_vs_soa': {
        'title': u'AoS vs SoA - swobody dostęp - przyspieszenie względne',
        'xaxis': u'n - liczba elementów',
        'yaxis': lambda norm_header, rest_headers: u'Przyspieszenie',
        'normalize_to_column': u'aos -O3 ',
        'normalize_columns': [u'soa -O3 '],
        'plot_name_fmt': '{}_normalized.pdf',
        'ylim_step': 0.1
    },
    'matrix_sum': {
        'title': u'Sumowanie elementów macierzy - przyspieszenie względne',
        'xaxis': u'dim*dim - liczba elementów macierzy',
        'yaxis': lambda norm_header, rest_headers: u'Przyspieszenie',
        'normalize_to_column': u'col traversal -O3 ',
        'normalize_columns': [u'row traversal -O3 '],
        'plot_name_fmt': '{}_normalized.pdf',
        'ylim_step': 1.0 
    },
    'filtered_sum': {
        'title': u'Przetwarzanie warunkowe - przyspieszenie względne',
        'xaxis': u'n - liczba elementów',
        'yaxis': lambda norm_header, rest_headers: u'Przyspieszenie',
        'normalize_to_column': u'unsorted -O2 ',
        'normalize_columns': [u'sorted -O2 ', u'unsorted -O3 ', u'sorted -O3 '],
        'plot_name_fmt': '{}_normalized.pdf',
        'ylim_step': 1.0,
        'legend': lambda ax: ax.legend(ncol=2, loc='center right', bbox_to_anchor=(1,0.3))
    },
    'data_alignment': {
        'title': u'Wyrównanie danych - przyspieszenie względne',
        'xaxis': u'n - liczba elementów tablicy',
        'yaxis': lambda norm_header, rest_headers: u'Przyspieszenie',
        'normalize_to_column': u'packed -O3 ',
        'normalize_columns': [u'padded -O3 '],
        'plot_name_fmt': '{}_normalized.pdf',
        'ylim_step': 0.1
    },
    'parallel_count': {
        'title': u'Równoległe przetwarzanie - przyspieszenie względne 1, 2 oraz 8 wątków',
        'xaxis': u'n - liczba elementów',
        'yaxis': lambda norm_header, rest_headers: u'Przyspieszenie',
        'normalize_to_column': u'near -O3 1 thread(s)',
        'normalize_columns': [u'far -O3 1 thread(s)', u'near -O3 1 thread(s)', u'far -O3 2 thread(s)', u'near -O3 2 thread(s)', u'near -O3 8 thread(s)', u'far -O3 8 thread(s)'],
        'plot_name_fmt': '{}_normalized.pdf',
        'style': '-',  # ['-o', '-*', '-x', '-v', '-^', '-<', '->'],
        'ylim_step': 1,
        #'points_every': 3,  # will change points list to points[::n] where n is the value here
        'legend': lambda ax: ax.legend(ncol=2, prop={'size': 16}, loc='upper center', bbox_to_anchor=(0.5, -0.15))
    },
}

def round_up(number, roundto=0.25):
    nearest_025 = round(number / roundto) * roundto
    v = nearest_025 + roundto if number > nearest_025 else nearest_025
    return v

def round_down(number, roundto=0.25):
    nearest_025 = round(number / roundto) * roundto
    v = nearest_025 - roundto if number < nearest_025 else nearest_025
    return v

for filepath in glob.glob(os.path.join(PLOT_OUTPUTS_DIR, '*.{}'.format(OUTPUTS_EXT))):
    filename_without_ext = os.path.splitext(os.path.basename(filepath))[0]

    if filename_without_ext not in benchmark2data: # or filename_without_ext != 'filtered_sum':
        print(">> Warning {} not recognized to plot.".format(filename_without_ext))
        print("Skipping it.")
        continue

    bench_data = benchmark2data[filename_without_ext]

    df = pd.read_csv(filepath, delimiter=OUTPUTS_DELIMITER)

    x_col_header = bench_data.get('x_serie', default_x_header)
    cols_headers = bench_data['normalize_columns']
    norm_to_col_header = bench_data['normalize_to_column']
    
    points_every = bench_data.get('points_every', 1)

    x = df[x_col_header][::points_every]
    normalize_to = df[norm_to_col_header][::points_every]
    cols_data = [(normalize_to/df[c])[::points_every] for c in cols_headers]

    d = {col_header.rstrip() + " / {}".format(norm_to_col_header): cols_data[i].tolist() for i, col_header in enumerate(cols_headers)}
    #d[norm_to_col_header] = [1.0] * len(normalize_to)

    plot_dataframe = pd.DataFrame(data=d, index=x)

    style = bench_data.get('style', '-o')
    plot_dataframe.plot(style=style, markersize=4, subplots=False)
    plt.plot([0, 2**27], [1, 1], 'k-')

    plt.title(bench_data['title'])
    plt.xscale('symlog', basex=2)
    plt.xticks(2**np.arange(10, 27, 1))

    plt.xlabel(bench_data['xaxis'])
    plt.ylabel(bench_data['yaxis'](norm_to_col_header, cols_headers))
    plt.grid(True)
    
    # tweaking plot so that x/y ticks looks fine on tight pdf...
    ax = plt.axes()

    for mt in ax.get_xaxis().majorTicks:
        mt.set_pad(8)
    for mt in ax.get_yaxis().majorTicks:
        mt.set_pad(5)

    step = bench_data.get('ylim_step', 0.25)
    ax.set_yticks(np.arange(0, 15, step))
    ymin=round_down(min(0.99, min((min(i) for i in cols_data))), roundto=step)
    ymax=round_up(max(1.01, max((max(i) for i in cols_data))), roundto=step)
    print("ymin", ymin, "ymax", ymax, "yticks step", step)
    plt.ylim(ymin=ymin, ymax=ymax)
    
    plot_name = os.path.join(NORMALIZED_PLOTS_DIR, bench_data['plot_name_fmt'].format(filename_without_ext))

    # setting proper legend for some plots...
    bbox_extra_artists = (bench_data['legend'](ax),) if 'legend' in bench_data else []

    print("Ploting", plot_name)
    plt.savefig(plot_name, bbox_extra_artists=bbox_extra_artists, bbox_inches='tight')

