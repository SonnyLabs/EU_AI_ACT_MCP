#!/usr/bin/env python3
"""
Test script for label_audio_deepfake tool
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import label_audio_deepfake

def test_standard_audio():
    """Test standard audio label"""
    print("=" * 60)
    print("Test 1: Standard AI-generated audio")
    print("=" * 60)
    
    result = label_audio_deepfake(
        audio_description="AI-generated voice message",
        is_artistic_work=False,
        language="en"
    )
    
    print(f"\n✓ Article: {result['article']}")
    print(f"✓ Obligation: {result['obligation']}")
    print(f"✓ Written label: '{result['written_label']}'")
    print(f"✓ Spoken label: '{result['spoken_label']}'")
    print(f"✓ Recommended method: {result['recommended_method']}")
    
    assert result['article'] == "50(4)"
    assert "audio" in result['written_label'].lower()
    print(f"\n✅ Test PASSED!")
    return True

def test_multilingual():
    """Test multilingual audio labels"""
    print(f"\n{'=' * 60}")
    print("Test 2: Multilingual labels")
    print("=" * 60)
    
    for lang in ["en", "es", "fr", "de"]:
        result = label_audio_deepfake(
            audio_description="Test audio",
            language=lang
        )
        print(f"\n✓ {lang.upper()}: {result['written_label']}")
    
    print(f"\n✅ Test PASSED!")
    return True

def main():
    print("\n" + "=" * 60)
    print("LABEL_AUDIO_DEEPFAKE - TEST SUITE")
    print("=" * 60)
    
    try:
        test_standard_audio()
        test_multilingual()
        
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
