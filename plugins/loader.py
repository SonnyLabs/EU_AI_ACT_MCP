"""
Plugin loader for EU AI Act MCP Server

Provides automatic plugin discovery and loading from the plugins directory.
"""

import os
import importlib
import inspect
from pathlib import Path
from typing import List
from .base import BasePlugin, PluginRegistry


def discover_plugins(plugins_dir: str = None) -> List[type]:
    """
    Discover all plugin classes in the plugins directory.
    
    Args:
        plugins_dir: Path to the plugins directory. If None, uses default.
    
    Returns:
        List of plugin classes (not instances)
    """
    if plugins_dir is None:
        # Default to plugins directory relative to this file
        plugins_dir = os.path.dirname(os.path.abspath(__file__))
    
    plugin_classes = []
    plugins_path = Path(plugins_dir)
    
    # Iterate through all Python files in the plugins directory
    for file_path in plugins_path.glob("*.py"):
        # Skip __init__.py, base.py, and loader.py
        if file_path.stem in ["__init__", "base", "loader"]:
            continue
        
        try:
            # Import the module
            module_name = f"plugins.{file_path.stem}"
            module = importlib.import_module(module_name)
            
            # Find all classes that inherit from BasePlugin
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BasePlugin) and obj is not BasePlugin:
                    plugin_classes.append(obj)
        
        except Exception as e:
            print(f"Warning: Failed to load plugin from {file_path}: {e}")
    
    return plugin_classes


def load_plugins(registry: PluginRegistry, plugins_dir: str = None) -> None:
    """
    Load all discovered plugins into the registry.
    
    Args:
        registry: The PluginRegistry to load plugins into
        plugins_dir: Path to the plugins directory. If None, uses default.
    """
    plugin_classes = discover_plugins(plugins_dir)
    
    for plugin_class in plugin_classes:
        try:
            # Instantiate the plugin
            plugin_instance = plugin_class()
            
            # Register it
            registry.register(plugin_instance)
            
            print(f"Loaded plugin: {plugin_instance.get_name()}")
        
        except Exception as e:
            print(f"Warning: Failed to register plugin {plugin_class.__name__}: {e}")


def load_plugin_by_name(registry: PluginRegistry, plugin_name: str, plugins_dir: str = None) -> None:
    """
    Load a specific plugin by name.
    
    Args:
        registry: The PluginRegistry to load the plugin into
        plugin_name: Name of the plugin file (without .py extension)
        plugins_dir: Path to the plugins directory. If None, uses default.
    """
    if plugins_dir is None:
        plugins_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Import the module
        module_name = f"plugins.{plugin_name}"
        module = importlib.import_module(module_name)
        
        # Find the plugin class
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BasePlugin) and obj is not BasePlugin:
                plugin_instance = obj()
                registry.register(plugin_instance)
                print(f"Loaded plugin: {plugin_instance.get_name()}")
                return
        
        raise ValueError(f"No plugin class found in module {module_name}")
    
    except Exception as e:
        raise RuntimeError(f"Failed to load plugin '{plugin_name}': {e}")
