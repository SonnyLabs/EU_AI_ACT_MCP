"""
EU AI Act Article 50 Compliance MCP Server (v2 - Plugin Architecture)

This MCP server provides tools and resources for EU AI Act Article 50 compliance,
including transparency obligations for AI systems.

Version 2 Features:
- Plugin-based architecture for extensibility
- Consolidated tools (17 tools -> 8 tools)
- Auto-discovery of plugins
- Easier to maintain and extend
"""

import os
from fastmcp import FastMCP
from dotenv import load_dotenv

# Import plugin system
from plugins import PluginRegistry, load_plugins

# Load environment variables
load_dotenv()

# Create an MCP server with a name
mcp = FastMCP("EU_AI_ACT_MCP")

# Create plugin registry
registry = PluginRegistry()

# Load all plugins from the plugins directory
load_plugins(registry)

# ============================================================================
# REGISTER TOOLS FROM PLUGINS
# ============================================================================

# Get all tools from plugins and register them with the MCP server
all_tools = registry.get_all_tools()

for tool_name, tool_func in all_tools.items():
    # Register each tool with the MCP server
    mcp.tool()(tool_func)

# ============================================================================
# REGISTER RESOURCES FROM PLUGINS
# ============================================================================

# Get all resources from plugins and register them with the MCP server
all_resources = registry.get_all_resources()

for resource_uri, resource_func in all_resources.items():
    # Register each resource with the MCP server
    mcp.resource(resource_uri)(resource_func)

# ============================================================================
# PLUGIN MANAGEMENT TOOL
# ============================================================================

@mcp.tool()
def list_plugins() -> dict:
    """
    List all loaded plugins and their capabilities.
    
    Returns information about each plugin including:
    - Plugin name
    - Description
    - Tools provided
    - Resources provided
    - Enabled status
    
    Returns:
        Dictionary with plugin information
    """
    plugins_info = registry.list_plugins()
    
    return {
        "total_plugins": len(plugins_info),
        "plugins": plugins_info,
        "total_tools": len(registry.get_all_tools()),
        "total_resources": len(registry.get_all_resources()),
        "plugin_directory": os.path.join(os.path.dirname(__file__), "plugins"),
        "usage": "Plugins are automatically loaded from the plugins directory"
    }


# ============================================================================
# SERVER INFO
# ============================================================================

print("=" * 70)
print("EU AI Act Compliance MCP Server v2 (Plugin Architecture)")
print("=" * 70)
print(f"Loaded {len(registry.get_all_plugins())} plugins")
print(f"Registered {len(all_tools)} tools")
print(f"Registered {len(all_resources)} resources")
print("\nLoaded Plugins:")
for plugin in registry.get_all_plugins():
    print(f"  - {plugin.get_name()}: {plugin.get_description()}")
print("=" * 70)
