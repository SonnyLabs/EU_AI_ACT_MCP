#!/usr/bin/env python3
"""
SonnyLabs MCP Security Proxy main entry point.
"""
from mcp.server.mcp_run import mcp_run

# Import our MCP server
from server import mcp

if __name__ == "__main__":
    # Run the MCP server using the mcp_run function
    mcp_run(mcp)
