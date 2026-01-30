from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import subprocess
import json
import os

app = FastAPI(title="Local LLM Test Case Generator")

# Resolve paths relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")
STATIC_DIR = os.path.join(FRONTEND_DIR, "static")
TEMPLATES_DIR = os.path.join(FRONTEND_DIR, "templates")

# Mount static files (for CSS/JS) and templates
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

class GenerateRequest(BaseModel):
    prompt: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate(request: GenerateRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Requirement cannot be empty")
    
    try:
        # Layer 2 logic: Routing to Layer 3 Tool
        tool_path = os.path.join(BASE_DIR, "tools", "ollama_generator.py")
        cmd = ["python", tool_path, "--prompt", request.prompt]
        process = subprocess.run(cmd, capture_output=True, text=True)
        
        if process.returncode != 0:
            return JSONResponse(
                status_code=500, 
                content={"error": "Tool execution failed", "detail": process.stderr}
            )
        
        result = json.loads(process.stdout)
        return result

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "Internal server error", "detail": str(e)}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
