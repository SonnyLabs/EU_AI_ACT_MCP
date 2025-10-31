# server.py
import os
from typing import Optional, Dict, Any
from mcp.server.fastmcp import FastMCP
from sonnylabs_py import SonnyLabsClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load SonnyLabs API credentials from environment variables
API_KEY = os.getenv("SONNYLABS_API_TOKEN")
ANALYSIS_ID = os.getenv("SONNYLABS_ANALYSIS_ID")
BASE_URL = os.getenv("SONNYLABS_BASE_URL", "https://sonnylabs-service.onrender.com")

# Initialize the SonnyLabs client
sonnylabs_client = None
if API_KEY and ANALYSIS_ID:
    sonnylabs_client = SonnyLabsClient(
        api_token=API_KEY,
        analysis_id=ANALYSIS_ID,
        base_url=BASE_URL
    )
else:
    print("WARNING: SonnyLabs API credentials not configured. Please set the required environment variables.")

# Create an MCP server
mcp = FastMCP("SonnyLabs")

# Add prompt injection detection tool
@mcp.tool()
def detect_prompt_injection(text: str, threshold: float = 0.65, tag: Optional[str] = None) -> Dict[str, Any]:
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
        raise ValueError("SonnyLabs API credentials not configured. Please set the required environment variables.")
    
    # Analyze the text using SonnyLabs API
    analysis_result = sonnylabs_client.analyze_text(text, scan_type="input", tag=tag)
    
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


# Create a FastAPI app for the REST API
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

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
    return detect_prompt_injection(request.text, request.threshold, request.tag)

# Start the server if this script is run directly
if __name__ == "__main__":
    import uvicorn
    
    # Run the server
    print("Starting SonnyLabs API server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)