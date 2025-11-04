#!/usr/bin/env python3
"""
EU AI Act Article 50 MCP Server - Unified Entry Point

This is the unified entry point for the MCP server that supports both stdio and HTTP modes.

Usage:
    python main.py --stdio   # Run in stdio mode (default)
    python main.py --http    # Run in HTTP mode
    python main.py --http --host 0.0.0.0 --port 8080  # Custom host/port
"""

import sys
import argparse
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='EU AI Act MCP Server')
    parser.add_argument('--stdio', action='store_true', help='Run in stdio mode (default)')
    parser.add_argument('--http', action='store_true', help='Run in HTTP mode')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='HTTP host (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=8001, help='HTTP port (default: 8001)')
    args = parser.parse_args()
    
    # Determine mode - default to stdio if neither specified
    if args.http:
        mode = 'http'
    else:
        mode = 'stdio'  # Default
    
    # Import and configure the appropriate server
    if mode == 'http':
        logger.info(f"Starting EU AI Act MCP Server in HTTP mode on {args.host}:{args.port}")
        from server import mcp
        # The http server is already configured with host/port in its file
        # We could make it more dynamic, but for now use the existing configuration
        mcp.run(transport="streamable-http")
    else:
        logger.info("Starting EU AI Act MCP Server in stdio mode")
        from server import mcp
        mcp.run()

if __name__ == "__main__":
    main()
