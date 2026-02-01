# Wwise 插件 ID

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise 插件 ID

Wwise 插件通过公司 ID 和插件 ID 进行标识。这些 ID 的定义位于 plugin.xml 文件中。

- **Company ID**（公司 ID）：用于精确识别特定公司
  - `EffectPlugin、` `SourcePlugin、` `ConversionPlugin` 等标签的属性 `CompanyID`
  - 介于 0-4095 之间的 12 位无符号整数。
  - 0-63 预留给 Audiokinetic 使用。
  - 64-255 可用于内部插件开发。
  - 256-4095 由 Audiokinetic 指派给插件程序员。
- **Plug-in ID**（插件 ID）：用于精确识别指定 Company ID 对应的某个插件
  - `EffectPlugin、` `SourcePlugin、` `ConversionPlugin` 等标签的属性 `PluginID`
  - 介于 0-32767 之间的 16 位无符号整数。
  - 由插件程序员自由设定。

|  |  |
| --- | --- |
|  | **备注:** Company ID 和 Plug-in ID 组合不可重复。 |

Within Wwise and the sound engine, the Company ID and Plug-in ID are combined with a 4-bit Plug-in Type value to form a 32-bit unique identifier. 这些插件类型值在 `AkPluginType` enum (IAkEffect.h) 中定义，如下所示：

- AkPluginTypeNone = 0，供 Audiokinetic 内部使用
- AkPluginTypeCodec = 1，转换插件
- AkPluginTypeSource = 2，源插件
- AkPluginTypeEffect = 3，效果器插件
- Audiokinetic 公司 ID 和插件 ID

|  |  |
| --- | --- |
|  | **备注:** 这个 4 位的插件类型值与 ID 的唯一性无关：Wwise 的 Plug-in Manager 将确保公司 ID 和插件 ID 的组合不会存在重复，不论其属于何种插件类型。 |

封装后的 32 位类 ID 组合如下：`插件 ID + 公司 ID + 插件类型 == 封装后的 32 位类 ID`。因此当插件 ID 为 1、公司 ID 为 0 并且插件类型为 1 时，封装的 32 位类 ID 为 0x00010001。

|  |  |
| --- | --- |
|  | **备注:** 按照 [AkTypes.h](_platforms_2_windows_2_ak_types_8h.html) 中的 `AKCOMPANYID_AUDIOKINETIC` 定义所述，所有 Audiokinetic 插件（转换插件、源插件和效果器插件）的公司 ID 均为 0，如 。 |

# 示例

以下是一个虚构的效果器插件的示例：

- Company ID: 72
- Plugin ID: 5

**XML:**

<?xml version="1.0" encoding="utf-8"?>

<!-- Copyright (C) 2020 Audiokinetic Inc. -->

<PluginModule>

<EffectPlugin Name="FictionalDelay" CompanyID="72" PluginID="5">

...

**Plugin Factory:**

...

AK\_IMPLEMENT\_PLUGIN\_FACTORY(FictionalDelayFX, [AkPluginTypeEffect](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4a2971cc4c818bf62c55175445d2be117d), 72, 5)

...

[AkPluginTypeEffect](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4a2971cc4c818bf62c55175445d2be117d)

@ AkPluginTypeEffect

Effect plug-in: applies processing to audio data.

**Definition:** [AkEnums.h:285](_ak_enums_8h_source.html#l00285)