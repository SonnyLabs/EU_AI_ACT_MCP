# Quick Start Guide - EU AI Act MCP Server v2

Get up and running with the new plugin-based architecture in 5 minutes.

## Prerequisites

- Python 3.8+
- Git (to clone the repo)

## 1. Install (30 seconds)

```bash
cd /path/to/EU_AI_ACT_MCP
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Test (30 seconds)

```bash
python test_plugins.py
```

Expected output:
```
======================================================================
EU AI ACT MCP SERVER - PLUGIN SYSTEM TESTS
======================================================================
✓ Loaded 6 plugins
✓ Registered 9 tools
✓ Registered 4 resources
✓ All consolidated tools working
======================================================================
ALL TESTS PASSED ✓
======================================================================
```

## 3. Configure Your AI Assistant (2 minutes)

### Claude Desktop

Edit `claude_desktop_config.json`:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["/absolute/path/to/main.py"]
    }
  }
}
```

### Windsurf

Edit `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/absolute/path/to/venv/bin/python",
      "args": ["/absolute/path/to/main.py"]
    }
  }
}
```

**Important:** Use absolute paths, not relative paths!

## 4. Restart Your AI Assistant (30 seconds)

Completely quit and reopen Claude Desktop or Windsurf.

## 5. Test It Works (1 minute)

Ask your AI assistant:

```
Use list_plugins to show me all available plugins
```

You should see:
```json
{
  "total_plugins": 6,
  "plugins": [
    {
      "name": "TransparencyPlugin",
      "description": "Provides EU AI Act Article 50 transparency disclosures",
      "enabled": true,
      "tools": ["get_disclosure", "get_deepfake_label_templates"]
    },
    // ... 5 more plugins
  ],
  "total_tools": 8,
  "total_resources": 4
}
```

## 6. Try a Consolidated Tool (1 minute)

### Watermark AI-Generated Text

Ask your AI assistant:

```
Use watermark_content to watermark this text:
- content_type: "text"
- text_content: "This is an AI-generated article about quantum computing."
- generator: "GPT-4"
- format_type: "markdown"
```

### Label AI-Generated Image

```
Use label_deepfake to label this image:
- content_type: "image"
- content_description: "AI-generated portrait photo"
- is_artistic_work: false
- language: "en"
```

### Get Chatbot Disclosure

```
Use get_disclosure to get a chatbot disclosure:
- disclosure_type: "ai_interaction"
- language: "en"
- style: "simple"
```

## Common Issues & Solutions

### Issue: "Plugin not found"

**Solution:** Check that all plugin files are in the `plugins/` directory:

```bash
ls plugins/
# Should show: __init__.py, base.py, loader.py, and 6 plugin files
```

### Issue: "Import error"

**Solution:** Make sure you're using the virtual environment:

```bash
which python  # Should point to venv/bin/python
```

### Issue: "Tool not working"

**Solution:** Check if the plugin loaded:

```bash
python -c "from plugins import PluginRegistry, load_plugins; r = PluginRegistry(); load_plugins(r); print(f'Loaded {len(r.get_all_plugins())} plugins')"
```

### Issue: "Old tool names don't work"

**Solution:** Update to new tool names. See the mapping:

| Old Tool | New Tool | Change |
|----------|----------|--------|
| `watermark_text` | `watermark_content` | Add `content_type="text"` |
| `label_image_deepfake` | `label_deepfake` | Add `content_type="image"` |
| `get_ai_interaction_disclosure` | `get_disclosure` | Add `disclosure_type="ai_interaction"` |

## What's Different from v1?

### Tool Count: 17 → 8

**Consolidated tools:**
- 4 watermarking tools → 1 `watermark_content`
- 4 deepfake labeling tools → 1 `label_deepfake`
- 2 disclosure tools → 1 `get_disclosure`

**Unchanged tools:**
- `classify_ai_system_risk`
- `check_prohibited_practices`
- `determine_eu_ai_act_role`
- `get_deepfake_label_templates`
- `scan_for_prompt_injection`
- `check_sensitive_file_access`

### New Parameter: `content_type`

When using consolidated tools, specify the content type:

```python
# Watermarking
watermark_content(content_type="text", ...)
watermark_content(content_type="image", ...)
watermark_content(content_type="video", ...)
watermark_content(content_type="audio", ...)

# Labeling
label_deepfake(content_type="text", ...)
label_deepfake(content_type="image", ...)
label_deepfake(content_type="video", ...)
label_deepfake(content_type="audio", ...)

# Disclosures
get_disclosure(disclosure_type="ai_interaction", ...)
get_disclosure(disclosure_type="emotion_recognition", ...)
```

## Next Steps

### Learn More

- **[PLUGIN_ARCHITECTURE.md](PLUGIN_ARCHITECTURE.md)** - Deep dive into the plugin system
- **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)** - Detailed migration instructions
- **[README_V2.md](README_V2.md)** - Complete v2 documentation

### Create a Custom Plugin

```python
# plugins/my_plugin.py

from typing import Dict, Any
from .base import BasePlugin

class MyPlugin(BasePlugin):
    def get_name(self) -> str:
        return "MyPlugin"
    
    def get_description(self) -> str:
        return "My custom compliance plugin"
    
    def get_tools(self) -> Dict[str, Any]:
        return {
            "my_tool": self.my_tool
        }
    
    def my_tool(self, param: str) -> Dict[str, Any]:
        """My custom tool"""
        return {
            "result": f"Processed: {param}",
            "compliance": "Custom check"
        }
```

Save the file and restart the server. Your plugin will be auto-loaded!

### Test Your Plugin

```bash
python -c "
from plugins.my_plugin import MyPlugin

plugin = MyPlugin()
result = plugin.my_tool('test')
print(result)
"
```

## Rollback to v1

If you need to go back to the original version:

1. Update `main.py` to use `server.py` instead of `server_v2.py`
2. Restart your AI assistant
3. Use the old tool names

## Support

### Questions?

1. Check the documentation in this directory
2. Run `python test_plugins.py` to verify setup
3. Test individual plugins with Python

### Found a Bug?

1. Check if it exists in v1 (`server.py`)
2. If v2-specific, identify which plugin
3. Check plugin source code in `plugins/` directory

## Summary

You now have:

✅ **8 consolidated tools** (down from 17)
✅ **6 modular plugins** for different compliance areas
✅ **Auto-discovery** of new plugins
✅ **Same functionality** with better organization
✅ **Extensible framework** for custom plugins

**Time to get started:** ~5 minutes
**Time to master:** Read the docs and experiment!

---

**Welcome to EU AI Act MCP Server v2!** 🎉

The plugin-based architecture makes compliance easier and more maintainable.
