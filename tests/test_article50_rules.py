#!/usr/bin/env python3
"""
Test script for article50_rules.json
Tests that the JSON file is valid and contains expected data
"""

import json
import os

def test_article50_rules():
    """Test the article50_rules.json file"""
    
    print("=" * 60)
    print("Testing article50_rules.json")
    print("=" * 60)
    
    # Check if file exists
    file_path = os.path.join("resources", "article50_rules.json")
    if not os.path.exists(file_path):
        print(f"✗ ERROR: {file_path} not found!")
        return False
    
    print(f"✓ File exists: {file_path}")
    
    # Load and parse JSON
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            rules_data = json.load(f)
        print("✓ JSON is valid")
    except json.JSONDecodeError as e:
        print(f"✗ ERROR: Invalid JSON - {e}")
        return False
    
    # Validate structure
    required_keys = ['article', 'title', 'obligations', 'penalties', 'key_definitions']
    for key in required_keys:
        if key not in rules_data:
            print(f"✗ ERROR: Missing required key '{key}'")
            return False
        print(f"✓ Has '{key}' field")
    
    # Display summary
    print(f"\n{'=' * 60}")
    print("Content Summary:")
    print("=" * 60)
    print(f"\n✓ Article: {rules_data['article']}")
    print(f"✓ Title: {rules_data['title'][:60]}...")
    print(f"✓ Compliance deadline: {rules_data['compliance_deadline']}")
    print(f"✓ Number of obligations: {len(rules_data['obligations'])}")
    
    print(f"\n{'=' * 60}")
    print("Obligations Breakdown:")
    print("=" * 60)
    
    for i, obligation in enumerate(rules_data['obligations'], 1):
        print(f"\n{i}. {obligation['paragraph']} - {obligation['obligation_type']}")
        print(f"   Applies to: {obligation['applies_to']}")
        print(f"   Deadline: {obligation['deadline']}")
        if 'exceptions' in obligation:
            print(f"   Exceptions: {len(obligation['exceptions'])} listed")
    
    print(f"\n{'=' * 60}")
    print("Penalties:")
    print("=" * 60)
    print(f"Non-compliance: {rules_data['penalties']['non_compliance']}")
    print(f"Enforcement: {rules_data['penalties']['enforcement_authority']}")
    
    print(f"\n{'=' * 60}")
    print("✅ TEST PASSED: article50_rules.json is valid and complete!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_article50_rules()
    exit(0 if success else 1)
