#!/usr/bin/env python3
"""
Test script for watermark_image, watermark_video, watermark_audio tools
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import watermark_image, watermark_video, watermark_audio

def test_watermark_image():
    """Test image watermarking"""
    print("=" * 60)
    print("Test 1: Watermark Image")
    print("=" * 60)
    
    result = watermark_image(
        image_description="AI-generated portrait",
        generator="DALL-E",
        format_type="png"
    )
    
    print(f"\n✓ Article: {result['article']}")
    print(f"✓ Obligation: {result['obligation']}")
    print(f"✓ Watermark standard: {result['watermark_standard']}")
    print(f"✓ Machine readable: {result['machine_readable']}")
    print(f"✓ Generator: {result['generator']}")
    
    assert result['article'] == "50(2)"
    assert 'c2pa_metadata' in result
    assert 'iptc_metadata' in result
    print(f"\n✅ Image watermark test PASSED!")
    return True

def test_watermark_video():
    """Test video watermarking"""
    print(f"\n{'=' * 60}")
    print("Test 2: Watermark Video")
    print("=" * 60)
    
    result = watermark_video(
        video_description="AI-generated animation",
        generator="Runway",
        format_type="mp4"
    )
    
    print(f"\n✓ Article: {result['article']}")
    print(f"✓ Watermark method: {result['watermark_method']}")
    print(f"✓ Format: {result['format']}")
    print(f"✓ Verification URL: {result['verification_url']}")
    
    assert result['article'] == "50(2)"
    assert 'c2pa_metadata' in result
    assert result['watermark_method'] == "Frame-level embedding"
    print(f"\n✅ Video watermark test PASSED!")
    return True

def test_watermark_audio():
    """Test audio watermarking"""
    print(f"\n{'=' * 60}")
    print("Test 3: Watermark Audio")
    print("=" * 60)
    
    result = watermark_audio(
        audio_description="AI-generated voice",
        generator="ElevenLabs",
        format_type="mp3"
    )
    
    print(f"\n✓ Article: {result['article']}")
    print(f"✓ Watermark method: {result['watermark_method']}")
    print(f"✓ Inaudible: {result['inaudible']}")
    print(f"✓ Format: {result['format']}")
    
    assert result['article'] == "50(2)"
    assert 'c2pa_metadata' in result
    assert 'audio_metadata' in result
    assert result['inaudible'] == True
    print(f"\n✅ Audio watermark test PASSED!")
    return True

def main():
    print("\n" + "=" * 60)
    print("WATERMARK MEDIA TOOLS - TEST SUITE")
    print("=" * 60)
    
    try:
        test_watermark_image()
        test_watermark_video()
        test_watermark_audio()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nAll watermark tools are working correctly.")
        print("They provide C2PA-compliant metadata for:")
        print("  • Images (with IPTC fallback)")
        print("  • Videos (frame-level embedding)")
        print("  • Audio (spectral + ID3 tags)")
        return True
    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
