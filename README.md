# Modular Text Data Pipeline

This project demonstrates a clean, modular, and testable data pipeline for a text-based emotion dataset using Python.  
It follows software engineering best practices commonly used in Data Science and Machine Learning projects.

The focus is on:
- clean code
- modular design
- defensive programming
- realistic DS/ML workflows

---

## 📂 Project Structure

```
├── data/
│ └── text_emotion.csv (not in present in this repository)
├── src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── features.py
│ ├── metrics.py
│ └── main.py
├── README.md
└── requirements.txt
```

---

## 🔄 Pipeline Overview

The pipeline follows a typical DS/ML workflow:

1. **Load data**
2. **Preprocess data**
3. **Engineer features**
4. **Compute metrics**
5. **Display results**

All logic is separated into small, reusable functions.

---

## 🧠 Modules Overview

### `data_loader.py`
Responsible only for loading CSV data safely from disk.

### `preprocessing.py`
Handles data cleaning:
- removing rows with missing values
- standardizing column names

### `features.py`
Creates model-ready features:
- categorical encoding
- text-based features (word count)

### `metrics.py`
Computes summary and evaluation metrics:
- class distributions
- basic statistical measures

### `main.py`
Orchestrates the full pipeline using the modules above.

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the pipeline:
```bash    
python src/main.py
```

Example output includes:
    processed data preview
    class distribution
    word count statistics
