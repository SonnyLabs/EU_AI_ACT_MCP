# EU AI Act Compliance MCP Server v2 🇪🇺

**Plugin-Based Architecture | 8 Consolidated Tools | Extensible Framework**

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server providing **EU AI Act compliance tools** with a modern plugin architecture. This server helps developers of AI applications meet transparency, security, and governance requirements.

## 🎯 What's New in v2?

### **17 Tools → 8 Tools** (Consolidated)

The new plugin architecture consolidates similar tools:

- **4 watermarking tools** → 1 `watermark_content` tool
- **4 deepfake labeling tools** → 1 `label_deepfake` tool  
- **2 disclosure tools** → 1 `get_disclosure` tool
- **7 other tools** remain unchanged

### **Plugin-Based Architecture**

- ✅ **Modular**: Each compliance area is a separate plugin
- ✅ **Extensible**: Add new plugins without modifying core code
- ✅ **Maintainable**: Isolated concerns, easier debugging
- ✅ **Auto-discovery**: Plugins load automatically

## 📦 What's Included

### 🔧 8 Consolidated Tools

#### **Risk & Role Classification (3 tools)**
- ✅ `classify_ai_system_risk` - Determine risk level (Articles 5, 6, 50)
- ✅ `check_prohibited_practices` - Check Article 5 violations
- ✅ `determine_eu_ai_act_role` - Identify your role (Article 3)

#### **Transparency & Disclosure (2 tools)**
- ✅ `get_disclosure` - **NEW!** Unified disclosures (Article 50(1) & 50(3))
- ✅ `get_deepfake_label_templates` - Access all label templates

#### **Content Watermarking (1 tool)**
- ✅ `watermark_content` - **NEW!** Unified watermarking for text/image/video/audio (Article 50(2))

#### **Deepfake Labeling (1 tool)**
- ✅ `label_deepfake` - **NEW!** Unified labeling for all content types (Article 50(4))

#### **AI Security (2 tools)**
- ✅ `scan_for_prompt_injection` - Detect prompt attacks (Article 15)
- ✅ `check_sensitive_file_access` - Monitor file access (Articles 10 & 15)

### 🔌 6 Plugins

Each plugin handles a specific compliance area:

1. **TransparencyPlugin** - Article 50 disclosures
2. **WatermarkingPlugin** - Article 50(2) watermarking
3. **DeepfakePlugin** - Article 50(4) labeling
4. **RiskClassificationPlugin** - Articles 5, 6 risk assessment
5. **RoleDeterminationPlugin** - Article 3 role identification
6. **SecurityPlugin** - Article 15 cybersecurity

### 📚 4 Resources

- ✅ `disclosure-templates://ai-interaction-and-emotion`
- ✅ `deepfake-labels://content-labeling`
- ✅ `article50-rules://official-text`
- ✅ `watermark-config://technical-standards`

## 🚀 Quick Start

### 1. Installation

```bash
cd /path/to/EU_AI_ACT_MCP
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Test the Plugin System

```bash
python test_plugins.py
```

You should see:
```
======================================================================
EU AI ACT MCP SERVER - PLUGIN SYSTEM TESTS
======================================================================
✓ Loaded 6 plugins
✓ Registered 9 tools
✓ Registered 4 resources
✓ All consolidated tools working
✓ Plugin system is ready for production!
```

### 3. Server Configuration Options

The MCP server supports multiple connection modes:

#### Default: STDIO Mode
```bash
python main.py
```
Used for local AI assistants (Claude Desktop, Windsurf) via stdio communication.

#### HTTP Mode (for web applications)
```bash
python main.py --http
```
Server runs on `http://127.0.0.1:8001/mcp` by default.

#### Custom HTTP Host/Port
```bash
python main.py --http --host 0.0.0.0 --port 8080
```

#### Command Line Options
- `--stdio`: Run in stdio mode (default for AI assistants)
- `--http`: Run in HTTP mode (default for web applications)
- `--host HOST`: HTTP host (default: 127.0.0.1)
- `--port PORT`: HTTP port (default: 8001)

#### View Help
```bash
python main.py --help
```

### 4. Configure Your AI Assistant

#### Claude Desktop

Edit `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/path/to/venv/bin/python",
      "args": ["/path/to/main.py"]
    }
  }
}
```

**Important:** Use absolute paths, not relative paths! For HTTP mode, ensure the Python executable can access the main.py file.

#### Windsurf

Edit `~/.codeium/windsurf/mcp_config.json`:

**STDIO Mode (default):**
```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/path/to/venv/bin/python",
      "args": ["/path/to/main.py"],
      "env": {
        "SONNYLABS_API_TOKEN": "your_token",
        "SONNYLABS_ANALYSIS_ID": "your_id"
      }
    }
  }
}
```

**HTTP Mode (for web integration):**
```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "python",
      "args": ["/path/to/main.py", "--http"],
      "env": {
        "SONNYLABS_API_TOKEN": "your_token",
        "SONNYLABS_ANALYSIS_ID": "your_id"
      }
    }
  }
}
```

### 5. Test It Works

Ask your AI assistant:

```
Use list_plugins to show me all available plugins
```

## 💡 How to Use the New Tools

### Consolidated Tool Examples

#### 1. Watermark Content (replaces 4 tools)

**Before (v1):**
```
Use watermark_text to watermark this article
Use watermark_image for this AI image
Use watermark_video for this AI video
Use watermark_audio for this AI audio
```

**After (v2):**
```
Use watermark_content with content_type="text" to watermark this article
Use watermark_content with content_type="image" for this AI image
Use watermark_content with content_type="video" for this AI video
Use watermark_content with content_type="audio" for this AI audio
```

#### 2. Label Deepfakes (replaces 4 tools)

**Before (v1):**
```
Use label_image_deepfake for this AI image
Use label_video_deepfake for this AI video
Use label_audio_deepfake for this AI audio
Use label_news_text for this AI article
```

**After (v2):**
```
Use label_deepfake with content_type="image" for this AI image
Use label_deepfake with content_type="video" for this AI video
Use label_deepfake with content_type="audio" for this AI audio
Use label_deepfake with content_type="text" for this AI article
```

#### 3. Get Disclosures (replaces 2 tools)

**Before (v1):**
```
Use get_ai_interaction_disclosure for chatbot
Use get_emotion_recognition_disclosure for emotion AI
```

**After (v2):**
```
Use get_disclosure with disclosure_type="ai_interaction" for chatbot
Use get_disclosure with disclosure_type="emotion_recognition" for emotion AI
```

### Detailed Examples

#### Watermark AI-Generated Text

```
Use watermark_content to watermark this text:
- content_type: "text"
- text_content: "This article discusses quantum computing advances..."
- generator: "GPT-4"
- format_type: "markdown"
```

#### Label AI-Generated Image

```
Use label_deepfake to label this image:
- content_type: "image"
- content_description: "AI-generated portrait photo"
- is_artistic_work: false
- language: "en"
```

#### Get Chatbot Disclosure

```
Use get_disclosure to get chatbot disclosure:
- disclosure_type: "ai_interaction"
- language: "en"
- style: "simple"
```

## 📖 Documentation

- **[PLUGIN_ARCHITECTURE.md](PLUGIN_ARCHITECTURE.md)** - Complete plugin system guide
- **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)** - v1 → v2 migration instructions
- **[README.md](README.md)** - Original v1 documentation

## 🔌 Creating Custom Plugins

### Simple Example

```python
# plugins/my_custom_plugin.py

from typing import Dict, Any
from .base import BasePlugin

class MyCustomPlugin(BasePlugin):
    def get_name(self) -> str:
        return "MyCustomPlugin"
    
    def get_description(self) -> str:
        return "Provides custom compliance tools"
    
    def get_tools(self) -> Dict[str, Any]:
        return {
            "my_custom_tool": self.my_custom_tool
        }
    
    def my_custom_tool(self, param: str) -> Dict[str, Any]:
        """My custom compliance tool"""
        return {
            "result": f"Processed: {param}",
            "compliance": "Custom compliance check"
        }
```

**That's it!** The plugin will be auto-discovered and loaded.

## 📋 Tool Reference

### Consolidated Tools

#### `watermark_content`

Watermark AI-generated content (text, image, video, audio).

**Parameters:**
- `content_type`: "text" | "image" | "video" | "audio"
- `content_description`: Brief description
- `generator`: AI system name (default: "AI")
- `format_type`: Output format (optional)
- `text_content`: Actual text (required for text only)

#### `label_deepfake`

Label AI-generated or manipulated content.

**Parameters:**
- `content_type`: "text" | "image" | "video" | "audio"
- `content_description`: Brief description
- `is_artistic_work`: Boolean (default: False)
- `is_satirical`: Boolean (default: False)
- `language`: Language code (default: "en")
- `text_content`: Actual text (required for text only)
- `has_human_editor`: Boolean (for text only)
- `editor_name`: String (for text only)

#### `get_disclosure`

Get transparency disclosure text.

**Parameters:**
- `disclosure_type`: "ai_interaction" | "emotion_recognition"
- `language`: Language code (default: "en")
- `style`: Disclosure style (default: "simple")

### Unchanged Tools

These work exactly the same as v1:

- `classify_ai_system_risk`
- `check_prohibited_practices`
- `determine_eu_ai_act_role`
- `get_deepfake_label_templates`
- `scan_for_prompt_injection`
- `check_sensitive_file_access`

## 🎯 Benefits of v2

### For Users
- ✅ **Fewer tools** to remember (8 vs 17)
- ✅ **Consistent API** across similar tools
- ✅ **Same functionality** with better organization

### For Developers
- ✅ **Easier to extend** - add plugins without touching core
- ✅ **Easier to test** - test plugins independently
- ✅ **Easier to maintain** - changes are isolated
- ✅ **Better code organization** - clear separation of concerns

### For Organizations
- ✅ **Customizable** - enable only needed plugins
- ✅ **Auditable** - clear plugin boundaries
- ✅ **Scalable** - add compliance areas as needed

## 🔄 Migration from v1

- **Keep using v1**: Modify `main.py` to use `server.py`  
- **Migrate to v2**: Use `main.py` which uses `server_v2.py` - see [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)

**Key changes:**
- Add `content_type` parameter to watermarking/labeling tools
- Add `disclosure_type` parameter to disclosure tools
- Everything else stays the same

## 📊 Architecture Comparison

### v1 (Monolithic)
```
server.py (1736 lines)
├── 17 tools defined inline
├── 4 resources defined inline
└── No separation of concerns
```

### v2 (Plugin-based)
```
server_v2.py (100 lines)
├── Plugin loading logic
└── Tool/resource registration

plugins/ (6 plugins, ~2000 lines)
├── transparency_plugin.py
├── watermarking_plugin.py
├── deepfake_plugin.py
├── risk_classification_plugin.py
├── role_determination_plugin.py
└── security_plugin.py
```

## 🧪 Testing

### Test All Plugins

```bash
python test_plugins.py
```

### Test Individual Plugin

```python
from plugins.watermarking_plugin import WatermarkingPlugin

plugin = WatermarkingPlugin()
result = plugin.watermark_content(
    content_type="text",
    text_content="Test",
    generator="GPT-4"
)
print(result)
```

## 📚 EU AI Act Coverage

| Article | What It Covers | Plugin |
|---------|----------------|--------|
| **Article 3** | Role definitions | RoleDeterminationPlugin |
| **Article 5** | Prohibited practices | RiskClassificationPlugin |
| **Article 6** | High-risk classification | RiskClassificationPlugin |
| **Article 15** | Cybersecurity | SecurityPlugin |
| **Article 50(1)** | AI interaction disclosure | TransparencyPlugin |
| **Article 50(2)** | Content watermarking | WatermarkingPlugin |
| **Article 50(3)** | Emotion recognition | TransparencyPlugin |
| **Article 50(4)** | Deepfake labeling | DeepfakePlugin |

**Key Deadline**: August 2, 2026 🗓️

## 💬 Support

### Need Help?

- **Plugin System**: See [PLUGIN_ARCHITECTURE.md](PLUGIN_ARCHITECTURE.md)
- **Migration**: See [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)
- **Original Docs**: See [README.md](README.md)

### Want to Contribute?

The plugin system makes contributions easy:

1. Create a new plugin file in `plugins/`
2. Inherit from `BasePlugin`
3. Implement `get_tools()` and/or `get_resources()`
4. Done! It will auto-load

## 📝 Summary

### What You Get

- ✅ **8 consolidated tools** (down from 17)
- ✅ **6 modular plugins** for different compliance areas
- ✅ **Auto-discovery** of new plugins
- ✅ **Same functionality** with better organization
- ✅ **Extensible framework** for future additions

### How to Get Started

1. **Install**: `pip install -r requirements.txt`
2. **Test**: `python test_plugins.py`
3. **Configure**: Configure your AI assistant to use `main.py`
4. **Use**: Ask your AI to use the consolidated tools!

### Compliance Checklist

- [ ] Classify your AI system risk level
- [ ] Determine your role (Provider, Deployer, etc.)
- [ ] Check for prohibited practices
- [ ] Add transparency disclosures
- [ ] Watermark AI-generated content (use `watermark_content`)
- [ ] Label deepfakes (use `label_deepfake`)
- [ ] Implement security scanning
- [ ] Document compliance actions

---

**EU AI Act Compliance MCP Server v2** - Making compliance easier through better architecture.
