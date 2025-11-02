#!/usr/bin/env python3
"""
Test script for label_video_deepfake tool
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import label_video_deepfake

def test_standard_video():
    """Test standard video label"""
    print("=" * 60)
    print("Test 1: Standard AI-generated video")
    print("=" * 60)
    
    result = label_video_deepfake(
        video_description="AI-generated video of a person speaking",
        is_artistic_work=False,
        language="en"
    )
    
    print(f"\n✓ Article: {result['article']}")
    print(f"✓ Obligation: {result['obligation']}")
    print(f"✓ Label: '{result['label_text']}'")
    print(f"✓ Recommended placement: {result['recommended_placement']}")
    print(f"✓ Exemption applies: {result['exemption_applies']}")
    
    assert result['article'] == "50(4)"
    assert "video" in result['label_text'].lower()
    print(f"\n✅ Test PASSED!")
    return True

def test_artistic_video():
    """Test artistic video label"""
    print(f"\n{'=' * 60}")
    print("Test 2: Artistic video (German)")
    print("=" * 60)
    
    result = label_video_deepfake(
        video_description="AI art film",
        is_artistic_work=True,
        language="de"
    )
    
    print(f"\n✓ Language: {result['language']}")
    print(f"✓ Label: '{result['label_text']}'")
    print(f"✓ Exemption: {result['exemption_applies']}")
    
    assert result['exemption_applies'] == True
    print(f"\n✅ Test PASSED!")
    return True

def main():
    print("\n" + "=" * 60)
    print("LABEL_VIDEO_DEEPFAKE - TEST SUITE")
    print("=" * 60)
    
    try:
        test_standard_video()
        test_artistic_video()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        return True
    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
