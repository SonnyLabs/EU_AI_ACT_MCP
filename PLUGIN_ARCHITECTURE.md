# EU AI Act MCP Server - Plugin Architecture Guide

## Overview

Version 2 of the EU AI Act MCP Server introduces a **plugin-based architecture** that makes the codebase more maintainable, extensible, and modular.

## Key Improvements

### 1. **Reduced Tool Count: 17 → 8 Tools**

The new architecture consolidates similar tools into unified interfaces:

| Old Tools (v1) | New Tool (v2) | Consolidation |
|----------------|---------------|---------------|
| `watermark_text`<br>`watermark_image`<br>`watermark_video`<br>`watermark_audio` | `watermark_content` | 4 → 1 |
| `label_image_deepfake`<br>`label_video_deepfake`<br>`label_audio_deepfake`<br>`label_news_text` | `label_deepfake` | 4 → 1 |
| `get_ai_interaction_disclosure`<br>`get_emotion_recognition_disclosure` | `get_disclosure` | 2 → 1 |
| Other tools | Kept as-is | 7 tools |

**Total: 8 consolidated tools** (down from 17)

### 2. **Plugin Architecture Benefits**

- ✅ **Modularity**: Each compliance area is a separate plugin
- ✅ **Extensibility**: Add new plugins without modifying core code
- ✅ **Maintainability**: Isolated concerns, easier debugging
- ✅ **Auto-discovery**: Plugins are automatically loaded
- ✅ **Hot-swappable**: Enable/disable plugins dynamically

## Architecture Components

### Core Components

```
plugins/
├── __init__.py              # Plugin system exports
├── base.py                  # BasePlugin class & PluginRegistry
├── loader.py                # Plugin discovery & loading
├── transparency_plugin.py   # Article 50 disclosures
├── watermarking_plugin.py   # Article 50(2) watermarking
├── deepfake_plugin.py       # Article 50(4) labeling
├── risk_classification_plugin.py  # Articles 5, 6
├── role_determination_plugin.py   # Article 3
└── security_plugin.py       # Article 15 security
```

### Plugin System Flow

```
1. Server starts
2. PluginRegistry created
3. load_plugins() discovers all plugins
4. Each plugin is instantiated and registered
5. Tools and resources are extracted from plugins
6. MCP server registers all tools/resources
7. Server ready to handle requests
```

## Creating a New Plugin

### Step 1: Create Plugin File

Create a new file in the `plugins/` directory:

```python
# plugins/my_new_plugin.py

from typing import Dict, Any
from .base import BasePlugin

class MyNewPlugin(BasePlugin):
    """
    Plugin for [describe functionality]
    """
    
    def get_name(self) -> str:
        return "MyNewPlugin"
    
    def get_description(self) -> str:
        return "Provides [describe what it does]"
    
    def get_tools(self) -> Dict[str, Any]:
        return {
            "my_tool_name": self.my_tool_function
        }
    
    def get_resources(self) -> Dict[str, Any]:
        return {
            "my-resource://uri": self.my_resource_function
        }
    
    def my_tool_function(self, param1: str, param2: int = 0) -> Dict[str, Any]:
        """
        Tool description here.
        
        Args:
            param1: Description
            param2: Description
        
        Returns:
            Dictionary with results
        """
        return {
            "result": "success",
            "data": f"Processed {param1} with {param2}"
        }
    
    def my_resource_function(self) -> str:
        """Resource description"""
        return "Resource content here"
```

### Step 2: That's It!

The plugin will be **automatically discovered and loaded** when the server starts. No need to modify any other files.

## Plugin Lifecycle

### Initialization

```python
def initialize(self) -> None:
    """Called when plugin is loaded"""
    # Setup code here
    pass
```

### Shutdown

```python
def shutdown(self) -> None:
    """Called when server is stopping"""
    # Cleanup code here
    pass
```

## Consolidated Tool Usage

### Before (v1): Multiple Tools

```python
# Old way - 4 separate tools
watermark_text(text_content="...", generator="GPT-4")
watermark_image(image_description="...", generator="DALL-E")
watermark_video(video_description="...", generator="AI")
watermark_audio(audio_description="...", generator="AI")
```

### After (v2): Single Tool

```python
# New way - 1 unified tool
watermark_content(content_type="text", text_content="...", generator="GPT-4")
watermark_content(content_type="image", content_description="...", generator="DALL-E")
watermark_content(content_type="video", content_description="...", generator="AI")
watermark_content(content_type="audio", content_description="...", generator="AI")
```

## Tool Consolidation Details

### 1. `watermark_content` (replaces 4 tools)

**Parameters:**
- `content_type`: "text" | "image" | "video" | "audio"
- `content_description`: Description of the content
- `generator`: AI system name (default: "AI")
- `format_type`: Output format (optional, auto-detected)
- `text_content`: Actual text (required only for text)

**Example:**
```python
watermark_content(
    content_type="image",
    content_description="AI-generated landscape",
    generator="DALL-E",
    format_type="png"
)
```

### 2. `label_deepfake` (replaces 4 tools)

**Parameters:**
- `content_type`: "text" | "image" | "video" | "audio"
- `content_description`: Description of the content
- `is_artistic_work`: Boolean (default: False)
- `is_satirical`: Boolean (default: False)
- `language`: Language code (default: "en")
- `text_content`: Actual text (required only for text)
- `has_human_editor`: Boolean (for text only)
- `editor_name`: String (for text only)

**Example:**
```python
label_deepfake(
    content_type="video",
    content_description="AI-generated speech video",
    is_artistic_work=False,
    language="en"
)
```

### 3. `get_disclosure` (replaces 2 tools)

**Parameters:**
- `disclosure_type`: "ai_interaction" | "emotion_recognition"
- `language`: Language code (default: "en")
- `style`: Disclosure style (default: "simple")

**Example:**
```python
get_disclosure(
    disclosure_type="ai_interaction",
    language="en",
    style="detailed"
)
```

## Plugin Management

### List All Plugins

```python
# Use the list_plugins tool
list_plugins()

# Returns:
{
    "total_plugins": 6,
    "plugins": [
        {
            "name": "TransparencyPlugin",
            "description": "Provides EU AI Act Article 50 transparency disclosures",
            "enabled": true,
            "tools": ["get_disclosure", "get_deepfake_label_templates"],
            "resources": ["disclosure-templates://ai-interaction-and-emotion"]
        },
        # ... more plugins
    ],
    "total_tools": 8,
    "total_resources": 4
}
```

## Migration Guide (v1 → v2)

### For Users

**No breaking changes!** All functionality is preserved. The API is slightly different but more intuitive.

#### Tool Name Changes

| v1 Tool | v2 Tool | Change |
|---------|---------|--------|
| `watermark_text` | `watermark_content(content_type="text", ...)` | Add content_type parameter |
| `watermark_image` | `watermark_content(content_type="image", ...)` | Add content_type parameter |
| `watermark_video` | `watermark_content(content_type="video", ...)` | Add content_type parameter |
| `watermark_audio` | `watermark_content(content_type="audio", ...)` | Add content_type parameter |
| `label_image_deepfake` | `label_deepfake(content_type="image", ...)` | Add content_type parameter |
| `label_video_deepfake` | `label_deepfake(content_type="video", ...)` | Add content_type parameter |
| `label_audio_deepfake` | `label_deepfake(content_type="audio", ...)` | Add content_type parameter |
| `label_news_text` | `label_deepfake(content_type="text", ...)` | Add content_type parameter |
| `get_ai_interaction_disclosure` | `get_disclosure(disclosure_type="ai_interaction", ...)` | Add disclosure_type parameter |
| `get_emotion_recognition_disclosure` | `get_disclosure(disclosure_type="emotion_recognition", ...)` | Add disclosure_type parameter |

All other tools remain unchanged.

### For Developers

If you've extended the server, you'll need to:

1. **Convert custom tools to plugins**: Follow the "Creating a New Plugin" guide above
2. **Update imports**: Use `from plugins import BasePlugin` instead of modifying `server.py`
3. **Test**: Run your plugin to ensure it loads correctly

## File Structure Comparison

### v1 (Monolithic)

```
server.py (1736 lines)
├── All 17 tools defined inline
├── All 4 resources defined inline
└── No separation of concerns
```

### v2 (Plugin-based)

```
server_v2.py (100 lines)
├── Plugin loading logic
└── Tool/resource registration

plugins/
├── base.py (150 lines) - Plugin framework
├── loader.py (100 lines) - Auto-discovery
├── transparency_plugin.py (200 lines)
├── watermarking_plugin.py (300 lines)
├── deepfake_plugin.py (300 lines)
├── risk_classification_plugin.py (400 lines)
├── role_determination_plugin.py (300 lines)
└── security_plugin.py (250 lines)
```

**Total: ~2000 lines across 9 files** (vs 1736 lines in 1 file)

## Benefits Summary

### For Users
- ✅ **Simpler API**: Fewer tools to remember
- ✅ **Consistent interface**: Similar tools work the same way
- ✅ **Better documentation**: Each plugin is self-contained

### For Developers
- ✅ **Easier to extend**: Add plugins without touching core
- ✅ **Easier to test**: Test plugins independently
- ✅ **Easier to maintain**: Changes are isolated
- ✅ **Easier to understand**: Clear separation of concerns

### For Organizations
- ✅ **Customizable**: Enable only needed plugins
- ✅ **Auditable**: Clear plugin boundaries
- ✅ **Scalable**: Add compliance areas as needed

## Testing Plugins

### Test Individual Plugin

```python
from plugins.transparency_plugin import TransparencyPlugin

plugin = TransparencyPlugin()
plugin.initialize()

# Test a tool
result = plugin.get_disclosure(
    disclosure_type="ai_interaction",
    language="en",
    style="simple"
)

print(result)
```

### Test Plugin Loading

```python
from plugins import PluginRegistry, load_plugins

registry = PluginRegistry()
load_plugins(registry)

print(f"Loaded {len(registry.get_all_plugins())} plugins")
print(f"Total tools: {len(registry.get_all_tools())}")
```

## Troubleshooting

### Plugin Not Loading

1. **Check file location**: Plugin must be in `plugins/` directory
2. **Check class name**: Must inherit from `BasePlugin`
3. **Check imports**: Must import `BasePlugin` from `.base`
4. **Check syntax**: Python syntax errors prevent loading

### Tool Not Appearing

1. **Check `get_tools()` method**: Must return dictionary
2. **Check tool name**: Must be unique across all plugins
3. **Check function signature**: Must have proper type hints

### Resource Not Appearing

1. **Check `get_resources()` method**: Must return dictionary
2. **Check resource URI**: Must be unique across all plugins
3. **Check function return**: Must return string

## Future Enhancements

Potential additions to the plugin system:

- [ ] Plugin dependencies (plugin A requires plugin B)
- [ ] Plugin versioning
- [ ] Plugin configuration files
- [ ] Plugin hot-reloading (without server restart)
- [ ] Plugin marketplace/registry
- [ ] Plugin sandboxing for security

## Summary

The v2 plugin architecture provides:

- **8 consolidated tools** (down from 17)
- **6 modular plugins** for different compliance areas
- **Auto-discovery** of new plugins
- **Extensible framework** for future additions
- **Same functionality** with better organization

The codebase is now easier to understand, maintain, and extend while providing the same comprehensive EU AI Act compliance coverage.
