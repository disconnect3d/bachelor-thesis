#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script takes benchmark csv outputs and plot them into pngs.
It assumes all benchmarks were launched with all optimization flags
(which might be bad for fast/small tests).
It can be of course modified - to plot particular benchmark which
were produced only by using -O3 for example, you have to comment out the rest
of the benchmarks from plot_mappings mapping and then change
-O3 mapping to use particular columns from csv
(change -O3 value in mapping dict to (1,2) )

Written by Dominik Czarnota.
"""

from __future__ import print_function, unicode_literals
import os
import sys
import errno
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.ticker import MaxNLocator

from utils import mkdir
from config import PLOT_OUTPUTS_DIR, PLOTS_DIR, OUTPUTS_DELIMITER

matplotlib.rcParams.update({'font.size': 18})

release = '--release' in sys.argv
only_show_plot = '--show' in sys.argv

EXTENSION = 'pdf' if release else 'png'

mkdir(PLOTS_DIR)

parallel_count_interesting_range = np.append(np.arange(16, 27, 2), 27)
parallel_count_out_csv = 'parallel_count'
parallel_count_xaxis = u'n - liczba elementów'
parallel_count_yaxis = u'średni czas przetworzenia elementu wektora [ns]'
parallel_count_title_fmt = u'Równoległe liczenie/zapis {}'
pc_interesting_ylim = [0.2, 1.5]
pc_legsize = 5
# If particular dict specified "output_file" key with value that names output file
# This means this file will be used as output_file instead of plot name
plot_mappings = {
    "aos_vs_soa": {
        "title": u"Organizacja danych AoS vs SoA {}",
        "xaxis": u"n - liczba elementów",
        "yaxis": u"czas dostępu do jednego elementu [ns]",
        "out_fmt": "aos_vs_soa_{}." + EXTENSION,
        "mapping": {
            "-O3": (1, 5),
            "-O2": (2, 6),
            "-O1": (3, 7),
            "-O0": (4, 8)
        }
    },
    "random_access_aos_vs_soa": {
        "title": u"AoS vs SoA - swobody dostęp {}",
        "xaxis": u"n - liczba elementów",
        "yaxis": u"czas dostępu do jednego elementu [ns]",
        "out_fmt": "random_access_aos_vs_soa_{}." + EXTENSION,
        "mapping": {
            "-O3": (1, 5),
            "-O2": (2, 6),
            "-O1": (3, 7),
            "-O0": (4, 8)
        }
    },
    "compact_aos_vs_soa": {
        "title": u"AoS vs SoA - mniejsze struktury {}",
        "xaxis": u"n - liczba elementów",
        "yaxis": u"czas dostępu do jednego elementu [ns]",
        "out_fmt": "compact_aos_vs_soa_{}." + EXTENSION,
        "mapping": {
            "-O3": (1, 5),
            "-O2": (2, 6),
            "-O1": (3, 7),
            "-O0": (4, 8)
        }
    },
    "parallel_count_1_2": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_1_2_{}." + EXTENSION,
        "mapping": {
            "-O3": (1, 5, 33, 37),
            "-O2": (2, 6, 34, 38),
            "-O1": (3, 7, 35, 39),
            "-O0": (4, 8, 36, 40)
        }
    },

    "parallel_count_2_3": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_2_3_{}." + EXTENSION,
        "mapping": {
            "-O3": (5, 9, 37, 41),
        }
    },
    "parallel_count_3_4": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_3_4_{}." + EXTENSION,
        "mapping": {
            "-O3": (9, 13, 41, 45),
        }
    },
    "parallel_count_4_5": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_4_5_{}." + EXTENSION,
        "mapping": {
            "-O3": (13, 17, 45, 49),
        }
    },

    "parallel_count_5_6": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_5_6_{}." + EXTENSION,
        "mapping": {
            "-O3": (17, 21, 49, 53),
        }
    },
    "parallel_count_6_7": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_6_7_{}." + EXTENSION,
        "mapping": {
            "-O3": (21, 25, 53, 57),
        }
    },
    "parallel_count_7_8": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_7_8_{}." + EXTENSION,
        "mapping": {
            "-O3": (25, 29, 57, 61),
        }
    },
    #"parallel_count_2_2": {      
    #    "output_file": parallel_count_out_csv,
    #    "title": parallel_count_title_fmt,
    #    "xaxis": parallel_count_xaxis,
    #    "yaxis": parallel_count_yaxis,
    #    "out_fmt": "parallel_count_2_2_{}." + EXTENSION,
    #    "mapping": {
    #        "-O3": (5, 37),
    #    },
    #    "xaxis_range": np.arange(16, 27, 2),
    #    "ylim": [0.5, 2]
    #},
    "parallel_count_interesting1": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_interesting1." + EXTENSION,
        "mapping": {
            "-O3": (5, 37, 9, 41), # thread 2, 3
        },
        "xaxis_range": parallel_count_interesting_range,
        "ylim": pc_interesting_ylim,
        "legend_size": pc_legsize
    },
    "parallel_count_interesting2": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_interesting2." + EXTENSION,
        "mapping": {
            "-O3": (9, 41, 13, 45), # thread 3, 4
        },
        "xaxis_range": parallel_count_interesting_range,
        "ylim": pc_interesting_ylim,
        "legend_size": pc_legsize
    },
    "parallel_count_interesting3": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_interesting3." + EXTENSION,
        "mapping": {
            "-O3": (13, 45, 17, 49), # thread 4, 5
        },
        "xaxis_range": parallel_count_interesting_range,
        "ylim": pc_interesting_ylim,
        "legend_size": pc_legsize
    },
    "parallel_count_interesting4": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_interesting4." + EXTENSION,
        "mapping": {
            "-O3": (17, 49, 21, 53), # thread 5, 6
        },
        "xaxis_range": parallel_count_interesting_range,
        "ylim": pc_interesting_ylim,
        "legend_size": pc_legsize
    },
    "parallel_count_interesting5": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_interesting5." + EXTENSION,
        "mapping": {
            "-O3": (21, 53, 25, 57), # thread 6, 7
        },
        "xaxis_range": parallel_count_interesting_range,
        "ylim": pc_interesting_ylim,
        "legend_size": pc_legsize
    },
    "parallel_count_interesting6": {      
        "output_file": parallel_count_out_csv,
        "title": parallel_count_title_fmt,
        "xaxis": parallel_count_xaxis,
        "yaxis": parallel_count_yaxis,
        "out_fmt": "parallel_count_interesting6." + EXTENSION,
        "mapping": {
            "-O3": (25, 57, 29, 61), # thread 7, 8
        },
        "xaxis_range": parallel_count_interesting_range,
        "ylim": pc_interesting_ylim,
        "legend_size": pc_legsize
    },

    #"parallel_count_1_2_8": {      
    #    "output_file": parallel_count_out_csv,
    #    "title": parallel_count_title_fmt,
    #    "xaxis": parallel_count_xaxis,
    #    "yaxis": parallel_count_yaxis,
    #    "out_fmt": "parallel_count_1_2_8_{}." + EXTENSION,
    #    "mapping": {
    #        "-O3": (1, 5, 29, 33, 37, 61),
    #    }
    #},
    "matrix_sum": {
        "title": u"Sumowanie elementów macierzy {}",
        "xaxis": u"dim*dim - liczba elementów macierzy",
        "yaxis": u"czas dostępu do jednego elementu [ns]",
        "out_fmt": "matrix_sum_{}." + EXTENSION,
        "mapping": {
            "-O3": (1, 5),
            "-O2": (2, 6),
            "-O1": (3, 7),
            "-O0": (4, 8)
        
}
    },
    "filtered_sum": {
        "title": u"Przetwarzanie warunkowe (>=128) {}",
        "xaxis": u"n - liczba elementów",
        "yaxis": u"czas przetwarzenia elementu [ns]",
        "out_fmt": "filtered_sum_{}." + EXTENSION,
        "mapping": {
            "-O3": (1, 5),
            "-O2": (2, 6),
            "-O1": (3, 7),
            "-O0": (4, 8)
        }
    },
    "data_alignment": {
        "title": u"Wyrównanie danych {}",
        "xaxis": "n - liczba elementów tablicy",
        "yaxis": "czas dostępu do jednego elementu [ns]",
        "out_fmt": "data_alignment_{}." + EXTENSION,
        "mapping": {
            "-O3": (1, 5),
            "-O2": (2, 6),
            "-O1": (3, 7),
            "-O0": (4, 8)
        }
    }
}

plot_benchmarks = list(plot_mappings.keys())

for arg in sys.argv:
    if arg.startswith('--benchs='):
        plot_benchmarks = arg[9:].split(',')

for arg in sys.argv:
    if arg.startswith('-k='):
        plot_benchmarks = [pb for pb in plot_benchmarks if arg[3:] in pb]
        print("Benchmarks to be plot:", plot_benchmarks)

if '-h' in sys.argv or '--help' in sys.argv:
    print("Options:")
    print("--release       -- plots info pdf instead of png")
    print("--show          -- shows plots instead of saving into file")
    print("--benchs=<...>  -- choose which benchmark to plot (delimited by ,)")
    print("Possible benchmarks:", ','.join(plot_benchmarks))
    sys.exit(0)



for plot_name, data in plot_mappings.items():
    if plot_name not in plot_benchmarks:
        continue
    for opt_flag, opt_cols in data['mapping'].items():
        try:
            output_file = data['output_file'] if 'output_file' in data else plot_name
            print("Plotting", plot_name, "from", output_file, "file using", opt_flag)
            f = os.path.join(PLOT_OUTPUTS_DIR, "{}.out".format(output_file))
            plt.plotfile(f, cols=(0,) + opt_cols, delimiter=OUTPUTS_DELIMITER, subplots=False, newfig=True)

            plt.title(data['title'].format(opt_flag))
            plt.xscale('symlog', basex=2)

            xaxis_range = 2**data.get('xaxis_range', np.append(np.arange(10, 27, 2), 27))
            plt.xticks(xaxis_range[:-1])
            plt.xlim(xaxis_range[0], xaxis_range[-1])

            if 'ylim' in data:
                plt.ylim(*data['ylim'])

            plt.grid(True)

            ax = plt.axes()
            for mt in ax.get_xaxis().majorTicks:
                mt.set_pad(8)
                #x, y = mt.label1.get_position()
                #mt.label1.set_position((x+0.116, y-0.016))
                pass
            for mt in ax.get_yaxis().majorTicks:
                mt.set_pad(5)

            plt.xlabel(data['xaxis'])#, labelpad=-1)
            plt.ylabel(data['yaxis'])

            if 'legend_size' in data:
                plt.setp(plt.gca().get_legend().get_texts(), fontsize='small')
                plt.legend(fontsize=data['legend_size'])

            if only_show_plot:
                plt.show()
            else:
                plt.savefig(os.path.join(PLOTS_DIR, data['out_fmt'].format(opt_flag[1:])), bbox_inches='tight')

        except Exception as e:
            pint("ERROR:\n{}".format(e))
