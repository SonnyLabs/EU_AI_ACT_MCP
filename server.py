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


@mcp.resource("deepfake-labels://content-labeling")
def get_deepfake_labels() -> str:
    """
    Provides pre-written deepfake and AI-generated content labels for EU AI Act Article 50(4) compliance.
    
    Contains labels for:
    - Text content (news articles, public interest content)
    - Image deepfakes
    - Video deepfakes
    - Audio deepfakes
    
    Available in multiple languages: en, es, fr, de
    """
    labels_path = os.path.join(os.path.dirname(__file__), "deepfake_labels.json")
    with open(labels_path, 'r', encoding='utf-8') as f:
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


@mcp.tool()
def get_deepfake_label_templates(language: str = "en") -> Dict[str, Any]:
    """
    Get all available deepfake and AI-generated content labels.
    
    This tool returns the complete set of labels available for different content types.
    Use this to see what labels are available for images, videos, audio, and text.
    
    Args:
        language: Language code (en, es, fr, de). Default: "en"
        
    Returns:
        Dictionary containing all available labels organized by content type
        
    Example:
        get_deepfake_label_templates(language="en")
        Returns all labels for English
    """
    labels_path = os.path.join(os.path.dirname(__file__), "deepfake_labels.json")
    
    with open(labels_path, 'r', encoding='utf-8') as f:
        all_labels = json.load(f)
    
    # Filter by language if available
    result = {
        "language": language,
        "content_types": {}
    }
    
    for content_type in ["text", "image", "video", "audio"]:
        if content_type in all_labels:
            if language in all_labels[content_type]:
                result["content_types"][content_type] = all_labels[content_type][language]
            else:
                result["content_types"][content_type] = {
                    "error": f"Language '{language}' not available for {content_type}",
                    "available_languages": list(all_labels[content_type].keys())
                }
    
    result["article"] = "50(2) and 50(4)"
    result["purpose"] = "Labels for AI-generated and manipulated content"
    result["available_languages"] = ["en", "es", "fr", "de"]
    
    return result


@mcp.tool()
def label_news_text(
    text_content: str,
    has_human_editor: bool = False,
    editor_name: str = "",
    language: str = "en"
) -> Dict[str, Any]:
    """
    Add AI-generated content disclosure to news articles and public interest text.
    
    This tool implements EU AI Act Article 50(4) compliance for AI-generated text
    published as news, journalism, or public interest content.
    
    Args:
        text_content: The AI-generated or AI-assisted text content
        has_human_editor: Whether a human editor reviewed the content (exemption qualifier)
        editor_name: Name of the human editor (if applicable)
        language: Language code (en, es, fr, de). Default: "en"
        
    Returns:
        Dictionary containing the labeled text with disclosure and compliance info
        
    Example:
        label_news_text(
            text_content="AI generated article...",
            has_human_editor=True,
            editor_name="Jane Doe",
            language="en"
        )
    """
    labels_path = os.path.join(os.path.dirname(__file__), "deepfake_labels.json")
    
    with open(labels_path, 'r', encoding='utf-8') as f:
        labels = json.load(f)
    
    # Get the appropriate label based on editor status
    try:
        if has_human_editor and editor_name:
            label_template = labels["text"][language]["news"]
            disclosure = label_template.replace("{editor}", editor_name)
        elif has_human_editor:
            label_template = labels["text"][language]["news"]
            disclosure = label_template.replace("{editor}", "editorial team")
        else:
            disclosure = labels["text"][language]["news_no_editor"]
    except KeyError:
        return {
            "error": f"Labels not found for language '{language}'",
            "available_languages": list(labels["text"].keys())
        }
    
    # Add disclosure at the beginning of the text
    labeled_text = f"[{disclosure}]\n\n{text_content}"
    
    # Determine if exemption applies
    exemption_applies = has_human_editor
    exemption_reason = "Human editorial oversight present" if has_human_editor else "No human editorial oversight"
    
    return {
        "article": "50(4)",
        "obligation": "AI-Generated Content Labeling (Text/News)",
        "language": language,
        "labeled_text": labeled_text,
        "disclosure": disclosure,
        "original_length": len(text_content),
        "labeled_length": len(labeled_text),
        "has_human_editor": has_human_editor,
        "exemption_applies": exemption_applies,
        "exemption_reason": exemption_reason,
        "compliance_deadline": "2026-08-02",
        "usage": "Publish the labeled_text instead of the original text"
    }