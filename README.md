# Outside the Box

## Environment Setup

**Note:** All commands below should be run from the project root directory (where this README is located).

You can set up the project using either `uv`, `pip`, or Docker.

### Using uv
1. **Install uv:**
   https://docs.astral.sh/uv/getting-started/installation/
2. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```
3. **Sync environment (creates environment and installs dependencies):**
   ```bash
   uv sync
   ```
   This command will create a virtual environment (if needed) and install all dependencies from pyproject.toml.

   Alternatively, you can run the following commands separately:
   ```bash
   uv venv .venv
   uv pip install -r requirements.txt
   ```

4. **Run a script:**
   ```bash
   uv run -m run.plot_toy_model
   # Or any other script, e.g.:
   uv run -m run.plot_boxes
   uv run -m run.run_experiments
   ```

### Using pip (Slower)
1. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows (PowerShell):
   .venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run a script:**
   ```bash
   python -B -m run.plot_toy_model
   # Or any other script, e.g.:
   python -B -m run.plot_boxes
   python -B -m run.run_experiments
   ```

### Using Docker
1. **Build the Docker image:**
   ```bash
   docker build -t outside-the-box-ngc -f Dockerfile .
   ```
2. **Run a container (interactive development) :**
   ```bash
   docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm outside-the-box-ngc bash
   ```
3. **Run a container (interactive development) with live mount:**
   ```bash
   docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -it -v ${PWD}:/app outside-the-box-ngc bash
   ```
4. **Run a specific script:**
   ```bash
   docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -v ${PWD}:/app outside-the-box-ngc python -B -m run.plot_toy_model
   ```


## How to Run Experiments

> **Warning:**
> - TensorFlow no longer supports GPU on Windows. Training and experiments will run on CPU unless you use Docker or Linux.
> - To use GPU with Docker, you must have compatible CUDA drivers installed on your system.
> - If running Docker in WSL, you might also need to install the NVIDIA Container Toolkit in your WSL environment to enable GPU support.
> - CIFAR model training takes a long time (200 epochs) CPU ~ 170 minutes / GPU ~ 50 minutes .

Before running any experiment scripts, you must train the required models. Follow these steps:

1. **Train the models:**
   You must run all training scripts before running the experiment scripts:
   ```bash
   python -B -m run.train_CIFAR
   python -B -m run.train_F_MNIST
   python -B -m run.train_MNIST
   python -B -m run.train_GTSRB
   ```

2. **Run the experiment script:**
   After training, run the experiment script:
   ```bash
   python -B -m run.run_experiments
   ```
   The `run_experiments` script will automatically run the following experiment scripts:
   - `run_experiment_distance.py`
   - `run_experiment_layer_variation.py`
   - `run_experiment_novelty_variation.py`
   - `run_experiment_other_abstractions.py`

Refer to the [Evaluation](#evaluation) section below to see which script produces which figure or table from the paper.
All output files (CSVs, PDFs) are saved in the `outputs/` directory.

# Citation

This repository contains the implementation and data used in the paper [Outside the Box: Abstraction-Based Monitoring of Neural Networks](http://ecai2020.eu/papers/1282_paper.pdf), published at [ECAI 2020](http://ecai2020.eu/). To cite the work, you can use:

```
@inproceedings{outsidethebox19,
  author    = {Thomas A. Henzinger and
               Anna Lukina and
               Christian Schilling},
  editor    = {Giuseppe De Giacomo and
               Alejandro Catal{\'{a}} and
               Bistra Dilkina and
               Michela Milano and
               Sen{\'{e}}n Barro and
               Alberto Bugar{\'{\i}}n and
               J{\'{e}}r{\^{o}}me Lang},
  title     = {Outside the Box: Abstraction-Based Monitoring of Neural Networks},
  booktitle = {{ECAI}},
  series    = {Frontiers in Artificial Intelligence and Applications},
  volume    = {325},
  pages     = {2433--2440},
  publisher = {{IOS} Press},
  year      = {2020},
  url       = {https://doi.org/10.3233/FAIA200375},
  doi       = {10.3233/FAIA200375}
}
```

# Installation

We use Python 3.6 but other Python versions may work as well. The easiest is to use a conda environment. The package requirements that need to be installed are found in the file `requirements.txt`.

# Recreation of the results

Below we describe how to obtain the results shown in the paper.

## Data

Due to Gihub's limitation of the file size, one of the datasets needed to be compressed. To use this dataset, you need to manually go to the folder `data/GTSRB/` and unzip the file `train.zip`.

## Models

The repository contains the pretrained models used in the evaluation.
The models can be recomputed using the scripts `run/train_INSTANCE.py` where `INSTANCE` is the name of the model/data combination.

## Evaluation

The scripts to reproduce the figures and tables of the paper are found in the folder `run/`:

- Fig. 2: `plot_toy_model.py`
- Fig. 3: `plot_boxes.py` (Note that this will not produce the exact same figure because we obtained the figure for a network with different training parameters that we forgot to note down.)
- Fig. 4: `plot_explanation_alpha_thresholding.py`
- Table 2: `plot_legend.py`
- Figures 5-8 and Table 3: `run_experiments.py` (This script calls scripts for the individual experiments that can also be run in isolation.)

Intermediate results of the experiments are stored in `.csv` files in the `run/` folder. The final plots are stored in the top folder.
