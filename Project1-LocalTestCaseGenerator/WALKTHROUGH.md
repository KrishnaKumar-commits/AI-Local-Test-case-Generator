# 📖 Project Walkthrough: Local LLM Test Case Generator

## 🌟 Overview
A premium, locally-hosted web application that leverages **Ollama (Llama 3.2)** to transform feature requirements into structured, high-quality software test cases.

## 🏗️ The B.L.A.S.T. / A.N.T. Build
The project is built on the **A.N.T.** 3-layer architecture to ensure deterministic results from a probabilistic LLM:

## 📂 Project Structure
- **`backend/`**: Contains the FastAPI server, Architecture logic, and Tools.
- **`frontend/`**: Contains the Stylized UI components (HTML/CSS).

### 1. Architecture Layer (`backend/architecture/sop_test_generation.md`)
- Contains the **Standard Operating Procedure (SOP)**.

### 2. Navigation Layer (`backend/main.py`)
- The **Orchestrator**. FastAPI backend.

### 3. Tool Layer (`backend/tools/ollama_generator.py`)
- The **Executor**. Communicates with Ollama.

---

## 🎨 Premium UI Features
- **Frontend Assets**: Located in `frontend/static` and `frontend/templates`.
- **Glassmorphism Design**: Modern dark-mode interface.

---

## 🚀 Persistent Deployment
The system is now configured to run **"Everytime"** (automatically at Windows Logon) in the background.

- **How it works**: A Windows Scheduled Task named `AITesterBlueprint_LocalLLM` starts the server silently.
- **Manual Launch**: You can double-click `run_app.bat` to see the log window.
- **Silent Launch**: Double-click `silent_start.vbs` to start it without a window.
- **Access URL**: [http://localhost:8000](http://localhost:8000)

### Managing the Background Task:
To stop or check the status:
1. Open **Task Scheduler** on Windows.
2. Search for `AITesterBlueprint_LocalLLM`.
3. You can Disable or Delete it from there.
3. **Usage**:
   - Enter a requirement (e.g., "Reset password via email link").
   - Click **Generate ✨**.
   - Review and Click **Download JSON Payload**.
