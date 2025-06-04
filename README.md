# PathCoRAG

PathCoRAG is a graph-based Retrieval-Augmented Generation (RAG) framework that incorporates Chain-of-Thought (CoT) style query expansion and path-aware retrieval for multi-step reasoning. It achieves enhanced performance on domain-specific QA tasks by integrating knowledge graph exploration and LLM-based reasoning.

## 📦 Installation

```bash
git clone https://github.com/RAGcody628/PathCoRAG
cd PathCoRAG
pip install -e .
pip install openai

## 🔑 API Key Setup

Make sure to set your OpenAI API key before using the LLM-based components:

```bash
export OPENAI_API_KEY='your-api-key-here'

##📁 Dataset Preparation
