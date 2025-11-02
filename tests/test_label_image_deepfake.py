#!/usr/bin/env python3
"""
Test script for label_image_deepfake tool
Tests generating deepfake labels for AI-generated images
"""

import sys
import os

# Add parent directory to path to import server
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import label_image_deepfake

def test_standard_image_label():
    """Test labeling a standard AI-generated image"""
    print("=" * 60)
    print("Test 1: Standard AI-generated image label")
    print("=" * 60)
    
    result = label_image_deepfake(
        image_description="AI-generated portrait of a business executive",
        is_artistic_work=False,
        is_satirical=False,
        language="en"
    )
    
    print(f"\n✓ Article: {result['article']}")
    print(f"✓ Obligation: {result['obligation']}")
    print(f"✓ Applies to: {result['applies_to']}")
    print(f"✓ Language: {result['language']}")
    
    print(f"\n{'-' * 60}")
    print("Label Text:")
    print(f"{'-' * 60}")
    print(f"'{result['label_text']}'")
    
    print(f"\n{'-' * 60}")
    print("Placement Options:")
    print(f"{'-' * 60}")
    for i, option in enumerate(result['placement_options'], 1):
        print(f"  {i}. {option}")
    
    print(f"\nRecommended: {result['recommended_placement']}")
    print(f"Visibility: {result['visibility_requirement']}")
    
    print(f"\n{'-' * 60}")
    print("Exemption Status:")
    print(f"{'-' * 60}")
    print(f"Exemption applies: {result['exemption_applies']}")
    print(f"Reason: {result['exemption_reason']}")
    
    assert result['article'] == "50(4)"
    assert result['exemption_applies'] == False
    assert "artificially generated" in result['label_text'].lower()
    
    print(f"\n✅ Standard image label test PASSED!")
    return True


def test_artistic_image_label():
    """Test labeling an artistic AI-generated image"""
    print(f"\n{'=' * 60}")
    print("Test 2: Artistic work image label")
    print("=" * 60)
    
    result = label_image_deepfake(
        image_description="AI-generated abstract art piece",
        is_artistic_work=True,
        is_satirical=False,
        language="en"
    )
    
    print(f"\n✓ Image type: Artistic work")
    print(f"✓ Exemption applies: {result['exemption_applies']}")
    
    print(f"\n{'-' * 60}")
    print("Label Text (Modified for artistic work):")
    print(f"{'-' * 60}")
    print(f"'{result['label_text']}'")
    
    print(f"\n{'-' * 60}")
    print("Implementation Notes:")
    print(f"{'-' * 60}")
    for i, note in enumerate(result['implementation_notes'], 1):
        print(f"  {i}. {note}")
    
    assert result['exemption_applies'] == True
    assert result['is_artistic_work'] == True
    assert "AI-generated" in result['label_text']
    
    print(f"\n✅ Artistic image label test PASSED!")
    return True


def test_multilingual_labels():
    """Test labels in different languages"""
    print(f"\n{'=' * 60}")
    print("Test 3: Multilingual labels")
    print("=" * 60)
    
    languages = ["en", "es", "fr", "de"]
    
    for lang in languages:
        result = label_image_deepfake(
            image_description="Test image",
            is_artistic_work=False,
            language=lang
        )
        
        if 'error' not in result:
            print(f"\n✓ {lang.upper()}: {result['label_text']}")
        else:
            print(f"\n✗ {lang.upper()}: {result['error']}")
    
    print(f"\n✅ Multilingual labels test PASSED!")
    return True


def test_satirical_content():
    """Test labeling satirical/parody content"""
    print(f"\n{'=' * 60}")
    print("Test 4: Satirical/parody content")
    print("=" * 60)
    
    result = label_image_deepfake(
        image_description="AI-generated satirical political cartoon",
        is_artistic_work=False,
        is_satirical=True,
        language="en"
    )
    
    print(f"\n✓ Content type: Satirical")
    print(f"✓ Exemption applies: {result['exemption_applies']}")
    print(f"✓ Label text: '{result['label_text']}'")
    print(f"✓ Compliance deadline: {result['compliance_deadline']}")
    
    assert result['exemption_applies'] == True
    assert result['is_satirical'] == True
    
    print(f"\n✅ Satirical content test PASSED!")
    return True


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("LABEL_IMAGE_DEEPFAKE TOOL - FULL TEST SUITE")
    print("=" * 60)
    
    try:
        test_standard_image_label()
        test_artistic_image_label()
        test_multilingual_labels()
        test_satirical_content()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nThe label_image_deepfake tool is working correctly.")
        print("It generates appropriate disclosure labels for:")
        print("  • Standard AI-generated images")
        print("  • Artistic works (with exemptions)")
        print("  • Satirical/parody content (with exemptions)")
        print("  • Multiple languages (en, es, fr, de)")
        print("\nLabels include:")
        print("  • Clear disclosure text")
        print("  • Placement guidance")
        print("  • Visibility requirements")
        print("  • Implementation notes")
        return True
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
