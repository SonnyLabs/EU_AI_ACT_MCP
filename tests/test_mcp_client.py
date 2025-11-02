#!/usr/bin/env python3
"""
Test MCP client to verify the server is working correctly
"""
import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp_server():
    """Test connecting to the MCP server and listing resources"""
    
    server_params = StdioServerParameters(
        command="/Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP/venv/bin/python",
        args=["/Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP/main.py"],
        env={}
    )
    
    print("=" * 60)
    print("Testing EU AI Act MCP Server Connection")
    print("=" * 60)
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            print("\n✓ Successfully connected to MCP server")
            
            # List available resources
            resources = await session.list_resources()
            
            print(f"\n📚 Found {len(resources.resources)} resource(s):")
            for resource in resources.resources:
                print(f"\n  Resource: {resource.name}")
                print(f"  URI: {resource.uri}")
                print(f"  Description: {resource.description[:100]}...")
                print(f"  MIME Type: {resource.mimeType}")
            
            # Try to read the first resource
            if resources.resources:
                first_resource = resources.resources[0]
                print(f"\n📖 Reading resource: {first_resource.uri}")
                
                content = await session.read_resource(first_resource.uri)
                
                print(f"\n✓ Resource content retrieved successfully!")
                print(f"  Length: {len(content.contents[0].text)} characters")
                
                # Parse and show a sample
                data = json.loads(content.contents[0].text)
                print(f"\n  Sample - AI Interaction Disclosure (English/Simple):")
                print(f"  \"{data['ai_interaction']['en']['simple']}\"")
                
            print("\n✅ All tests passed!")

if __name__ == "__main__":
    asyncio.run(test_mcp_server())
