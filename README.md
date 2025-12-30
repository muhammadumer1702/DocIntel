DocIntel — Document Intelligence AI

DocIntel is an AI-powered system that converts unstructured documents (text files, reports, contracts, notes) into structured, actionable decisions such as risk classification.

This project demonstrates a working end-to-end AI pipeline:

Raw documents → decision engine → predictions

Designed to scale from rule-based logic to machine-learning models

API-ready and demo-friendly

 -----------------------------------------

🚀 What Problem Does This Solve?

Organizations deal with massive volumes of unstructured text:

Contracts

Reports

Support tickets

Internal documentation

Manual review is slow, expensive, and inconsistent.

DocIntel automates the first layer of decision-making, turning documents into clear signals like:

HIGH_RISK

MEDIUM_RISK

LOW_RISK

 -----------------------------------------

🧠 Current Capabilities

Reads documents from disk

Analyzes content

Outputs decision labels

Produces consistent, repeatable results

Ready to be upgraded to ML-based training

Example output:

doc1.txt -> HIGH_RISK
doc2.txt -> MEDIUM_RISK
doc3.txt -> LOW_RISK

 -----------------------------------------

📁 Project Structure
DocIntel/
├── data/
│   └── raw/                # Input documents (.txt)
├── experiments/
│   └── decision_engine.py  # Core decision logic
├── api/                    # (Next step) FastAPI service
├── models/                 # (Future) trained ML models
├── training/               # (Future) model training scripts
└── README.md

 -----------------------------------------

⚙️ Setup & Requirements
Prerequisites

Windows

Python 3.x (via py launcher)

Install dependencies
py -m pip install fastapi uvicorn

 -----------------------------------------

▶️ Run the Decision Engine

From the project root:

py experiments\decision_engine.py


This will process all files inside:

data/raw/


and print predictions to the terminal.

 -----------------------------------------

🌐 API (Next Step)

The system is designed to be wrapped in an API using FastAPI, allowing:

File upload

Real-time predictions

Easy browser-based demos

This makes the project investor-demo ready.

 -----------------------------------------

🔮 Roadmap

 End-to-end document → decision pipeline

 Demo-ready outputs

 FastAPI endpoint

 ML-based training with labeled data

 Web dashboard for non-technical users

 Real-world dataset integration

 -----------------------------------------

💡 Vision

DocIntel is a foundation for enterprise-grade document intelligence:

Faster decisions

Lower operational cost

Scalable learning over time

The system is intentionally modular so that:

Rules today can become learning models tomorrow.
