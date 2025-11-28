"""
Transparency Plugin - Article 50 Disclosures

Provides consolidated disclosure tools for AI interaction and emotion recognition.
"""

import os
import json
from typing import Dict, Any
from .base import BasePlugin


class TransparencyPlugin(BasePlugin):
    """
    Plugin for EU AI Act Article 50 transparency disclosures.
    
    Consolidates:
    - get_ai_interaction_disclosure
    - get_emotion_recognition_disclosure
    
    Into a single tool: get_disclosure
    """
    
    def get_name(self) -> str:
        return "TransparencyPlugin"
    
    def get_description(self) -> str:
        return "Provides EU AI Act Article 50 transparency disclosures for AI systems"
    
    def get_tools(self) -> Dict[str, Any]:
        return {
            "get_disclosure": self.get_disclosure,
            "get_deepfake_label_templates": self.get_deepfake_label_templates
        }
    
    def get_resources(self) -> Dict[str, Any]:
        return {
            "disclosure-templates://ai-interaction-and-emotion": self.get_disclosure_templates_resource
        }
    
    def get_disclosure_templates_resource(self) -> str:
        """Resource: Pre-written disclosure templates"""
        template_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "disclosure_templates.json"
        )
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def get_disclosure(
        self, 
        disclosure_type: str,
        language: str = "en", 
        style: str = "simple"
    ) -> Dict[str, Any]:
        """
        Get transparency disclosure text for EU AI Act Article 50 compliance.
        
        This consolidated tool provides disclosures for both AI interaction (50(1))
        and emotion recognition (50(3)).
        
        Args:
            disclosure_type: Type of disclosure - "ai_interaction" or "emotion_recognition"
            language: Language code (en, es, fr, de, it). Default: "en"
            style: Disclosure style. Default: "simple"
                For ai_interaction: "simple", "detailed", "voice"
                For emotion_recognition: "simple", "detailed", "privacy_notice"
        
        Returns:
            Dictionary containing the disclosure text and metadata
        
        Example:
            get_disclosure(disclosure_type="ai_interaction", language="en", style="simple")
            get_disclosure(disclosure_type="emotion_recognition", language="fr", style="detailed")
        """
        template_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "disclosure_templates.json"
        )
        
        with open(template_path, 'r', encoding='utf-8') as f:
            templates = json.load(f)
        
        # Validate disclosure type
        if disclosure_type not in ["ai_interaction", "emotion_recognition"]:
            return {
                "error": f"Invalid disclosure_type '{disclosure_type}'",
                "valid_types": ["ai_interaction", "emotion_recognition"]
            }
        
        # Get the requested disclosure
        try:
            disclosure_text = templates[disclosure_type][language][style]
        except KeyError:
            return {
                "error": f"Disclosure not found for type '{disclosure_type}', language '{language}', style '{style}'",
                "available_languages": list(templates.get(disclosure_type, {}).keys()),
                "available_styles": list(templates.get(disclosure_type, {}).get(language, {}).keys()) if language in templates.get(disclosure_type, {}) else []
            }
        
        # Build response based on type
        if disclosure_type == "ai_interaction":
            return {
                "article": "50(1)",
                "obligation": "AI Interaction Transparency",
                "disclosure_type": disclosure_type,
                "language": language,
                "style": style,
                "disclosure": disclosure_text,
                "usage": "Display this text to users before or during AI interaction",
                "compliance_deadline": "2026-08-02"
            }
        else:  # emotion_recognition
            return {
                "article": "50(3)",
                "obligation": "Emotion Recognition Transparency",
                "disclosure_type": disclosure_type,
                "language": language,
                "style": style,
                "disclosure": disclosure_text,
                "usage": "Display this text to users before activating emotion recognition",
                "gdpr_compliance": "Ensure user consent is obtained",
                "compliance_deadline": "2026-08-02"
            }
    
    def get_deepfake_label_templates(self, language: str = "en") -> Dict[str, Any]:
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
        """
        labels_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "deepfake_labels.json"
        )
        
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
