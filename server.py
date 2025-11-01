# server.py
"""
EU AI Act Article 50 Compliance MCP Server

This MCP server provides tools and resources for EU AI Act Article 50 compliance,
including transparency obligations for AI systems.
"""

import os
import json
from typing import Dict, Any, List
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables (if needed for future extensions)
load_dotenv()

# Create an MCP server with a name
mcp = FastMCP("EU_AI_ACT_MCP")


# ============================================================================
# RESOURCES - Data files that agents can read
# ============================================================================

@mcp.resource("disclosure-templates://ai-interaction-and-emotion")
def get_disclosure_templates() -> str:
    """
    Provides pre-written disclosure text templates for EU AI Act Article 50 compliance.
    
    Contains:
    - AI interaction disclosures (Article 50(1))
    - Emotion recognition disclosures (Article 50(3))
    
    Available in multiple languages: en, es, fr, de, it
    """
    template_path = os.path.join(os.path.dirname(__file__), "disclosure_templates.json")
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


# ============================================================================
# TOOLS - Article 50 Compliance Tools
# ============================================================================

@mcp.tool()
def get_ai_interaction_disclosure(language: str = "en", style: str = "simple") -> Dict[str, Any]:
    """
    Get AI interaction disclosure text for EU AI Act Article 50(1) compliance.
    
    This tool provides pre-written disclosure text that MUST be shown to users
    when they interact with an AI system (chatbots, voice assistants, etc.).
    
    Args:
        language: Language code (en, es, fr, de, it). Default: "en"
        style: Disclosure style (simple, detailed, voice). Default: "simple"
        
    Returns:
        Dictionary containing the disclosure text and metadata
        
    Example:
        get_ai_interaction_disclosure(language="en", style="simple")
        Returns: {"disclosure": "You are chatting with an AI assistant.", ...}
    """
    template_path = os.path.join(os.path.dirname(__file__), "disclosure_templates.json")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        templates = json.load(f)
    
    # Get the requested disclosure
    try:
        disclosure_text = templates["ai_interaction"][language][style]
    except KeyError:
        return {
            "error": f"Disclosure not found for language '{language}' and style '{style}'",
            "available_languages": list(templates["ai_interaction"].keys()),
            "available_styles": ["simple", "detailed", "voice"]
        }
    
    return {
        "article": "50(1)",
        "obligation": "AI Interaction Transparency",
        "language": language,
        "style": style,
        "disclosure": disclosure_text,
        "usage": "Display this text to users before or during AI interaction",
        "compliance_deadline": "2026-08-02"
    }


@mcp.tool()
def get_emotion_recognition_disclosure(language: str = "en", style: str = "simple") -> Dict[str, Any]:
    """
    Get emotion recognition disclosure text for EU AI Act Article 50(3) compliance.
    
    This tool provides pre-written disclosure text that MUST be shown to users
    when an AI system uses emotion recognition technology.
    
    Args:
        language: Language code (en, es, fr, de, it). Default: "en"
        style: Disclosure style (simple, detailed, privacy_notice). Default: "simple"
        
    Returns:
        Dictionary containing the disclosure text and metadata
        
    Example:
        get_emotion_recognition_disclosure(language="en", style="detailed")
    """
    template_path = os.path.join(os.path.dirname(__file__), "disclosure_templates.json")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        templates = json.load(f)
    
    # Get the requested disclosure
    try:
        disclosure_text = templates["emotion_recognition"][language][style]
    except KeyError:
        return {
            "error": f"Disclosure not found for language '{language}' and style '{style}'",
            "available_languages": list(templates["emotion_recognition"].keys()),
            "available_styles": ["simple", "detailed", "privacy_notice"]
        }
    
    return {
        "article": "50(3)",
        "obligation": "Emotion Recognition Transparency",
        "language": language,
        "style": style,
        "disclosure": disclosure_text,
        "usage": "Display this text to users before activating emotion recognition",
        "gdpr_compliance": "Ensure user consent is obtained",
        "compliance_deadline": "2026-08-02"
    }