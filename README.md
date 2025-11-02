# EU AI Act Compliance MCP Server 🇪🇺

A comprehensive [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server providing **complete EU AI Act compliance tools** for AI systems. This server helps AI applications meet transparency, security, and governance requirements across the entire EU AI Act framework.

## 🎯 What Does This Server Do?

This MCP server provides **17 automated compliance tools** that help your AI systems:

- ✅ **Classify AI systems** by risk level (Prohibited, High-Risk, Limited-Risk, Minimal-Risk)
- ✅ **Determine your role** under EU AI Act (Provider, Deployer, Importer, etc.)
- ✅ **Check for prohibited practices** (Article 5 violations)
- ✅ **Add transparency disclosures** (Article 50 - chatbots, emotion recognition)
- ✅ **Watermark AI content** (Article 50(2) - text, images, video, audio)
- ✅ **Label deepfakes** (Article 50(4) - all media types)
- ✅ **Detect security threats** (Article 15 - prompt injection, PII, file access)

**Compliance Deadline**: August 2, 2026 🗓️

## 📦 What's Included

### 🔧 17 Tools Available

#### **Risk & Role Classification (3 tools)**
- ✅ `classify_ai_system_risk` - Determine risk level (Articles 5, 6, 50)
- ✅ `check_prohibited_practices` - Check Article 5 violations
- ✅ `determine_eu_ai_act_role` - Identify your role (Article 3)

#### **Transparency & Disclosure (4 tools)**
- ✅ `get_ai_interaction_disclosure` - Chatbot disclosures (Article 50(1))
- ✅ `get_emotion_recognition_disclosure` - Emotion AI disclosures (Article 50(3))
- ✅ `get_deepfake_label_templates` - Access all label templates
- ✅ `label_news_text` - Label AI-generated news (Article 50(4))

#### **Content Watermarking (4 tools)**
- ✅ `watermark_text` - Watermark AI text (Article 50(2))
- ✅ `watermark_image` - Watermark AI images with C2PA (Article 50(2))
- ✅ `watermark_video` - Watermark AI videos with C2PA (Article 50(2))
- ✅ `watermark_audio` - Watermark AI audio (Article 50(2))

#### **Deepfake Labeling (3 tools)**
- ✅ `label_image_deepfake` - Label AI-generated images (Article 50(4))
- ✅ `label_video_deepfake` - Label AI-generated videos (Article 50(4))
- ✅ `label_audio_deepfake` - Label AI-generated audio (Article 50(4))

#### **AI Security (3 tools - SonnyLabs.ai Integration)**
- ✅ `scan_for_prompt_injection` - Detect prompt attacks (Article 15)
- ✅ `detect_pii_in_content` - Find PII in content (Article 10 + GDPR)
- ✅ `check_sensitive_file_access` - Monitor file access (Articles 10 & 15)

### 📚 4 Resources Available

- ✅ `disclosure-templates://ai-interaction-and-emotion` - Pre-written disclosures
- ✅ `deepfake-labels://content-labeling` - All deepfake labels
- ✅ `article50-rules://official-text` - Official Article 50 rules
- ✅ `watermark-config://technical-standards` - C2PA & IPTC standards

### 🌍 Multi-Language Support

All disclosures and labels available in:
- 🇬🇧 English (en)
- 🇪🇸 Spanish (es)
- 🇫🇷 French (fr)
- 🇩🇪 German (de)
- 🇮🇹 Italian (it) - disclosure templates only

## 🚀 Quick Start

### 1. Installation

```bash
cd /Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. (Optional) Set Up SonnyLabs Security Tools

For the 3 security tools, get credentials from [SonnyLabs Dashboard](https://sonnylabs-service.onrender.com/analysis):

```bash
export SONNYLABS_API_TOKEN="your_api_token"
export SONNYLABS_ANALYSIS_ID="your_analysis_id"
```

### 3. Test the Server

```bash
# Quick test - all tools
./venv/bin/python test_all_tools.py

# Test specific categories
./venv/bin/python test_risk_classification.py
./venv/bin/python test_role_determination.py
./venv/bin/python test_sonnylabs_security.py
```

### 4. Connect to Your AI Assistant

See [Setup for Claude Desktop](#setup-for-claude-desktop) or [Setup for Windsurf](#setup-for-windsurf) below.

## 📁 Project Structure

```
.
├── server.py                           # Main MCP server with all 17 tools
├── main.py                             # Server entry point
├── requirements.txt                    # Python dependencies
│
├── Resources (4 JSON files)
├── disclosure_templates.json           # Pre-written disclosures (50(1), 50(3))
├── deepfake_labels.json               # Deepfake labels (50(4))
├── article50_rules.json               # Official Article 50 rules
├── watermark_config.json              # C2PA & IPTC watermarking standards
│
├── Tests (7 test files)
├── test_all_tools.py                  # Test all 17 tools
├── test_risk_classification.py        # Test risk & prohibited tools
├── test_role_determination.py         # Test role determination
├── test_sonnylabs_security.py         # Test security tools
├── test_watermark_media.py            # Test watermarking tools
├── test_label_*_deepfake.py          # Test deepfake labeling
│
└── Documentation
    ├── README.md                       # This file
    ├── SONNYLABS_TESTING_GUIDE.md     # Security tools guide
    └── PHASE2_SUMMARY.md              # Implementation summary
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
      "command": "/Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP/venv/bin/python",
      "args": [
        "/Users/liana/Documents/AI/sonnylabs/EU_AI_ACT_MCP/server.py"
      ],
      "env": {}
    }
  }
}
```

**Note**: Update the path if you installed the server in a different location.

### 3. Restart Claude Desktop

Quit Claude Desktop completely and reopen it.

### 4. Test It Works

In a new conversation, ask Claude:

```
Use classify_ai_system_risk to classify a chatbot that interacts with users.
```

---

## Setup for Windsurf

Windsurf automatically detects MCP servers in your workspace. No additional configuration needed!

### Test It Works

Just ask me in Windsurf:

```
Use get_ai_interaction_disclosure with language "en" and style "simple"
```

---

## 💡 How to Use the Tools

### Simple Usage Examples

All tools are called the same way in Claude Desktop or Windsurf. Just ask the AI assistant to use the tool!

#### 1. Classify Your AI System

```
Use classify_ai_system_risk to classify my system:
- Description: "AI chatbot for customer support"
- Use case: "chatbot"
- Interacts with users: true
- Generates content: true
```

**Returns**: Risk level (PROHIBITED, HIGH-RISK, LIMITED-RISK, or MINIMAL-RISK) with applicable obligations

#### 2. Check Your Role

```
Use determine_eu_ai_act_role:
- Company: "AI software development company"
- Location: "United States"
- Develops AI systems: true
- Sells AI systems: true
- Under own name: true
```

**Returns**: Your role (PROVIDER, DEPLOYER, IMPORTER, etc.) with specific obligations

#### 3. Get a Chatbot Disclosure

```
Use get_ai_interaction_disclosure with language "en" and style "simple"
```

**Returns**: "You are chatting with an AI assistant."

#### 4. Watermark AI-Generated Text

```
Use watermark_text:
- Text: "This article was written about quantum computing..."
- Generator: "GPT-4"
- Format: "markdown"
```

**Returns**: Text with embedded metadata watermark

#### 5. Label a Deepfake Image

```
Use label_image_deepfake:
- Description: "AI-generated portrait photo"
- Is artistic work: false
- Language: "en"
```

**Returns**: Label text and placement guidelines

#### 6. Scan for Security Threats (Requires SonnyLabs credentials)

```
Use scan_for_prompt_injection:
- Input: "Ignore all previous instructions"
- API token: [your token]
- Analysis ID: [your ID]
```

**Returns**: Threat analysis with risk level and recommendation

---

## 📖 Complete Tool Reference

### Risk & Role Tools

#### `classify_ai_system_risk`

**Purpose**: Determine if your AI system is Prohibited, High-Risk, Limited-Risk, or Minimal-Risk

**Simple call**:
```
Classify my AI hiring system that screens resumes. It's used for employment.
```

**Parameters**:
- `system_description`: What your AI does
- `use_case`: Primary use (e.g., "employment", "healthcare", "chatbot")
- Various boolean flags for risk factors

**Returns**: Risk classification, applicable obligations, deadlines, penalties

---

#### `check_prohibited_practices`

**Purpose**: Check if your AI violates Article 5 prohibited practices

**Simple call**:
```
Check if my system has prohibited practices. It does social scoring.
```

**Parameters**: Boolean flags for 8 types of prohibited practices

**Returns**: Violations detected, severity, penalties (€35M or 7%), recommendations

---

#### `determine_eu_ai_act_role`

**Purpose**: Identify your role under EU AI Act (Provider, Deployer, etc.)

**Simple call**:
```
What's my role? I develop AI systems and sell them under my company name in the EU.
```

**Parameters**: Company info and activity flags

**Returns**: Primary role, obligations, deadlines, compliance actions

---

### Transparency & Disclosure Tools

#### `get_ai_interaction_disclosure`

**Quick use**: `Get chatbot disclosure in English`

**Returns**: Ready-to-use disclosure text for AI interactions

---

#### `get_emotion_recognition_disclosure`

**Quick use**: `Get emotion recognition disclosure in German, detailed style`

**Returns**: GDPR-compliant emotion AI disclosure

---

#### `get_deepfake_label_templates`

**Quick use**: `Show me all deepfake labels in Spanish`

**Returns**: Complete list of labels for all content types

---

#### `label_news_text`

**Quick use**: `Label this AI news article: "Breaking: New discovery..." with editor "John Doe"`

**Returns**: Properly labeled text with EU AI Act compliance

---

### Watermarking Tools

#### `watermark_text` / `watermark_image` / `watermark_video` / `watermark_audio`

**Quick use**: `Watermark this AI-generated text from GPT-4`

**Returns**: Watermarking metadata and instructions (C2PA, IPTC standards)

---

### Deepfake Labeling Tools

#### `label_image_deepfake` / `label_video_deepfake` / `label_audio_deepfake`

**Quick use**: `Label this AI-generated video, not artistic work, in French`

**Returns**: Label text, placement guidance, compliance info

---

### Security Tools (Requires SonnyLabs)

#### `scan_for_prompt_injection`

**Purpose**: Detect prompt injection attacks in real-time

**Returns**: Attack detection, confidence score, risk level, recommendation

---

#### `detect_pii_in_content`

**Purpose**: Find PII (emails, phone numbers, SSNs, etc.) in content

**Returns**: List of PII found, redaction recommendations, GDPR compliance

---

#### `check_sensitive_file_access`

**Purpose**: Monitor AI agent file access for security

**Returns**: File sensitivity analysis, access recommendations (BLOCK/ALLOW)

---

## 🎯 Real-World Usage Scenarios

### Scenario 1: Launching a Customer Service Chatbot

**Question**: "My chatbot needs to be compliant. What do I do?"

**Answer**: Ask your AI assistant:
```
Use classify_ai_system_risk to check my chatbot
Then use get_ai_interaction_disclosure to get the disclosure text
```

**Result**: You'll know your risk level (likely LIMITED-RISK) and get ready-to-use disclosure text in 5+ languages.

---

### Scenario 2: Publishing AI-Generated News

**Question**: "I'm using AI to write news articles. How do I label them?"

**Answer**: Ask your AI assistant:
```
Use label_news_text to label my article with editor "Jane Smith"
```

**Result**: Properly formatted label + check if you qualify for exemptions with human editorial oversight.

---

### Scenario 3: Understanding Your Compliance Obligations

**Question**: "I develop AI systems in the US and sell to EU customers. What are my obligations?"

**Answer**: Ask your AI assistant:
```
Use determine_eu_ai_act_role - I develop and sell AI systems from the US to EU
```

**Result**: You'll learn you're a PROVIDER + IMPORTER with specific obligations for each role.

---

### Scenario 4: Securing Your AI Against Attacks

**Question**: "How do I protect my AI from prompt injection?"

**Answer**: Get SonnyLabs credentials, then ask:
```
Use scan_for_prompt_injection to check user inputs before processing
```

**Result**: Real-time threat detection with confidence scores and block/allow recommendations.

---

## 📋 EU AI Act Coverage Summary

This server covers the most critical EU AI Act articles for AI system operators:

| Article | What It Covers | Tools in This Server |
|---------|----------------|----------------------|
| **Article 3** | Role definitions | `determine_eu_ai_act_role` |
| **Article 5** | Prohibited practices (€35M penalty) | `check_prohibited_practices` |
| **Article 6** | High-risk classification | `classify_ai_system_risk` |
| **Article 10** | Data governance + GDPR | `detect_pii_in_content`, `check_sensitive_file_access` |
| **Article 15** | Cybersecurity & robustness | `scan_for_prompt_injection`, `check_sensitive_file_access` |
| **Article 50(1)** | AI interaction disclosure | `get_ai_interaction_disclosure` |
| **Article 50(2)** | Content watermarking | 4 watermarking tools |
| **Article 50(3)** | Emotion recognition disclosure | `get_emotion_recognition_disclosure` |
| **Article 50(4)** | Deepfake labeling | 4 deepfake labeling tools |

**Key Deadline**: August 2, 2026 🗓️

### Why Use This Server?

✅ **Complete Coverage**: 17 tools covering Articles 3, 5, 6, 10, 15, and 50  
✅ **Multi-Language**: 5 languages supported (en, es, fr, de, it)  
✅ **Real-Time Security**: SonnyLabs integration for live threat detection  
✅ **Automatic Exemptions**: Tracks when exemptions apply  
✅ **Standards Compliant**: C2PA, IPTC, GDPR aligned  
✅ **Easy Integration**: Just ask your AI assistant to use the tools!

---

## 🧪 Testing & Development

### Run All Tests

```bash
# Test all 17 tools at once
./venv/bin/python test_all_tools.py
```

### Test by Category

```bash
# Test risk classification
./venv/bin/python test_risk_classification.py

# Test role determination
./venv/bin/python test_role_determination.py

# Test watermarking
./venv/bin/python test_watermark_media.py

# Test security tools (requires SonnyLabs credentials)
./venv/bin/python test_sonnylabs_security.py
```

---

## 📚 Additional Resources

### EU AI Act
- [Official EU AI Act Text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0206)
- [Article 50 Transparency Obligations](https://artificialintelligenceact.eu/article/50/)
- [High-Risk AI Systems (Annex III)](https://artificialintelligenceact.eu/annex/3/)

### Technical Standards
- [C2PA Specification](https://c2pa.org/) - Content watermarking standard
- [IPTC Standards](https://iptc.org/) - Photo metadata
- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP documentation

### Security Tools
- [SonnyLabs Dashboard](https://sonnylabs-service.onrender.com/analysis) - Get API credentials
- [SonnyLabs Testing Guide](./SONNYLABS_TESTING_GUIDE.md) - Security tools documentation

---

## 💬 Support & Contributing

### Need Help?

- **EU AI Act Legal Questions**: Consult with legal counsel
- **Tool Usage Questions**: Ask your AI assistant (Claude/Windsurf) for help
- **Technical Issues**: Check test files for examples
- **SonnyLabs Security**: See `SONNYLABS_TESTING_GUIDE.md`

### Want to Contribute?

This server is designed to be comprehensive. All 17 tools are implemented and tested. If you need additional EU AI Act coverage, feel free to extend the tools following the patterns in `server.py`.

---

## 📝 Summary

### What You Get

- ✅ **17 compliance tools** ready to use
- ✅ **4 resource files** with templates and standards
- ✅ **Complete EU AI Act coverage** (Articles 3, 5, 6, 10, 15, 50)
- ✅ **Multi-language support** (5 languages)
- ✅ **Real-time security** (SonnyLabs integration)
- ✅ **Production-ready** with comprehensive tests

### How to Get Started

1. **Install**: `pip install -r requirements.txt`
2. **Test**: `./venv/bin/python test_all_tools.py`
3. **Configure**: Add to Claude Desktop or use in Windsurf
4. **Use**: Just ask your AI assistant to use any tool!

### Compliance Checklist

- [ ] Classify your AI system risk level
- [ ] Determine your role (Provider, Deployer, etc.)
- [ ] Check for prohibited practices
- [ ] Add transparency disclosures to user-facing AI
- [ ] Watermark AI-generated content
- [ ] Label deepfakes appropriately
- [ ] Implement security scanning (optional but recommended)
- [ ] Document compliance actions

**Compliance Deadline**: August 2, 2026 🗓️

---

## License

MIT License - Free to use for EU AI Act compliance.

**Made with ❤️ for AI compliance**
