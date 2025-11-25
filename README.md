## Project Goal
Develop a locally-run text generation application trained on real-world data.

## Part One: Data Cleaning
Clean and standardize the noisy dataset `corrupt_movie_corpus.txt` containing HTML tags, URLs, excessive punctuation, and special characters.

### Phase 1: Data Analysis
Analyze raw data to determine:
- **Size & Language**: Total line count and primary language
- **Noise Patterns**: Inspect at least 10 sample lines to identify corruption types (URLs, HTML tags, repeated punctuation)

### Phase 2: Data Cleaning
Using Python's `re` package, implement:
- **HTML Tag Removal**: Strip all tags using `<.*?>`
- **URL Removal**: Remove http://, https://, and www\. addresses
- **Character Cleanup**: Remove non-alphanumeric symbols identified during analysis
- **Whitespace Normalization**: Collapse multiple spaces into single spaces

### Deliverables
- Data Analysis phase results
- 5 sample lines of cleaned text

## Part Two: 
This portion of README documents the setup, configuration, and execution of Phase 2 of the project. The goal is to adapt Andrej Karpathy's `nanoGPT` repository to train a GPT model on a cleaned movie corpus dataset.

---

## 1. Project Overview

This phase utilizes the following core components from the original `nanoGPT` repository:

1. **`prepare.py`**: Tokenizes the raw text data (`input.txt`) and splits it into binary `train.bin` and `val.bin` files.
2. **`train.py`**: Initializes, configures, and trains the Transformer model using the generated binary files.
3. **`sample.py`**: Loads the trained model to generate new, coherent text based on the learned patterns.

---

## 2. Prerequisites and Setup

### 2.1. Install Required Packages

Use `uv` to install the necessary Python packages:

```bash
uv add torch
uv add numpy
uv add transformers
uv add datasets
uv add tiktoken
uv add wandb
uv add tqdm
```

### 2.2. Create Directory Structure

Create a subdirectory named `myNanoGPT` inside your main project directory, and then set up the specific dataset directory structure within it:

```
/myNanoGPT
└── /data
    └── /movies
```

---

## 3. File Placement and Configuration

Place the required files into the corresponding directories as follows:

| Filename | Source | Destination Directory | Notes |
|----------|--------|----------------------|-------|
| `input.txt` | Your cleaned movie corpus | `myNanoGPT/data/movies/` | Rename your corpus file to `input.txt`. |
| `prepare.py` | `nanoGPT/data/shakespeare_char/prepare.py` | `myNanoGPT/data/movies/` | This script prepares your data. |
| `config.py` | `nanoGPT/config/train_shakespeare_char.py` | `myNanoGPT/` | Requires Edits (see Section 3.1). |
| `configurator.py` | `nanoGPT/configurator.py` | `myNanoGPT/` | Standard file. |
| `model.py` | `nanoGPT/model.py` | `myNanoGPT/` | Standard file. |
| `sample.py` | `nanoGPT/sample.py` | `myNanoGPT/` | Requires Edits (see Section 3.2). |
| `train.py` | `nanoGPT/train.py` | `myNanoGPT/` | Standard file. |

### 3.1. Edits to `config.py` (Previously `train_shakespeare_char.py`)

In the new `config.py` file, make the following mandatory edits to adapt it to the movie dataset:

| Original Setting | Change To |
|-----------------|-----------|
| `out_dir = 'out-shakespeare-char'` | `out_dir = 'out-movies'` |
| `wandb_project = 'shakespeare-char'` | `wandb_project = 'movies'` |
| `dataset = 'shakespeare_char'` | `dataset = 'movies'` |
| `wandb_run_name = 'mini-gpt'` | Remove this line entirely. |

### 3.2. Edits to `sample.py`

Modify `sample.py` to ensure compatibility with the execution environment:

| Original Setting | Change To |
|-----------------|-----------|
| `num_samples = 10` (or similar) | `num_samples = 1` |
| `device = 'cuda'` | `device = 'cpu'` |

---

## 4. Execution Steps

All commands should be run from the main `myNanoGPT` directory.

### Step 1: Prepare the Data

Run the `prepare.py` script, which will tokenize your `input.txt` and generate `train.bin` and `val.bin` files inside the `data/movies` directory.

```bash
python data/movies/prepare.py
```

### Step 2: Train the Model

Run the `train.py` script with the specified hyperparameter overrides. This command will initialize the model and start the training process, saving checkpoints to the `out-movies` directory.

```bash
python train.py config.py --device=cpu --compile=False --eval_iters=20 --log-interval=1 --block-size=64 --batch-size=12 --n-layer=6 --n-head=4 --n-embd=128 --max-iters=2000 --lr-decay-iters=2000 --dropout=0.0
```

### Step 3: Sample the Generated Text

Run the `sample.py` script to load the trained model from the `out-movies` directory and generate new text based on the movie corpus.

```bash
python sample.py --out_dir=out-movies
```

---

## Final Goal

Successfully execute all three steps to see the model generate new text based on the cleaned movie corpus dataset.

## Part Three: Connecting Your Generator to a UI

Create a web interface to interact with your trained nanoGPT model using Flask.

---

## Setup

Install Flask in your `uv` environment:

```bash
uv add flask
```

---

## Implementation

This phase requires two files:

### 1. `index.html` - Frontend
Contains the user interface with input fields, generate button, and output display.

**Location:** `myNanoGPT/index.html`

### 2. `app.py` - Backend
Flask server that loads the model, handles requests, and generates text.

**Location:** `myNanoGPT/app.py`

---

## Running the Application

1. Ensure your trained model exists in `out-movies` directory
2. Start the Flask server:

```bash
python app.py
```

3. Open your browser and navigate to `http://127.0.0.1:5000`
4. Click button to generate text

---

## Goal

Provide a simple web interface where users can generate randomized text from your trained model at the click of a button.