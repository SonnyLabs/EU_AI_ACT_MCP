"""
Plugin system for EU AI Act MCP Server

This module provides a plugin architecture for extending the MCP server
with new compliance tools and features.
"""

from .base import BasePlugin, PluginRegistry
from .loader import load_plugins

__all__ = ['BasePlugin', 'PluginRegistry', 'load_plugins']
