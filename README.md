# Multimodal Image-to-Story Generation

A research project for multimodal image understanding and story generation using modern Vision-Language Models and Retrieval-Augmented Generation (RAG).

---

## Overview

This project investigates automatic story generation from images by combining computer vision, semantic retrieval, and large language models.

Instead of directly generating stories from an image, the system retrieves semantically similar examples, constructs context-aware prompts, and generates coherent narratives using Qwen2.5 language models.

---

## Research Objectives

- Multimodal Image Understanding
- Image-to-Story Generation
- Retrieval-Augmented Generation (RAG)
- Vision-Language Models
- Efficient LLM Inference
- Prompt Engineering
- Human Evaluation

---

## Technologies

- Python
- PyTorch
- Hugging Face Transformers
- Qwen2.5
- FAISS
- CUDA
- GGUF
- LoRA / QLoRA

---

## Pipeline

Image

↓

Feature Extraction

↓

Semantic Retrieval (FAISS)

↓

Prompt Construction

↓

Qwen2.5 Generation

↓

Story Evaluation

---

## Current Status

✅ Dataset Preparation

✅ Semantic Retrieval

✅ Prompt Generation

✅ Story Generation

🔄 Human Evaluation

🔄 Model Comparison

---

## Repository Structure

```
src/
models/
data/
evaluation/
results/
images/
```

---

## Future Work

- Arabic Vision-Language Models

- Better Retrieval

- Fine-tuning

- Human Evaluation Platform

- Automatic Story Scoring

---
## Quick Start

Clone the repository:

```bash
git clone https://github.com/ahmedshaban-ai/multimodal-image-to-story-generation.git
cd multimodal-image-to-story-generation
```

Create a virtual environment and install the requirements:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux or macOS:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the semantic retrieval demonstration:

```bash
python src/retrieval_demo.py
```

## Reproducibility Note

This public repository contains a lightweight and reproducible demonstration of the research pipeline. The complete 100,000-image dataset and large model files are not included because of storage, licensing, privacy, and research-management considerations.

## Contact

Ahmed Sha'ban

MSc Student in Smart Systems Engineering

An-Najah National University

Email:
s12154757@stu.najah.edu

LinkedIn

https://www.linkedin.com/in/ahmed-shaban-a37b14238/
