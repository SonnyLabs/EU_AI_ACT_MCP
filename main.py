#!/usr/bin/env python3
"""
EU AI Act Article 50 MCP Server - Main Entry Point

This is the entry point for the MCP server. It imports and runs the FastMCP server.
"""

# Import our MCP server instance
import argparse
from server import mcp
import uvicorn
from starlette.middleware.cors import CORSMiddleware

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='EU AI Act MCP Server')
    parser.add_argument('--stdio', action='store_true', help='Run in stdio mode (default)')
    parser.add_argument('--http', action='store_true', help='Run in HTTP mode')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='HTTP host (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=8001, help='HTTP port (default: 8001)')
    args = parser.parse_args()
    if args.http:
        # Get the Starlette app for streamable HTTP
        starlette_app = mcp.streamable_http_app()

        starlette_app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Allow all origins for development; restrict in production
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Run the server
        uvicorn.run(starlette_app, host=args.host, port=args.port)


        
else:
    mcp = FastMCP("EU_AI_ACT_MCP")



    # Run the MCP server using FastMCP's built-in run method
    # This will start the server and make all tools and resources available via MCP protocol
    mcp.run()
