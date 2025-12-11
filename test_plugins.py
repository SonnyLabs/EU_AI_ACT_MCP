#!/usr/bin/env python3
"""
Test script for the plugin-based EU AI Act MCP Server

This script tests:
1. Plugin loading
2. Tool registration
3. Resource registration
4. Consolidated tool functionality
"""

import sys
from plugins import PluginRegistry, load_plugins


def test_plugin_loading():
    """Test that all plugins load correctly"""
    print("\n" + "="*70)
    print("TEST 1: Plugin Loading")
    print("="*70)
    
    registry = PluginRegistry()
    load_plugins(registry)
    
    plugins = registry.get_all_plugins()
    print(f"✓ Loaded {len(plugins)} plugins")
    
    for plugin in plugins:
        print(f"  - {plugin.get_name()}: {plugin.get_description()}")
    
    assert len(plugins) == 6, f"Expected 6 plugins, got {len(plugins)}"
    print("\n✓ Plugin loading test PASSED")
    return registry


def test_tool_registration(registry):
    """Test that all tools are registered"""
    print("\n" + "="*70)
    print("TEST 2: Tool Registration")
    print("="*70)
    
    tools = registry.get_all_tools()
    print(f"✓ Registered {len(tools)} tools")
    
    expected_tools = [
        "get_disclosure",
        "get_deepfake_label_templates",
        "watermark_content",
        "label_deepfake",
        "classify_ai_system_risk",
        "check_prohibited_practices",
        "determine_eu_ai_act_role",
        "scan_for_prompt_injection",
        "check_sensitive_file_access"
    ]
    
    for tool_name in expected_tools:
        if tool_name in tools:
            print(f"  ✓ {tool_name}")
        else:
            print(f"  ✗ {tool_name} NOT FOUND")
            sys.exit(1)
    
    print(f"\n✓ Tool registration test PASSED ({len(tools)} tools)")
    return tools


def test_resource_registration(registry):
    """Test that all resources are registered"""
    print("\n" + "="*70)
    print("TEST 3: Resource Registration")
    print("="*70)
    
    resources = registry.get_all_resources()
    print(f"✓ Registered {len(resources)} resources")
    
    expected_resources = [
        "disclosure-templates://ai-interaction-and-emotion",
        "watermark-config://technical-standards",
        "deepfake-labels://content-labeling",
        "article50-rules://official-text"
    ]
    
    for resource_uri in expected_resources:
        if resource_uri in resources:
            print(f"  ✓ {resource_uri}")
        else:
            print(f"  ✗ {resource_uri} NOT FOUND")
            sys.exit(1)
    
    print(f"\n✓ Resource registration test PASSED ({len(resources)} resources)")


def test_watermark_content(tools):
    """Test the consolidated watermark_content tool"""
    print("\n" + "="*70)
    print("TEST 4: Consolidated watermark_content Tool")
    print("="*70)
    
    watermark_tool = tools["watermark_content"]
    
    # Test text watermarking
    print("\nTesting text watermarking...")
    result = watermark_tool(
        content_type="text",
        content_description="Test article",
        text_content="This is a test article about AI.",
        generator="GPT-4",
        format_type="markdown"
    )
    assert result["content_type"] == "text"
    assert "watermarked_text" in result
    print("  ✓ Text watermarking works")
    
    # Test image watermarking
    print("Testing image watermarking...")
    result = watermark_tool(
        content_type="image",
        content_description="AI-generated landscape",
        generator="DALL-E",
        format_type="png"
    )
    assert result["content_type"] == "image"
    assert "c2pa_metadata" in result
    print("  ✓ Image watermarking works")
    
    # Test video watermarking
    print("Testing video watermarking...")
    result = watermark_tool(
        content_type="video",
        content_description="AI-generated video",
        generator="AI",
        format_type="mp4"
    )
    assert result["content_type"] == "video"
    assert "c2pa_metadata" in result
    print("  ✓ Video watermarking works")
    
    # Test audio watermarking
    print("Testing audio watermarking...")
    result = watermark_tool(
        content_type="audio",
        content_description="AI-generated audio",
        generator="AI",
        format_type="mp3"
    )
    assert result["content_type"] == "audio"
    assert "c2pa_metadata" in result
    print("  ✓ Audio watermarking works")
    
    print("\n✓ watermark_content test PASSED (all 4 content types)")


def test_label_deepfake(tools):
    """Test the consolidated label_deepfake tool"""
    print("\n" + "="*70)
    print("TEST 5: Consolidated label_deepfake Tool")
    print("="*70)
    
    label_tool = tools["label_deepfake"]
    
    # Test image labeling
    print("\nTesting image labeling...")
    result = label_tool(
        content_type="image",
        content_description="AI-generated portrait",
        is_artistic_work=False,
        language="en"
    )
    assert result["content_type"] == "image"
    assert "label_text" in result
    print("  ✓ Image labeling works")
    
    # Test video labeling
    print("Testing video labeling...")
    result = label_tool(
        content_type="video",
        content_description="AI-generated speech",
        is_artistic_work=False,
        language="en"
    )
    assert result["content_type"] == "video"
    assert "label_text" in result
    print("  ✓ Video labeling works")
    
    # Test audio labeling
    print("Testing audio labeling...")
    result = label_tool(
        content_type="audio",
        content_description="AI-generated voice",
        is_artistic_work=False,
        language="en"
    )
    assert result["content_type"] == "audio"
    assert "written_label" in result
    print("  ✓ Audio labeling works")
    
    # Test text labeling
    print("Testing text labeling...")
    result = label_tool(
        content_type="text",
        content_description="AI news article",
        text_content="Breaking news: AI breakthrough announced.",
        has_human_editor=True,
        editor_name="John Doe",
        language="en"
    )
    assert result["content_type"] == "text"
    assert "labeled_text" in result
    print("  ✓ Text labeling works")
    
    print("\n✓ label_deepfake test PASSED (all 4 content types)")


def test_get_disclosure(tools):
    """Test the consolidated get_disclosure tool"""
    print("\n" + "="*70)
    print("TEST 6: Consolidated get_disclosure Tool")
    print("="*70)
    
    disclosure_tool = tools["get_disclosure"]
    
    # Test AI interaction disclosure
    print("\nTesting AI interaction disclosure...")
    result = disclosure_tool(
        disclosure_type="ai_interaction",
        language="en",
        style="simple"
    )
    assert result["disclosure_type"] == "ai_interaction"
    assert result["article"] == "50(1)"
    assert "disclosure" in result
    print("  ✓ AI interaction disclosure works")
    
    # Test emotion recognition disclosure
    print("Testing emotion recognition disclosure...")
    result = disclosure_tool(
        disclosure_type="emotion_recognition",
        language="en",
        style="detailed"
    )
    assert result["disclosure_type"] == "emotion_recognition"
    assert result["article"] == "50(3)"
    assert "disclosure" in result
    print("  ✓ Emotion recognition disclosure works")
    
    print("\n✓ get_disclosure test PASSED (both disclosure types)")


def test_unchanged_tools(tools):
    """Test that unchanged tools still work"""
    print("\n" + "="*70)
    print("TEST 7: Unchanged Tools")
    print("="*70)
    
    # Test classify_ai_system_risk
    print("\nTesting classify_ai_system_risk...")
    classify_tool = tools["classify_ai_system_risk"]
    result = classify_tool(
        system_description="Test chatbot",
        use_case="chatbot",
        interacts_with_users=True,
        generates_content=True
    )
    assert "risk_level" in result
    print("  ✓ classify_ai_system_risk works")
    
    # Test check_prohibited_practices
    print("Testing check_prohibited_practices...")
    check_tool = tools["check_prohibited_practices"]
    result = check_tool(
        social_scoring=False,
        detects_emotions_in_workplace=False
    )
    assert "is_prohibited" in result
    print("  ✓ check_prohibited_practices works")
    
    # Test determine_eu_ai_act_role
    print("Testing determine_eu_ai_act_role...")
    role_tool = tools["determine_eu_ai_act_role"]
    result = role_tool(
        company_description="AI software company",
        company_location="United States",
        develops_ai_system=True,
        uses_ai_system=True
    )
    assert "primary_role" in result
    print("  ✓ determine_eu_ai_act_role works")
    
    print("\n✓ Unchanged tools test PASSED")


def main():
    """Run all tests"""
    print("\n" + "="*70)
    print("EU AI ACT MCP SERVER - PLUGIN SYSTEM TESTS")
    print("="*70)
    
    try:
        # Test 1: Plugin loading
        registry = test_plugin_loading()
        
        # Test 2: Tool registration
        tools = test_tool_registration(registry)
        
        # Test 3: Resource registration
        test_resource_registration(registry)
        
        # Test 4: Consolidated watermark_content
        test_watermark_content(tools)
        
        # Test 5: Consolidated label_deepfake
        test_label_deepfake(tools)
        
        # Test 6: Consolidated get_disclosure
        test_get_disclosure(tools)
        
        # Test 7: Unchanged tools
        test_unchanged_tools(tools)
        
        # Summary
        print("\n" + "="*70)
        print("ALL TESTS PASSED ✓")
        print("="*70)
        print(f"\nSummary:")
        print(f"  - 6 plugins loaded")
        print(f"  - 9 tools registered (down from 17)")
        print(f"  - 4 resources registered")
        print(f"  - All consolidated tools working")
        print(f"  - All unchanged tools working")
        print("\n✓ Plugin system is ready for production!")
        print("="*70)
        
        return 0
        
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
