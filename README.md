<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/system-flow-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/system-flow-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/system-flow-dark.svg">
  <img src="assets/system-flow-light.svg" width="960" alt="Aruthra Sathish Kumar — Software Engineer. Backend & Distributed Systems. Applied AI / ML.">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/aruthrasathish/"><strong>LinkedIn</strong></a>
  &nbsp; / &nbsp;
  <a href="mailto:aruthra.sathish@gmail.com"><strong>Email</strong></a>
  &nbsp; / &nbsp;
  <a href="#selected-systems"><strong>Selected systems</strong></a>
  &nbsp; / &nbsp;
  <a href="#research"><strong>Research</strong></a>
</p>

## About me

I’m a **Software Engineer working at the intersection of backend systems, distributed computing, and applied AI/ML**. I build applications that connect real-time data, backend services, and machine learning.

- **⚙️ Systems engineering:** Building event-driven applications with **Kafka, Flink, Redis, PostgreSQL, and Kubernetes**—from real-time ranking to AI-assisted incident response.
- **🧠 Applied AI:** Currently working on **CAM-Soft at American University**, investigating contextual language understanding with **8B language models, transformer embeddings, LoRA/PEFT, and cross-dataset evaluation**.
- **🎓 Academic recognition:** M.S. Information Systems from **George Mason University**, with a **3.97/4.0 GPA and the Academic Excellence Award**.
- **🤝 Opportunities:** Interested in **Software Engineering, Backend & Distributed Systems, AI Engineering, and ML Systems** roles.

## Selected systems

<table>
<tr>
<td>

**01 / INCIDENT RESPONSE**

### [WatchTower](https://github.com/aruthrasathish/Watchtower-MCP-server-for-incident-response)

**From operational evidence to controlled Kubernetes remediation.**

An AI-assisted investigation platform that connects operational data, ranks suspects, and places an **HMAC-SHA256 approval broker** between investigation and remediation.

<table>
<tr>
<th align="left">Investigation interface</th>
<th align="left">Evidence collection</th>
<th align="left">Simulated triage</th>
</tr>
<tr>
<td><strong>12 MCP tools</strong></td>
<td><strong>4 data sources</strong></td>
<td><strong>~83% less time</strong></td>
</tr>
</table>

**Engineering focus:** Connecting AI-assisted investigation to an explicit approval boundary for Kubernetes operations.

Python · MCP · Kubernetes · PostgreSQL · TimescaleDB · pgvector

[**Inspect the implementation →**](https://github.com/aruthrasathish/Watchtower-MCP-server-for-incident-response)

</td>
</tr>
</table>

<table>
<tr>
<td width="50%" valign="top">

**02 / STREAM PROCESSING**

### [Real-Time Search Ranking](https://github.com/aruthrasathish/Real-time-Search-Ranking-System)

**Continuously updated rankings. Separate request serving.**

Kafka ingests clickstream events. Flink aggregates clicks in **30-second windows**. Redis sorted sets maintain rankings for Node.js APIs.

**Engineering focus:** Deterministic ranking, asynchronous computation, and tiered caching.

Kafka · Apache Flink · Redis · Node.js

[**Inspect the pipeline →**](https://github.com/aruthrasathish/Real-time-Search-Ranking-System)

</td>
<td width="50%" valign="top">

**03 / RETRIEVAL & INFERENCE**

### [USDA AI Assistant](https://github.com/aruthrasathish/usda-chatbot)

**176 federal programs. Retrieval-augmented discovery.**

BGE embeddings and FAISS retrieval connect program information to Mistral 7B generation.

**Project measurements:** Response latency reduced from **~90s to 8s**; automated **11+ hours of scraping work**.

FastAPI · PostgreSQL · FAISS · LlamaIndex · Mistral 7B

[**Inspect the implementation →**](https://github.com/aruthrasathish/usda-chatbot)

</td>
</tr>
</table>

<details>
<summary><strong>More engineering / voice infrastructure, authentication, and sequence modeling</strong></summary>

<br>

### [SpeakUp](https://github.com/aruthrasathish/anonymous-voice-QA-platform)

Anonymous voice Q&A with **Kafka-backed voice processing and WebSocket interaction**. Designed for **500+ concurrent users per room**; the project README reports **sub-100ms real-time updates**. Groq Whisper supports transcription across **99+ languages**.

Next.js · Fastify · Kafka · WebSockets · Redis · PostgreSQL · Groq Whisper

### [CareerLens](https://github.com/aruthrasathish/job-application-tracker)

Application analytics across a web application and Chrome extension. Connects **Google OAuth and cross-origin JWT authentication** to **21 REST endpoints** for application tracking, funnel analytics, and burnout detection.

React · FastAPI · PostgreSQL · Google OAuth · JWT · Chrome Extension

### [Academic Performance Intelligence](https://github.com/aruthrasathish/academic-performance-predictor-CNN-GRU)

PyTorch sequence-model experiments tracked with MLflow. Reported results distinguish **88.9% classification accuracy for GRU v1** from **7.40-point grade-prediction MAE for CNN-GRU v2**.

PyTorch · CNN · GRU · Attention · Pandas · MLflow

</details>

## Research

### CAM-Soft · American University

**AI/ML Research Intern · 2026–Present**

Investigating soft hate speech whose meaning depends on context and implication. My work brings together **Llama 3.1 8B, transformer embeddings, LoRA/PEFT, and cross-dataset evaluation**, using **PyTorch and Hugging Face**.

Ongoing research directions include counterfactual learning and scalable NLP experimentation.

## 🧰 Toolbox

**Programming Languages:**
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-E68A00?style=flat&logo=openjdk&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat&logo=postgresql&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat&logo=gnubash&logoColor=white)

**Backend & APIs:**
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-43853D?style=flat&logo=nodedotjs&logoColor=white)
![Fastify](https://img.shields.io/badge/Fastify-202020?style=flat&logo=fastify&logoColor=white)
![REST APIs](https://img.shields.io/badge/REST_APIs-2563EB?style=flat)
![WebSockets](https://img.shields.io/badge/WebSockets-6D28D9?style=flat)

**Distributed Systems & Data:**
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat&logo=apachekafka&logoColor=white)
![Apache Flink](https://img.shields.io/badge/Apache_Flink-E6526F?style=flat&logo=apacheflink&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)

**AI & Machine Learning:**
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat&logo=huggingface&logoColor=black)
![Transformers](https://img.shields.io/badge/Transformers-4051B5?style=flat)
![LoRA / PEFT](https://img.shields.io/badge/LoRA%20%2F%20PEFT-7C3AED?style=flat)
![RAG](https://img.shields.io/badge/RAG-087F8C?style=flat)
![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=flat)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat&logo=mlflow&logoColor=white)

**Cloud & Infrastructure:**
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=flat&logo=googlecloud&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=flat&logo=terraform&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)

**Developer Tools:**
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-168B6A?style=flat)

## Professional experience

**AI/ML Research Intern · American University · 2026–Present**  
CAM-Soft research involving language models, embeddings, parameter-efficient adaptation, and cross-dataset evaluation.

**Graduate Teaching Assistant · George Mason University**  
IT 207 — Server-Side Development. Taught backend programming, Node.js, REST APIs, SQL, MySQL, and debugging.

**Software Engineer Intern · Verzeo Edutech**  
Worked with React, Django, Django REST Framework, authentication, API optimization, and relational databases.

## Education & recognition

**George Mason University**  
M.S. Information Systems · Graduated May 2026  
**🏆 Academic Excellence Award · 3.97 / 4.0 GPA**

**Anna University**  
B.Tech Information Technology

---

<p align="center">
  <strong>Backend systems · Distributed infrastructure · Applied AI · ML systems</strong>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/aruthrasathish/"><strong>Connect on LinkedIn</strong></a>
  &nbsp; / &nbsp;
  <a href="mailto:aruthra.sathish@gmail.com"><strong>Get in touch</strong></a>
</p>
