# AI Text Generator

A locally-run text generation application trained on real-world movie review data, built using a modified version of Andrej Karpathy's nanoGPT.

---

## Table of Contents
- [Part 1: Data Cleaning](#part-1-data-cleaning)
- [Part 2: Model Training](#part-2-model-training)
- [Part 3: Web Interface](#part-3-web-interface)

---

## Part 1: Data Cleaning

Clean and standardize the noisy dataset `corrupt_movie_corpus.txt` containing HTML tags, URLs, excessive punctuation, and special characters.

### Phase 1: Data Analysis

Analyze raw data to determine:
- **Size & Language**: Total line count and primary language
- **Noise Patterns**: Inspect at least 10 sample lines to identify corruption types (URLs, HTML tags, repeated punctuation)

### Phase 2: Data Cleaning

Using Python's `re` package, implement the following cleaning steps:
- **HTML Tag Removal**: Strip all tags using `<.*?>`
- **URL Removal**: Remove http://, https://, and www\. addresses
- **Character Cleanup**: Remove non-alphanumeric symbols identified during analysis
- **Whitespace Normalization**: Collapse multiple spaces into single spaces

### Deliverables
- Data analysis phase results
- 5 sample lines of cleaned text
- Cleaned corpus saved as `cleaned_text_file.txt`

---

## Part 2: Model Training

Train a GPT model on the cleaned movie corpus using a modified nanoGPT implementation.

### Prerequisites

Install required packages using `uv`:

```bash
uv add torch numpy transformers datasets tiktoken wandb tqdm
```

### Directory Structure

Create the following directory structure:

```
myNanoGPT/
├── data/
│   └── movies/
│       ├── input.txt
│       └── prepare.py
├── config.py
├── configurator.py
├── model.py
├── train.py
└── sample.py
```

### File Setup

| File | Source | Destination | Notes |
|------|--------|-------------|-------|
| `input.txt` | Your cleaned corpus | `myNanoGPT/data/movies/` | Cleaned movie reviews (Requires edits see below)|
| `prepare.py` | `nanoGPT/data/shakespeare_char/prepare.py` | `myNanoGPT/data/movies/` | Data preparation script |
| `config.py` | `nanoGPT/config/train_shakespeare_char.py` | `myNanoGPT/` | Requires edits (see below) |
| `configurator.py` | `nanoGPT/configurator.py` | `myNanoGPT/` | Copy as-is |
| `model.py` | `nanoGPT/model.py` | `myNanoGPT/` | Copy as-is |
| `train.py` | `nanoGPT/train.py` | `myNanoGPT/` | Copy as-is |
| `sample.py` | `nanoGPT/sample.py` | `myNanoGPT/` | Requires edits (see below) |

### Configuration Changes

**input.txt** (rename from `cleaned_text_file.txt`);
**config.py** (rename from `train_shakespeare_char.py`):
```python
out_dir = 'out-movies'  # changed from 'out-shakespeare-char'
wandb_project = 'movies'  # changed from 'shakespeare-char'
dataset = 'movies'  # changed from 'shakespeare_char'
# Remove: wandb_run_name = 'mini-gpt'
```

**sample.py**:
```python
num_samples = 1  # changed from 10
device = 'cpu'  # changed from 'cuda'
```

### Training Steps

Run the following commands from the `myNanoGPT` directory:

**Step 1: Prepare the Data**
```bash
python data/movies/prepare.py
```
This tokenizes `input.txt` and creates `train.bin` and `val.bin` files.

**Step 2: Train the Model**
```bash
python train.py config.py --device=cpu --compile=False --eval_iters=20 --log-interval=1 --block-size=64 --batch-size=12 --n-layer=6 --n-head=4 --n-embd=128 --max-iters=2000 --lr-decay-iters=2000 --dropout=0.0
```
This trains the model and saves checkpoints to `out-movies/`.

**Step 3: Generate Sample Text**
```bash
python sample.py --out_dir=out-movies
```
This loads the trained model and generates text based on learned patterns.

---

## Part 3: Web Interface

Create a simple web interface to interact with your trained model using Flask.

### Setup

Install Flask:

```bash
uv add flask
```

### Implementation Files

**1. index.html** - Place in `myNanoGPT/index.html`
- Contains the user interface with generate button and output display

**2. app.py** - Place in `myNanoGPT/app.py`
- Flask server that loads the model and handles text generation requests

### Running the Application

1. Ensure your trained model exists in the `out-movies/` directory
2. Start the Flask server:
   ```bash
   python app.py
   ```
3. Open your browser to `http://127.0.0.1:5000`
4. Click the generate button to create new text from your trained model

---

## Project Summary

This project demonstrates the complete pipeline for training a custom text generation model:
1. **Data Cleaning**: Transform noisy real-world data into a clean training corpus
2. **Model Training**: Adapt nanoGPT to train on custom data with appropriate hyperparameters
3. **Deployment**: Create an accessible web interface for generating text on-demand