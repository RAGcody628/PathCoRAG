# PathCoRAG

PathCoRAG is a graph-based Retrieval-Augmented Generation (RAG) framework that incorporates Chain-of-Thought (CoT) style query expansion and path-aware retrieval for multi-step reasoning. It achieves enhanced performance on domain-specific QA tasks by integrating knowledge graph exploration and LLM-based reasoning.

## Installation


```bash
git clone https://github.com/RAGcody628/PathCoRAG
cd PathCoRAG
pip install -e .
pip install openai
```


## 🔑 API Key Setup

Make sure to set your OpenAI API key before using the LLM-based components:

```bash
export OPENAI_API_KEY='your-api-key-here'
```


## 📁 Dataset Preparation

1. Create the dataset directory:

```bash
mkdir -p datasets
```

2. Download the UltraDomain dataset (Mix, CS, Legal, Agriculture) from:

https://huggingface.co/datasets/TommyChien/UltraDomain

Place the downloaded files into the datasets/ directory.

## 🧩 Step-by-Step Pipeline
### Step 0: Extract Document Contexts
```bash
python reproduce/Step_0.py
```
### Step 1: Build Knowledge Graph
```bash
python reproduce/Step_1.py
```
### Step 2: Generate Question Files
```bash
pip install transformers
mkdir -p datasets/questions
python reproduce/Step_2.py
```
### Step 3: Run PathCoRAG Method
```bash
python reproduce/Step_3.py
```
### Step 4: Evaluate Answer Quality Using LLM
```bash
python examples/batch_eval.py
python eval.py
```
### Step 5: Visualize Evaluation Results
```bash
python eval2.py
```

## 📊 Evaluation
We use GPT-based win-rate scoring to evaluate answers in terms of:

Comprehensiveness

Diversity

Empowerment

Overall Quality

See eval.py and eval2.py for details.

## 🗂️ Project Structure
```bash
PathCoRAG/
├── PathCoRAG/             # Main package (KG, LLM, prompt, etc.)
├── datasets/              # Input datasets and generated questions
├── reproduce/             # Reproducibility scripts (Step_0~3)
├── examples/              # Evaluation prompt builder
├── eval.py                # Main evaluation execution
├── eval2.py               # Visualization of evaluation results
├── install.sh             # Installation helper script
├── README.md
```

## 📝 License
This project is licensed under the MIT License.