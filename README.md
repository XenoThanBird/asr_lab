# 🧠 ASR Lab - Automatic Speech Recognition Optimization Toolkit

![ASR Lab](https://img.shields.io/badge/AI/NLP-ASR_Lab-blueviolet) 
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/GUI-Streamlit-orange)
![Docker](https://img.shields.io/badge/Containerized-Docker-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


# asr_lab
# Automatic Speech Recognition (ASR) Config Testing and Optimization Lab for Kore.ai IVR Systems.

#Current Problem:
#After migrating from Nuance Krypton to Azure Speech (via UniMRCP) for ASR (Automatic Speech Recognition) inside a Kore.ai-based IVR we encountered the following issue:

#Issue: Azure Speech Recognition hypersentivity - it hears "background noise" and causes immediate "No Match" failures even though all prompts are set to be non-barge-in capable (non-bargeable).

#Project Overview

This ASR Testing Lab provides a full professional framework to evaluate, optimize, and deploy Automatic Speech Recognition (ASR) configurations IVR and virtual voice assistant platforms, including Kore.ai, Azure Speech, Deepgram, and Speechmatics integrations.

**Created by:** Matthan Bird
**Version**: 1.0.0
**License**: MIT
**Year**: 2025

The lab allows for:
- Batch-Testing of ASR configuration against multiple real-world background noise scenarios
- Fine-tuning of speech sensitivity thresholds to optimize detection vs background resilience
- Streamlined configuration management with YAML/JSON converters
- Visualization and manual testing through a Streamlit Dashboard
- Full containerization support with Docker
- Installation via standard 'pip install' setup

---

| Component | Description |
| :-------- | :---------- |
| Batch Tester | Tests multiple ASR configs against diverse background noise scenarios |
| Sensitivity Optimizer | Calculates optimal ASR sensitivity thresholds automatically |
| GUI Dashboard | Drag-and-drop testing of configs and audio samples |
| YAML <-> JSON Converter | Simplifies deployment vs version control workflows |
| Dockerfile | Containerizes the lab for cloud/server use |
| Prebuilt Background Samples | Airport, Office, Restaurant, Street, Crowd noise simulations |

---

## Key Technologies
- Python 3.11
- Streamlit (GUI Dashboard)
- PyYAML, Pandas, NumPy, Pydub, Matplotlib
- Docker for cloud containerization
- Kore.ai-compatible ASR optimatization
- Deepgram, Azure Speech, Speechmatics ASR engines

---

## Why This Lab?

Traditional ASR testing often lacks structured simulation environments, leading to:
- Overly aggressive No Match behaviors
- False Positives due to background noise
- Expensive Manual QA cycles

---

## 🧠 About the Author

Matthan Bird is a Voice AI Engineer and Conversational AI Architect passionate about designing better NLP/ASR systems.

This project showcases engineering practices in:
- Real-world noise simulation
- Automated ASR sensitivity tuning
- AI/IVR system optimization
- End-to-end deployment from local pipelines to cloud-ready containers

Available for collaborations and consultations in Conversational AI, NLP Optimization, and Voice Technology Innovation.

📫 Contact: [www.linkedin.com/in/matthan-bird-jd-1b280642] | [matthanbird@gmail.com]

---

This lab automates the testing and tuning cycle, drastically improving:
- ASR accuracy
- Call Center Technologies, Virtual Assistant, & Customer Service NLU performance
- First Call Resolution (FCR) metrics
- Customer Experience (CX) KPIs
