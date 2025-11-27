# EU AI Act MCP Server - Architecture Diagrams

## v1 Architecture (Monolithic)

```
┌─────────────────────────────────────────────────────────────┐
│                        server.py                            │
│                      (1,736 lines)                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │              17 Tools (inline)                      │  │
│  ├─────────────────────────────────────────────────────┤  │
│  │ • watermark_text                                    │  │
│  │ • watermark_image                                   │  │
│  │ • watermark_video                                   │  │
│  │ • watermark_audio                                   │  │
│  │ • label_image_deepfake                              │  │
│  │ • label_video_deepfake                              │  │
│  │ • label_audio_deepfake                              │  │
│  │ • label_news_text                                   │  │
│  │ • get_ai_interaction_disclosure                     │  │
│  │ • get_emotion_recognition_disclosure                │  │
│  │ • get_deepfake_label_templates                      │  │
│  │ • classify_ai_system_risk                           │  │
│  │ • check_prohibited_practices                        │  │
│  │ • determine_eu_ai_act_role                          │  │
│  │ • scan_for_prompt_injection                         │  │
│  │ • check_sensitive_file_access                       │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │              4 Resources (inline)                   │  │
│  ├─────────────────────────────────────────────────────┤  │
│  │ • disclosure-templates://...                        │  │
│  │ • deepfake-labels://...                             │  │
│  │ • article50-rules://...                             │  │
│  │ • watermark-config://...                            │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Problems:
❌ Single large file (1,736 lines)
❌ High coupling
❌ Low cohesion
❌ Hard to extend
❌ Hard to test
```

## v2 Architecture (Plugin-Based)

```
┌─────────────────────────────────────────────────────────────────────┐
│                         server_v2.py                                │
│                         (100 lines)                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              Plugin System Core                             │  │
│  ├─────────────────────────────────────────────────────────────┤  │
│  │ • PluginRegistry                                            │  │
│  │ • load_plugins()                                            │  │
│  │ • Auto-discovery                                            │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│                            ↓ loads                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                 │
                                 │
        ┌────────────────────────┴────────────────────────┐
        │                                                  │
        ↓                                                  ↓
┌───────────────────┐                            ┌───────────────────┐
│   plugins/        │                            │   resources/      │
│   (6 plugins)     │                            │   (4 JSON files)  │
├───────────────────┤                            ├───────────────────┤
│                   │                            │                   │
│ ┌───────────────┐ │                            │ • disclosure_     │
│ │Transparency   │ │                            │   templates.json  │
│ │Plugin         │ │                            │                   │
│ ├───────────────┤ │                            │ • deepfake_       │
│ │ Tools:        │ │                            │   labels.json     │
│ │ • get_        │ │                            │                   │
│ │   disclosure  │ │                            │ • article50_      │
│ │ • get_deepfake│ │                            │   rules.json      │
│ │   _label_     │ │                            │                   │
│ │   templates   │ │                            │ • watermark_      │
│ └───────────────┘ │                            │   config.json     │
│                   │                            │                   │
│ ┌───────────────┐ │                            └───────────────────┘
│ │Watermarking   │ │
│ │Plugin         │ │
│ ├───────────────┤ │
│ │ Tools:        │ │
│ │ • watermark_  │ │
│ │   content     │ │
│ │   (4 types)   │ │
│ └───────────────┘ │
│                   │
│ ┌───────────────┐ │
│ │Deepfake       │ │
│ │Plugin         │ │
│ ├───────────────┤ │
│ │ Tools:        │ │
│ │ • label_      │ │
│ │   deepfake    │ │
│ │   (4 types)   │ │
│ └───────────────┘ │
│                   │
│ ┌───────────────┐ │
│ │Risk           │ │
│ │Classification │ │
│ │Plugin         │ │
│ ├───────────────┤ │
│ │ Tools:        │ │
│ │ • classify_   │ │
│ │   ai_system_  │ │
│ │   risk        │ │
│ │ • check_      │ │
│ │   prohibited_ │ │
│ │   practices   │ │
│ └───────────────┘ │
│                   │
│ ┌───────────────┐ │
│ │Role           │ │
│ │Determination  │ │
│ │Plugin         │ │
│ ├───────────────┤ │
│ │ Tools:        │ │
│ │ • determine_  │ │
│ │   eu_ai_act_  │ │
│ │   role        │ │
│ └───────────────┘ │
│                   │
│ ┌───────────────┐ │
│ │Security       │ │
│ │Plugin         │ │
│ ├───────────────┤ │
│ │ Tools:        │ │
│ │ • scan_for_   │ │
│ │   prompt_     │ │
│ │   injection   │ │
│ │ • check_      │ │
│ │   sensitive_  │ │
│ │   file_access │ │
│ └───────────────┘ │
│                   │
└───────────────────┘

Benefits:
✅ Modular (9 files vs 1 file)
✅ Low coupling (plugins independent)
✅ High cohesion (related code together)
✅ Easy to extend (add plugins)
✅ Easy to test (test plugins separately)
```

## Plugin Loading Flow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Server Startup                                           │
│    python server_v2.py                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Create PluginRegistry                                    │
│    registry = PluginRegistry()                              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Load Plugins                                             │
│    load_plugins(registry)                                   │
│    ├─ Discover .py files in plugins/                        │
│    ├─ Import each module                                    │
│    ├─ Find BasePlugin subclasses                            │
│    └─ Instantiate plugin classes                            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Register Each Plugin                                     │
│    registry.register(plugin)                                │
│    ├─ Call plugin.initialize()                              │
│    ├─ Extract tools via plugin.get_tools()                  │
│    ├─ Extract resources via plugin.get_resources()          │
│    └─ Store in registry                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Register with MCP Server                                 │
│    for tool_name, tool_func in registry.get_all_tools():    │
│        mcp.tool()(tool_func)                                │
│    for resource_uri, resource_func in registry.get_all...   │
│        mcp.resource(resource_uri)(resource_func)            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓
┌─────────────────────────────────────────────────────────────┐
│ 6. Server Ready                                             │
│    ✓ 6 plugins loaded                                       │
│    ✓ 8 tools registered                                     │
│    ✓ 4 resources registered                                 │
└─────────────────────────────────────────────────────────────┘
```

## Tool Consolidation Example

### Before (v1): 4 Separate Tools

```
┌─────────────────────────────────────────────────────────────┐
│                    Watermarking Tools                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  watermark_text(text_content, generator, format_type)      │
│       ↓                                                     │
│  [Text watermarking logic - 50 lines]                      │
│                                                             │
│  ─────────────────────────────────────────────────────     │
│                                                             │
│  watermark_image(image_description, generator, format)     │
│       ↓                                                     │
│  [Image watermarking logic - 50 lines]                     │
│                                                             │
│  ─────────────────────────────────────────────────────     │
│                                                             │
│  watermark_video(video_description, generator, format)     │
│       ↓                                                     │
│  [Video watermarking logic - 50 lines]                     │
│                                                             │
│  ─────────────────────────────────────────────────────     │
│                                                             │
│  watermark_audio(audio_description, generator, format)     │
│       ↓                                                     │
│  [Audio watermarking logic - 50 lines]                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Total: 4 tools, ~200 lines, duplicated validation
```

### After (v2): 1 Unified Tool

```
┌─────────────────────────────────────────────────────────────┐
│                 Consolidated Tool                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  watermark_content(content_type, ...)                      │
│       ↓                                                     │
│  [Validate content_type]                                   │
│       ↓                                                     │
│  ┌──────────────────────────────────────────────┐          │
│  │  if content_type == "text":                  │          │
│  │      return _watermark_text(...)             │          │
│  │  elif content_type == "image":               │          │
│  │      return _watermark_image(...)            │          │
│  │  elif content_type == "video":               │          │
│  │      return _watermark_video(...)            │          │
│  │  elif content_type == "audio":               │          │
│  │      return _watermark_audio(...)            │          │
│  └──────────────────────────────────────────────┘          │
│       ↓                                                     │
│  [Private methods for each type]                           │
│  • _watermark_text() - 40 lines                            │
│  • _watermark_image() - 40 lines                           │
│  • _watermark_video() - 40 lines                           │
│  • _watermark_audio() - 40 lines                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Total: 1 tool, ~180 lines, shared validation
Benefits: -75% tools, -10% code, better UX
```

## Plugin Class Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                      BasePlugin                             │
│                   (Abstract Base Class)                     │
├─────────────────────────────────────────────────────────────┤
│ Abstract Methods:                                           │
│ • get_name() -> str                                         │
│ • get_description() -> str                                  │
│                                                             │
│ Optional Methods:                                           │
│ • get_tools() -> Dict[str, Callable]                        │
│ • get_resources() -> Dict[str, Callable]                    │
│ • initialize() -> None                                      │
│ • shutdown() -> None                                        │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ inherits
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ↓                           ↓
┌──────────────────┐      ┌──────────────────┐
│Transparency      │      │Watermarking      │
│Plugin            │      │Plugin            │
├──────────────────┤      ├──────────────────┤
│• get_disclosure  │      │• watermark_      │
│• get_deepfake_   │      │  content         │
│  label_templates │      │                  │
└──────────────────┘      └──────────────────┘
        │                           │
        ↓                           ↓
┌──────────────────┐      ┌──────────────────┐
│Deepfake          │      │Risk              │
│Plugin            │      │Classification    │
├──────────────────┤      │Plugin            │
│• label_deepfake  │      ├──────────────────┤
│                  │      │• classify_ai_    │
└──────────────────┘      │  system_risk     │
        │                 │• check_          │
        ↓                 │  prohibited_     │
┌──────────────────┐      │  practices       │
│Role              │      └──────────────────┘
│Determination     │                │
│Plugin            │                ↓
├──────────────────┤      ┌──────────────────┐
│• determine_eu_   │      │Security          │
│  ai_act_role     │      │Plugin            │
└──────────────────┘      ├──────────────────┤
                          │• scan_for_       │
                          │  prompt_         │
                          │  injection       │
                          │• check_          │
                          │  sensitive_      │
                          │  file_access     │
                          └──────────────────┘
```

## Comparison Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    v1 vs v2 Comparison                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Metric              │  v1 (Monolithic)  │  v2 (Plugins)  │
│  ───────────────────────────────────────────────────────── │
│  Tools               │  17               │  8             │
│  Files               │  1                │  9             │
│  Lines per file      │  1,736            │  100-400       │
│  Plugins             │  0                │  6             │
│  Extensibility       │  ❌               │  ✅            │
│  Testability         │  ❌               │  ✅            │
│  Maintainability     │  ❌               │  ✅            │
│  Code organization   │  ❌               │  ✅            │
│  Coupling            │  High             │  Low           │
│  Cohesion            │  Low              │  High          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Summary

The v2 architecture provides:

✅ **53% fewer tools** (17 → 8)
✅ **Modular design** (6 independent plugins)
✅ **Auto-discovery** (plugins load automatically)
✅ **Extensibility** (add plugins without touching core)
✅ **Better organization** (clear separation of concerns)
✅ **Easier testing** (test plugins independently)
✅ **Same functionality** (all features preserved)

The plugin-based architecture makes the codebase professional, maintainable, and ready for future growth.
