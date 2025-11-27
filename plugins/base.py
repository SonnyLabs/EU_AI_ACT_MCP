"""
Base plugin classes and registry for EU AI Act MCP Server
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Callable, Optional
import inspect


class BasePlugin(ABC):
    """
    Base class for all EU AI Act compliance plugins.
    
    Plugins can provide:
    - Tools (callable functions)
    - Resources (data files)
    - Configuration
    """
    
    def __init__(self):
        self.name = self.__class__.__name__
        self.enabled = True
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the plugin name"""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Return a description of what this plugin provides"""
        pass
    
    def get_tools(self) -> Dict[str, Callable]:
        """
        Return a dictionary of tool functions provided by this plugin.
        Key: tool name, Value: callable function
        """
        return {}
    
    def get_resources(self) -> Dict[str, Callable]:
        """
        Return a dictionary of resource functions provided by this plugin.
        Key: resource URI, Value: callable function
        """
        return {}
    
    def initialize(self) -> None:
        """
        Initialize the plugin. Called when the plugin is loaded.
        Override this to perform setup tasks.
        """
        pass
    
    def shutdown(self) -> None:
        """
        Shutdown the plugin. Called when the server is stopping.
        Override this to perform cleanup tasks.
        """
        pass


class PluginRegistry:
    """
    Registry for managing plugins in the EU AI Act MCP Server.
    
    Provides plugin discovery, registration, and lifecycle management.
    """
    
    def __init__(self):
        self._plugins: Dict[str, BasePlugin] = {}
        self._tools: Dict[str, Callable] = {}
        self._resources: Dict[str, Callable] = {}
    
    def register(self, plugin: BasePlugin) -> None:
        """
        Register a plugin with the registry.
        
        Args:
            plugin: The plugin instance to register
        """
        plugin_name = plugin.get_name()
        
        if plugin_name in self._plugins:
            raise ValueError(f"Plugin '{plugin_name}' is already registered")
        
        # Initialize the plugin
        plugin.initialize()
        
        # Register the plugin
        self._plugins[plugin_name] = plugin
        
        # Register tools
        for tool_name, tool_func in plugin.get_tools().items():
            if tool_name in self._tools:
                raise ValueError(f"Tool '{tool_name}' is already registered by another plugin")
            self._tools[tool_name] = tool_func
        
        # Register resources
        for resource_uri, resource_func in plugin.get_resources().items():
            if resource_uri in self._resources:
                raise ValueError(f"Resource '{resource_uri}' is already registered by another plugin")
            self._resources[resource_uri] = resource_func
    
    def unregister(self, plugin_name: str) -> None:
        """
        Unregister a plugin from the registry.
        
        Args:
            plugin_name: Name of the plugin to unregister
        """
        if plugin_name not in self._plugins:
            raise ValueError(f"Plugin '{plugin_name}' is not registered")
        
        plugin = self._plugins[plugin_name]
        
        # Shutdown the plugin
        plugin.shutdown()
        
        # Remove tools
        for tool_name in plugin.get_tools().keys():
            del self._tools[tool_name]
        
        # Remove resources
        for resource_uri in plugin.get_resources().keys():
            del self._resources[resource_uri]
        
        # Remove plugin
        del self._plugins[plugin_name]
    
    def get_plugin(self, plugin_name: str) -> Optional[BasePlugin]:
        """Get a plugin by name"""
        return self._plugins.get(plugin_name)
    
    def get_all_plugins(self) -> List[BasePlugin]:
        """Get all registered plugins"""
        return list(self._plugins.values())
    
    def get_all_tools(self) -> Dict[str, Callable]:
        """Get all registered tools from all plugins"""
        return self._tools.copy()
    
    def get_all_resources(self) -> Dict[str, Callable]:
        """Get all registered resources from all plugins"""
        return self._resources.copy()
    
    def get_tool(self, tool_name: str) -> Optional[Callable]:
        """Get a specific tool by name"""
        return self._tools.get(tool_name)
    
    def get_resource(self, resource_uri: str) -> Optional[Callable]:
        """Get a specific resource by URI"""
        return self._resources.get(resource_uri)
    
    def list_plugins(self) -> List[Dict[str, str]]:
        """
        List all registered plugins with their metadata.
        
        Returns:
            List of dictionaries containing plugin information
        """
        return [
            {
                "name": plugin.get_name(),
                "description": plugin.get_description(),
                "enabled": plugin.enabled,
                "tools": list(plugin.get_tools().keys()),
                "resources": list(plugin.get_resources().keys())
            }
            for plugin in self._plugins.values()
        ]
