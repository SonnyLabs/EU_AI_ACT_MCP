#!/usr/bin/env python3
"""
Standalone version of the SonnyLabs prompt injection detection server.
This version doesn't require the MCP library and can be run directly.
"""
import os
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load SonnyLabs API credentials from environment variables
API_KEY = os.getenv("SONNYLABS_API_TOKEN")
ANALYSIS_ID = os.getenv("SONNYLABS_ANALYSIS_ID")
BASE_URL = os.getenv("SONNYLABS_BASE_URL", "https://sonnylabs-service.onrender.com")

# Initialize SonnyLabs client
sonnylabs_client = None
try:
    from sonnylabs_py import SonnyLabsClient
    
    if API_KEY and ANALYSIS_ID:
        sonnylabs_client = SonnyLabsClient(
            api_token=API_KEY,
            analysis_id=ANALYSIS_ID,
            base_url=BASE_URL
        )
    else:
        print("WARNING: SonnyLabs API credentials not configured. Please set the required environment variables.")
except ImportError:
    print("WARNING: sonnylabs_py package not installed. Please install it with: pip install git+https://github.com/SonnyLabs/sonnylabs_py")

# Create the FastAPI app
app = FastAPI(title="SonnyLabs Prompt Injection Detection API")

# Define the request model
class PromptInjectionRequest(BaseModel):
    text: str
    threshold: Optional[float] = 0.5
    tag: Optional[str] = None

# Add a FastAPI route for direct API access
@app.post("/detect_prompt_injection")
async def api_detect_prompt_injection(request: PromptInjectionRequest):
    """
    Detects if the given text contains a prompt injection attempt.
    
    Args:
        text: The text to analyze for prompt injection.
        threshold: Threshold above which to consider a prompt injection detected (default: 0.5).
        tag: Optional tag to identify this request.
        
    Returns:
        A dictionary containing analysis results and a unique tag.
    """
    if not sonnylabs_client:
        raise HTTPException(
            status_code=500,
            detail="SonnyLabs API credentials not configured or sonnylabs_py package not installed."
        )
    
    try:
        # Analyze the text using SonnyLabs API
        analysis_result = sonnylabs_client.analyze_text(request.text, scan_type="input", tag=request.tag)
        
        # Extract prompt injection score
        injection_score = 0.0
        for analysis in analysis_result.get("analysis", []):
            if analysis.get("type") == "score" and analysis.get("name") == "prompt_injection":
                injection_score = analysis.get("result", 0.0)
                break
                
        # Debug output to see what we're getting from the API
        print(f"Debug - Full API response: {analysis_result}")
        print(f"Debug - Extracted injection score: {injection_score}")
        
        return {
            "analysis": [
                {
                    "type": "score",
                    "name": "prompt_injection",
                    "result": injection_score
                },
            ],
            "tag": analysis_result.get("tag")
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing text: {str(e)}"
        )

@app.get("/")
async def root():
    """Root endpoint that provides basic information about the API."""
    return {
        "name": "SonnyLabs Prompt Injection Detection API",
        "description": "API for detecting prompt injections in text using SonnyLabs security services",
        "version": "1.0.0",
        "endpoints": {
            "/detect_prompt_injection": "POST - Analyze text for prompt injections"
        }
    }

if __name__ == "__main__":
    # Run the server
    print("Starting SonnyLabs API server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
