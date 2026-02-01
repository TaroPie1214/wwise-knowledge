# Audio Devices

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > Audio Devices

### Audio Devices

The Devices hierarchy is a series of Audio Devices, each representing the physical and virtual outputs provided by the supported platforms. Wwise 默认包含以下内置 Audio Device：

- Communication
- Controller Headphones
- DVR Bypass
- No Output
- Controller Speaker
- System

有关每一类型的详细信息，请参阅[“内置音频设备”一节](../../../../07-完善工程/01-管理输出/06-内置音频设备.md "内置音频设备")章节。

每个 Audio Device 属性选项的描述都可在以下 Audio Device Editor（音频设备编辑器）分区中找到：

- [“Audio Device Editor：System”一节](01-Audio-Device-Editor：System.md "Audio Device Editor：System")
- [“Audio Device Editor：其他”一节](02-Audio-Device-Editor：其他.md "Audio Device Editor：其他")

|  |  |
| --- | --- |
| [备注] | 备注 |
| 只有 System Audio Device 支持潜在 [3D Audio](../../../../14-词汇表.md#glossary_3daudio "3D Audio") 功能。因此，System Audio Device Editor 内包含很多其他 Audio Device 类型的 Audio Device Editor 中没有的属性。 |

另外，还可通过安装第三方插件来添加其他虚拟输出。在这种情况下，Audio Device Editor 会显示开发者希望包含的各项信息。不过会依据针对 Audio Device 插件创建的 XML 中提供的信息，自动生成默认 UI（类似 [Source Editor: Plug-ins](https://www.audiokinetic.com/library/2019.2.7_7402/?source=Help&id=source_plug_in_editor)）及相关字段。请参阅 [“第三方和自定义 Audio Device”一节](../../../../10-Wwise-插件/01-Audio-Device-插件/02-第三方和自定义-Audio-Device.md "第三方和自定义 Audio Device") 了解详细信息。

**相关主题**

- [“内置音频设备”一节](../../../../07-完善工程/01-管理输出/06-内置音频设备.md "内置音频设备")
- [“第三方和自定义 Audio Device”一节](../../../../10-Wwise-插件/01-Audio-Device-插件/02-第三方和自定义-Audio-Device.md "第三方和自定义 Audio Device")

---