#!/usr/bin/env python3
"""
Test script for the label_news_text tool
"""

from server import label_news_text


def test_news_without_editor():
    """Test news article WITHOUT human editor"""
    print("=" * 70)
    print("📰 Test 1: News article WITHOUT human editor")
    print("=" * 70)
    
    result = label_news_text(
        text_content="Scientists have discovered a new planet in a distant solar system. The planet, named Kepler-452c, shows signs of having liquid water.",
        has_human_editor=False,
        language="en"
    )
    
    print(f"\n✓ Article: {result['article']}")
    print(f"✓ Obligation: {result['obligation']}")
    print(f"✓ Disclosure: {result['disclosure']}")
    print(f"✓ Exemption Applies: {result['exemption_applies']}")
    print(f"✓ Exemption Reason: {result['exemption_reason']}")
    print(f"\n📝 Labeled Text:")
    print(result['labeled_text'])
    print()


def test_news_with_editor():
    """Test news article WITH human editor"""
    print("=" * 70)
    print("📰 Test 2: News article WITH human editor")
    print("=" * 70)
    
    result = label_news_text(
        text_content="Breaking news: Local community comes together to support new initiative for renewable energy.",
        has_human_editor=True,
        editor_name="Jane Smith",
        language="en"
    )
    
    print(f"\n✓ Article: {result['article']}")
    print(f"✓ Disclosure: {result['disclosure']}")
    print(f"✓ Exemption Applies: {result['exemption_applies']}")
    print(f"✓ Has Human Editor: {result['has_human_editor']}")
    print(f"\n📝 Labeled Text:")
    print(result['labeled_text'])
    print()


def test_spanish_language():
    """Test Spanish language"""
    print("=" * 70)
    print("📰 Test 3: Spanish language")
    print("=" * 70)
    
    result = label_news_text(
        text_content="El equipo de fútbol local ganó el campeonato regional.",
        has_human_editor=False,
        language="es"
    )
    
    print(f"\n✓ Language: {result['language']}")
    print(f"✓ Disclosure: {result['disclosure']}")
    print(f"\n📝 Labeled Text:")
    print(result['labeled_text'])
    print()


def test_french_with_editor():
    """Test French language with editor"""
    print("=" * 70)
    print("📰 Test 4: French language with editor")
    print("=" * 70)
    
    result = label_news_text(
        text_content="Le gouvernement annonce de nouvelles mesures pour l'environnement.",
        has_human_editor=True,
        editor_name="Pierre Dubois",
        language="fr"
    )
    
    print(f"\n✓ Language: {result['language']}")
    print(f"✓ Disclosure: {result['disclosure']}")
    print(f"✓ Exemption Applies: {result['exemption_applies']}")
    print(f"\n📝 Labeled Text:")
    print(result['labeled_text'])
    print()


if __name__ == "__main__":
    print("\n🚀 Testing label_news_text Tool (Article 50(4))\n")
    
    test_news_without_editor()
    test_news_with_editor()
    test_spanish_language()
    test_french_with_editor()
    
    print("=" * 70)
    print("✅ All tests completed!")
    print("=" * 70)
    print("\nThis tool implements Article 50(4) compliance for AI-generated text.")
    print("Use it to label news articles and public interest content.")
