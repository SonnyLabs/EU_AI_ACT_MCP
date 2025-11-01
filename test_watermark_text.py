#!/usr/bin/env python3
"""
Test script for watermark_text tool
Tests adding metadata watermarks to AI-generated text
"""

import sys
import os

# Add parent directory to path to import server
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import watermark_text

def test_watermark_text_plain():
    """Test watermarking text in plain format"""
    print("=" * 60)
    print("Test 1: Watermark text (plain format)")
    print("=" * 60)
    
    original_text = "The quick brown fox jumps over the lazy dog. This is AI-generated content for testing purposes."
    
    result = watermark_text(
        text_content=original_text,
        generator="GPT-4",
        format_type="plain"
    )
    
    print(f"\n✓ Article: {result['article']}")
    print(f"✓ Obligation: {result['obligation']}")
    print(f"✓ Original length: {result['original_length']} chars")
    print(f"✓ Watermarked length: {result['watermarked_length']} chars")
    print(f"✓ Format: {result['format']}")
    print(f"✓ Machine readable: {result['machine_readable']}")
    
    print(f"\n{'-' * 60}")
    print("Metadata:")
    print(f"{'-' * 60}")
    for key, value in result['metadata'].items():
        print(f"  {key}: {value}")
    
    print(f"\n{'-' * 60}")
    print("Watermarked Text Preview (first 200 chars):")
    print(f"{'-' * 60}")
    print(result['watermarked_text'][:200])
    
    # Verify metadata is in the text
    assert '[AI-WATERMARK:' in result['watermarked_text']
    assert original_text in result['watermarked_text']
    print(f"\n✅ Plain format test PASSED!")
    
    return True


def test_watermark_text_markdown():
    """Test watermarking text in markdown format"""
    print(f"\n{'=' * 60}")
    print("Test 2: Watermark text (markdown format)")
    print("=" * 60)
    
    original_text = "# AI Generated Article\n\nThis is an AI-generated article about technology."
    
    result = watermark_text(
        text_content=original_text,
        generator="Claude",
        format_type="markdown"
    )
    
    print(f"\n✓ Format: {result['format']}")
    print(f"✓ Generator: {result['metadata']['generator']}")
    
    print(f"\n{'-' * 60}")
    print("Watermarked Text:")
    print(f"{'-' * 60}")
    print(result['watermarked_text'])
    
    # Verify markdown comment is in the text
    assert '<!-- AI Watermark:' in result['watermarked_text']
    assert original_text in result['watermarked_text']
    print(f"\n✅ Markdown format test PASSED!")
    
    return True


def test_watermark_text_html():
    """Test watermarking text in HTML format"""
    print(f"\n{'=' * 60}")
    print("Test 3: Watermark text (HTML format)")
    print("=" * 60)
    
    original_text = "<p>This is an AI-generated HTML paragraph.</p>"
    
    result = watermark_text(
        text_content=original_text,
        generator="Custom AI",
        format_type="html"
    )
    
    print(f"\n✓ Format: {result['format']}")
    print(f"✓ Compliance: {result['metadata']['compliance']}")
    print(f"✓ Content hash: {result['verification']}")
    
    print(f"\n{'-' * 60}")
    print("Watermarked Text:")
    print(f"{'-' * 60}")
    print(result['watermarked_text'])
    
    # Verify HTML comment is in the text
    assert '<!-- AI-Generated Content Metadata' in result['watermarked_text']
    assert original_text in result['watermarked_text']
    print(f"\n✅ HTML format test PASSED!")
    
    return True


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("WATERMARK_TEXT TOOL - FULL TEST SUITE")
    print("=" * 60)
    
    try:
        test_watermark_text_plain()
        test_watermark_text_markdown()
        test_watermark_text_html()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nThe watermark_text tool is working correctly.")
        print("It adds machine-readable metadata to AI-generated text")
        print("in plain, markdown, and HTML formats.")
        return True
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
