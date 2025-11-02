#!/usr/bin/env python3
"""
Test script for the get_deepfake_label_templates tool
"""

from server import get_deepfake_label_templates
import json


def test_english_labels():
    """Test getting English labels"""
    print("=" * 70)
    print("🏷️  Test 1: Get English deepfake labels")
    print("=" * 70)
    
    result = get_deepfake_label_templates(language="en")
    
    print(f"\n✓ Language: {result['language']}")
    print(f"✓ Article: {result['article']}")
    print(f"✓ Purpose: {result['purpose']}")
    print(f"\n📋 Available Content Types:")
    
    for content_type, labels in result['content_types'].items():
        print(f"\n  {content_type.upper()}:")
        print(json.dumps(labels, indent=4))
    print()


def test_spanish_labels():
    """Test getting Spanish labels"""
    print("=" * 70)
    print("🏷️  Test 2: Get Spanish deepfake labels")
    print("=" * 70)
    
    result = get_deepfake_label_templates(language="es")
    
    print(f"\n✓ Language: {result['language']}")
    print(f"\n📋 Text Labels:")
    print(json.dumps(result['content_types']['text'], indent=4))
    print()


if __name__ == "__main__":
    print("\n🚀 Testing get_deepfake_label_templates Tool\n")
    
    test_english_labels()
    test_spanish_labels()
    
    print("=" * 70)
    print("✅ All tests completed!")
    print("=" * 70)
    print("\nThis tool provides access to all deepfake label templates.")
    print("Use it to see what labels are available for different content types.")
