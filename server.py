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
    rules_path = os.path.join(os.path.dirname(__file__), "article50_rules.json")
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
    config_path = os.path.join(os.path.dirname(__file__), "watermark_config.json")
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
    labels_path = os.path.join(os.path.dirname(__file__), "deepfake_labels.json")
    
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
    labels_path = os.path.join(os.path.dirname(__file__), "deepfake_labels.json")
    
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
    labels_path = os.path.join(os.path.dirname(__file__), "deepfake_labels.json")
    
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