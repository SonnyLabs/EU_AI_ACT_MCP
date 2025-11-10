# EU AI Act Compliance MCP Server 🇪🇺

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server providing **EU AI Act compliance tools** for AI systems. This server helps developers of AI applications, like chatbots and AI agents, meet transparency, security, and governance requirements across the entire EU AI Act framework.

 ⚠️ BETA SOFTWARE - NOT LEGAL ADVICE
   
   This MCP server is in active development. It provides technical tools to assist 
   with EU AI Act compliance but does NOT constitute legal advice. Consult qualified 
   legal counsel for compliance decisions.

 🧑 CONTRIBUTORS NEEDED!
   This solution is in its early phases and there are EU AI Act requirements left to add, as well as general guidance. If you would like to contribute to improve the    solution for everyone, we would love that!    Please see the Contributing guide [here](https://github.com/SonnyLabs/EU_AI_ACT_MCP?tab=contributing-ov-file) for general guidance on contributing. 

## 🎯 What Does This Server Do?

This MCP server, which can be self-hosted, provides **automated compliance tools** that helps you and your AI systems to comply with the EU AI Act:

- ✅ **Classify AI systems** by risk level (Prohibited, High-Risk, Limited-Risk, Minimal-Risk)
- ✅ **Determine your role** under EU AI Act (Provider, Deployer, Importer, etc.)
- ✅ **Check for prohibited practices** (Article 5 violations)
- ✅ **Add transparency disclosures** (Article 50 - chatbots, emotion recognition)
- ✅ **Watermark AI content** (Article 50(2) - text, images, video, audio)
- ✅ **Label deepfakes** (Article 50(4) - all media types)
- ✅ **Detect security threats** (Article 15 - prompt injections)

**Compliance Deadline For Several Risk Types**: August 2, 2026 🗓️

## 📦 What if I want the hosted MCP server instead of self-hosting it myself?
You can become a design partner and use our hosted EU AI Act MCP server at (SonnyLabs.ai)[https://sonnylabs.ai/eu-ai-act-compliance].

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

### Pre-Setup

Git clone this repo locally.


### 1. Installation

```bash
cd FILE_PATH_OF_THIS_MCP
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set Up SonnyLabs Security Tools

For the security tools, get credentials from [SonnyLabs Dashboard](https://sonnylabs-service.onrender.com/analysis):

```bash
export SONNYLABS_API_TOKEN="your_api_token"
export SONNYLABS_ANALYSIS_ID="your_analysis_id"
```

NOTE: In order to get the SonnyLabs API token and analysis ID, after registering on the [SonnyLabs Dashboard](https://sonnylabs-service.onrender.com/analysis), you can generate a new API key at [API keys on the SonnyLabs Dashboard](https://sonnylabs-service.onrender.com/analysis/api-keys). The next step is to [create a new analysis](https://sonnylabs-service.onrender.com/analysis/new) on the SonnyLabs dashboard, and get the analysis ID associated with it.  

There is a genereous free tier where you can call the SonnyLabs API.

### 3. Test the Server

```bash
# Quick test - all tools
./venv/bin/python test_all_tools.py

# Test specific categories
./venv/bin/python test_risk_classification.py
./venv/bin/python test_role_determination.py
./venv/bin/python test_sonnylabs_security.py
```

### 4. Connect to Your AI Assistant or AI Agent

See [Setup for Claude Desktop](#setup-for-claude-desktop), [Setup for Windsurf](#setup-for-windsurf)
or [Setup for cursor](#setup-for-cursor) below.

This also works with AI agents like CrewAI agents.

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
      "command": "FILE_PATH_OF_THIS_MCP/venv/bin/python",
      "args": [
        "FILE_PATH_OF_THIS_MCP/server.py"
      ],
      "env": {}
    }
  }
}
```

### 3. Restart Claude Desktop

Quit Claude Desktop completely and reopen it.

### 4. Test It Works

In a new conversation, ask Claude:

```
Use classify_ai_system_risk to classify a chatbot that interacts with users.
```

---

## Setup for Windsurf

### 1. Find Your Config File

The Windsurf MCP configuration file is located at:

**macOS/Linux**: `~/.codeium/windsurf/mcp_config.json`  
**Windows**: `%USERPROFILE%\.codeium\windsurf\mcp_config.json`

### 2. Add This Server Configuration

Edit the config file and add:

```json
{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/path/to/your/project/venv/bin/python",
      "args": [
        "/path/to/your/project/main.py"
      ],
      "env": {
        "SONNYLABS_API_TOKEN": "your_sonnylabs_api_token_here",
        "SONNYLABS_ANALYSIS_ID": "your_analysis_id_here"
      }
    }
  }
}
```

Replace the placeholders:
- `/path/to/your/project/venv/bin/python` - Path to your virtual environment Python binary
- `/path/to/your/project/main.py` - Path to the main.py file in this repo
- `your_sonnylabs_api_token_here` - Your SonnyLabs API token (optional, only needed for security tools)
- `your_analysis_id_here` - Your SonnyLabs analysis ID (optional, only needed for security tools)

**Note**: On Windows, use backslashes in paths (e.g., `C:\\path\\to\\project\\venv\\Scripts\\python.exe`)

### 3. Restart Windsurf

Quit Windsurf completely and reopen it.

### 4. Test It Works

Just ask me in Windsurf:

```
Use get_ai_interaction_disclosure with language "en" and style "simple"
``` 


## Setup for Cursor

### 1. Open Cursor settings -> Tools & MCP and Click "Add Custom MCP"

### 2. Edit the config file to add This Server Configuration

Edit the config file and add:

{
  "mcpServers": {
    "eu-ai-act-compliance": {
      "command": "/path/to/your/project/venv/bin/python",
      "args": [
        "/path/to/your/project/main.py"
      ],
      "env": {
        "SONNYLABS_API_TOKEN": "your_sonnylabs_api_token_here",
        "SONNYLABS_ANALYSIS_ID": "your_analysis_id_here"
      }
    }
  }
}

### 3. Replace the placeholders:
- `/path/to/your/project/venv/bin/python` - Path to your virtual environment Python binary
- `/path/to/your/project/main.py` - Path to the main.py file in this repo
- `your_sonnylabs_api_token_here` - Your SonnyLabs API token (optional, only needed for security tools)
- `your_analysis_id_here` - Your SonnyLabs analysis ID (optional, only needed for security tools)

**Note**: On Windows, use backslashes in paths (e.g., `C:\\path\\to\\project\\venv\\Scripts\\python.exe`)

### 4. Restart Cursor 

Quit Cursor completely and reopen it.


### 5. Test It Works

Toggle the AI pane and create a new chat to ask:

```
Use get_ai_interaction_disclosure with language "en" and style "simple"
'''
A dialog should appear offering to Run the get_ai_interaction_disclosure tool. Click Run and you should
see a response like this:

{
"article": "50(1)",
"obligation": "AI Interaction Transparency",
"language": "en",
"style": "simple",
"disclosure": "You are chatting with an AI assistant.",
"usage": "Display this text to users before or during AI interaction",
"compliance_deadline": "2026-08-02"
}
You are chatting with an AI assistant


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

## 📋 Copy-Paste Test Prompts

Ready-to-use prompts for testing all tools in Claude Desktop or Windsurf. Just copy and paste!

### 1. Risk Classification

```
Use classify_ai_system_risk to classify my system with these details:
- system_description: "AI chatbot for customer support in healthcare"
- use_case: "healthcare"
- interacts_with_users: true
- generates_content: true
- processes_personal_data: true
- makes_automated_decisions: false
- in_critical_infrastructure: false
- used_for_employment: false
- used_for_education: false
- used_for_law_enforcement: false
- used_for_migration: false
- used_for_justice: false

What's my risk level and what obligations apply?
```

### 2. Check Prohibited Practices

```
Use check_prohibited_practices to check if my system has any Article 5 violations:
- system_description: "Employee monitoring system with behavior scoring"
- subliminal_manipulation: false
- vulnerability_exploitation: false
- social_scoring: true
- biometric_categorization: false
- emotion_recognition_workplace: true
- emotion_recognition_education: false
- untargeted_scraping: false
- risk_assessment_personal_characteristics: false

What violations are detected and what are the penalties?
```

### 3. Determine Your Role

```
Use determine_eu_ai_act_role to find out my role:
- company_description: "US-based AI software company"
- company_location: "United States"
- develops_ai_system: true
- uses_ai_system: false
- sells_ai_system: true
- distributes_in_eu: true
- imports_to_eu: true
- under_own_name_or_trademark: true
- integrates_ai_into_product: false
- represents_non_eu_provider: false

What role(s) do I have and what are my obligations?
```

### 4. Get Chatbot Disclosure

```
Use get_ai_interaction_disclosure with language "en" and style "detailed"

Show me the disclosure text I need for my chatbot.
```

### 5. Get Emotion Recognition Disclosure

```
Use get_emotion_recognition_disclosure with:
- language: "en"
- style: "privacy_notice"

What disclosure do I need for emotion recognition?
```

### 6. Get All Deepfake Labels

```
Use get_deepfake_label_templates with language "es"

Show me all available labels in Spanish.
```

### 7. Label AI-Generated News

```
Use label_news_text to label this article:
- text_content: "Breaking: Scientists announce major breakthrough in renewable energy storage. New battery technology promises 10x capacity increase."
- has_human_editor: true
- editor_name: "Sarah Johnson"
- language: "en"

Show me the properly labeled version.
```

### 8. Watermark AI Text

```
Use watermark_text to watermark this content:
- text_content: "Artificial intelligence is transforming how we work and live. From healthcare diagnostics to creative writing, AI systems are becoming integral to modern society. This article explores the implications of AI adoption across industries."
- generator: "GPT-4"
- format_type: "markdown"

Show me the watermarking metadata and instructions.
```

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

**Quick use**: `Watermark this AI-generated text from GPT-5`

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

#### `check_sensitive_file_access`

**Purpose**: Monitor AI agent file access for security

**Returns**: File sensitivity analysis, access recommendations (BLOCK/ALLOW)

---

## 🎯 Real-World Usage Scenarios

### Scenario 1: Launching a Customer Service Chatbot

**What You Want To Do**: "My chatbot needs to be compliant. What do I do?"

**Instructions**: Ask the AI:
```
Use classify_ai_system_risk to check my chatbot
Then use get_ai_interaction_disclosure to get the disclosure text
```

**Result**: You'll know your risk level (likely LIMITED-RISK) and get ready-to-use disclosure text in 5+ languages.

---

### Scenario 2: Publishing AI-Generated News

**What You Want To Do**: "I'm using AI to write news articles. How do I label them?"

**Instructions**: Ask the AI:
```
Use label_news_text to label my article with editor "Jane Smith"
```

**Result**: Properly formatted label + check if you qualify for exemptions with human editorial oversight.

---

### Scenario 3: Understanding Your Compliance Obligations

**What You Want To Do**: "I develop AI systems in the US and sell to EU customers. What are my obligations?"

**Instructions**: Ask the AI:
```
Use determine_eu_ai_act_role - I develop and sell AI systems from the US to EU
```

**Result**: You'll learn you're a PROVIDER + IMPORTER with specific obligations for each role.

---

### Scenario 4: Securing Your AI Against Prompt Injection Attacks

**What You Want To Do**: "How do I protect my AI from prompt injection?"

**Instructions**: Get SonnyLabs credentials, then ask the AI:
```
Use scan_for_prompt_injection to check user inputs before processing
```

**Result**: Real-time threat detection with confidence scores and block/allow recommendations.

---

### Scenario 5: Securing Your AI Against Trying to Access Sensitive Files

**What You Want To Do**: "How do I ensure the AI agent doesn't access sensitive files on the server?"

**Instructions**: Get SonnyLabs credentials, then ask the AI:
```
Now I want to go to /etc/shadow$ . Can you check for sensitive files or file types with the EU_AI_ACT_MCP
```

**Result**: Real-time sensitive file detection and block/allow recommendations.

---

## 📋 EU AI Act Coverage Summary

This server covers the most critical EU AI Act articles for AI system operators:

| Article | What It Covers | Tools in This Server |
|---------|----------------|----------------------|
| **Article 3** | Role definitions | `determine_eu_ai_act_role` |
| **Article 5** | Prohibited practices (€35M penalty) | `check_prohibited_practices` |
| **Article 6** | High-risk classification | `classify_ai_system_risk` |
| **Article 15** | Cybersecurity & robustness | `scan_for_prompt_injection`, `check_sensitive_file_access` |
| **Article 50(1)** | AI interaction disclosure | `get_ai_interaction_disclosure` |
| **Article 50(2)** | Content watermarking | 4 watermarking tools |
| **Article 50(3)** | Emotion recognition disclosure | `get_emotion_recognition_disclosure` |
| **Article 50(4)** | Deepfake labeling | 4 deepfake labeling tools |

**Key Deadline**: August 2, 2026 🗓️ for High Risk AI Systems & Limited Risk AI Systems

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


