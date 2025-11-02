# Testing EU AI Act MCP Server Tools

## ✅ Step 1 Complete: `label_news_text` Tool (Article 50(4))

### What Was Added:
1. **Resource**: `deepfake_labels.json` - Contains AI-generated content labels
2. **Tool**: `label_news_text()` - Adds disclosures to AI-generated news articles

### Local Testing (Completed ✅):
```bash
./venv/bin/python test_label_news_text.py
```

---

## Testing in Claude Desktop

### 1. Update Claude Desktop Configuration

Add the MCP server to your Claude Desktop config file:

**Location**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Add this configuration**:
```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP/venv/bin/python",
      "args": [
        "-m",
        "mcp.server.stdio",
        "server:mcp"
      ],
      "cwd": "/Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP"
    }
  }
}
```

### 2. Restart Claude Desktop
- Quit Claude Desktop completely
- Reopen it

### 3. Test the Tool in Claude Desktop

In a new conversation, ask Claude:

```
Can you use the label_news_text tool to label this news article?

"Scientists discover breakthrough in renewable energy. New solar panels achieve 45% efficiency."

Please label it without a human editor, in English.
```

**Expected Output**: Claude should call the `label_news_text` tool and return the labeled text with the disclosure.

### 4. Test the Deepfake Labels Tool in Claude Desktop

**Note**: Direct resource URIs don't always work in Claude Desktop. Instead, use this tool:

Ask Claude:
```
Use the get_deepfake_label_templates tool to show me all available deepfake labels in English.
```

**Expected Output**: Claude should call the tool and return all available labels for text, image, video, and audio content.

---

## Testing in Windsurf (Cascade)

### 1. Update Windsurf MCP Configuration

Windsurf uses the same configuration format as Claude Desktop.

**Location**: Check your Windsurf settings for the MCP server configuration location (usually similar to Claude Desktop).

**Add the same configuration**:
```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP/venv/bin/python",
      "args": [
        "-m",
        "mcp.server.stdio",
        "server:mcp"
      ],
      "cwd": "/Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP"
    }
  }
}
```

### 2. Restart Windsurf
- Close Windsurf
- Reopen it

### 3. Test in Windsurf

In the AI assistant panel, ask:
```
Use the label_news_text tool to add an AI disclosure to this article:

"The mayor announced new infrastructure plans today."

Set has_human_editor to true and editor_name to "John Doe".
```

---

## Quick Test Commands

### Test Tool Directly (Python):
```bash
cd /Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP
./venv/bin/python test_label_news_text.py
```

### Test Server Startup:
```bash
cd /Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP
./venv/bin/python main.py
```
(Press Ctrl+C to stop)

---

## Available Tools So Far

| Tool Name | Article | Status | Description |
|-----------|---------|--------|-------------|
| `get_ai_interaction_disclosure` | 50(1) | ✅ | AI chatbot disclosure |
| `get_emotion_recognition_disclosure` | 50(3) | ✅ | Emotion recognition disclosure |
| `get_deepfake_label_templates` | 50(2)/50(4) | ✅ NEW | Get all available labels |
| `label_news_text` | 50(4) | ✅ NEW | Label AI-generated news |

## Available Resources So Far

| Resource URI | Status | Description |
|--------------|--------|-------------|
| `disclosure-templates://ai-interaction-and-emotion` | ✅ | AI interaction & emotion templates |
| `deepfake-labels://content-labeling` | ✅ NEW | Deepfake and AI content labels |

---

## Next Tool to Implement

The next simplest tool will be **`watermark_text`** (Article 50(2)) - adds metadata to AI-generated text.

This will be purely text-based (no media processing), making it the next easiest to implement.
