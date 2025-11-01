# server.py
"""
Basic MCP Server Template

This is a minimal MCP (Model Context Protocol) server setup that you can use as a template
for building your own MCP servers with custom tools.
"""

import os
from typing import Dict, Any, List
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables (if needed for future extensions)
load_dotenv()

# Create an MCP server with a name
mcp = FastMCP("BasicMCP")


# Example Tool 1: Simple text processing
@mcp.tool()
def reverse_text(text: str) -> Dict[str, str]:
    """
    Reverses the given text string.
    
    Args:
        text: The text to reverse
        
    Returns:
        A dictionary with the original and reversed text
    """
    return {
        "original": text,
        "reversed": text[::-1]
    }


# Example Tool 2: Math operations
@mcp.tool()
def calculate(operation: str, a: float, b: float) -> Dict[str, Any]:
    """
    Performs basic math operations.
    
    Args:
        operation: The operation to perform (add, subtract, multiply, divide)
        a: First number
        b: Second number
        
    Returns:
        A dictionary with the operation result
    """
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else None
    }
    
    if operation not in operations:
        return {
            "error": f"Unknown operation: {operation}",
            "valid_operations": list(operations.keys())
        }
    
    result = operations[operation]
    if result is None:
        return {"error": "Division by zero"}
    
    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }


# Example Tool 3: String manipulation
@mcp.tool()
def text_stats(text: str) -> Dict[str, Any]:
    """
    Returns statistics about the given text.
    
    Args:
        text: The text to analyze
        
    Returns:
        A dictionary with text statistics
    """
    words = text.split()
    return {
        "character_count": len(text),
        "word_count": len(words),
        "line_count": len(text.split('\n')),
        "uppercase_count": sum(1 for c in text if c.isupper()),
        "lowercase_count": sum(1 for c in text if c.islower()),
        "digit_count": sum(1 for c in text if c.isdigit())
    }