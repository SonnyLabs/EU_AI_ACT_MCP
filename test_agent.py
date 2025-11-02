"""
Simple Python MCP Tester

Tests a local MCP server by:
1. Connecting via stdio
2. Discovering available tools
3. Testing each tool
4. Reporting results

Usage:
    python mcp_tester.py

Prerequisites:
    pip install mcp
"""

import asyncio
import json
import sys, os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from contextlib import AsyncExitStack

# Add parent directory to path to import server
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class MCPTester:
    """Simple tester for local MCP servers"""
    
    def __init__(self, server_command: str, server_args: list = None):
        """
        Initialize the MCP tester
        
        Args:
            server_command: Command to run the MCP server (e.g., 'node', 'python')
            server_args: Arguments for the server command (e.g., ['server.js'])
        """
        self.server_command = server_command
        self.server_args = server_args or []
        self.session = None
        self.exit_stack = AsyncExitStack()
    
    async def connect(self):
        """Connect to the MCP server"""
        print(f"🔌 Connecting to MCP server...")
        print(f"   Command: {self.server_command}")
        print(f"   Args: {self.server_args}")
        
        try:
            server_params = StdioServerParameters(
                command=self.server_command,
                args=self.server_args,
                env=None
            )
            
            stdio_transport = await self.exit_stack.enter_async_context(
                stdio_client(server_params)
            )
            
            self.stdio, self.write = stdio_transport
            self.session = await self.exit_stack.enter_async_context(
                ClientSession(self.stdio, self.write)
            )
            
            await self.session.initialize()
            print("✅ Connected successfully!\n")
            return True
            
        except Exception as e:
            print(f"❌ Connection failed: {e}\n")
            return False
    
    async def list_tools(self):
        """List all available tools"""
        print("🔧 Discovering available tools...")
        
        try:
            response = await self.session.list_tools()
            
            if not response.tools:
                print("   No tools found")
                return []
            
            print(f"   Found {len(response.tools)} tool(s):\n")
            
            for tool in response.tools:
                print(f"   📌 {tool.name}")
                print(f"      Description: {tool.description}")
                
                if hasattr(tool, 'inputSchema') and tool.inputSchema:
                    schema = tool.inputSchema
                    if 'properties' in schema:
                        print(f"      Parameters:")
                        for param_name, param_info in schema['properties'].items():
                            param_type = param_info.get('type', 'unknown')
                            param_desc = param_info.get('description', 'No description')
                            required = param_name in schema.get('required', [])
                            req_marker = " (required)" if required else ""
                            print(f"        - {param_name} ({param_type}){req_marker}: {param_desc}")
                print()
            
            return response.tools
            
        except Exception as e:
            print(f"❌ Failed to list tools: {e}\n")
            return []
    
    async def test_tool(self, tool_name: str, arguments: dict):
        """
        Test a specific tool with given arguments
        
        Args:
            tool_name: Name of the tool to test
            arguments: Dictionary of arguments to pass to the tool
        """
        print(f"🧪 Testing tool: {tool_name}")
        print(f"   Arguments: {json.dumps(arguments, indent=2)}")
        
        try:
            response = await self.session.call_tool(tool_name, arguments)
            
            print(f"   ✅ Success!")
            print(f"   Response:")
            
            for content in response.content:
                if content.type == "text":
                    print(f"      {content.text}")
                else:
                    print(f"      {content}")
            
            print()
            return True
            
        except Exception as e:
            print(f"   ❌ Failed: {e}\n")
            return False
    
    async def list_resources(self):
        """List all available resources"""
        print("📚 Discovering available resources...")
        
        try:
            response = await self.session.list_resources()
            
            if not response.resources:
                print("   No resources found\n")
                return []
            
            print(f"   Found {len(response.resources)} resource(s):\n")
            
            for resource in response.resources:
                print(f"   📄 {resource.uri}")
                print(f"      Name: {resource.name}")
                print(f"      Description: {resource.description}")
                print(f"      MIME Type: {resource.mimeType if hasattr(resource, 'mimeType') else 'N/A'}")
                print()
            
            return response.resources
            
        except Exception as e:
            print(f"❌ Failed to list resources: {e}\n")
            return []
    
    async def list_prompts(self):
        """List all available prompts"""
        print("💬 Discovering available prompts...")
        
        try:
            response = await self.session.list_prompts()
            
            if not response.prompts:
                print("   No prompts found\n")
                return []
            
            print(f"   Found {len(response.prompts)} prompt(s):\n")
            
            for prompt in response.prompts:
                print(f"   💭 {prompt.name}")
                print(f"      Description: {prompt.description}")
                if hasattr(prompt, 'arguments') and prompt.arguments:
                    print(f"      Arguments: {[arg.name for arg in prompt.arguments]}")
                print()
            
            return response.prompts
            
        except Exception as e:
            print(f"❌ Failed to list prompts: {e}\n")
            return []
    
    async def get_server_info(self):
        """Get server information"""
        print("ℹ️  Server Information:")
        
        if hasattr(self.session, '_server_info'):
            info = self.session._server_info
            print(f"   Name: {getattr(info, 'name', 'Unknown')}")
            print(f"   Version: {getattr(info, 'version', 'Unknown')}")
        else:
            print("   Server info not available")
        print()
    
    async def disconnect(self):
        """Disconnect from the MCP server"""
        print("👋 Disconnecting...")
        await self.exit_stack.aclose()
        print("✅ Disconnected\n")


async def main():
    """
    Main test function - customize this for your MCP server
    """
    
    print("=" * 70)
    print("MCP Server Tester")
    print("=" * 70)
    print()
    
    # ========================================================================
    # CONFIGURE YOUR MCP SERVER HERE
    # ========================================================================
    
    # Example : Python MCP server
    tester = MCPTester(
        server_command="python",
        server_args=["./main.py"]
    )
    
    # ========================================================================
    # RUN TESTS
    # ========================================================================
    
    # Connect to server
    if not await tester.connect():
        return
    
    try:
        # Get server info
        await tester.get_server_info()
        
        # List all capabilities
        tools = await tester.list_tools()
        resources = await tester.list_resources()
        prompts = await tester.list_prompts()
        
        # Test tools (customize these based on your server's tools)
        if tools:
            print("=" * 70)
            print("Testing Tools")
            print("=" * 70)
            print()
            
            # Example tool tests - customize for your server
            # await tester.test_tool("calculator", {"operation": "add", "a": 5, "b": 3})
            # await tester.test_tool("get_weather", {"city": "New York"})
            
            print("💡 Add your tool tests in the main() function\n")
        
        # Summary
        print("=" * 70)
        print("Test Summary")
        print("=" * 70)
        print(f"✅ Tools discovered: {len(tools)}")
        print(f"✅ Resources discovered: {len(resources)}")
        print(f"✅ Prompts discovered: {len(prompts)}")
        print()
        
    finally:
        await tester.disconnect()


if __name__ == "__main__":
    print("""
    MCP Server Tester
    =================
    
    This script tests a local MCP server by:
    1. Connecting via stdio
    2. Discovering available tools, resources, and prompts
    3. Testing tools with sample inputs
    
    Setup:
    1. Install: pip install mcp
    2. Edit the main() function to configure your server path
    3. Add tool tests with your server's actual tools
    4. Run: python mcp_tester.py
    
    """)
    
    asyncio.run(main())