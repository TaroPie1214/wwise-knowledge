# ak_wwise_plugin_undo_event_pair_v1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](structak__wwise__plugin__undo__event__pair__v1-members.html) |
[Public 属性](#pub-attribs)

ak\_wwise\_plugin\_undo\_event\_pair\_v1结构体 参考

[Global](group__global.html)

A definition of an undo event, with a specific interface and instance.
[更多...](structak__wwise__plugin__undo__event__pair__v1.html#details)

`#include <PluginDef.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| struct [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1.html) \* | [m\_interface](structak__wwise__plugin__undo__event__pair__v1_a5b3be1790b702a1ec38d3605798d7e7e.html#a5b3be1790b702a1ec38d3605798d7e7e) |
|  | The interface to execute that undo event's commands. [更多...](structak__wwise__plugin__undo__event__pair__v1_a5b3be1790b702a1ec38d3605798d7e7e.html#a5b3be1790b702a1ec38d3605798d7e7e) |
|  | |
| struct [ak\_wwise\_plugin\_undo\_event\_instance\_v1](structak__wwise__plugin__undo__event__instance__v1.html) \* | [m\_instance](structak__wwise__plugin__undo__event__pair__v1_aac9df9fcc5fe32fa2c2995431a990204.html#aac9df9fcc5fe32fa2c2995431a990204) |
|  | The specific instance usued for that particular undo event. [更多...](structak__wwise__plugin__undo__event__pair__v1_aac9df9fcc5fe32fa2c2995431a990204.html#aac9df9fcc5fe32fa2c2995431a990204) |
|  | |

## 详细描述

A definition of an undo event, with a specific interface and instance.

Allows to bind an event from any source: Authoring or any plug-in. Allows to have multiple separate interfaces.

- [ak\_wwise\_plugin\_undo\_event\_v1](structak__wwise__plugin__undo__event__v1.html "API to create a custom undo event in a plug-in.") C interface for an undo event.
- [ak\_wwise\_plugin\_undo\_event\_instance\_v1](structak__wwise__plugin__undo__event__instance__v1.html "Base instance type for providing custom undo operations through ak_wwise_plugin_undo_event_v1.") C instance for an undo event.
- [AK::Wwise::Plugin::V1::UndoEvent](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_event.html "Base API to create a custom undo event in a plug-in.") C++ class for an undo event.
- [ak\_wwise\_plugin\_host\_undo\_manager\_v1](structak__wwise__plugin__host__undo__manager__v1.html "Host API to handle the plug-in's undo operations.") C interface for the undo manager.
- [AK::Wwise::Plugin::V1::UndoManager](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_undo_manager.html "Host API to handle the plug-in's undo operations.") C++ class for the undo manager.

在文件 [PluginDef.h](_plugin_def_8h_source.html) 第 [505](_plugin_def_8h_source.html#l00505) 行定义.