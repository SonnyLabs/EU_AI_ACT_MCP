#!/usr/bin/env python3
"""
Test script for the first resource: disclosure_templates.json
"""
import json
import os

def test_disclosure_templates_resource():
    """Test that the disclosure templates resource works"""
    print("=" * 60)
    print("Testing: disclosure_templates.json Resource")
    print("=" * 60)
    
    # Directly test the resource file
    template_path = os.path.join(os.path.dirname(__file__), "disclosure_templates.json")
    
    if not os.path.exists(template_path):
        print(f"❌ File NOT found: {template_path}")
        return False
    
    print(f"✓ File found: {template_path}")
    
    # Read and parse the JSON
    with open(template_path, 'r', encoding='utf-8') as f:
        templates = json.load(f)
    
    print("\n📋 Available disclosure categories:")
    for category in templates.keys():
        print(f"  - {category}")
    
    print("\n🌍 AI Interaction Disclosures (English):")
    if "ai_interaction" in templates and "en" in templates["ai_interaction"]:
        for style, text in templates["ai_interaction"]["en"].items():
            print(f"  [{style}]: {text}")
    
    print("\n🧠 Emotion Recognition Disclosures (English):")
    if "emotion_recognition" in templates and "en" in templates["emotion_recognition"]:
        for style, text in templates["emotion_recognition"]["en"].items():
            print(f"  [{style}]: {text}")
    
    # Test that the MCP server can be imported
    print("\n🔌 Testing MCP Server Import:")
    try:
        from server import mcp, get_disclosure_templates
        print("  ✓ MCP server imported successfully")
        print(f"  ✓ Server name: {mcp.name}")
        
        # Test the resource function directly
        result = get_disclosure_templates()
        result_data = json.loads(result)
        print(f"  ✓ Resource function works - returned {len(result_data)} categories")
        
    except Exception as e:
        print(f"  ❌ MCP server import failed: {e}")
        return False
    
    print("\n✅ Resource test PASSED!")
    return True

if __name__ == "__main__":
    success = test_disclosure_templates_resource()
    exit(0 if success else 1)
