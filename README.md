# EU AI Act Article 50 Compliance MCP Server

An [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that provides **automated EU AI Act Article 50 compliance** for AI systems. This server helps AI agents and applications meet transparency obligations for AI-generated content, AI interactions, and deepfake/synthetic media.

## What is This Server?

This MCP server implements **EU AI Act Article 50** transparency obligations as **automated tools** that AI agents can call to ensure compliance. Instead of manually adding disclosures and labels, AI systems can use these tools to automatically:

- ✅ Add chatbot interaction disclosures (Article 50(1))
- ✅ Add emotion recognition disclosures (Article 50(3))
- ✅ Label AI-generated news and text content (Article 50(4))
- ✅ Access pre-written disclosure templates in 24+ languages
- ✅ Get deepfake/synthetic content labels for all media types

**Compliance Deadline**: August 2, 2026

## Features

### 🔧 Tools (4 Implemented, 6 More Planned)

**Currently Available:**
- ✅ **get_ai_interaction_disclosure** - Get chatbot/AI interaction disclosure text (Article 50(1))
- ✅ **get_emotion_recognition_disclosure** - Get emotion recognition system disclosure (Article 50(3))
- ✅ **get_deepfake_label_templates** - Access all deepfake and AI content labels (Article 50(2)/50(4))
- ✅ **label_news_text** - Label AI-generated news articles and text (Article 50(4))

**Coming Soon:**
- ⏳ **watermark_text** - Add metadata to AI-generated text (Article 50(2))
- ⏳ **watermark_image** - Add C2PA watermarks to images (Article 50(2))
- ⏳ **watermark_video** - Add C2PA watermarks to videos (Article 50(2))
- ⏳ **watermark_audio** - Add audio fingerprints (Article 50(2))
- ⏳ **label_image_deepfake** - Label AI-generated images (Article 50(4))
- ⏳ **label_video_deepfake** - Label AI-generated videos (Article 50(4))
- ⏳ **label_audio_deepfake** - Label AI-generated audio (Article 50(4))

### 📚 Resources (2 Implemented, 2 More Planned)

**Currently Available:**
- ✅ **disclosure-templates://ai-interaction-and-emotion** - Pre-written disclosure text (AI interaction & emotion recognition)
- ✅ **deepfake-labels://content-labeling** - Pre-written labels for deepfakes and AI content

**Coming Soon:**
- ⏳ **watermark-config://c2pa-iptc** - C2PA and IPTC watermarking configuration
- ⏳ **article50-rules://compliance** - Official Article 50 text and compliance rules

### 🌍 Multi-Language Support

All disclosures and labels available in:
- 🇬🇧 English (en)
- 🇪🇸 Spanish (es)
- 🇫🇷 French (fr)
- 🇩🇪 German (de)
- 🇮🇹 Italian (it) - disclosure templates only

## Quick Start

### 1. Clone and Install

```bash
git clone <your-repo-url>
cd EU_AI_ACT_MCP
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Test Locally

```bash
# Test the server starts without errors
./venv/bin/python main.py

# Run tool tests (in another terminal)
./venv/bin/python test_label_news_text.py
./venv/bin/python test_deepfake_labels.py
```

### 3. Configure Claude Desktop or Windsurf

See [Setup for Claude Desktop](#setup-for-claude-desktop) or [Setup for Windsurf](#setup-for-windsurf) below.

## Project Structure

```
.
├── server.py                      # Main MCP server with all tools and resources
├── main.py                        # Entry point that runs the server
├── disclosure_templates.json      # Pre-written disclosure text (50(1), 50(3))
├── deepfake_labels.json          # Pre-written deepfake/AI content labels (50(4))
├── requirements.txt              # Python dependencies
├── pyproject.toml                # Project metadata
├── test_label_news_text.py       # Tests for news labeling tool
├── test_deepfake_labels.py       # Tests for label templates
├── TEST_INSTRUCTIONS.md          # Complete testing guide
└── README.md                     # This file
```

---

## Setup for Claude Desktop

### 1. Find Your Config File

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`  
**Linux**: `~/.config/Claude/claude_desktop_config.json`

### 2. Add This Server Configuration

Edit the config file and add:

```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/FULL/PATH/TO/EU_AI_ACT_MCP/venv/bin/python",
      "args": [
        "/FULL/PATH/TO/EU_AI_ACT_MCP/main.py"
      ],
      "env": {}
    }
  }
}
```

**Important**: Replace `/FULL/PATH/TO/EU_AI_ACT_MCP` with your actual path!

### 3. Restart Claude Desktop

Quit Claude Desktop completely and reopen it.

### 4. Test It Works

In a new conversation, ask:

```
Use the get_ai_interaction_disclosure tool with language "en" and style "simple"
```

You should see Claude call the tool and return: "You are chatting with an AI assistant."

---

## Setup for Windsurf

### 1. Find Windsurf MCP Config

Check your Windsurf settings for MCP server configuration (similar location to Claude Desktop).

### 2. Add the Same Configuration

```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/FULL/PATH/TO/EU_AI_ACT_MCP/venv/bin/python",
      "args": [
        "/FULL/PATH/TO/EU_AI_ACT_MCP/main.py"
      ],
      "env": {}
    }
  }
}
```

### 3. Restart Windsurf

### 4. Test It Works

In the AI assistant panel, ask:

```
Use the label_news_text tool to label this article: "Scientists discover new planet." Set has_human_editor to false.
```

---

## Real-World Usage Scenarios

### Scenario 1: Chatbot Application (Article 50(1))

**Requirement**: AI chatbots must disclose they are AI to users.

**Before (Manual - Non-Compliant)**:
```python
# Developer has to remember to add disclosure text
# and translate it for every language
response = generate_ai_response(user_message)
return response  # ❌ Missing disclosure!
```

**After (Automated with MCP)**:
```python
# AI agent automatically gets compliant disclosure
disclosure = mcp_client.call_tool(
    "get_ai_interaction_disclosure",
    {"language": "en", "style": "simple"}
)
# Returns: "You are chatting with an AI assistant."

response = generate_ai_response(user_message)
return f"{disclosure['disclosure']}\n\n{response}"  # ✅ Compliant!
```

**Result**: Automatic compliance in 5+ languages with one tool call.

---

### Scenario 2: AI-Generated News Articles (Article 50(4))

**Requirement**: AI-generated news content must be labeled. Human editorial oversight may qualify for exemptions.

**Before (Manual - Error-Prone)**:
```python
# Developer has to remember disclosure format
# and handle editor attribution
article = generate_news_article(topic)
if has_editor:
    article = f"[AI-assisted. Reviewed by {editor}]\n{article}"
else:
    article = f"[AI-generated]\n{article}"  # ❌ Wrong format!
```

**After (Automated with MCP)**:
```python
# AI agent automatically labels with correct format
result = mcp_client.call_tool(
    "label_news_text",
    {
        "text_content": article,
        "has_human_editor": True,
        "editor_name": "Jane Smith",
        "language": "en"
    }
)

labeled_article = result["labeled_text"]
# Returns: "[This article was generated with AI assistance. Reviewed by Jane Smith.]\n\n{article}"

# Bonus: Check if exemption applies
if result["exemption_applies"]:
    print("✅ Qualifies for Article 50(4) exemption")
```

**Result**: Automatic compliance with correct legal format, multi-language support, and exemption tracking.

---

### Scenario 3: Content Moderation Platform

**Requirement**: Platform needs to check what labels are available for different content types.

**Use Case**:
```python
# Get all available labels
labels = mcp_client.call_tool(
    "get_deepfake_label_templates",
    {"language": "en"}
)

# Access labels by content type
text_labels = labels["content_types"]["text"]
image_labels = labels["content_types"]["image"]
video_labels = labels["content_types"]["video"]

# Use appropriate label based on content
if content_type == "news":
    label = text_labels["news_no_editor"]
elif content_type == "image":
    label = image_labels["standard"]
```

**Result**: Centralized label management across your entire platform.

---

### Scenario 4: Emotion Recognition System (Article 50(3))

**Requirement**: Systems using emotion recognition must inform users before activation.

**Use Case**:
```python
# Before starting emotion detection
disclosure = mcp_client.call_tool(
    "get_emotion_recognition_disclosure",
    {"language": "de", "style": "detailed"}
)

# Show to user in German
display_notice(disclosure["disclosure"])
# "Dieses System analysiert emotionale Ausdrücke aus Ihrem Gesicht, Stimme oder Text."

# Only proceed after user acknowledges
if user_acknowledged:
    start_emotion_recognition()
```

**Result**: GDPR-compliant emotion recognition with proper disclosures.

---

## Tool Reference

### 1. get_ai_interaction_disclosure

**Article**: 50(1) - AI Interaction Transparency

**Purpose**: Get disclosure text for AI chatbots, voice assistants, and conversational AI.

**Parameters**:
- `language` (string, default: "en"): Language code (en, es, fr, de, it)
- `style` (string, default: "simple"): Disclosure style (simple, detailed, voice)

**Example Request**:
```json
{
  "language": "en",
  "style": "simple"
}
```

**Example Response**:
```json
{
  "article": "50(1)",
  "obligation": "AI Interaction Transparency",
  "language": "en",
  "style": "simple",
  "disclosure": "You are chatting with an AI assistant.",
  "usage": "Display this text to users before or during AI interaction",
  "compliance_deadline": "2026-08-02"
}
```

**When to Use**:
- Chatbot interfaces
- Voice assistants
- AI customer service systems
- Any conversational AI system

---

### 2. get_emotion_recognition_disclosure

**Article**: 50(3) - Emotion Recognition Transparency

**Purpose**: Get disclosure text for systems that detect emotions from facial expressions, voice, or text.

**Parameters**:
- `language` (string, default: "en"): Language code (en, es, fr, de)
- `style` (string, default: "simple"): Disclosure style (simple, detailed, privacy_notice)

**Example Request**:
```json
{
  "language": "en",
  "style": "detailed"
}
```

**Example Response**:
```json
{
  "article": "50(3)",
  "obligation": "Emotion Recognition Transparency",
  "language": "en",
  "style": "detailed",
  "disclosure": "This system analyzes emotional expressions from your face, voice, or text. Your emotional data is processed according to GDPR regulations.",
  "usage": "Display this text to users before activating emotion recognition",
  "gdpr_compliance": "Ensure user consent is obtained",
  "compliance_deadline": "2026-08-02"
}
```

**When to Use**:
- Emotion detection systems
- Sentiment analysis tools
- Facial expression recognition
- Voice tone analysis

---

### 3. get_deepfake_label_templates

**Article**: 50(2) and 50(4) - Content Labeling

**Purpose**: Access all available labels for AI-generated and manipulated content across all media types.

**Parameters**:
- `language` (string, default: "en"): Language code (en, es, fr, de)

**Example Request**:
```json
{
  "language": "en"
}
```

**Example Response**:
```json
{
  "language": "en",
  "article": "50(2) and 50(4)",
  "purpose": "Labels for AI-generated and manipulated content",
  "content_types": {
    "text": {
      "standard": "This content was generated with AI assistance.",
      "news": "This article was generated with AI assistance. Reviewed by {editor}.",
      "news_no_editor": "This article was generated with AI. No human editorial oversight."
    },
    "image": {
      "standard": "This image has been artificially generated or manipulated.",
      "artistic": "This work contains AI-generated imagery."
    },
    "video": {
      "standard": "This video has been artificially generated or manipulated.",
      "artistic": "This work contains AI-generated content."
    },
    "audio": {
      "standard": "This audio has been artificially generated.",
      "spoken": "Warning: This audio was created using artificial intelligence."
    }
  },
  "available_languages": ["en", "es", "fr", "de"]
}
```

**When to Use**:
- Content moderation platforms
- Media generation systems
- Checking available labels before implementing tools
- Documentation and compliance audits

---

### 4. label_news_text

**Article**: 50(4) - AI-Generated Content Labeling (Text/News)

**Purpose**: Add EU AI Act compliant disclosure to AI-generated news articles and public interest text.

**Parameters**:
- `text_content` (string, required): The AI-generated or AI-assisted text
- `has_human_editor` (boolean, default: false): Whether a human editor reviewed the content
- `editor_name` (string, optional): Name of the human editor
- `language` (string, default: "en"): Language code (en, es, fr, de)

**Example Request**:
```json
{
  "text_content": "Breaking news: Scientists discover new renewable energy source.",
  "has_human_editor": true,
  "editor_name": "Jane Smith",
  "language": "en"
}
```

**Example Response**:
```json
{
  "article": "50(4)",
  "obligation": "AI-Generated Content Labeling (Text/News)",
  "language": "en",
  "labeled_text": "[This article was generated with AI assistance. Reviewed by Jane Smith.]\n\nBreaking news: Scientists discover new renewable energy source.",
  "disclosure": "This article was generated with AI assistance. Reviewed by Jane Smith.",
  "original_length": 65,
  "labeled_length": 139,
  "has_human_editor": true,
  "exemption_applies": true,
  "exemption_reason": "Human editorial oversight present",
  "compliance_deadline": "2026-08-02",
  "usage": "Publish the labeled_text instead of the original text"
}
```

**When to Use**:
- AI-generated news articles
- Automated journalism systems
- Content generation platforms
- Public interest content publishing

**Important Notes**:
- Human editorial oversight may qualify for Article 50(4) exemptions
- Always use `labeled_text` in the response for publication
- Check `exemption_applies` to understand compliance status

---

## Compliance Information

### What is EU AI Act Article 50?

**Article 50** of the EU Artificial Intelligence Act mandates **transparency obligations** for providers and deployers of certain AI systems. These obligations ensure users can make informed decisions when interacting with AI.

### Key Obligations

#### Article 50(1) - AI Interaction Disclosure
**Who**: Providers of AI systems that interact with natural persons  
**What**: Must inform users they are interacting with an AI  
**Exceptions**: Law enforcement, obvious AI systems  
**Deadline**: August 2, 2026

#### Article 50(2) - Content Watermarking
**Who**: Providers of AI systems generating synthetic content  
**What**: Must mark AI-generated content (text, images, audio, video)  
**Method**: Technical watermarks (C2PA, IPTC, metadata)  
**Deadline**: August 2, 2026

#### Article 50(3) - Emotion Recognition Disclosure
**Who**: Deployers of emotion recognition systems  
**What**: Must inform users about emotion recognition processing  
**Additional**: Must comply with GDPR consent requirements  
**Deadline**: August 2, 2026

#### Article 50(4) - Deepfake Labeling
**Who**: Deployers of AI systems generating deepfakes  
**What**: Must label AI-generated or manipulated content  
**Exceptions**: Artistic/satirical works with appropriate safeguards  
**Deadline**: August 2, 2026

### Why Use This MCP Server?

✅ **Automated Compliance**: Tools handle disclosure formats automatically  
✅ **Multi-Language**: Pre-translated disclosures in 5+ languages  
✅ **Exemption Handling**: Automatically tracks when exemptions apply  
✅ **Future-Proof**: Updates as regulations evolve  
✅ **Integration-Ready**: Works with any MCP-compatible AI system  

---

## Development

### Running Tests

```bash
# Test news labeling
./venv/bin/python test_label_news_text.py

# Test label templates
./venv/bin/python test_deepfake_labels.py

# Test server startup
./venv/bin/python main.py
```

### Adding New Tools

See the existing tools in `server.py` as examples. Follow the pattern:

```python
@mcp.tool()
def your_new_tool(param: str) -> Dict[str, Any]:
    """
    Tool description for AI agents.
    
    Args:
        param: Parameter description
        
    Returns:
        Dictionary with results
    """
    # Implementation
    return {"result": "value"}
```

---

## Resources

- [EU AI Act Official Text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)
- [MCP Documentation](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)
- [C2PA Specification](https://c2pa.org/)

---

## License

MIT License - Use freely for compliance purposes.

---

## Support

For questions about:
- **EU AI Act compliance**: Consult legal counsel
- **MCP server issues**: Open an issue on GitHub
- **Tool requests**: Submit feature requests via issues

**Compliance Deadline Reminder**: August 2, 2026 🗓️
