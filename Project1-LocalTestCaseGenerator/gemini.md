# Project Constitution: Local LLM Testcase Generator

## 1. Vision & Scope
A local web application that uses Ollama to generate high-quality software test cases based on user-provided requirements or prompts.

## 2. 3-Layer A.N.T. Architecture
- **Architecture (Core/Backend)**: FastAPI (Python) to handle requests and communicate with Ollama.
- **Navigation (UI Logic)**: React or Vanilla JS to manage application state and routing.
- **Tools (Execution)**: Scripts for Ollama API interaction and file exports.

## 3. Data Schema (The Payload)

### Input Schema (User Requirement)
```json
{
  "prompt": "string",
  "system_instruction": "string"
}
```

### Output Schema (Generated Test Case)
```json
[
  {
    "id": "TC-001",
    "title": "string",
    "pre_conditions": "string",
    "steps": [
      "Step 1: ...",
      "Step 2: ..."
    ],
    "expected_result": "string",
    "priority": "High | Medium | Low"
  }
]
```

## 4. Behavioral Rules
- **Model:** Strictly use `llama3.2` via Ollama.
- **Format:** Always respond in valid JSON format to allow UI rendering.
- **Tone:** Technical, precise, and professional.
- **Edge Cases:** LLM should actively seek to generate edge case scenarios.

## 5. Architectural Invariants
- No external LLM dependencies (strictly local).
- Modular design following the A.N.T. layers.
