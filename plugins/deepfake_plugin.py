"""
Deepfake Labeling Plugin - Article 50(4) Content Labeling

Provides consolidated deepfake labeling tools for all content types.
"""

import os
import json
from typing import Dict, Any
from .base import BasePlugin


class DeepfakePlugin(BasePlugin):
    """
    Plugin for EU AI Act Article 50(4) deepfake labeling.
    
    Consolidates:
    - label_image_deepfake
    - label_video_deepfake
    - label_audio_deepfake
    - label_news_text
    
    Into a single tool: label_deepfake
    """
    
    def get_name(self) -> str:
        return "DeepfakePlugin"
    
    def get_description(self) -> str:
        return "Provides EU AI Act Article 50(4) deepfake labeling for AI-generated content"
    
    def get_tools(self) -> Dict[str, Any]:
        return {
            "label_deepfake": self.label_deepfake
        }
    
    def get_resources(self) -> Dict[str, Any]:
        return {
            "deepfake-labels://content-labeling": self.get_deepfake_labels_resource
        }
    
    def get_deepfake_labels_resource(self) -> str:
        """Resource: Deepfake labels"""
        labels_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "deepfake_labels.json"
        )
        with open(labels_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def label_deepfake(
        self,
        content_type: str,
        content_description: str,
        is_artistic_work: bool = False,
        is_satirical: bool = False,
        language: str = "en",
        text_content: str = None,
        has_human_editor: bool = False,
        editor_name: str = ""
    ) -> Dict[str, Any]:
        """
        Generate deepfake label for AI-generated or manipulated content per Article 50(4).
        
        This consolidated tool handles labeling for all content types:
        text, image, video, and audio.
        
        Args:
            content_type: Type of content - "text", "image", "video", or "audio"
            content_description: Brief description of the content
            is_artistic_work: Whether this is artistic/creative work (may qualify for exemption)
            is_satirical: Whether this is parody/satire (may qualify for exemption)
            language: Language code (en, es, fr, de). Default: "en"
            text_content: The actual text content (required only for content_type="text")
            has_human_editor: Whether a human editor reviewed the content (for text only)
            editor_name: Name of the human editor (for text only)
        
        Returns:
            Dictionary with label text, placement guidance, and compliance info
        
        Example:
            label_deepfake(content_type="image", content_description="AI portrait", language="en")
            label_deepfake(content_type="text", text_content="Article...", has_human_editor=True)
        """
        # Validate content type
        valid_types = ["text", "image", "video", "audio"]
        if content_type not in valid_types:
            return {
                "error": f"Invalid content_type '{content_type}'",
                "valid_types": valid_types
            }
        
        # Route to appropriate handler
        if content_type == "text":
            return self._label_text(text_content, has_human_editor, editor_name, language, content_description)
        elif content_type == "image":
            return self._label_image(content_description, is_artistic_work, is_satirical, language)
        elif content_type == "video":
            return self._label_video(content_description, is_artistic_work, is_satirical, language)
        else:  # audio
            return self._label_audio(content_description, is_artistic_work, language)
    
    def _label_text(
        self, 
        text_content: str, 
        has_human_editor: bool, 
        editor_name: str, 
        language: str,
        content_description: str
    ) -> Dict[str, Any]:
        """Label AI-generated text/news"""
        if text_content is None:
            return {
                "error": "text_content is required for content_type='text'",
                "usage": "Provide the actual text to be labeled"
            }
        
        labels_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "deepfake_labels.json"
        )
        
        with open(labels_path, 'r', encoding='utf-8') as f:
            labels = json.load(f)
        
        # Get the appropriate label
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
        
        # Add disclosure at the beginning
        labeled_text = f"[{disclosure}]\n\n{text_content}"
        
        # Determine exemption
        exemption_applies = has_human_editor
        exemption_reason = "Human editorial oversight present" if has_human_editor else "No human editorial oversight"
        
        return {
            "article": "50(4)",
            "obligation": "AI-Generated Content Labeling (Text/News)",
            "content_type": "text",
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
    
    def _label_image(
        self, 
        image_description: str, 
        is_artistic_work: bool, 
        is_satirical: bool, 
        language: str
    ) -> Dict[str, Any]:
        """Label AI-generated images"""
        labels_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "deepfake_labels.json"
        )
        
        with open(labels_path, 'r', encoding='utf-8') as f:
            labels = json.load(f)
        
        # Get the appropriate label
        try:
            if is_artistic_work or is_satirical:
                label_text = labels["image"][language]["artistic"]
                exemption_applies = True
                exemption_reason = "Artistic work or satire - modified disclosure"
            else:
                label_text = labels["image"][language]["standard"]
                exemption_applies = False
                exemption_reason = "Standard disclosure required"
        except KeyError:
            return {
                "error": f"Labels not found for language '{language}'",
                "available_languages": list(labels.get("image", {}).keys())
            }
        
        # Placement guidance
        placement_options = [
            "Top-left corner overlay",
            "Bottom banner overlay",
            "Visible watermark across image",
            "Caption below image"
        ]
        
        return {
            "article": "50(4)",
            "obligation": "Deepfake Labeling (Image)",
            "applies_to": "deployer",
            "content_type": "image",
            "image_description": image_description,
            "label_text": label_text,
            "language": language,
            "placement_options": placement_options,
            "recommended_placement": "Top-left corner overlay with semi-transparent background",
            "visibility_requirement": "Prominent and clearly distinguishable",
            "label_persistence": "Must not be easily removable",
            "is_artistic_work": is_artistic_work,
            "is_satirical": is_satirical,
            "exemption_applies": exemption_applies,
            "exemption_reason": exemption_reason,
            "compliance_deadline": "2026-08-02",
            "implementation_notes": [
                "Label must be visible without zooming or special tools",
                "Text size must be legible (minimum 12pt or 5% of image height)",
                "Background contrast must ensure readability",
                "Label should persist in downloaded/shared versions"
            ],
            "usage": "Add this label text to the image using one of the placement options"
        }
    
    def _label_video(
        self, 
        video_description: str, 
        is_artistic_work: bool, 
        is_satirical: bool, 
        language: str
    ) -> Dict[str, Any]:
        """Label AI-generated videos"""
        labels_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "deepfake_labels.json"
        )
        
        with open(labels_path, 'r', encoding='utf-8') as f:
            labels = json.load(f)
        
        # Get the appropriate label
        try:
            if is_artistic_work or is_satirical:
                label_text = labels["video"][language]["artistic"]
                exemption_applies = True
                exemption_reason = "Artistic work or satire - modified disclosure"
            else:
                label_text = labels["video"][language]["standard"]
                exemption_applies = False
                exemption_reason = "Standard disclosure required"
        except KeyError:
            return {
                "error": f"Labels not found for language '{language}'",
                "available_languages": list(labels.get("video", {}).keys())
            }
        
        # Placement guidance
        placement_options = [
            "Persistent overlay in corner throughout video",
            "Opening title card (3-5 seconds)",
            "Closing credit with disclosure",
            "Intermittent overlay every 30 seconds"
        ]
        
        return {
            "article": "50(4)",
            "obligation": "Deepfake Labeling (Video)",
            "applies_to": "deployer",
            "content_type": "video",
            "video_description": video_description,
            "label_text": label_text,
            "language": language,
            "placement_options": placement_options,
            "recommended_placement": "Persistent semi-transparent overlay in top-left corner",
            "visibility_requirement": "Clearly visible and distinguishable throughout playback",
            "label_persistence": "Must persist in all playback formats and cannot be easily removed",
            "timing_guidance": "If using title card, display for minimum 3 seconds at start",
            "is_artistic_work": is_artistic_work,
            "is_satirical": is_satirical,
            "exemption_applies": exemption_applies,
            "exemption_reason": exemption_reason,
            "compliance_deadline": "2026-08-02",
            "implementation_notes": [
                "Label must be visible at standard playback resolution",
                "Text size must be legible (minimum 5% of frame height)",
                "Use high contrast background for readability",
                "Label must persist through video editing and re-encoding",
                "Consider accessibility: include spoken disclosure for audio description"
            ],
            "usage": "Add this label to the video using one of the placement options"
        }
    
    def _label_audio(
        self, 
        audio_description: str, 
        is_artistic_work: bool, 
        language: str
    ) -> Dict[str, Any]:
        """Label AI-generated audio"""
        labels_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "deepfake_labels.json"
        )
        
        with open(labels_path, 'r', encoding='utf-8') as f:
            labels = json.load(f)
        
        # Get labels
        try:
            written_label = labels["audio"][language]["standard"]
            spoken_label = labels["audio"][language]["spoken"]
            
            exemption_applies = is_artistic_work
            exemption_reason = "Artistic work - modified disclosure may apply" if is_artistic_work else "Standard disclosure required"
        except KeyError:
            return {
                "error": f"Labels not found for language '{language}'",
                "available_languages": list(labels.get("audio", {}).keys())
            }
        
        # Disclosure methods
        disclosure_methods = [
            "Spoken announcement at beginning of audio",
            "Written disclosure in audio player interface",
            "Metadata embedded in audio file",
            "Text description accompanying audio"
        ]
        
        return {
            "article": "50(4)",
            "obligation": "Deepfake Labeling (Audio)",
            "applies_to": "deployer",
            "content_type": "audio",
            "audio_description": audio_description,
            "written_label": written_label,
            "spoken_label": spoken_label,
            "language": language,
            "disclosure_methods": disclosure_methods,
            "recommended_method": "Spoken announcement at beginning + written metadata",
            "spoken_disclosure_timing": "Beginning of audio (first 3 seconds)",
            "is_artistic_work": is_artistic_work,
            "exemption_applies": exemption_applies,
            "exemption_reason": exemption_reason,
            "compliance_deadline": "2026-08-02",
            "implementation_notes": [
                "Spoken disclosure should be clear and at normal speech volume",
                "Written disclosure must accompany audio in player/platform",
                "Embed disclosure in audio file metadata (ID3 tags, etc.)",
                "Consider accessibility: provide written version for deaf users",
                "Disclosure should be in same language as primary audio content"
            ],
            "usage": "Add spoken disclosure at audio start and include written label in metadata/description"
        }
