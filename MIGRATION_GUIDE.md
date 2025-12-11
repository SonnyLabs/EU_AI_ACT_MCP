# Migration Guide: v1 → v2

## Overview

This guide helps you migrate from the monolithic v1 server to the plugin-based v2 architecture.

## What Changed?

### Summary
- **17 tools → 8 tools** (consolidated similar tools)
- **Monolithic server.py → Plugin architecture**
- **Same functionality, better organization**

## Quick Start

### Option 1: Use New Server (Recommended)

Update your MCP configuration to use `server_v2.py`:

```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/path/to/venv/bin/python",
      "args": [
        "/path/to/server_v2.py"
      ]
    }
  }
}
```

### Option 2: Keep Old Server

The original `server.py` still works. No changes needed if you want to keep using v1.

## Tool Migration Reference

### Watermarking Tools (4 → 1)

#### Before (v1)
```python
# Separate tool for each content type
watermark_text(text_content="...", generator="GPT-4", format_type="markdown")
watermark_image(image_description="...", generator="DALL-E", format_type="png")
watermark_video(video_description="...", generator="AI", format_type="mp4")
watermark_audio(audio_description="...", generator="AI", format_type="mp3")
```

#### After (v2)
```python
# Single unified tool with content_type parameter
watermark_content(
    content_type="text",
    text_content="...",
    generator="GPT-4",
    format_type="markdown"
)

watermark_content(
    content_type="image",
    content_description="...",
    generator="DALL-E",
    format_type="png"
)

watermark_content(
    content_type="video",
    content_description="...",
    generator="AI",
    format_type="mp4"
)

watermark_content(
    content_type="audio",
    content_description="...",
    generator="AI",
    format_type="mp3"
)
```

### Deepfake Labeling Tools (4 → 1)

#### Before (v1)
```python
# Separate tool for each content type
label_image_deepfake(
    image_description="...",
    is_artistic_work=False,
    language="en"
)

label_video_deepfake(
    video_description="...",
    is_artistic_work=False,
    language="en"
)

label_audio_deepfake(
    audio_description="...",
    is_artistic_work=False,
    language="en"
)

label_news_text(
    text_content="...",
    has_human_editor=True,
    editor_name="John Doe",
    language="en"
)
```

#### After (v2)
```python
# Single unified tool with content_type parameter
label_deepfake(
    content_type="image",
    content_description="...",
    is_artistic_work=False,
    language="en"
)

label_deepfake(
    content_type="video",
    content_description="...",
    is_artistic_work=False,
    language="en"
)

label_deepfake(
    content_type="audio",
    content_description="...",
    is_artistic_work=False,
    language="en"
)

label_deepfake(
    content_type="text",
    text_content="...",
    has_human_editor=True,
    editor_name="John Doe",
    language="en"
)
```

### Disclosure Tools (2 → 1)

#### Before (v1)
```python
# Separate tool for each disclosure type
get_ai_interaction_disclosure(language="en", style="simple")
get_emotion_recognition_disclosure(language="en", style="detailed")
```

#### After (v2)
```python
# Single unified tool with disclosure_type parameter
get_disclosure(
    disclosure_type="ai_interaction",
    language="en",
    style="simple"
)

get_disclosure(
    disclosure_type="emotion_recognition",
    language="en",
    style="detailed"
)
```

### Unchanged Tools

These tools work exactly the same in v2:

- ✅ `classify_ai_system_risk`
- ✅ `check_prohibited_practices`
- ✅ `determine_eu_ai_act_role`
- ✅ `get_deepfake_label_templates`
- ✅ `scan_for_prompt_injection`
- ✅ `check_sensitive_file_access`

## Complete Tool Mapping

| v1 Tool Name | v2 Tool Name | Parameters Change |
|--------------|--------------|-------------------|
| `watermark_text` | `watermark_content` | Add `content_type="text"` |
| `watermark_image` | `watermark_content` | Add `content_type="image"` |
| `watermark_video` | `watermark_content` | Add `content_type="video"` |
| `watermark_audio` | `watermark_content` | Add `content_type="audio"` |
| `label_image_deepfake` | `label_deepfake` | Add `content_type="image"` |
| `label_video_deepfake` | `label_deepfake` | Add `content_type="video"` |
| `label_audio_deepfake` | `label_deepfake` | Add `content_type="audio"` |
| `label_news_text` | `label_deepfake` | Add `content_type="text"` |
| `get_ai_interaction_disclosure` | `get_disclosure` | Add `disclosure_type="ai_interaction"` |
| `get_emotion_recognition_disclosure` | `get_disclosure` | Add `disclosure_type="emotion_recognition"` |
| `classify_ai_system_risk` | `classify_ai_system_risk` | No change |
| `check_prohibited_practices` | `check_prohibited_practices` | No change |
| `determine_eu_ai_act_role` | `determine_eu_ai_act_role` | No change |
| `get_deepfake_label_templates` | `get_deepfake_label_templates` | No change |
| `scan_for_prompt_injection` | `scan_for_prompt_injection` | No change |
| `check_sensitive_file_access` | `check_sensitive_file_access` | No change |

## Example Migrations

### Example 1: Watermarking AI Text

**v1 Code:**
```python
result = watermark_text(
    text_content="This is AI-generated content about quantum computing.",
    generator="GPT-4",
    format_type="markdown"
)
```

**v2 Code:**
```python
result = watermark_content(
    content_type="text",  # NEW: specify content type
    text_content="This is AI-generated content about quantum computing.",
    generator="GPT-4",
    format_type="markdown"
)
```

### Example 2: Labeling Deepfake Video

**v1 Code:**
```python
result = label_video_deepfake(
    video_description="AI-generated video of a speech",
    is_artistic_work=False,
    language="en"
)
```

**v2 Code:**
```python
result = label_deepfake(
    content_type="video",  # NEW: specify content type
    content_description="AI-generated video of a speech",
    is_artistic_work=False,
    language="en"
)
```

### Example 3: Getting Chatbot Disclosure

**v1 Code:**
```python
result = get_ai_interaction_disclosure(
    language="en",
    style="simple"
)
```

**v2 Code:**
```python
result = get_disclosure(
    disclosure_type="ai_interaction",  # NEW: specify disclosure type
    language="en",
    style="simple"
)
```

## For AI Assistant Users (Claude, Windsurf, etc.)

### Natural Language Prompts

The AI assistant will understand both old and new syntax. You can use natural language:

**Old way:**
```
Use watermark_text to watermark this AI-generated article
```

**New way (recommended):**
```
Use watermark_content to watermark this AI-generated text article
```

**Both work!** The AI will adapt to the available tools.

## Testing Your Migration

### Step 1: Install v2

```bash
cd /path/to/EU_AI_ACT_MCP
# No new dependencies needed - same requirements.txt
```

### Step 2: Test Server Loads

```bash
python server_v2.py
```

You should see:
```
======================================================================
EU AI Act Compliance MCP Server v2 (Plugin Architecture)
======================================================================
Loaded 6 plugins
Registered 8 tools
Registered 4 resources

Loaded Plugins:
  - TransparencyPlugin: Provides EU AI Act Article 50 transparency disclosures
  - WatermarkingPlugin: Provides EU AI Act Article 50(2) watermarking
  - DeepfakePlugin: Provides EU AI Act Article 50(4) deepfake labeling
  - RiskClassificationPlugin: Provides EU AI Act risk classification
  - RoleDeterminationPlugin: Provides EU AI Act role determination
  - SecurityPlugin: Provides EU AI Act Article 15 cybersecurity tools
======================================================================
```

### Step 3: Test a Tool

```bash
python -c "
from plugins.watermarking_plugin import WatermarkingPlugin

plugin = WatermarkingPlugin()
result = plugin.watermark_content(
    content_type='text',
    text_content='Test content',
    generator='GPT-4'
)
print(result)
"
```

### Step 4: Update MCP Config

Update your Claude Desktop, Windsurf, or Cursor config to use `server_v2.py`.

### Step 5: Test in AI Assistant

Ask your AI assistant:
```
Use list_plugins to show me all available plugins
```

Then test a consolidated tool:
```
Use watermark_content to watermark an AI-generated image description "sunset landscape" from DALL-E
```

## Rollback Plan

If you need to rollback to v1:

1. **Update MCP config** to use `server.py` instead of `server_v2.py`
2. **Restart your AI assistant**
3. **Continue using old tool names**

Both versions will be maintained for compatibility.

## Benefits of Migrating

### Immediate Benefits
- ✅ **Fewer tools to remember** (8 vs 17)
- ✅ **More consistent API** (similar tools work the same way)
- ✅ **Better error messages** (plugin-level validation)

### Long-term Benefits
- ✅ **Easier to extend** (add new plugins without touching core)
- ✅ **Better performance** (lazy loading of plugins)
- ✅ **Future-proof** (plugin system allows for new features)

## Common Issues

### Issue: "Plugin not found"

**Solution:** Make sure all plugin files are in the `plugins/` directory.

### Issue: "Tool already registered"

**Solution:** Check for duplicate tool names across plugins.

### Issue: "Import error"

**Solution:** Ensure `plugins/__init__.py` exists and imports are correct.

### Issue: "Old tool names don't work"

**Solution:** Update to new tool names with `content_type` or `disclosure_type` parameters.

## Support

### Questions?

1. Check `PLUGIN_ARCHITECTURE.md` for detailed documentation
2. Review plugin source code in `plugins/` directory
3. Test with `python server_v2.py` to see loaded plugins

### Found a Bug?

1. Check if it exists in v1 (`server.py`)
2. If v2-specific, check plugin implementation
3. Report with plugin name and tool name

## Summary

**Migration is simple:**

1. Use `server_v2.py` instead of `server.py`
2. Add `content_type` parameter to watermarking and labeling tools
3. Add `disclosure_type` parameter to disclosure tools
4. Everything else stays the same

**Benefits:**
- Fewer tools (8 vs 17)
- Better organization (6 plugins)
- Same functionality
- Easier to extend

**Rollback:**
- Just switch back to `server.py` if needed
- Both versions maintained
