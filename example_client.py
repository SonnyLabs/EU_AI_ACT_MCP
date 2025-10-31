#!/usr/bin/env python3
"""
Example client for using the SonnyLabs MCP server to detect prompt injections.
"""
import sys
import json
import httpx
from typing import Dict, Any

def call_detect_prompt_injection(text: str, threshold: float = 0.65, tag: str = None) -> Dict[str, Any]:
    """Call the detect_prompt_injection tool on the MCP server.
    
    Args:
        text: The text to analyze for prompt injection
        threshold: Threshold above which to consider a prompt injection detected
        tag: Optional tag to identify this request
        
    Returns:
        The API response as a dictionary
    """
    base_url = "http://localhost:8000"
    endpoint = f"{base_url}/detect_prompt_injection"
    
    # Prepare the request payload
    payload = {
        "text": text,
        "threshold": threshold
    }
    if tag:
        payload["tag"] = tag
    
    # Make the API request
    with httpx.Client() as client:
        response = client.post(endpoint, json=payload)
        
    # Check for success and parse the response
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API call failed with status {response.status_code}: {response.text}")

def main():
    """Main entry point for the example client."""
    # Get input text to analyze (from command line or prompt user)
    text_to_analyze = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter text to analyze for prompt injection: ")
    
    print(f"\nAnalyzing text for prompt injection: '{text_to_analyze}'\n")
    
    # Call the prompt injection detection tool
    try:
        result = call_detect_prompt_injection(text_to_analyze)
        
        # Extract the prompt injection score
        injection_score = result["analysis"][0]["result"]
        tag = result["tag"]
        
        # Determine if it's a prompt injection (using default threshold of 0.65)
        is_injection = injection_score > 0.65
        
        # Print the results
        print("Analysis Results:")
        print(f"Text: {text_to_analyze}")
        print(f"Prompt Injection Score: {injection_score:.4f}")
        print(f"Detected as Prompt Injection: {'YES' if is_injection else 'NO'}")
        print(f"Request Tag: {tag}")
        
        # Print full JSON result
        print("\nFull API Response:")
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure the SonnyLabs MCP server is running and API credentials are properly set.")


if __name__ == "__main__":
    main()
