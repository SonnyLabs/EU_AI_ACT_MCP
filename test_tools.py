#!/usr/bin/env python3
"""
Simple test script to demonstrate the MCP server tools.

This script shows how the tools work locally without needing an MCP client.
You can use this to verify your server setup and test your custom tools.
"""

from server import reverse_text, calculate, text_stats


def test_reverse_text():
    """Test the reverse_text tool"""
    print("=" * 50)
    print("Testing reverse_text tool")
    print("=" * 50)
    result = reverse_text("Hello, MCP!")
    print(f"Original: {result['original']}")
    print(f"Reversed: {result['reversed']}")
    print()


def test_calculate():
    """Test the calculate tool"""
    print("=" * 50)
    print("Testing calculate tool")
    print("=" * 50)
    
    operations = [
        ("add", 10, 5),
        ("subtract", 10, 5),
        ("multiply", 10, 5),
        ("divide", 10, 5),
        ("divide", 10, 0),  # Test error handling
    ]
    
    for op, a, b in operations:
        result = calculate(op, a, b)
        if "error" in result:
            print(f"{op}({a}, {b}) -> Error: {result['error']}")
        else:
            print(f"{op}({a}, {b}) = {result['result']}")
    print()


def test_text_stats():
    """Test the text_stats tool"""
    print("=" * 50)
    print("Testing text_stats tool")
    print("=" * 50)
    
    text = "Hello MCP!\nThis is a TEST of the text statistics tool.\n123 numbers included!"
    result = text_stats(text)
    
    print(f"Text: {text[:50]}...")
    print(f"\nStatistics:")
    for key, value in result.items():
        print(f"  {key}: {value}")
    print()


if __name__ == "__main__":
    print("\n🚀 Testing Basic MCP Server Tools\n")
    
    test_reverse_text()
    test_calculate()
    test_text_stats()
    
    print("=" * 50)
    print("✅ All tests completed!")
    print("=" * 50)
    print("\nTo use these tools via MCP:")
    print("1. Run: python main.py")
    print("2. Connect your MCP client to the server")
    print("3. Call the tools through the MCP protocol")
