#!/usr/bin/env python3
"""
Test script for risk classification tools
Tests classify_ai_system_risk and check_prohibited_practices
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server import classify_ai_system_risk, check_prohibited_practices

def test_prohibited_system():
    """Test a prohibited AI system"""
    print("=" * 70)
    print("Test 1: PROHIBITED - Social Scoring System")
    print("=" * 70)
    
    result = classify_ai_system_risk(
        system_description="Social credit scoring system for citizens",
        use_case="social_scoring",
        social_scoring=True,
        interacts_with_users=True
    )
    
    print(f"\n✓ Risk Level: {result['risk_level']}")
    print(f"✓ Article: {result['article']}")
    print(f"✓ Reason: {result['reason']}")
    print(f"✓ Penalties: {result['penalties']}")
    print(f"✓ Action: {result['compliance_action']}")
    
    assert result['risk_level'] == "PROHIBITED"
    assert "35 million" in result['penalties']
    print(f"\n✅ Prohibited system test PASSED!")
    return True

def test_high_risk_system():
    """Test a high-risk AI system"""
    print(f"\n{'=' * 70}")
    print("Test 2: HIGH-RISK - Employment Screening System")
    print("=" * 70)
    
    result = classify_ai_system_risk(
        system_description="AI hiring tool that screens resumes and ranks candidates",
        use_case="employment",
        interacts_with_users=True
    )
    
    print(f"\n✓ Risk Level: {result['risk_level']}")
    print(f"✓ Article: {result['article']}")
    print(f"✓ Annex: {result['annex_reference']}")
    print(f"✓ Reason: {result['reason']}")
    print(f"✓ Compliance Deadline: {result['compliance_deadline']}")
    print(f"✓ Obligations: {len(result['applicable_obligations'])} required")
    
    assert result['risk_level'] == "HIGH-RISK"
    assert "employment" in result['reason'].lower()
    assert len(result['applicable_obligations']) > 0
    print(f"\n✅ High-risk system test PASSED!")
    return True

def test_limited_risk_system():
    """Test a limited-risk AI system"""
    print(f"\n{'=' * 70}")
    print("Test 3: LIMITED-RISK - Chatbot with Content Generation")
    print("=" * 70)
    
    result = classify_ai_system_risk(
        system_description="AI chatbot that interacts with users and generates text responses",
        use_case="chatbot",
        generates_content=True,
        interacts_with_users=True
    )
    
    print(f"\n✓ Risk Level: {result['risk_level']}")
    print(f"✓ Article: {result['article']}")
    print(f"✓ Reason: {result['reason']}")
    print(f"✓ Compliance Deadline: {result['compliance_deadline']}")
    print(f"✓ Obligations: {result['applicable_obligations']}")
    
    assert result['risk_level'] == "LIMITED-RISK"
    assert "Article 50" in result['article']
    print(f"\n✅ Limited-risk system test PASSED!")
    return True

def test_minimal_risk_system():
    """Test a minimal-risk AI system"""
    print(f"\n{'=' * 70}")
    print("Test 4: MINIMAL-RISK - Simple Spam Filter")
    print("=" * 70)
    
    result = classify_ai_system_risk(
        system_description="Email spam filter using ML",
        use_case="spam_detection"
    )
    
    print(f"\n✓ Risk Level: {result['risk_level']}")
    print(f"✓ Reason: {result['reason']}")
    print(f"✓ Compliance: {result['compliance_deadline']}")
    print(f"✓ Penalties: {result['penalties_if_non_compliant']}")
    
    assert result['risk_level'] == "MINIMAL-RISK"
    print(f"\n✅ Minimal-risk system test PASSED!")
    return True

def test_check_prohibited_none():
    """Test prohibited practices check - no violations"""
    print(f"\n{'=' * 70}")
    print("Test 5: Check Prohibited Practices - Clean System")
    print("=" * 70)
    
    result = check_prohibited_practices(
        uses_subliminal_techniques=False,
        social_scoring=False,
        detects_emotions_in_workplace=False
    )
    
    print(f"\n✓ Is Prohibited: {result['is_prohibited']}")
    print(f"✓ Violations: {result['violation_count']}")
    print(f"✓ Status: {result['compliance_status']}")
    print(f"✓ Recommendation: {result['recommendation']}")
    
    assert result['is_prohibited'] == False
    assert result['violation_count'] == 0
    print(f"\n✅ Clean system test PASSED!")
    return True

def test_check_prohibited_violations():
    """Test prohibited practices check - with violations"""
    print(f"\n{'=' * 70}")
    print("Test 6: Check Prohibited Practices - Multiple Violations")
    print("=" * 70)
    
    result = check_prohibited_practices(
        social_scoring=True,
        detects_emotions_in_workplace=True,
        scrapes_facial_images=True
    )
    
    print(f"\n✓ Is Prohibited: {result['is_prohibited']}")
    print(f"✓ Severity: {result['severity']}")
    print(f"✓ Violation Count: {result['violation_count']}")
    print(f"✓ Penalty Exposure: {result['total_penalty_exposure']}")
    
    print(f"\n{'-' * 70}")
    print("Violations Detected:")
    print(f"{'-' * 70}")
    for i, violation in enumerate(result['violations'], 1):
        print(f"\n  {i}. {violation['article']}: {violation['violation']}")
        print(f"     Penalty: {violation['penalty']}")
    
    assert result['is_prohibited'] == True
    assert result['violation_count'] == 3
    assert "CRITICAL" in result['severity']
    print(f"\n✅ Violations detection test PASSED!")
    return True

def test_education_high_risk():
    """Test education-based high-risk classification"""
    print(f"\n{'=' * 70}")
    print("Test 7: HIGH-RISK - Education Assessment System")
    print("=" * 70)
    
    result = classify_ai_system_risk(
        system_description="AI system for student performance evaluation and grading",
        use_case="education",
        education=True
    )
    
    print(f"\n✓ Risk Level: {result['risk_level']}")
    print(f"✓ Annex: {result['annex_reference']}")
    print(f"✓ Reason: {result['reason']}")
    
    assert result['risk_level'] == "HIGH-RISK"
    assert "education" in result['reason'].lower()
    print(f"\n✅ Education high-risk test PASSED!")
    return True

def main():
    print("\n" + "=" * 70)
    print("RISK CLASSIFICATION TOOLS - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    try:
        test_prohibited_system()
        test_high_risk_system()
        test_limited_risk_system()
        test_minimal_risk_system()
        test_check_prohibited_none()
        test_check_prohibited_violations()
        test_education_high_risk()
        
        print("\n" + "=" * 70)
        print("✅ ALL TESTS PASSED!")
        print("=" * 70)
        print("\nRisk Classification Tools Working:")
        print("  • classify_ai_system_risk - All 4 risk levels tested")
        print("  • check_prohibited_practices - Article 5 violations")
        print("\nCoverage:")
        print("  ✓ PROHIBITED (Article 5)")
        print("  ✓ HIGH-RISK (Article 6 + Annex III)")
        print("  ✓ LIMITED-RISK (Article 50)")
        print("  ✓ MINIMAL-RISK (No specific article)")
        return True
        
    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
