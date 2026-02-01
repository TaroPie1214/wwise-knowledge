# 第三方和自定义 Audio Device

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [Audio Device 插件](00-Audio-Device-插件.md) > 第三方和自定义 Audio Device

## 第三方和自定义 Audio Device

在 Wwise 工程中，您可以访问第三方音频设备。如果适用，则请查阅文档以获得详细信息。但是，通过 Wwise 的开放式输出插件框架，程序员可创建和集成自己的 Audio Device 输出插件。

若想使用 sink 插件以便执行后期处理或将音频信号输出至非标硬件，请定义新的 Audio Device（音频设备）。若游戏不使用此类自定义处理，则无需创建 Audio Device。在默认情况下，Wwise 会显示工程中所用平台支持的内置 Audio Device。

一个工程中可定义多个 Audio Device 对象。You can select the one to use in the property page of any of the main busses of your project. 请记住，有些设备仅适用于部分平台。因此，请使用 Link/Unlink（链接/取消链接）功能在各个平台上指定不同的设备。注意，程序员可在初始化时或添加二路输出时改写代码中选择的设备。如需了解如何选择设备，请参阅《 [SDK 文档](https://www.audiokinetic.com/library/?source=SDK&id=struct_ak_output_settings_af1ff3ac68f3fa137c847144117d01535.html#af1ff3ac68f3fa137c847144117d01535)》。

### 有关为 Wwise 开发插件的详细信息

有关为 Wwise 开发插件的详细信息，请查阅  [SDK 文档](https://www.audiokinetic.com/library/?source=SDK&id=effectpluginsoundengine.html) 。

**相关主题**

- [“内置音频设备”一节](../../07-完善工程/01-管理输出/06-内置音频设备.md "内置音频设备")
- [*建立输出总线的结构*](../../03-设置工程/07-建立输出总线的结构/00-建立输出总线的结构.md "建立输出总线的结构")
- [“Secondary Bus 层级结构”一节](../../03-设置工程/07-建立输出总线的结构/00-建立输出总线的结构.md#the_master_secondary_bus_hierarchy "Secondary Bus 层级结构")
- [集成 Secondary Outputs](https://www.audiokinetic.com/library/edge/?source=SDK&id=integrating__secondary__outputs.html)

---