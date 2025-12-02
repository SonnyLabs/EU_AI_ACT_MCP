#!/usr/bin/env python3
"""
EU AI Act Article 50 MCP Server - Main Entry Point

This is the entry point for the MCP server. It imports and runs the FastMCP server.
"""

# Import our MCP server instance
from server import mcp

def main():
    """Main entry point for the MCP server."""
    # Run the MCP server using FastMCP's built-in run method
    # This will start the server and make all tools and resources available via MCP protocol
    mcp.run()

if __name__ == "__main__":
    main()
