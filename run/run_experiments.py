# --- Backend consistency patch for `dd` package ---
# On Linux, the `dd` library normally uses the CUDD backend (`dd.cudd`),
# while on Windows it usually falls back to the pure-Python backend (`dd.autoref`).
# This creates a mismatch: `dd.cudd.BDD` objects cannot be deep-copied,
# but `dd.autoref.BDD` can. Our abstraction code relies on deepcopy working.
#
# To enforce consistent behavior across platforms, we always force `dd` to use
# the `autoref` backend:
#   1. Insert `autoref` into sys.modules under the name `dd.cudd`.
#      -> Any later `import dd.cudd` will transparently resolve to autoref.
#   2. Explicitly override `dd.BDD` so that code using `dd.BDD()` always creates
#      autoref BDDs instead of cudd BDDs.
#
# This guarantees deepcopy-safe behavior on both Windows and Linux,
# at the cost of lower performance compared to the CUDD backend.
# NOTE: This patch must run before any other module imports `dd`.

import sys
import dd.autoref as autoref
sys.modules['dd.cudd'] = autoref            # any future 'import dd.cudd' gets autoref
import dd
dd.BDD = autoref.BDD                        # ensure dd.BDD() always maps to autoref

from run.run_experiment_novelty_variation import *
from run.run_experiment_layer_variation import *
from run.run_experiment_distance import *
from run.run_experiment_other_abstractions import *


def run_all_experiments():
    run_experiment_novelty_variation_all()
    run_experiment_layer_variation_all()
    run_experiment_other_abstractions_all()
    run_experiment_distance()


if __name__ == "__main__":
    run_all_experiments()
