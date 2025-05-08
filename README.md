# 🤖 Local Chatbot Experiment with Ollama, Phidata & Streamlit

Welcome to my experimental project where I’m building a **local AI chatbot** by integrating:

✅ **Ollama** for running LLMs locally  
✅ **Phidata** as the orchestration framework  
✅ **Streamlit** for a simple, interactive frontend

The goal is to explore deploying a fully local chatbot solution without relying on external APIs, ensuring privacy, control, and customization.

---

## 🚀 Features

- Run **LLMs locally** using [Ollama](https://ollama.com/)
- Manage pipelines & agents with **Phidata**
- Friendly web UI powered by **Streamlit**
- Easily extensible for new models or workflows
- No cloud dependency (everything runs on your machine)

---

## 🏗️ Project Structure


```bash
├── src/
│   ├── app/
│   │   └── app.py             # Streamlit frontend
│   ├── phidata/
│   │   ├── phidata_config.py  # Phidata configuration
│   │   └── chatbot_agent.py   # Bot logic / pipeline
├── requirements.txt            # Python dependencies
└── README.md                   # This file