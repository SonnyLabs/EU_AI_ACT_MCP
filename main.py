#!/usr/bin/env python3
"""
Basic MCP Server - Main Entry Point

This is the entry point for the MCP server. It imports the server 
from server.py and runs it using the mcp_run function.
"""
from mcp.server.mcp_run import mcp_run

# Import our MCP server instance
from server import mcp

if __name__ == "__main__":
    # Run the MCP server
    # This will start the server and make all tools available via MCP protocol
    mcp_run(mcp)
