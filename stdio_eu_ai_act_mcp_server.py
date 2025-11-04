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
    template_path = os.path.join(os.path.dirname(__file__), "resources", "disclosure_templates.json")
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
    labels_path = os.path.join(os.path.dirname(__file__), "resources", "deepfake_labels.json")
    with open(labels_path, 'r', encoding='utf-8') as f:
        return f.read()


@mcp.resource("article50-rules://official-text")
def get_article50_rules() -> str:
    """
    Provides the official EU AI Act Article 50 rules and requirements.
    
    Contains:
    - Complete Article 50 obligations (paragraphs 50(1), 50(2), 50(3), 50(4))
    - Provider obligations (AI interaction, content watermarking)
    - Deployer obligations (emotion recognition, deepfake labeling)
    - Exceptions and exemptions
    - Compliance deadlines
    - Penalty information
    - Key definitions
    
    Use this resource to understand which obligations apply to your AI system.
    """
    rules_path = os.path.join(os.path.dirname(__file__), "resources", "article50_rules.json")
    with open(rules_path, 'r', encoding='utf-8') as f:
        return f.read()


@mcp.resource("watermark-config://technical-standards")
def get_watermark_config() -> str:
    """
    Provides watermarking configuration and technical standards for Article 50(2).
    
    Contains:
    - C2PA 2.1 specifications (Coalition for Content Provenance and Authenticity)
    - IPTC metadata standards
    - Content type configurations (image, video, audio, text)
    - Embedding settings and parameters
    - Verification methods
    - Implementation guide
    
    Use this resource to understand how to properly watermark AI-generated content
    with machine-readable, detectable metadata that complies with Article 50(2).
    """
    config_path = os.path.join(os.path.dirname(__file__), "resources", "watermark_config.json")
    with open(config_path, 'r', encoding='utf-8') as f:
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
    template_path = os.path.join(os.path.dirname(__file__), "resources", "disclosure_templates.json")
    
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
    template_path = os.path.join(os.path.dirname(__file__), "resources", "disclosure_templates.json")
    
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
    labels_path = os.path.join(os.path.dirname(__file__), "resources", "deepfake_labels.json")
    
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
    labels_path = os.path.join(os.path.dirname(__file__), "resources", "deepfake_labels.json")
    
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


@mcp.tool()
def watermark_text(
    text_content: str,
    generator: str = "AI",
    format_type: str = "plain"
) -> Dict[str, Any]:
    """
    Add metadata watermark to AI-generated text for EU AI Act Article 50(2) compliance.
    
    This tool adds machine-readable metadata to AI-generated text content,
    marking it as artificially generated. This is required for provider compliance
    with Article 50(2) for text content generation systems.
    
    Args:
        text_content: The AI-generated text to watermark
        generator: Name of the AI system that generated it (e.g., "GPT-4", "Claude", "Custom AI")
        format_type: Output format (plain, markdown, html). Default: "plain"
        
    Returns:
        Dictionary containing the watermarked text with embedded metadata
        
    Example:
        watermark_text(
            text_content="This is AI-generated content...",
            generator="GPT-4",
            format_type="markdown"
        )
    """
    import hashlib
    from datetime import datetime, timezone
    
    # Generate content hash for integrity verification
    content_hash = hashlib.sha256(text_content.encode('utf-8')).hexdigest()[:16]
    
    # Create timestamp
    timestamp = datetime.now(timezone.utc).isoformat()
    
    # Create metadata
    metadata = {
        "ai_generated": True,
        "generator": generator,
        "timestamp": timestamp,
        "content_hash": content_hash,
        "compliance": "EU AI Act Article 50(2)",
        "watermark_version": "1.0"
    }
    
    # Format the watermarked text based on format type
    if format_type == "html":
        watermarked_text = f'''<!-- AI-Generated Content Metadata
{json.dumps(metadata, indent=2)}
-->
{text_content}'''
    elif format_type == "markdown":
        watermarked_text = f'''<!-- AI Watermark: {json.dumps(metadata)} -->

{text_content}'''
    else:  # plain text
        metadata_str = json.dumps(metadata, separators=(',', ':'))
        watermarked_text = f"[AI-WATERMARK:{metadata_str}]\n\n{text_content}"
    
    return {
        "article": "50(2)",
        "obligation": "Content Watermarking (Text)",
        "watermarked_text": watermarked_text,
        "metadata": metadata,
        "original_length": len(text_content),
        "watermarked_length": len(watermarked_text),
        "format": format_type,
        "machine_readable": True,
        "detectable": True,
        "compliance_deadline": "2026-08-02",
        "usage": "Use watermarked_text instead of original. Metadata is machine-readable.",
        "verification": f"Content hash: {content_hash}"
    }


@mcp.tool()
def label_image_deepfake(
    image_description: str,
    is_artistic_work: bool = False,
    is_satirical: bool = False,
    language: str = "en"
) -> Dict[str, Any]:
    """
    Generate deepfake label for AI-generated or manipulated images per Article 50(4).
    
    This tool provides the appropriate disclosure text and guidance for labeling
    images that have been artificially generated or manipulated. The label must
    be prominent, clear, and distinguishable.
    
    Args:
        image_description: Brief description of the image for context
        is_artistic_work: Whether this is artistic/creative work (may qualify for exemption)
        is_satirical: Whether this is parody/satire (may qualify for exemption)
        language: Language code (en, es, fr, de). Default: "en"
        
    Returns:
        Dictionary with label text, placement guidance, and compliance info
        
    Example:
        label_image_deepfake(
            image_description="AI-generated portrait of a person",
            is_artistic_work=False,
            language="en"
        )
    """
    labels_path = os.path.join(os.path.dirname(__file__), "resources", "deepfake_labels.json")
    
    with open(labels_path, 'r', encoding='utf-8') as f:
        labels = json.load(f)
    
    # Get the appropriate label based on artistic status
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
    
    # Generate placement guidance
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


@mcp.tool()
def label_video_deepfake(
    video_description: str,
    is_artistic_work: bool = False,
    is_satirical: bool = False,
    language: str = "en"
) -> Dict[str, Any]:
    """
    Generate deepfake label for AI-generated or manipulated videos per Article 50(4).
    
    This tool provides the appropriate disclosure text and guidance for labeling
    videos that have been artificially generated or manipulated. The label must
    be prominent, clear, and distinguishable throughout the video.
    
    Args:
        video_description: Brief description of the video for context
        is_artistic_work: Whether this is artistic/creative work (may qualify for exemption)
        is_satirical: Whether this is parody/satire (may qualify for exemption)
        language: Language code (en, es, fr, de). Default: "en"
        
    Returns:
        Dictionary with label text, placement guidance, and compliance info
        
    Example:
        label_video_deepfake(
            video_description="AI-generated video of a speech",
            is_artistic_work=False,
            language="en"
        )
    """
    labels_path = os.path.join(os.path.dirname(__file__), "resources", "deepfake_labels.json")
    
    with open(labels_path, 'r', encoding='utf-8') as f:
        labels = json.load(f)
    
    # Get the appropriate label based on artistic status
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
    
    # Generate placement guidance for video
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


@mcp.tool()
def label_audio_deepfake(
    audio_description: str,
    is_artistic_work: bool = False,
    language: str = "en"
) -> Dict[str, Any]:
    """
    Generate deepfake label for AI-generated or manipulated audio per Article 50(4).
    
    This tool provides disclosure text for audio content that has been artificially
    generated or manipulated. For audio, disclosure can be spoken, written in
    accompanying materials, or both.
    
    Args:
        audio_description: Brief description of the audio for context
        is_artistic_work: Whether this is artistic/creative work (may qualify for exemption)
        language: Language code (en, es, fr, de). Default: "en"
        
    Returns:
        Dictionary with label text (written and spoken), placement guidance, and compliance info
        
    Example:
        label_audio_deepfake(
            audio_description="AI-generated voice recording",
            is_artistic_work=False,
            language="en"
        )
    """
    labels_path = os.path.join(os.path.dirname(__file__), "resources", "deepfake_labels.json")
    
    with open(labels_path, 'r', encoding='utf-8') as f:
        labels = json.load(f)
    
    # Get labels for audio
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
    
    # Disclosure methods for audio
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


@mcp.tool()
def watermark_image(
    image_description: str,
    generator: str = "AI",
    format_type: str = "png"
) -> Dict[str, Any]:
    """
    Generate watermarking metadata for AI-generated images per Article 50(2).
    
    This tool provides C2PA-compliant metadata and instructions for watermarking
    AI-generated images. The watermark must be machine-readable and detectable.
    
    Args:
        image_description: Brief description of the image
        generator: Name of AI system that generated it (e.g., "DALL-E", "Midjourney")
        format_type: Image format (png, jpg, webp). Default: "png"
        
    Returns:
        Dictionary with watermarking metadata, instructions, and compliance info
        
    Example:
        watermark_image(
            image_description="AI-generated landscape",
            generator="DALL-E",
            format_type="png"
        )
    """
    from datetime import datetime, timezone
    import hashlib
    
    timestamp = datetime.now(timezone.utc).isoformat()
    content_hash = hashlib.sha256(image_description.encode()).hexdigest()[:16]
    
    # C2PA metadata structure
    c2pa_metadata = {
        "claim_generator": "EU AI Act Compliance MCP Server",
        "claim_timestamp": timestamp,
        "assertions": {
            "c2pa.actions": "ai_generated",
            "stds.schema-org.CreativeWork": {
                "creator": generator,
                "dateCreated": timestamp,
                "description": image_description,
                "ai_generated": True
            }
        },
        "signature": "ES256",
        "hash_algorithm": "SHA-256",
        "content_hash": content_hash
    }
    
    # IPTC metadata
    iptc_metadata = {
        "Digital Source Type": "trainedAlgorithmicMedia",
        "Credit": f"Generated by {generator}",
        "Creator": generator,
        "Date Created": timestamp,
        "Copyright Notice": "AI-generated content subject to EU AI Act Article 50(2)"
    }
    
    return {
        "article": "50(2)",
        "obligation": "Content Watermarking (Image)",
        "applies_to": "provider",
        "image_description": image_description,
        "generator": generator,
        "format": format_type,
        "c2pa_metadata": c2pa_metadata,
        "iptc_metadata": iptc_metadata,
        "watermark_standard": "C2PA 2.1",
        "machine_readable": True,
        "detectable": True,
        "compliance_deadline": "2026-08-02",
        "implementation_instructions": [
            f"1. Use C2PA library to embed metadata in {format_type} file",
            "2. Add IPTC metadata as fallback",
            "3. Ensure watermark survives compression and resizing",
            "4. Verify watermark using C2PA verification tools",
            "5. Store watermarked version separately from original"
        ],
        "verification_url": "https://verify.contentauthenticity.org/",
        "usage": "Use provided metadata to watermark the image file using C2PA-compliant tools"
    }


@mcp.tool()
def watermark_video(
    video_description: str,
    generator: str = "AI",
    format_type: str = "mp4"
) -> Dict[str, Any]:
    """
    Generate watermarking metadata for AI-generated videos per Article 50(2).
    
    This tool provides C2PA-compliant metadata and instructions for watermarking
    AI-generated videos. The watermark must be machine-readable and detectable.
    
    Args:
        video_description: Brief description of the video
        generator: Name of AI system that generated it
        format_type: Video format (mp4, webm, mov). Default: "mp4"
        
    Returns:
        Dictionary with watermarking metadata, instructions, and compliance info
    """
    from datetime import datetime, timezone
    import hashlib
    
    timestamp = datetime.now(timezone.utc).isoformat()
    content_hash = hashlib.sha256(video_description.encode()).hexdigest()[:16]
    
    c2pa_metadata = {
        "claim_generator": "EU AI Act Compliance MCP Server",
        "claim_timestamp": timestamp,
        "assertions": {
            "c2pa.actions": "ai_generated",
            "stds.schema-org.VideoObject": {
                "creator": generator,
                "dateCreated": timestamp,
                "description": video_description,
                "ai_generated": True
            }
        },
        "signature": "ES256",
        "hash_algorithm": "SHA-256",
        "content_hash": content_hash
    }
    
    return {
        "article": "50(2)",
        "obligation": "Content Watermarking (Video)",
        "applies_to": "provider",
        "video_description": video_description,
        "generator": generator,
        "format": format_type,
        "c2pa_metadata": c2pa_metadata,
        "watermark_standard": "C2PA 2.1",
        "watermark_method": "Frame-level embedding",
        "machine_readable": True,
        "detectable": True,
        "compliance_deadline": "2026-08-02",
        "implementation_instructions": [
            f"1. Use C2PA video library to embed metadata in {format_type} file",
            "2. Apply watermark at frame level for persistence",
            "3. Embed metadata in video container and frames",
            "4. Ensure watermark survives re-encoding",
            "5. Test with multiple video players"
        ],
        "verification_url": "https://verify.contentauthenticity.org/",
        "usage": "Use provided metadata to watermark the video file using C2PA-compliant tools"
    }


@mcp.tool()
def watermark_audio(
    audio_description: str,
    generator: str = "AI",
    format_type: str = "mp3"
) -> Dict[str, Any]:
    """
    Generate watermarking metadata for AI-generated audio per Article 50(2).
    
    This tool provides metadata and instructions for watermarking AI-generated audio.
    Audio watermarks use fingerprinting and metadata embedding.
    
    Args:
        audio_description: Brief description of the audio
        generator: Name of AI system that generated it
        format_type: Audio format (mp3, wav, opus). Default: "mp3"
        
    Returns:
        Dictionary with watermarking metadata, instructions, and compliance info
    """
    from datetime import datetime, timezone
    import hashlib
    
    timestamp = datetime.now(timezone.utc).isoformat()
    content_hash = hashlib.sha256(audio_description.encode()).hexdigest()[:16]
    
    c2pa_metadata = {
        "claim_generator": "EU AI Act Compliance MCP Server",
        "claim_timestamp": timestamp,
        "assertions": {
            "c2pa.actions": "ai_generated",
            "stds.schema-org.AudioObject": {
                "creator": generator,
                "dateCreated": timestamp,
                "description": audio_description,
                "ai_generated": True
            }
        },
        "content_hash": content_hash
    }
    
    # Audio-specific metadata
    audio_metadata = {
        "ID3_tags": {
            "TIT2": audio_description,
            "TPE1": generator,
            "COMM": "AI-generated audio - EU AI Act Article 50(2)",
            "TDRC": timestamp
        }
    }
    
    return {
        "article": "50(2)",
        "obligation": "Content Watermarking (Audio)",
        "applies_to": "provider",
        "audio_description": audio_description,
        "generator": generator,
        "format": format_type,
        "c2pa_metadata": c2pa_metadata,
        "audio_metadata": audio_metadata,
        "watermark_method": "Spectral embedding + ID3 tags",
        "machine_readable": True,
        "detectable": True,
        "inaudible": True,
        "compliance_deadline": "2026-08-02",
        "implementation_instructions": [
            f"1. Embed C2PA metadata in {format_type} file",
            "2. Add ID3 tags for MP3 or equivalent for other formats",
            "3. Apply inaudible spectral watermark (18-20kHz range)",
            "4. Ensure watermark survives format conversion",
            "5. Test detectability after compression"
        ],
        "usage": "Use provided metadata to watermark the audio file"
    }


# ============================================================================
# RISK CLASSIFICATION TOOLS - Articles 5, 6, and Annex III
# ============================================================================

@mcp.tool()
def classify_ai_system_risk(
    system_description: str,
    use_case: str,
    biometric_data: bool = False,
    critical_infrastructure: bool = False,
    education: bool = False,
    law_enforcement: bool = False,
    predicts_criminal_behavior: bool = False,
    social_scoring: bool = False,
    emotion_detection_workplace: bool = False,
    generates_content: bool = False,
    interacts_with_users: bool = False
) -> Dict[str, Any]:
    """
    Determine AI system risk level per EU AI Act classification framework.
    
    Classifies system as: PROHIBITED, HIGH-RISK, LIMITED-RISK, or MINIMAL-RISK
    based on Articles 5, 6, and 50.
    
    Args:
        system_description: Description of the AI system
        use_case: Primary use case (e.g., "employment", "healthcare", "chatbot")
        biometric_data: Uses biometric identification/categorization
        critical_infrastructure: Used in critical infrastructure
        education: Used in education/vocational training
        law_enforcement: Used for law enforcement
        predicts_criminal_behavior: Predicts criminal behavior from profiling
        social_scoring: Performs social scoring
        emotion_detection_workplace: Detects emotions in workplace/education
        generates_content: Generates synthetic content
        interacts_with_users: Interacts with natural persons
        
    Returns:
        Risk classification with applicable obligations and deadlines
    """
    
    # Step 1: Check Article 5 - PROHIBITED practices
    if social_scoring:
        return {
            "risk_level": "PROHIBITED",
            "article": "Article 5(1)(c)",
            "reason": "Social scoring by public authorities or on their behalf",
            "system_description": system_description,
            "compliance_action": "MUST NOT deploy - System is prohibited",
            "penalties": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "deadline": "Immediate - Already in effect",
            "recommendation": "Discontinue development or deployment immediately"
        }
    
    if emotion_detection_workplace:
        return {
            "risk_level": "PROHIBITED",
            "article": "Article 5(1)(f)",
            "reason": "Emotion recognition in workplace or education (except medical/safety)",
            "system_description": system_description,
            "compliance_action": "MUST NOT deploy - System is prohibited",
            "exception": "Allowed only for medical or safety reasons",
            "penalties": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "deadline": "Immediate - Already in effect",
            "recommendation": "Remove emotion detection or limit to medical/safety contexts"
        }
    
    if predicts_criminal_behavior:
        return {
            "risk_level": "PROHIBITED",
            "article": "Article 5(1)(d)",
            "reason": "Risk assessment predicting criminal offenses based on profiling",
            "system_description": system_description,
            "compliance_action": "MUST NOT deploy - System is prohibited",
            "penalties": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "deadline": "Immediate - Already in effect",
            "recommendation": "Discontinue predictive profiling features"
        }
    
    # Step 2: Check Article 6 + Annex III - HIGH-RISK systems
    high_risk_checks = []
    
    if biometric_data:
        high_risk_checks.append({
            "reason": "Biometric identification or categorization",
            "annex_point": "Annex III point 1",
            "article_ref": "Article 6(2)"
        })
    
    if use_case.lower() in ["employment", "hiring", "hr", "recruitment"]:
        high_risk_checks.append({
            "reason": "AI system for employment, recruitment, or HR decisions",
            "annex_point": "Annex III point 4(a)",
            "article_ref": "Article 6(2)"
        })
    
    if education:
        high_risk_checks.append({
            "reason": "AI system for education or vocational training",
            "annex_point": "Annex III point 3",
            "article_ref": "Article 6(2)"
        })
    
    if law_enforcement:
        high_risk_checks.append({
            "reason": "AI system for law enforcement",
            "annex_point": "Annex III point 6",
            "article_ref": "Article 6(2)"
        })
    
    if critical_infrastructure:
        high_risk_checks.append({
            "reason": "AI system for critical infrastructure",
            "annex_point": "Annex III point 2",
            "article_ref": "Article 6(2)"
        })
    
    if high_risk_checks:
        return {
            "risk_level": "HIGH-RISK",
            "article": high_risk_checks[0]["article_ref"],
            "annex_reference": high_risk_checks[0]["annex_point"],
            "reason": high_risk_checks[0]["reason"],
            "system_description": system_description,
            "all_high_risk_factors": [check["reason"] for check in high_risk_checks],
            "applicable_obligations": [
                "Risk management system (Article 9)",
                "Data governance and management (Article 10)",
                "Technical documentation (Article 11)",
                "Record-keeping/logging (Article 12)",
                "Transparency and information to users (Article 13)",
                "Human oversight (Article 14)",
                "Accuracy, robustness, cybersecurity (Article 15)",
                "Quality management system (Article 17)",
                "Conformity assessment (Article 43)",
                "Registration in EU database (Article 49)",
                "Post-market monitoring (Article 72)"
            ],
            "compliance_deadline": "2027-08-02",
            "penalties_if_non_compliant": "Up to €15 million or 3% of global annual turnover",
            "next_steps": [
                "Conduct conformity assessment",
                "Implement risk management system",
                "Create technical documentation",
                "Establish human oversight mechanisms",
                "Register in EU database before deployment"
            ]
        }
    
    # Step 3: Check Article 50 - LIMITED-RISK systems
    limited_risk_checks = []
    
    if interacts_with_users:
        limited_risk_checks.append({
            "reason": "AI system interacts with natural persons",
            "article": "Article 50(1)",
            "obligation": "Must disclose AI interaction to users"
        })
    
    if generates_content:
        limited_risk_checks.append({
            "reason": "Generates synthetic audio, image, video, or text content",
            "article": "Article 50(2)",
            "obligation": "Must watermark AI-generated content"
        })
    
    if limited_risk_checks:
        return {
            "risk_level": "LIMITED-RISK",
            "article": "Article 50",
            "reason": "; ".join([check["reason"] for check in limited_risk_checks]),
            "system_description": system_description,
            "applicable_obligations": [check["obligation"] for check in limited_risk_checks],
            "compliance_deadline": "2026-08-02",
            "penalties_if_non_compliant": "Up to €15 million or 3% of global annual turnover",
            "next_steps": [
                "Implement transparency disclosures (Article 50)",
                "Add watermarks if generating content (Article 50(2))",
                "Ensure users know they're interacting with AI (Article 50(1))"
            ]
        }
    
    # Step 4: Default - MINIMAL-RISK
    return {
        "risk_level": "MINIMAL-RISK",
        "article": "No specific article applies",
        "reason": "System does not fall under prohibited, high-risk, or limited-risk categories",
        "system_description": system_description,
        "applicable_obligations": [
            "Voluntary codes of conduct (Article 95)",
            "General transparency best practices"
        ],
        "compliance_deadline": "No mandatory deadline",
        "penalties_if_non_compliant": "None (voluntary compliance)",
        "next_steps": [
            "Consider voluntary transparency measures",
            "Follow industry best practices",
            "Monitor for regulatory updates"
        ]
    }


@mcp.tool()
def check_prohibited_practices(
    uses_subliminal_techniques: bool = False,
    exploits_vulnerabilities: bool = False,
    social_scoring: bool = False,
    predicts_crime_from_profiling: bool = False,
    scrapes_facial_images: bool = False,
    detects_emotions_in_workplace: bool = False,
    biometric_categorization_sensitive_attributes: bool = False,
    real_time_biometric_identification_public: bool = False
) -> Dict[str, Any]:
    """
    Check if AI system violates prohibited practices under Article 5.
    
    These practices carry the HIGHEST penalties: €35M or 7% of global revenue.
    
    Args:
        uses_subliminal_techniques: Manipulates behavior via subliminal techniques
        exploits_vulnerabilities: Exploits vulnerabilities of specific groups
        social_scoring: Social scoring by/for public authorities
        predicts_crime_from_profiling: Predicts criminal behavior from profiling
        scrapes_facial_images: Scrapes facial images from internet/CCTV
        detects_emotions_in_workplace: Emotion recognition in workplace/education
        biometric_categorization_sensitive_attributes: Infers race, politics, etc. from biometrics
        real_time_biometric_identification_public: Real-time biometric ID in public spaces
        
    Returns:
        Violations found with penalties and recommendations
    """
    
    violations = []
    
    if uses_subliminal_techniques:
        violations.append({
            "article": "Article 5(1)(a)",
            "violation": "Subliminal techniques to manipulate behavior",
            "description": "AI systems that deploy subliminal techniques beyond a person's consciousness to materially distort behavior",
            "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "exception": "None"
        })
    
    if exploits_vulnerabilities:
        violations.append({
            "article": "Article 5(1)(b)",
            "violation": "Exploitation of vulnerabilities",
            "description": "AI systems that exploit vulnerabilities of specific groups (age, disability, social/economic situation)",
            "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "exception": "None"
        })
    
    if social_scoring:
        violations.append({
            "article": "Article 5(1)(c)",
            "violation": "Social scoring",
            "description": "AI systems for social scoring by public authorities or on their behalf",
            "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "exception": "None"
        })
    
    if predicts_crime_from_profiling:
        violations.append({
            "article": "Article 5(1)(d)",
            "violation": "Predictive policing based on profiling",
            "description": "AI systems that make risk assessments of natural persons to predict criminal offenses based solely on profiling",
            "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "exception": "None"
        })
    
    if scrapes_facial_images:
        violations.append({
            "article": "Article 5(1)(e)",
            "violation": "Untargeted scraping of facial images",
            "description": "Creating or expanding facial recognition databases through untargeted scraping from internet or CCTV",
            "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "exception": "None"
        })
    
    if detects_emotions_in_workplace:
        violations.append({
            "article": "Article 5(1)(f)",
            "violation": "Emotion recognition in workplace or education",
            "description": "AI systems that infer emotions in workplace or educational institutions",
            "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "exception": "Medical or safety reasons only"
        })
    
    if biometric_categorization_sensitive_attributes:
        violations.append({
            "article": "Article 5(1)(g)",
            "violation": "Biometric categorization of sensitive attributes",
            "description": "Biometric categorization systems that infer race, political opinions, trade union membership, religious/philosophical beliefs, sex life, or sexual orientation",
            "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "exception": "Limited exceptions for law enforcement with safeguards"
        })
    
    if real_time_biometric_identification_public:
        violations.append({
            "article": "Article 5(1)(h)",
            "violation": "Real-time remote biometric identification in public",
            "description": "Real-time remote biometric identification systems in publicly accessible spaces for law enforcement",
            "penalty": "Up to €35 million or 7% of global annual turnover (whichever is higher)",
            "exception": "Very limited exceptions for serious crimes with judicial authorization"
        })
    
    if violations:
        return {
            "is_prohibited": True,
            "severity": "CRITICAL - Highest penalty tier",
            "violations": violations,
            "violation_count": len(violations),
            "total_penalty_exposure": "Up to €35 million or 7% of global annual turnover PER violation",
            "recommendation": "STOP IMMEDIATELY - These AI practices are PROHIBITED under EU AI Act",
            "required_actions": [
                "Cease development and deployment immediately",
                "Notify relevant supervisory authorities",
                "Assess alternatives that comply with EU AI Act",
                "Consult legal counsel for remediation strategy"
            ],
            "compliance_status": "NON-COMPLIANT - Critical violation"
        }
    
    return {
        "is_prohibited": False,
        "severity": "None",
        "violations": [],
        "violation_count": 0,
        "recommendation": "No prohibited practices detected",
        "compliance_status": "COMPLIANT with Article 5 prohibitions",
        "next_steps": [
            "Continue to check high-risk and limited-risk classifications",
            "Monitor for regulatory updates",
            "Maintain compliance documentation"
        ]
    }


@mcp.tool()
def determine_eu_ai_act_role(
    company_description: str,
    company_location: str,
    develops_ai_system: bool = False,
    uses_ai_system: bool = False,
    sells_ai_system: bool = False,
    imports_to_eu: bool = False,
    distributes_in_eu: bool = False,
    integrates_ai_into_product: bool = False,
    represents_non_eu_provider: bool = False,
    under_own_name_or_trademark: bool = False,
    substantial_modification: bool = False,
    change_intended_purpose: bool = False
) -> Dict[str, Any]:
    """
    Determine which EU AI Act role(s) apply to your organization.
    
    Different roles have different obligations under the EU AI Act.
    Understanding your role is CRITICAL to knowing which requirements apply.
    
    Args:
        company_description: Brief description of your company/organization
        company_location: Country/region where company is based
        develops_ai_system: You develop AI systems or commission their development
        uses_ai_system: You use AI systems in your operations
        sells_ai_system: You sell or offer AI systems
        imports_to_eu: You bring AI systems from outside EU into EU market
        distributes_in_eu: You distribute/resell AI systems in EU
        integrates_ai_into_product: You integrate AI into physical products
        represents_non_eu_provider: You represent a non-EU AI provider in the EU
        under_own_name_or_trademark: AI system bears your name/trademark
        substantial_modification: You substantially modify existing AI systems
        change_intended_purpose: You change the intended purpose of AI systems
        
    Returns:
        Role determination with definitions and applicable obligations
    """
    
    roles_identified = []
    role_details = {}
    is_in_eu = company_location.lower() in ["eu", "european union"] or any(
        country in company_location.lower() 
        for country in ["germany", "france", "spain", "italy", "netherlands", 
                       "belgium", "austria", "ireland", "portugal", "greece"]
    )
    
    # Step 1: Check if PROVIDER
    is_provider = (
        develops_ai_system or
        (sells_ai_system and under_own_name_or_trademark) or
        substantial_modification or
        change_intended_purpose
    )
    
    if is_provider:
        reason_parts = []
        if develops_ai_system:
            reason_parts.append("develops AI systems")
        if sells_ai_system and under_own_name_or_trademark:
            reason_parts.append("places AI on market under own name/trademark")
        if substantial_modification:
            reason_parts.append("substantially modifies AI systems")
        if change_intended_purpose:
            reason_parts.append("changes intended purpose of AI systems")
        
        roles_identified.append("PROVIDER")
        role_details["provider"] = {
            "article": "Article 3(3)",
            "definition": "Develops the AI system or has it developed, and places it on the market or puts it into service under own name or trademark",
            "applies_to_you": True,
            "reason": f"You {' and '.join(reason_parts)}",
            "key_obligations": [
                "Establish risk management system (Article 9)",
                "Data governance and quality (Article 10)",
                "Technical documentation (Article 11)",
                "Automatic logging (Article 12)",
                "Design for human oversight (Article 14)",
                "Accuracy and robustness (Article 15)",
                "Cybersecurity measures (Article 15)",
                "Quality management system (Article 17)",
                "Conformity assessment (Article 43)",
                "CE marking (Article 48)",
                "EU database registration (Article 49)"
            ],
            "deadline": "2027-08-02 (for high-risk systems)",
            "penalties": "Up to €15M or 3% of global turnover for non-compliance"
        }
    
    # Step 2: Check if DEPLOYER
    is_deployer = uses_ai_system
    
    if is_deployer:
        roles_identified.append("DEPLOYER")
        role_details["deployer"] = {
            "article": "Article 3(4)",
            "definition": "Uses an AI system under their authority, except for personal non-professional activity",
            "applies_to_you": True,
            "reason": "You use AI systems in your operations",
            "key_obligations": [
                "Use AI according to instructions (Article 26(1))",
                "Ensure human oversight (Article 26(2))",
                "Monitor AI system operation (Article 26(3))",
                "Report serious incidents (Article 26(4))",
                "Keep logs generated by AI system (Article 26(5))",
                "Conduct fundamental rights impact assessment (Article 27)",
                "Inform workers about AI monitoring systems (Article 26(7))",
                "Ensure input data quality (Article 26(6))"
            ],
            "deadline": "2027-08-02 (for high-risk systems)",
            "penalties": "Up to €15M or 3% of global turnover for non-compliance"
        }
    
    # Step 3: Check if IMPORTER
    is_importer = (
        not is_in_eu and
        imports_to_eu and
        (sells_ai_system or distributes_in_eu) and
        under_own_name_or_trademark
    )
    
    if is_importer:
        roles_identified.append("IMPORTER")
        role_details["importer"] = {
            "article": "Article 3(5)",
            "definition": "Places on the market an AI system that bears the name or trademark of a person established outside the EU",
            "applies_to_you": True,
            "reason": f"You are based in {company_location} and import AI systems to EU market",
            "key_obligations": [
                "Verify provider's conformity assessment (Article 23(1))",
                "Verify CE marking and documentation (Article 23(2))",
                "Ensure registration in EU database (Article 23(3))",
                "Keep copy of technical documentation (Article 23(4))",
                "Provide authorities with documentation (Article 23(5))",
                "Ensure storage/transport doesn't affect compliance (Article 23(6))",
                "Appoint authorized representative in EU (Article 22)"
            ],
            "deadline": "2027-08-02",
            "penalties": "Up to €15M or 3% of global turnover for non-compliance"
        }
    
    # Step 4: Check if DISTRIBUTOR
    is_distributor = (
        distributes_in_eu and
        not is_provider and
        not is_importer and
        sells_ai_system
    )
    
    if is_distributor:
        roles_identified.append("DISTRIBUTOR")
        role_details["distributor"] = {
            "article": "Article 3(6)",
            "definition": "Makes an AI system available on the market without being the provider or importer",
            "applies_to_you": True,
            "reason": "You distribute AI systems in the EU market",
            "key_obligations": [
                "Verify CE marking present (Article 24(1))",
                "Verify required documentation provided (Article 24(2))",
                "Verify provider/importer obligations met (Article 24(3))",
                "Inform provider/importer of non-compliance (Article 24(4))",
                "Cooperate with authorities (Article 24(5))"
            ],
            "deadline": "2027-08-02",
            "penalties": "Up to €15M or 3% of global turnover for non-compliance"
        }
    
    # Step 5: Check if AUTHORIZED REPRESENTATIVE
    is_authorized_rep = (
        is_in_eu and
        represents_non_eu_provider
    )
    
    if is_authorized_rep:
        roles_identified.append("AUTHORIZED REPRESENTATIVE")
        role_details["authorized_representative"] = {
            "article": "Article 3(7)",
            "definition": "Natural or legal person located in the EU who has received a written mandate from a provider outside the EU",
            "applies_to_you": True,
            "reason": f"You are based in {company_location} (EU) and represent a non-EU AI provider",
            "key_obligations": [
                "Perform tasks specified in mandate (Article 22(1))",
                "Provide copy of technical documentation to authorities (Article 22(2))",
                "Cooperate with authorities (Article 22(3))",
                "Terminate mandate if provider non-compliant (Article 22(4))"
            ],
            "deadline": "2027-08-02",
            "penalties": "Provider's penalties may apply"
        }
    
    # Step 6: Check if PRODUCT MANUFACTURER
    is_product_manufacturer = (
        integrates_ai_into_product and
        under_own_name_or_trademark
    )
    
    if is_product_manufacturer:
        roles_identified.append("PRODUCT MANUFACTURER")
        role_details["product_manufacturer"] = {
            "article": "Article 3(8) + Article 25",
            "definition": "Manufactures a product and integrates an AI system into it, where the AI is a safety component or the product itself",
            "applies_to_you": True,
            "reason": "You integrate AI systems into physical products under your name/trademark",
            "key_obligations": [
                "Assume provider obligations for AI component (Article 25(1))",
                "Ensure AI system complies with requirements (Article 25(2))",
                "Affix own name/trademark to product (Article 25(3))",
                "Follow relevant product safety legislation",
                "Conduct conformity assessment for AI component"
            ],
            "deadline": "2027-08-02",
            "penalties": "Provider penalties apply (up to €15M or 3% of turnover)"
        }
    
    # Determine primary role
    if not roles_identified:
        return {
            "primary_role": "NO DIRECT ROLE",
            "additional_roles": [],
            "role_details": {},
            "company_description": company_description,
            "company_location": company_location,
            "assessment": "Based on provided information, you may not have direct EU AI Act obligations",
            "recommendation": "If you interact with AI systems in any way, review the questions again. You may be a deployer if you use AI systems.",
            "next_steps": [
                "Verify you are not using AI systems in your operations",
                "If you are using AI, you are likely a DEPLOYER",
                "Monitor for regulatory changes that may affect your activities"
            ]
        }
    
    primary_role = roles_identified[0]
    additional_roles = roles_identified[1:] if len(roles_identified) > 1 else []
    
    return {
        "primary_role": primary_role,
        "additional_roles": additional_roles,
        "all_roles": roles_identified,
        "role_details": role_details,
        "company_description": company_description,
        "company_location": company_location,
        "is_eu_based": is_in_eu,
        "total_roles": len(roles_identified),
        "critical_note": "If you have multiple roles, you must comply with ALL obligations for each role",
        "most_common_combination": "Many companies are both PROVIDER (they develop) and DEPLOYER (they use their own AI)",
        "recommendation": f"Focus first on {primary_role} obligations, then address {', '.join(additional_roles) if additional_roles else 'other compliance areas'}",
        "next_steps": [
            f"Review all {primary_role} obligations in detail",
            "Determine which AI systems are high-risk vs limited-risk",
            "Create compliance timeline based on deadlines",
            "Assign responsibility for each obligation",
            "Consider consulting legal counsel for complex cases"
        ]
    }


# ============================================================================
# SONNYLABS AI SECURITY INTEGRATION - EU AI Act Article 15
# ============================================================================

@mcp.tool()
def scan_for_prompt_injection(
    user_input: str,
    sonnylabs_api_token: str,
    sonnylabs_analysis_id: str,
    tag: str = "mcp_scan"
) -> Dict[str, Any]:
    """
    Scans user input for prompt injection attacks using SonnyLabs.ai API.
    
    Helps comply with EU AI Act Article 15 cybersecurity requirements.
    Detects attempts to manipulate AI behavior through prompt injection.
    
    Args:
        user_input: The user input text to scan for threats
        sonnylabs_api_token: Your SonnyLabs API token (Bearer token)
        sonnylabs_analysis_id: Your SonnyLabs analysis ID
        tag: Optional identifier for this scan (default: "mcp_scan")
        
    Returns:
        Dictionary with threat analysis and EU AI Act compliance info
    """
    import requests
    
    try:
        # Call SonnyLabs API
        url = f"https://sonnylabs-service.onrender.com/v1/analysis/{sonnylabs_analysis_id}"
        
        response = requests.post(
            url,
            params={
                "tag": tag,
                "scan_type": "input",
                "detections": "prompt_injection,long_prompt_injection"
            },
            headers={
                "Authorization": f"Bearer {sonnylabs_api_token}",
                "Content-Type": "text/plain"
            },
            data=user_input.encode('utf-8'),
            timeout=10
        )
        
        response.raise_for_status()
        result = response.json()
        
        # Extract prompt injection scores
        prompt_injection_score = 0.0
        long_injection_score = 0.0
        attack_type = "none"
        
        for item in result.get("analysis", []):
            if item.get("name") == "prompt_injection" and item.get("type") == "score":
                prompt_injection_score = item.get("result", 0.0)
            elif item.get("name") == "long_prompt_injection" and item.get("type") == "score":
                long_injection_score = item.get("result", 0.0)
        
        # Determine attack severity
        max_score = max(prompt_injection_score, long_injection_score)
        is_attack = max_score > 0.7
        
        if max_score > 0.9:
            risk_level = "CRITICAL"
            recommendation = "BLOCK immediately - high confidence attack"
        elif max_score > 0.7:
            risk_level = "HIGH"
            recommendation = "BLOCK this input - likely attack"
        elif max_score > 0.5:
            risk_level = "MEDIUM"
            recommendation = "WARN user - suspicious input"
        else:
            risk_level = "LOW"
            recommendation = "ALLOW - input appears safe"
        
        if is_attack:
            attack_type = "instruction_override" if prompt_injection_score > long_injection_score else "long_form_injection"
        
        return {
            "is_prompt_injection": is_attack,
            "confidence": round(max_score, 3),
            "attack_type": attack_type,
            "risk_level": risk_level,
            "recommendation": recommendation,
            "scores": {
                "basic_injection": round(prompt_injection_score, 3),
                "long_form_injection": round(long_injection_score, 3)
            },
            "eu_ai_act_relevance": "Article 15 - Cybersecurity and robustness requirements",
            "article_15_compliance": "Detecting and preventing manipulation attempts meets Article 15(1) requirements",
            "sonnylabs_analysis": {
                "detection_method": "Multi-model ensemble (pattern matching + LLM classifier)",
                "api_endpoint": url,
                "tag": tag
            },
            "next_steps": [
                "Block input if risk level is HIGH or CRITICAL",
                "Log incident for security audit",
                "Consider implementing rate limiting",
                "Review similar patterns in historical data"
            ] if is_attack else [
                "Process input normally",
                "Continue monitoring for anomalies"
            ]
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "error": "SonnyLabs API request failed",
            "details": str(e),
            "is_prompt_injection": None,
            "recommendation": "Unable to verify - proceed with caution or use fallback detection",
            "eu_ai_act_relevance": "Article 15 - Unable to verify cybersecurity compliance",
            "fallback_suggestion": "Implement basic keyword filtering as temporary measure"
        }
    except Exception as e:
        return {
            "error": "Unexpected error during analysis",
            "details": str(e),
            "is_prompt_injection": None,
            "recommendation": "System error - review logs and retry"
        }


@mcp.tool()
def check_sensitive_file_access(
    file_path: str,
    agent_action: str,
    sonnylabs_api_token: str,
    sonnylabs_analysis_id: str,
    tag: str = "file_access_check"
) -> Dict[str, Any]:
    """
    Checks if AI agent is attempting to access sensitive files using SonnyLabs.ai API.
    
    Helps comply with EU AI Act Article 15 (Security) and Article 10 (Data governance).
    Prevents unauthorized access to confidential files and system resources.
    
    Args:
        file_path: The file path being accessed by the AI agent
        agent_action: The action being performed (e.g., "read", "write", "execute")
        sonnylabs_api_token: Your SonnyLabs API token (Bearer token)
        sonnylabs_analysis_id: Your SonnyLabs analysis ID
        tag: Optional identifier for this check (default: "file_access_check")
        
    Returns:
        Dictionary with file sensitivity analysis and access recommendations
    """
    import requests
    
    try:
        # Create analysis text
        analysis_text = f"Agent attempting to {agent_action} file: {file_path}"
        
        # Call SonnyLabs API
        url = f"https://sonnylabs-service.onrender.com/v1/analysis/{sonnylabs_analysis_id}"
        
        response = requests.post(
            url,
            params={
                "tag": tag,
                "scan_type": "input",
                "detections": "sensitive_path_detection"
            },
            headers={
                "Authorization": f"Bearer {sonnylabs_api_token}",
                "Content-Type": "text/plain"
            },
            data=analysis_text.encode('utf-8'),
            timeout=10
        )
        
        response.raise_for_status()
        result = response.json()
        
        # Extract sensitive path detections
        sensitive_paths = []
        is_sensitive = False
        sensitivity_level = "LOW"
        detected_data_types = []
        
        for item in result.get("analysis", []):
            if item.get("type") == "sensitive_path_detection":
                paths = item.get("result", [])
                for path_info in paths:
                    sensitive_paths.append(path_info)
                    is_sensitive = True
                    
                    # Determine sensitivity level
                    confidence = path_info.get("confidence", 0)
                    category = path_info.get("category", "unknown")
                    
                    if confidence > 0.9 or category in ["system_file", "credential_file"]:
                        sensitivity_level = "HIGHLY_CONFIDENTIAL"
                    elif confidence > 0.7 or category in ["config_file", "database"]:
                        sensitivity_level = "CONFIDENTIAL"
                    elif sensitivity_level not in ["HIGHLY_CONFIDENTIAL", "CONFIDENTIAL"]:
                        sensitivity_level = "SENSITIVE"
                    
                    # Track data types
                    if category not in detected_data_types:
                        detected_data_types.append(category)
        
        # Determine recommendation
        if is_sensitive and sensitivity_level == "HIGHLY_CONFIDENTIAL":
            recommendation = "DENY access immediately - highly sensitive file"
            action = "BLOCK"
        elif is_sensitive:
            recommendation = "REQUIRE explicit authorization before allowing access"
            action = "REQUIRE_AUTH"
        else:
            recommendation = "ALLOW access - file does not appear sensitive"
            action = "ALLOW"
        
        return {
            "is_sensitive": is_sensitive,
            "sensitivity_level": sensitivity_level,
            "detected_paths": sensitive_paths,
            "detected_data_types": detected_data_types,
            "file_path": file_path,
            "agent_action": agent_action,
            "recommendation": recommendation,
            "action": action,
            "eu_ai_act_relevance": "Article 10 - Data governance requirements & Article 15 - Security measures",
            "article_10_compliance": "AI systems must only access data necessary for their intended purpose",
            "article_15_compliance": "AI systems must implement security measures to prevent unauthorized access",
            "access_control_recommendation": "Implement role-based access control (RBAC) with principle of least privilege",
            "sonnylabs_analysis": {
                "detection_method": "Pattern matching + File path analysis",
                "api_endpoint": url,
                "tag": tag
            },
            "security_measures": [
                "Implement file access logging",
                "Require authentication for sensitive directories",
                "Use allowlist for permitted file paths",
                "Monitor and alert on suspicious access patterns",
                "Regularly audit AI agent file access permissions"
            ],
            "compliance_actions": [
                "Document access attempt in audit log",
                "Verify AI agent has legitimate need for file access",
                "Implement technical safeguards (encryption, access controls)",
                "Conduct regular security reviews of AI agent permissions"
            ] if is_sensitive else [
                "Log access for audit trail",
                "Continue monitoring access patterns"
            ]
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "error": "SonnyLabs API request failed",
            "details": str(e),
            "is_sensitive": None,
            "recommendation": "Unable to verify - deny access by default for security",
            "action": "DENY_SAFE",
            "eu_ai_act_relevance": "Article 15 - Unable to verify security compliance"
        }
    except Exception as e:
        return {
            "error": "Unexpected error during file access check",
            "details": str(e),
            "is_sensitive": None,
            "recommendation": "System error - deny access and review logs"
        }