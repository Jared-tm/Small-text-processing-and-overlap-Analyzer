```md
# Amharic–Tigrigna Linguistic Overlap Analyzer

A local Python NLP pipeline for analyzing lexical and phoneme-level similarity between Amharic and Tigrigna texts.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Results](#results)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [License](#license)
- [Author](#author)

---

## Overview
This project processes Amharic and Tigrigna text datasets to identify shared vocabulary, compute phoneme overlap using SERA-based G2P transcription, and detect similar words with fuzzy matching.  
It runs entirely locally and was developed as part of the ECEg-1052 course at Addis Ababa University.

---

## Features
- Tokenization and text cleaning for Ethiopic scripts  
- Lemmatization using simplified morphological rules  
- G2P transcription using the System for Ethiopic Representation in ASCII (SERA)  
- Fuzzy word similarity matching  
- Unique shared word detection using sets  
- Phoneme frequency analysis  
- Statistical metrics:
  - Word-level overlap  
  - Phoneme-level overlap  
  - Similarity groups  

---

## Results
Using Bible and news datasets, the pipeline achieved:
- **48.89%** word-level overlap  
- **70.73%** phoneme-level overlap  
- **9.5×** improvement over baseline (5.14%)

---

## Technologies
- Python 3.x  
- NLTK (optional/custom tokenizers)  
- FuzzyWuzzy  
- Regular expressions  
- Custom SERA G2P mapper  

---

## Project Structure
```

project/
├── data/
│   ├── amharic_bible.txt
│   ├── tigrigna_bible.txt
│   ├── news_am.txt
│   └── news_ti.txt
│
├── src/
│   ├── main.py
│   ├── preprocessing.py
│   ├── g2p_sera.py
│   ├── analysis.py
│   └── utils.py
│
├── results/
│   └── output.json
│
└── README.md

````

---

## Installation
Install dependencies:

```bash
pip install -r requirements.txt
````

---

## Usage

Run the main script:

```bash
python src/main.py
```

This processes the datasets and prints the analysis results to the console.
Output is also saved to `results/output.json`.

---

## Sample Output

```
Shared unique words: 185
Word-level overlap: 48.89%
Phoneme-level overlap: 70.73%
Similarity improvement over baseline: 9.5×
```

---

## License

This project is open-source under the MIT License.
Feel free to modify and use for research or educational purposes.

---

## Author

Yared Tamir Mitiku


```