# Final Year Research Project Similarity Score Demo

# SimilarityDemo

This demo showcases how to compute semantic similarity between disaster-related news messages and an ontology using Sentence-BERT and a Flask web app.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/zuhrahmohammed/SimilarityDemo.git
cd SimilarityDemo
```

### 2. Set Up Your Environment

Make sure you have Python 3.8+ installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Flask App

```bash
flask run
```

The app will start on `http://127.0.0.1:5000/`.

---

## How It Works

The app loads ontology descriptions from `ontology_descriptions.json` and uses Sentence-BERT to compute a similarity score between a user-input message and known disaster-related concepts.

---

## Project Structure

```
SimilarityDemo/
├── app.py                     # Flask app entry point
├── similarity_model.py        # Semantic similarity logic using Sentence-BERT
├── ontology_descriptions.json # Ontology-based descriptions
├── templates/
│   └── index.html             # Web UI for input and output
└── requirements.txt           # Python dependencies
```

---

## 📸 Demo Preview

![Demo Screenshot](demo_screenshot.png) <!-- Optional: Add a screenshot or GIF if you have one -->

---


This demo was used in a presentation on ontology-enhanced fake news detection during disasters.  
For more context, see the paper or presentation slides.

---


