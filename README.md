# Power Move: Enterprise AI Baseball Analytics

**Power Move** is a high-performance, agentic AI platform designed for MLB front offices. It combines real-time data from the MLB Stats API with large language models (Gemini) to provide autonomous scouting reports and deep-dive analytics.

---

## 🚀 The Stack

- **Backend**: Python 3.13 / FastAPI (High-performance asynchronous API)
- **AI/ML**: Google Gemini (LLM) / Mock Agent Fallback (Architectural Pattern)
- **Frontend**: React (Modular Component Architecture)
- **Infrastructure**: Docker / Docker-Compose / Terraform (IaC)

---

## 🧠 Key Features

### 1. The War Room (Agentic AI)
An autonomous scouting assistant that analyzes live player data. 
- **Pattern**: ReAct (Reason + Act).
- **Capability**: The agent can fetch stats, compare players, and generate natural language scouting reports.
- **Fallback Mode**: The application gracefully degrades to a simulation mode if API keys are missing, ensuring 100% uptime for portfolio reviews.

### 2. Deep Analytics
Proxy services for the official MLB Stats API, providing real-time season data for every player in the league.

### 3. Enterprise Ready
- **Containerized**: Full Docker support for consistent deployments.
- **IaC**: Terraform configurations for AWS (VPC, ECS, ECR).
- **Security**: Robust environment management via `pydantic-settings`.

---

## 🛠️ Setup & Installation

### Local Development (Python)
1. Clone the repository.
2. Create a virtual environment: `py -m venv venv`.
3. Install dependencies: `pip install -r backend/requirements.txt`.
4. Configure `.env`: Use `backend/.env.example` as a template.
5. Run the API: `uvicorn backend.main:app --reload`.

### Docker Deployment
```bash
docker-compose up --build
```

---

## 📈 Vision for Oteemo
This project demonstrates the core technical skills requested for the **Full Stack Engineer - Enterprise AI Applications** role:
- **Full-Stack Proficiency**: Seamless integration between a Python backend and React frontend.
- **AI/ML Engineering**: Hands-on integration with LLMs and prompt engineering.
- **DevOps/MLOps**: Infrastructure as Code and containerization as first-class citizens.
- **Resilient Architecture**: Designing for reliability through fallback patterns.
