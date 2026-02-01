# AK ASIO Output

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [Audio Device 插件](00-Audio-Device-插件.md) > AK ASIO Output

## AK ASIO Output

（请参阅下文的 [“AK ASIO output properties”一节](01-AK-ASIO-Output.md#asio_output_plug_in_properties "AK ASIO output properties")。）

AK ASIO Output 插件使用 Steinberg Audio Stream Input/Output (ASIO) SDK 连接兼容 ASIO 的输出设备。

### 借助 AK ASIO 输出设备在 Wwise 设计工具中监控工程

To monitor your project in Wwise Authoring through an AK ASIO output device, an ASIO driver can be selected for a main bus. 请参阅 [“Selecting audio output devices”一节](../../02-入门/04-个性化您的工作空间/05-Setting-authoring-audio-preferences.md#setting_output_devices "Selecting audio output devices")。

### Selecting an ASIO driver outside of Wwise Authoring

|  |  |
| --- | --- |
| [注意] | 注意 |
| - WWISEASIODRV 环境变量会改写 Authoring Audio Preferences 中选择的驱动程序。 - Selecting AK ASIO Output as the Audio Device on multiple main busses is not   supported. - Selecting a System Audio Device on a bus while having an ASIO Audio Device on   another bus might cause device exclusivity conflicts. |

To select an ASIO hardware device outside of the Wwise authoring tool, it is necessary to create a "WWISEASIODRV" environment variable with a value set to match the ASIO driver name specified for a main bus in Authoring Audio Preferences. 请参阅 [“Selecting audio output devices”一节](../../02-入门/04-个性化您的工作空间/05-Setting-authoring-audio-preferences.md#setting_output_devices "Selecting audio output devices")。

比如，对于名为 ASIO\_Output 的 "ASIO Output" Audio Device ShareSet（音频设备共享集），若 Hardware Device 列中显示“ASIO\_Output - ASIO 驱动程序的名称”，则必须将 WWISEASIODRV 值设为 ASIO 驱动程序的名称。

### AK ASIO output properties

| 界面元素 | 描述 |
| --- | --- |
| **AK ASIO Output 属性** | |
| Channel Configuration | 声道配置。设置输出设备的声道数及声道配置。有关详细信息，请参阅[“了解总线配置”一节](../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。  若选择 **Default**（默认），则沿用所选 ASIO 硬件设备的声道数。  另外，对于非标准配置的总线的声道数，还可使用匿名配置来设置。若要配置匿名声道数，请打开 `C:\Program Files (x86)\Audiokinetic\Wwise <version>\Authoring\x64\Release\bin\plugins\ASIO.xml`，然后添加下图中指示的命令行。本例所示为 6 个声道，不过只要数值在 1 ~ 255 之间都是允许的。 |
| Base Channel | 基准声道。对总线的所有输出声道进行偏置，以便将第一个输出声道作为基准声道。系统会从基准声道开始顺序输出各个声道。  默认值为 1，即从第一个声道开始输出。  比如，若针对立体声配置（两个声道）将基准声道设为 2，则将输出到声道 2 和 3 而非 1 和 2。 |

**相关主题**

- [“AK ASIO Input ”一节](../03-源插件/01-AK-ASIO-Input.md "AK ASIO Input")

---