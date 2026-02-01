# AkSinkFactory.h

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](dir_82efb7d747620ecf0c13ab9b5d2ed63d.html)
- [Plugin](dir_815d3776a7d381c10e5f611b84aea7f6.html)

[变量](#var-members)

AkSinkFactory.h 文件参考

[浏览源代码.](_ak_sink_factory_8h_source.html)

|  |  |
| --- | --- |
| 变量 | |
| const unsigned long | [AKEFFECTID\_SINK](_ak_sink_factory_8h_a24a9a3e985b9b4c0f8187cd90011fd0d.html#a24a9a3e985b9b4c0f8187cd90011fd0d) = 152 |
|  | |

## 详细描述

Plug-in unique ID and creation functions (hooks) necessary to register the mixer plug-in in the sound engine.   
**Wwise effect name:** Sink   
**Library file:** AkSink.lib

Registers the Audio Sink Sample plugin automatically. This file should be included once in a .CPP (not a .h, really). The simple inclusion of this file and the linking of the library is enough to use the plugin. **WARNING**: Include this file only if you wish to link statically with the plugins. Dynamic Libaries (DLL, so, etc) are automatically detected and do not need this include file.   
**Wwise plugin name:** Audio Sink Sample   
**Library file:** AkSink.lib

在文件 [AkSinkFactory.h](_ak_sink_factory_8h_source.html) 中定义.