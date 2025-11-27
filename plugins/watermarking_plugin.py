"""
Watermarking Plugin - Article 50(2) Content Watermarking

Provides consolidated watermarking tools for all content types.
"""

import os
import json
import hashlib
from datetime import datetime, timezone
from typing import Dict, Any
from .base import BasePlugin


class WatermarkingPlugin(BasePlugin):
    """
    Plugin for EU AI Act Article 50(2) content watermarking.
    
    Consolidates:
    - watermark_text
    - watermark_image
    - watermark_video
    - watermark_audio
    
    Into a single tool: watermark_content
    """
    
    def get_name(self) -> str:
        return "WatermarkingPlugin"
    
    def get_description(self) -> str:
        return "Provides EU AI Act Article 50(2) watermarking for AI-generated content"
    
    def get_tools(self) -> Dict[str, Any]:
        return {
            "watermark_content": self.watermark_content
        }
    
    def get_resources(self) -> Dict[str, Any]:
        return {
            "watermark-config://technical-standards": self.get_watermark_config_resource
        }
    
    def get_watermark_config_resource(self) -> str:
        """Resource: Watermarking technical standards"""
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "resources", 
            "watermark_config.json"
        )
        with open(config_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def watermark_content(
        self,
        content_type: str,
        content_description: str,
        generator: str = "AI",
        format_type: str = None,
        text_content: str = None
    ) -> Dict[str, Any]:
        """
        Add watermark metadata to AI-generated content for EU AI Act Article 50(2) compliance.
        
        This consolidated tool handles watermarking for all content types:
        text, image, video, and audio.
        
        Args:
            content_type: Type of content - "text", "image", "video", or "audio"
            content_description: Brief description of the content
            generator: Name of AI system that generated it (e.g., "GPT-4", "DALL-E")
            format_type: Output format (optional, defaults based on content_type)
                - text: "plain", "markdown", "html"
                - image: "png", "jpg", "webp"
                - video: "mp4", "webm", "mov"
                - audio: "mp3", "wav", "opus"
            text_content: The actual text content (required only for content_type="text")
        
        Returns:
            Dictionary containing watermarking metadata and instructions
        
        Example:
            watermark_content(content_type="image", content_description="AI landscape", generator="DALL-E")
            watermark_content(content_type="text", text_content="Article text...", generator="GPT-4")
        """
        # Validate content type
        valid_types = ["text", "image", "video", "audio"]
        if content_type not in valid_types:
            return {
                "error": f"Invalid content_type '{content_type}'",
                "valid_types": valid_types
            }
        
        # Set default format_type based on content_type
        if format_type is None:
            defaults = {
                "text": "plain",
                "image": "png",
                "video": "mp4",
                "audio": "mp3"
            }
            format_type = defaults[content_type]
        
        # Route to appropriate handler
        if content_type == "text":
            return self._watermark_text(text_content, generator, format_type, content_description)
        elif content_type == "image":
            return self._watermark_image(content_description, generator, format_type)
        elif content_type == "video":
            return self._watermark_video(content_description, generator, format_type)
        else:  # audio
            return self._watermark_audio(content_description, generator, format_type)
    
    def _watermark_text(
        self, 
        text_content: str, 
        generator: str, 
        format_type: str,
        content_description: str
    ) -> Dict[str, Any]:
        """Watermark text content"""
        if text_content is None:
            return {
                "error": "text_content is required for content_type='text'",
                "usage": "Provide the actual text to be watermarked"
            }
        
        # Generate content hash
        content_hash = hashlib.sha256(text_content.encode('utf-8')).hexdigest()[:16]
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
        
        # Format the watermarked text
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
            "content_type": "text",
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
    
    def _watermark_image(
        self, 
        image_description: str, 
        generator: str, 
        format_type: str
    ) -> Dict[str, Any]:
        """Generate watermarking metadata for images"""
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
            "content_type": "image",
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
    
    def _watermark_video(
        self, 
        video_description: str, 
        generator: str, 
        format_type: str
    ) -> Dict[str, Any]:
        """Generate watermarking metadata for videos"""
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
            "content_type": "video",
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
    
    def _watermark_audio(
        self, 
        audio_description: str, 
        generator: str, 
        format_type: str
    ) -> Dict[str, Any]:
        """Generate watermarking metadata for audio"""
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
            "content_type": "audio",
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
