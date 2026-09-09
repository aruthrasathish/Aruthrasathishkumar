## Aruthra Sathish Kumar

**Software Engineer · Backend & Distributed Systems · Applied AI/ML**

I build scalable backend systems, real-time infrastructure, and intelligent applications.

[LinkedIn](https://www.linkedin.com/in/aruthrasathish/) · [Email](mailto:aruthra.sathish@gmail.com)

AI/ML Research @ **American University** · M.S. @ **George Mason University** · **Academic Excellence Award**

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/system-flow-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/system-flow-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/system-flow-dark.svg">
  <img src="assets/system-flow-light.svg" alt="Distributed systems and applied AI: Kafka to Flink to Redis and API; BGE embeddings to FAISS retrieval to Mistral generation. Illustrative flows with a separate GitHub contribution snapshot." width="840">
</picture>

## Featured systems

### [WatchTower — incident investigation with controlled remediation](https://github.com/aruthrasathish/Watchtower-MCP-server-for-incident-response)

Connects operational evidence to AI-assisted investigation through **12 MCP tools across 4 data sources**. Combines suspect ranking with an **HMAC-SHA256 approval broker** for Kubernetes remediation.

`Evidence → investigation → suspect ranking → approval → remediation`

**Result:** approximately **83% less triage time in simulated incidents**.<br>
**Built with:** Python · MCP · Kubernetes · PostgreSQL · TimescaleDB · pgvector

### [Real-Time Search Ranking — from clickstream to serving](https://github.com/aruthrasathish/Real-time-Search-Ranking-System)

Processes clickstream events with **Kafka and Apache Flink**, aggregates clicks in **30-second windows**, stores rankings in **Redis sorted sets**, and serves results through **Node.js**. Connects asynchronous stream processing to low-latency request handling.

`Clickstream → Kafka → Flink → Redis → Node.js API`

**Focus:** deterministic click-based ranking, tiered caching, and low-latency serving.<br>
**Built with:** Kafka · Apache Flink · Redis · Node.js

### [USDA AI Assistant — retrieval with faster GPU inference](https://github.com/aruthrasathish/usda-chatbot)

Makes **176 federal programs** searchable through a RAG pipeline using **BGE embeddings, FAISS retrieval, and Mistral 7B**. Automates program-data collection and connects retrieval to GPU-backed generation.

**Result:** response latency reduced from approximately **90s to 8s** in project measurements; automated **11+ hours of scraping work**.<br>
**Built with:** FastAPI · PostgreSQL · FAISS · LlamaIndex · Mistral 7B

<details>
<summary><strong>More engineering work — real-time communication, authentication, and sequence modeling</strong></summary>

### [SpeakUp — asynchronous voice Q&A](https://github.com/aruthrasathish/anonymous-voice-QA-platform)

Separates voice processing from real-time interaction using Kafka and WebSockets. Designed for **500+ concurrent users per room**, with **sub-100ms real-time updates** reported in the project README, and transcription across **99+ languages** through Groq Whisper.

**Built with:** Next.js · Fastify · Kafka · WebSockets · Redis · PostgreSQL · Groq Whisper

### [CareerLens — application analytics across browser contexts](https://github.com/aruthrasathish/job-application-tracker)

Connects a web application and Chrome extension through **Google OAuth and cross-origin JWT authentication**. Exposes **21 REST endpoints** for application tracking, funnel analytics, and burnout detection.

**Built with:** React · FastAPI · PostgreSQL · Google OAuth · JWT · Chrome Extension

### [Academic Performance Intelligence — sequence-based risk prediction](https://github.com/aruthrasathish/academic-performance-predictor-CNN-GRU)

Models academic-risk patterns with a **CNN-GRU architecture and attention**, using PyTorch and MLflow for experimentation. Reported results distinguish the models: **88.9% classification accuracy for GRU v1** and **7.40-point grade-prediction MAE for CNN-GRU v2**.

**Built with:** PyTorch · CNN · GRU · attention · Pandas · MLflow

</details>

## Research / CAM-Soft

**AI/ML Research Intern · American University · 2026–Present**

Investigating how language models can identify soft hate speech whose meaning depends on implication and context. My work brings together **Llama 3.1 8B, transformer embeddings, PyTorch, and Hugging Face tooling**, with **LoRA/PEFT and cross-dataset evaluation**.

Research directions include counterfactual learning and scalable NLP experimentation. **Ongoing research.**

## Technical toolkit

**Languages:** Python · Java · TypeScript · JavaScript · SQL · Bash<br>
**Backend:** FastAPI · Django · Node.js · Fastify · REST APIs · WebSockets<br>
**Distributed systems & data:** Kafka · Apache Flink · Redis · PostgreSQL · MySQL<br>
**AI/ML:** PyTorch · Transformers · LoRA/PEFT · RAG · FAISS · embeddings<br>
**Infrastructure:** Linux · Docker · Kubernetes · AWS · Terraform · GitHub Actions

## Foundation

**George Mason University** — M.S. Information Systems, May 2026<br>
**3.97 / 4.0 GPA · Academic Excellence Award**

Previously: **Graduate Teaching Assistant**, GMU — server-side development, REST APIs, and SQL; **Software Engineer Intern**, Verzeo Edutech — authentication, API optimization, and relational databases. B.Tech Information Technology, Anna University.

---

Interested in engineering roles across **backend systems, distributed infrastructure, applied AI, and ML systems**. [Let's connect.](https://www.linkedin.com/in/aruthrasathish/)
