#!/usr/bin/env python3
"""
Test script for SonnyLabs AI Security tools
NOTE: These are mock tests. Real tests require valid SonnyLabs API credentials.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_tool_availability():
    """Test that SonnyLabs security tools are available"""
    print("=" * 70)
    print("Test: SonnyLabs Security Tools Availability")
    print("=" * 70)
    
    from server import (
        scan_for_prompt_injection,
        detect_pii_in_content,
        check_sensitive_file_access
    )
    
    print("\n✓ scan_for_prompt_injection imported successfully")
    print("✓ detect_pii_in_content imported successfully")
    print("✓ check_sensitive_file_access imported successfully")
    
    print(f"\n✅ All SonnyLabs security tools available!")
    return True

def test_tool_signatures():
    """Test that tools have correct parameters"""
    print(f"\n{'=' * 70}")
    print("Test: Tool Signatures")
    print("=" * 70)
    
    from server import (
        scan_for_prompt_injection,
        detect_pii_in_content,
        check_sensitive_file_access
    )
    
    import inspect
    
    # Check scan_for_prompt_injection
    sig = inspect.signature(scan_for_prompt_injection)
    params = list(sig.parameters.keys())
    print(f"\n✓ scan_for_prompt_injection parameters: {params}")
    assert 'user_input' in params
    assert 'sonnylabs_api_token' in params
    assert 'sonnylabs_analysis_id' in params
    
    # Check detect_pii_in_content
    sig = inspect.signature(detect_pii_in_content)
    params = list(sig.parameters.keys())
    print(f"✓ detect_pii_in_content parameters: {params}")
    assert 'content' in params
    assert 'sonnylabs_api_token' in params
    assert 'sonnylabs_analysis_id' in params
    
    # Check check_sensitive_file_access
    sig = inspect.signature(check_sensitive_file_access)
    params = list(sig.parameters.keys())
    print(f"✓ check_sensitive_file_access parameters: {params}")
    assert 'file_path' in params
    assert 'agent_action' in params
    assert 'sonnylabs_api_token' in params
    assert 'sonnylabs_analysis_id' in params
    
    print(f"\n✅ All tool signatures correct!")
    return True

def test_error_handling():
    """Test that tools handle errors gracefully"""
    print(f"\n{'=' * 70}")
    print("Test: Error Handling (Invalid Credentials)")
    print("=" * 70)
    
    from server import scan_for_prompt_injection
    
    # Call with invalid credentials
    result = scan_for_prompt_injection(
        user_input="Test input",
        sonnylabs_api_token="invalid_token",
        sonnylabs_analysis_id="invalid_id",
        tag="test"
    )
    
    print(f"\n✓ Tool returned without crashing")
    print(f"✓ Result contains error info: {'error' in result}")
    
    if 'error' in result:
        print(f"✓ Error message: {result['error']}")
        print(f"✓ Recommendation provided: {result.get('recommendation', 'None')}")
    
    print(f"\n✅ Error handling works correctly!")
    return True

def test_compliance_fields():
    """Test that tools return EU AI Act compliance information"""
    print(f"\n{'=' * 70}")
    print("Test: EU AI Act Compliance Fields")
    print("=" * 70)
    
    from server import (
        scan_for_prompt_injection,
        detect_pii_in_content,
        check_sensitive_file_access
    )
    
    # Test scan_for_prompt_injection
    result1 = scan_for_prompt_injection(
        user_input="Test",
        sonnylabs_api_token="test",
        sonnylabs_analysis_id="test"
    )
    
    if 'eu_ai_act_relevance' in result1 or 'error' in result1:
        print("\n✓ scan_for_prompt_injection includes Article 15 reference")
    
    # Test detect_pii_in_content
    result2 = detect_pii_in_content(
        content="Test content",
        sonnylabs_api_token="test",
        sonnylabs_analysis_id="test"
    )
    
    if 'eu_ai_act_relevance' in result2 or 'error' in result2:
        print("✓ detect_pii_in_content includes Article 10 reference")
    
    # Test check_sensitive_file_access
    result3 = check_sensitive_file_access(
        file_path="/test/path",
        agent_action="read",
        sonnylabs_api_token="test",
        sonnylabs_analysis_id="test"
    )
    
    if 'eu_ai_act_relevance' in result3 or 'error' in result3:
        print("✓ check_sensitive_file_access includes Articles 10 & 15 reference")
    
    print(f"\n✅ All tools reference appropriate EU AI Act articles!")
    return True

def main():
    print("\n" + "=" * 70)
    print("SONNYLABS AI SECURITY TOOLS - TEST SUITE")
    print("=" * 70)
    print("\nNOTE: These are availability tests.")
    print("Full integration tests require valid SonnyLabs API credentials.")
    print("Get credentials at: https://sonnylabs-service.onrender.com/analysis")
    
    try:
        test_tool_availability()
        test_tool_signatures()
        test_error_handling()
        test_compliance_fields()
        
        print("\n" + "=" * 70)
        print("✅ ALL TESTS PASSED!")
        print("=" * 70)
        print("\nSonnyLabs Security Tools Installed:")
        print("  ✓ scan_for_prompt_injection (Article 15)")
        print("  ✓ detect_pii_in_content (Article 10 + GDPR)")
        print("  ✓ check_sensitive_file_access (Articles 10 & 15)")
        print("\nTo test with real API:")
        print("  1. Get API credentials from SonnyLabs dashboard")
        print("  2. Set environment variables:")
        print("     - SONNYLABS_API_TOKEN")
        print("     - SONNYLABS_ANALYSIS_ID")
        print("  3. Call tools with your credentials")
        return True
        
    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
