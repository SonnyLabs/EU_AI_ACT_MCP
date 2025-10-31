# SonnyLabs MCP Server for Prompt Injection Detection

This MCP (Model Context Protocol) server integrates with the SonnyLabs API to provide prompt injection detection capabilities that can be used with other MCP servers.

## Features

- **Detection API**: Detect prompt injections in text using SonnyLabs AI security API
- **MCP Security Proxy**: Intercept and scan communications between MCP clients and servers to detect hidden prompt injections
- **Cross-server protection**: Secure multiple MCP servers accessed through the same client
- **Configurable detection threshold**: Adjust sensitivity based on your security requirements
- **Flexible response options**: Block or just log detected injections
- **Request tagging**: Track related analyses with unique identifiers

## Setup

1. First, install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Set up your SonnyLabs API credentials:

   - Copy the `.env` file and fill in your API credentials:
   - Replace `your_api_token_here` with your actual SonnyLabs API token
   - Replace `your_analysis_id_here` with your actual SonnyLabs Analysis ID

3. Register for SonnyLabs credentials if you don't have them:
   - Go to https://sonnylabs-service.onrender.com and register
   - Confirm your email address and login to your new SonnyLabs account
   - Get a SonnyLabs API token from the API Keys section
   - Create a new analysis and get the analysis ID from the URL

## Usage

### Running the MCP Server

To start the MCP server:

```bash
python server.py
```

The server will start on `localhost:8000` by default.

### Using the Prompt Injection Detection Tool

The MCP server provides a tool called `detect_prompt_injection` that analyzes text for potential prompt injection attacks.

Example usage within another MCP application:

```python
# Assuming you have the MCP client connected to this server
result = mcp_client.call_tool("detect_prompt_injection", text="Your text to analyze")

# Check the prompt injection score
injection_score = result["analysis"][0]["result"]
print(f"Prompt injection score: {injection_score}")

# The result includes a unique tag for tracking related analyses
tag = result["tag"]
```

### Parameters

The `detect_prompt_injection` tool accepts the following parameters:

- `text` (required): The text to analyze for prompt injection
- `threshold` (optional, default: 0.65): Threshold above which to consider prompt injection detected
- `tag` (optional): A unique identifier for linking related analyses

### Response Format

The tool returns a JSON object with the following structure:

```json
{
  "analysis": [
    {
      "type": "score",
      "name": "prompt_injection",
      "result": 0.99  // Score between 0.0 and 1.0
    }
  ],
  "tag": "unique-request-identifier"
}
```

## Example Implementation

Here's an example of how to use this MCP server to check for prompt injections in another MCP application:

```python
from mcp.client import MCPClient

# Connect to the SonnyLabs MCP server
sonnylabs_mcp = MCPClient("http://localhost:8000")

def check_for_prompt_injection(user_input):
    """
    Check if user input contains a prompt injection attempt.
    
    Args:
        user_input: The text to check
        
    Returns:
        bool: True if prompt injection is detected, False otherwise
    """
    try:
        result = sonnylabs_mcp.call_tool("detect_prompt_injection", text=user_input)
        score = result["analysis"][0]["result"]
        
        # Usually a score above 0.65 indicates a prompt injection attempt
        if score > 0.65:
            print(f"Prompt injection detected with score: {score}")
            return True
        return False
    except Exception as e:
        print(f"Error checking for prompt injection: {e}")
        # Fail open or closed based on your security requirements
        return False
```

## MCP Security Proxy

The MCP Security Proxy allows you to detect hidden prompt injections in communications between MCP clients and other MCP servers. It works as a middleware that intercepts and analyzes all tool calls before they're sent to the target servers.

### Using the MCP Security Proxy

To use the MCP Security Proxy, simply wrap your existing MCP client:

```python
from mcp.client import YourMCPClient  # Your actual MCP client import
from mcp_proxy import secure_mcp_client

# Create your regular MCP client
client = YourMCPClient("http://some-mcp-server.com")

# Wrap it with the security proxy
secure_client = secure_mcp_client(
    client,
    threshold=0.65,  # Adjust sensitivity as needed
    block_injections=True,  # Set to False to log but not block
    callback=lambda text, score, tag: print(f"Injection detected: {text} (score: {score})")
)

# Use secure_client as you would normally use client
# All calls will be automatically scanned for prompt injections
result = secure_client.call_tool("some_tool", text="Your input here")
```

### How It Works

The MCP Security Proxy:

1. Intercepts all tool calls made through the MCP client
2. Extracts all text content from the parameters, including nested parameters
3. Analyzes the extracted text for potential prompt injections using the SonnyLabs API
4. Either blocks the request (if `block_injections=True`) or allows it but logs the detection
5. Forwards clean requests to the target MCP server

### Detecting Hidden Prompt Injections

The proxy can detect various types of prompt injections, including:

- **Obvious injections**: Direct attempts like "Ignore previous instructions"
- **Hidden injections**: Injections disguised within normal-looking content
- **Nested parameter injections**: Injections hidden within complex parameter structures

### Running the Example

To try out the MCP Security Proxy:

```bash
python example_proxy_usage.py
```

This will demonstrate how the proxy detects various types of prompt injections in tool calls.

## Security Considerations

- Always validate and sanitize user inputs before passing them to LLMs
- Use the MCP Security Proxy to protect all communications between MCP clients and servers
- The detection system may produce false positives or false negatives
- Consider implementing different thresholds for different types of applications
- Use this tool as part of a defense-in-depth strategy
- Monitor and log all detected injection attempts
