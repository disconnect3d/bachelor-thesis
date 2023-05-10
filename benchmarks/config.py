import os

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

SRC_DIR = 'src'
BUILDS_DIR = 'builds'
OUTPUTS_DIR = 'mind_outputs'
OUTPUTS_DELIMITER = ';'
# not used in all files yet so changing it is risky.
OUTPUTS_EXT = 'out'

ONE_TIMING_DELIMITER = ','  # this delimiter is set in measure.h
PLOT_OUTPUTS_DIR = 'mind_outputs_to_plot'
PLOTS_DIR = 'mind_plots'

NORMALIZED_PLOTS_DIR = 'mind_normalized_plots'

# just in case...
assert OUTPUTS_EXT != ''
assert OUTPUTS_DIR != PLOT_OUTPUTS_DIR
assert PLOTS_DIR != NORMALIZED_PLOTS_DIR


