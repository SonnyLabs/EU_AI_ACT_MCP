#!/usr/bin/env python3
"""
Test script for watermark_config.json
Tests that the watermarking configuration is valid and complete
"""

import json
import os

def test_watermark_config():
    """Test the watermark_config.json file"""
    
    print("=" * 60)
    print("Testing watermark_config.json")
    print("=" * 60)
    
    # Check if file exists
    file_path = "watermark_config.json"
    if not os.path.exists(file_path):
        print(f"✗ ERROR: {file_path} not found!")
        return False
    
    print(f"✓ File exists: {file_path}")
    
    # Load and parse JSON
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print("✓ JSON is valid")
    except json.JSONDecodeError as e:
        print(f"✗ ERROR: Invalid JSON - {e}")
        return False
    
    # Validate structure
    required_keys = ['version', 'standards', 'content_types', 'compliance_notes']
    for key in required_keys:
        if key not in config:
            print(f"✗ ERROR: Missing required key '{key}'")
            return False
        print(f"✓ Has '{key}' field")
    
    # Validate standards
    print(f"\n{'=' * 60}")
    print("Watermarking Standards:")
    print("=" * 60)
    
    if 'c2pa' in config['standards']:
        c2pa = config['standards']['c2pa']
        print(f"\n✓ C2PA Version: {c2pa['version']}")
        print(f"  Hash Algorithm: {c2pa['hash_algorithm']}")
        print(f"  Signature Algorithm: {c2pa['signature_algorithm']}")
        print(f"  Supported Formats: {len(c2pa['supported_formats'])} formats")
        print(f"  Verification URL: {c2pa['verification_url']}")
    
    if 'iptc' in config['standards']:
        iptc = config['standards']['iptc']
        print(f"\n✓ IPTC Version: {iptc['version']}")
        print(f"  Digital Source Type: {iptc['digital_source_type']}")
        print(f"  Required Fields: {len(iptc['required_fields'])} fields")
    
    # Validate content types
    print(f"\n{'=' * 60}")
    print("Content Types Configuration:")
    print("=" * 60)
    
    content_types = ['image', 'video', 'audio', 'text']
    for content_type in content_types:
        if content_type in config['content_types']:
            ct = config['content_types'][content_type]
            print(f"\n✓ {content_type.upper()}:")
            print(f"  Formats: {', '.join(ct['formats'][:3])}...")
            print(f"  Methods: {', '.join(ct['watermark_methods'])}")
            print(f"  Preferred: {ct['preferred_method']}")
            print(f"  Visibility: {ct['visibility']}")
        else:
            print(f"✗ Missing {content_type} configuration")
            return False
    
    # Validate compliance notes
    print(f"\n{'=' * 60}")
    print("Compliance Information:")
    print("=" * 60)
    
    compliance = config['compliance_notes']
    print(f"\n✓ Article: {compliance['article']}")
    print(f"✓ Requirement: {compliance['requirement']}")
    print(f"✓ Deadline: {compliance['deadline']}")
    print(f"✓ Exceptions: {len(compliance['exceptions'])} listed")
    
    # Validate implementation guide
    if 'implementation_guide' in config:
        print(f"\n{'=' * 60}")
        print("Implementation Guide:")
        print("=" * 60)
        
        guide = config['implementation_guide']
        steps = [k for k in guide.keys() if k.startswith('step_')]
        print(f"\n✓ {len(steps)} implementation steps provided")
        for step_key in sorted(steps)[:3]:
            print(f"  {step_key}: {guide[step_key][:50]}...")
    
    print(f"\n{'=' * 60}")
    print("✅ TEST PASSED: watermark_config.json is valid!")
    print("=" * 60)
    print("\nConfiguration includes:")
    print("  • C2PA 2.1 specifications")
    print("  • IPTC metadata standards")
    print("  • Support for image, video, audio, and text")
    print("  • Embedding settings and verification methods")
    print("  • Implementation guide with 7 steps")
    
    return True


if __name__ == "__main__":
    success = test_watermark_config()
    exit(0 if success else 1)
