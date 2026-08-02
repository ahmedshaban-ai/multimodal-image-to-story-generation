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

## Contact

Ahmed Sha'ban

MSc Student in Smart Systems Engineering

An-Najah National University

Email:
s12154757@stu.najah.edu

LinkedIn

https://www.linkedin.com/in/ahmed-shaban-a37b14238/
