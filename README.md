# Basic MCP Server Template

A minimal template for building [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers. Use this as a starting point to create your own MCP servers with custom tools and capabilities.

## What is MCP?

The Model Context Protocol (MCP) is an open standard that enables seamless integration between AI applications and external data sources and tools. MCP servers expose tools that AI assistants can use to perform various tasks.

## Features

This template includes:
- ✅ Basic MCP server setup with FastMCP
- ✅ Three example tools demonstrating different patterns:
  - **Text reversal** - Simple string manipulation
  - **Calculator** - Basic math operations with error handling
  - **Text statistics** - Data analysis and aggregation
- ✅ Minimal dependencies for easy extension
- ✅ Environment variable support with `.env` file
- ✅ Clean, documented code structure

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python main.py
```

The MCP server will start and be ready to accept connections from MCP clients.

### 3. Test the Tools

You can test the server using any MCP client. The following tools are available:

- `reverse_text` - Reverses a text string
- `calculate` - Performs basic math operations (add, subtract, multiply, divide)
- `text_stats` - Returns statistics about text (character count, word count, etc.)

## Project Structure

```
.
├── server.py           # Main server file with tool definitions
├── main.py             # Entry point that runs the server
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project metadata and configuration
├── .env.example        # Example environment variables
└── README.md          # This file
```

## Adding Your Own Tools

To add new tools to your MCP server:

1. Open `server.py`
2. Define a new function with the `@mcp.tool()` decorator:

```python
@mcp.tool()
def your_tool_name(param1: str, param2: int) -> Dict[str, Any]:
    """
    Description of what your tool does.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        A dictionary with the tool results
    """
    # Your tool implementation here
    return {"result": "your_result"}
```

3. Restart the server to make the new tool available

## Adding Resources

MCP servers can also expose resources (data sources). To add resources:

```python
@mcp.resource("resource://your-resource-name")
def get_resource() -> str:
    """Returns resource data"""
    return "Your resource content"
```

## Environment Variables

The template supports environment variables through `.env` files. To use:

1. Copy `.env.example` to `.env`
2. Add your variables:
   ```
   YOUR_API_KEY=your_key_here
   YOUR_CONFIG_VALUE=value_here
   ```
3. Access in code:
   ```python
   import os
   api_key = os.getenv("YOUR_API_KEY")
   ```

## Common Use Cases

This template can be extended for various use cases:

- **API Integrations**: Connect to external APIs and expose them as MCP tools
- **Database Access**: Query databases and return results
- **File Operations**: Read, write, and process files
- **Data Processing**: Transform and analyze data
- **System Operations**: Execute system commands or scripts
- **Custom Business Logic**: Implement domain-specific functionality

## Next Steps

1. **Customize the server name**: Change `FastMCP("BasicMCP")` in `server.py` to your desired name
2. **Remove example tools**: Delete the example tool functions you don't need
3. **Add your tools**: Implement your custom tools following the examples
4. **Update metadata**: Modify `pyproject.toml` with your project details
5. **Add dependencies**: Update `requirements.txt` as you add new functionality

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

## License

This template is provided as-is for you to build upon. Customize and use freely for your projects.
