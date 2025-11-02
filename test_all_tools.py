#!/usr/bin/env python3
"""
Comprehensive test for ALL EU AI Act Article 50 compliance tools
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import (
    get_ai_interaction_disclosure,
    get_emotion_recognition_disclosure,
    get_deepfake_label_templates,
    label_news_text,
    watermark_text,
    label_image_deepfake,
    label_video_deepfake,
    label_audio_deepfake,
    watermark_image,
    watermark_video,
    watermark_audio
)

def test_all_tools():
    """Test all 10 tools"""
    print("=" * 70)
    print("EU AI ACT ARTICLE 50 COMPLIANCE - COMPLETE TOOL TEST")
    print("=" * 70)
    
    tools_tested = []
    
    # Test 1: AI Interaction Disclosure (50(1))
    print("\n1. Testing get_ai_interaction_disclosure...")
    result = get_ai_interaction_disclosure(language="en", style="simple")
    assert result['article'] == "50(1)"
    tools_tested.append("✓ get_ai_interaction_disclosure")
    
    # Test 2: Emotion Recognition Disclosure (50(3))
    print("2. Testing get_emotion_recognition_disclosure...")
    result = get_emotion_recognition_disclosure(language="en")
    assert result['article'] == "50(3)"
    tools_tested.append("✓ get_emotion_recognition_disclosure")
    
    # Test 3: Deepfake Label Templates
    print("3. Testing get_deepfake_label_templates...")
    result = get_deepfake_label_templates(language="en")
    assert 'content_types' in result
    tools_tested.append("✓ get_deepfake_label_templates")
    
    # Test 4: Label News Text (50(4))
    print("4. Testing label_news_text...")
    result = label_news_text(
        text_content="Test article",
        has_human_editor=True,
        editor_name="John Doe"
    )
    assert result['article'] == "50(4)"
    tools_tested.append("✓ label_news_text")
    
    # Test 5: Watermark Text (50(2))
    print("5. Testing watermark_text...")
    result = watermark_text(
        text_content="Test content",
        generator="GPT-4"
    )
    assert result['article'] == "50(2)"
    tools_tested.append("✓ watermark_text")
    
    # Test 6: Label Image Deepfake (50(4))
    print("6. Testing label_image_deepfake...")
    result = label_image_deepfake(
        image_description="Test image",
        is_artistic_work=False
    )
    assert result['article'] == "50(4)"
    tools_tested.append("✓ label_image_deepfake")
    
    # Test 7: Label Video Deepfake (50(4))
    print("7. Testing label_video_deepfake...")
    result = label_video_deepfake(
        video_description="Test video",
        is_artistic_work=False
    )
    assert result['article'] == "50(4)"
    tools_tested.append("✓ label_video_deepfake")
    
    # Test 8: Label Audio Deepfake (50(4))
    print("8. Testing label_audio_deepfake...")
    result = label_audio_deepfake(
        audio_description="Test audio",
        is_artistic_work=False
    )
    assert result['article'] == "50(4)"
    tools_tested.append("✓ label_audio_deepfake")
    
    # Test 9: Watermark Image (50(2))
    print("9. Testing watermark_image...")
    result = watermark_image(
        image_description="Test image",
        generator="DALL-E"
    )
    assert result['article'] == "50(2)"
    tools_tested.append("✓ watermark_image")
    
    # Test 10: Watermark Video (50(2))
    print("10. Testing watermark_video...")
    result = watermark_video(
        video_description="Test video",
        generator="AI"
    )
    assert result['article'] == "50(2)"
    tools_tested.append("✓ watermark_video")
    
    # Test 11: Watermark Audio (50(2))
    print("11. Testing watermark_audio...")
    result = watermark_audio(
        audio_description="Test audio",
        generator="AI"
    )
    assert result['article'] == "50(2)"
    tools_tested.append("✓ watermark_audio")
    
    # Summary
    print("\n" + "=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)
    print(f"\nAll {len(tools_tested)} tools tested successfully:\n")
    for tool in tools_tested:
        print(f"  {tool}")
    
    print("\n" + "=" * 70)
    print("Article 50 Coverage:")
    print("=" * 70)
    print("  ✓ 50(1) - AI Interaction Disclosure")
    print("  ✓ 50(2) - Content Watermarking (text, image, video, audio)")
    print("  ✓ 50(3) - Emotion Recognition Disclosure")
    print("  ✓ 50(4) - Deepfake Labeling (text, image, video, audio)")
    
    print("\n" + "=" * 70)
    print("✅ ALL TOOLS WORKING! MCP SERVER IS COMPLETE!")
    print("=" * 70)
    
    return True

if __name__ == "__main__":
    try:
        success = test_all_tools()
        exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
