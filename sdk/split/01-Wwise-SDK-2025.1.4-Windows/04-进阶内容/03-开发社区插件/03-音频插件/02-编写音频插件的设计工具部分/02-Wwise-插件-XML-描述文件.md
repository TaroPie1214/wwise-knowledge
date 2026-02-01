# Wwise 插件 XML 描述文件

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise 插件 XML 描述文件

Wwise 的开放式架构支持各种不同的插件：

- 音频插件。其中包括：
  - 源插件，用于生成声音
  - 效果器插件，用于变换声音
  - Sink 插件，用于向媒介输出声音
- 版本控制插件，允许在 Wwise 内使用版本控制软件

音频插件以 XML 文件的形式描述其模型。藉此，无需重新编译代码便可快速更改插件的各项设置，包括默认属性值。倘若插件没有提供自定义 GUI，还可使用此模型中描述的属性，在 Wwise 中以属性表的形式提供默认图形界面。

# XML 文件概述

XML 描述文件包含有关 Wwise 插件的多方面信息，包括：

- 插件名称
- 公司 ID 和插件 ID。请参阅 [Wwise 插件 ID](plugin_ids.html) 了解详情。
- 各平台所支持的功能
- 属性定义，包括：
  - 属性名称（在代码中和持久化文件中标识属性的字符串）
  - 属性类型
  - RTPC 支持
  - 默认值
  - 声音引擎属性 ID（将此属性绑定到声音引擎插件的代码中）
  - 值域限制或枚举限制
  - 对其他属性的依赖性
  - 用户界面描述元素
- 内部对象类型定义，包括：
  - 内部对象类型名称（标识内部对象类型的字符串）
  - 内部对象属性

在使用 [wp.py 开发工具](effectplugin_tools.html)时，会提供默认的 XML 文件并预先填入创建时提供的信息。有关更多详细信息，请参阅 [创建音频插件](effectplugin_tools_newplugin.html) 章节。

|  |  |
| --- | --- |
|  | **备注:** Wwise 插件动态库可包含多个插件（参见 [设计工具插件库格式](plugin_dll.html) 章节），每个插件都必须在单独的关联 XML 文件中加以描述。 |

# XML 文件命名

每个 Wwise 插件动态库的 XML 描述文件都要采用与动态库相同的名称，只不过 XML 文件扩展名不同且不带 lib 前缀。

比如，若将动态库命名为 **MyPlugin.dll** 或 **libMyPlugin.dylib**，则须将插件描述文件命名为 **MyPlugin.xml**。

# 示例：XML 描述文件

以下是一个简单插件 XML 描述文件的示例。

<?xml version="1.0" encoding="UTF-8"?>

<!-- Copyright (C) 2020 Audiokinetic Inc. -->

<PluginModule>

<EffectPlugin Name="Parametric EQ" CompanyID="0" PluginID="105">

<[PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823)>

<PlatformSupport>

<Platform Name="Windows">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

<Platform Name="Mac">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

<Platform Name="iOS">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

<Platform Name="XboxOne">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

<Platform Name="PS4">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

</PlatformSupport>

</[PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823)>

<Properties>

<Property Name="OnOffBand1" [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="bool" SupportRTPCType="Exclusive" ForceRTPCCurveSegmentShape="Constant" DisplayName="Band 1 Enable">

<DefaultValue>true</DefaultValue>

<AudioEnginePropertyID>4</AudioEnginePropertyID>

</Property>

<Property Name="FilterTypeBand1" [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="int32" SupportRTPCType="Exclusive" ForceRTPCCurveSegmentShape="Constant" DisplayName="Band 1 Filter Type">

<DefaultValue>5</DefaultValue>

<AudioEnginePropertyID>10</AudioEnginePropertyID>

<Restrictions>

<ValueRestriction>

<Enumeration [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="int32">

<Value DisplayName="Low Pass">0</Value>

<Value DisplayName="High Pass">1</Value>

<Value DisplayName="Band Pass">2</Value>

<Value DisplayName="Notch">3</Value>

<Value DisplayName="Low Shelf">4</Value>

<Value DisplayName="High Shelf">5</Value>

<Value DisplayName="Peaking">6</Value>

</Enumeration>

</ValueRestriction>

</Restrictions>

<Dependencies>

<PropertyDependency Name="OnOffBand1" Action="Enable">

<Condition>

<Enumeration [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="bool">

<Value>1</Value>

</Enumeration>

</Condition>

</PropertyDependency>

</Dependencies>

</Property>

<Property Name="GainBand1" [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="Real32" SupportRTPCType="Exclusive" DataMeaning="Decibels" DisplayName="Band 1 Gain">

<UserInterface Step="0.5" Fine="0.1" Decimals="1" />

<DefaultValue>0</DefaultValue>

<AudioEnginePropertyID>1</AudioEnginePropertyID>

<Restrictions>

<ValueRestriction>

<Range [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="Real32">

<[Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)>-24</[Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)>

<[Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)>24</[Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)>

</Range>

</ValueRestriction>

</Restrictions>

<Dependencies>

<PropertyDependency Name="OnOffBand1" Action="Enable">

<Condition>

<Enumeration [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="bool">

<Value>1</Value>

</Enumeration>

</Condition>

</PropertyDependency>

</Dependencies>

</Property>

</Properties>

</EffectPlugin>

</PluginModule>

# XML 描述文件的各个部分

让我们详细地考察 XML 文件的各个部分。

## XML 描述文件头

让我们考察此 XML 文件头的组成部分并详细地讨论。

<?xml version="1.0" encoding="UTF-8"?>

<!-- Copyright (C) 2020 Audiokinetic Inc. -->

任何 XML 文件的第一行都是定义 XML 版本和编码方式。在本例中，XML 版本是 1.0，编码方式是 `UTF-8` 。任何 Wwise 插件描述文件的第一行应该总是与此完全一致。第二行是 XML 注释，在本例中是版权声明。您可以在 XML 文件的所需位置添加注释。

## PluginModule元素

<PluginModule>

...

</PluginModule>

本文档中的主要 XML 元素命名为 `PluginModule` ，包含此文件中定义的各种插件的全部信息。

## 插件类型元素

In the category of Audio plug-ins, there are four possible plug-in type elements:

- SourcePlugin
- EffectPlugin
- SinkPlugin
- MetadataPlugin

<EffectPlugin Name="Parametric EQ" CompanyID="0" PluginID="105" SupportsIsSendModeEffect="false">

...

</EffectPlugin>

The `EffectPlugin` element is the main element for the definition of a single effect plug-in, while `SourcePlugin`, `SinkPlugin` and `MetadataPlugin` are the element names for source plug-ins, sink plug-ins and metadata plug-ins, respectively.

|  |  |
| --- | --- |
|  | **备注:** 若在动态库中实现了多个插件，则 XML 文件将包含多个插件元素。 动态库并不限于某一类型的音频插件。 |

这些元素包含三个必需属性：

- `Name` (必需)：此字符串指定插件在 Wwise 中的实际显示名称。
- [CompanyID](plugin_xml.html#wwiseplugin_xml_id_specification) (必需)：此字符串必须为介于 0-4095 之间的正整数（参见 `wwiseplugin_xml_id_specification` 章节）。
- [PluginID](plugin_xml.html#wwiseplugin_xml_id_specification) (必需)：此字符串必须为介于 0-32767 之间的正整数。每个 PluginID 对于指定的 CompanyID 必须唯一。

可指定两个可选属性：

- `SupportsIsSendModeEffect` (可选)：（仅效果器插件）此布尔值通过在初始化期间查询 `AK::IAkEffectPluginContext::IsSendModeEffect()` 来指示插件是否支持发送模式。在 `IsSendModeEffect()` 返回 true 时，插件不应输出干声信号且应忽略干声电平属性。
- `EngineDllName` (可选)：此字符串值会覆盖游戏运行时所要加载的声音引擎动态库的名称（在默认情况下，名称与 XML 相同）。若指定了 `EngineDllName` ，请确保声音引擎静态库和动态库共用相同的名称。在商用游戏引擎（例如 Unity 和 Unreal 4）中，必须为您的插件提供 DLL/so 文件。这并不影响设计工具插件动态库的命名，其应与 XML 文件的名称严格对应。

## Company ID 和 Plug-in ID

Wwise 使用数字 ID 将插件模型定义与插件实现关联。 每个插件的 XML 描述和插件库的插件描述符中都会提供这些 ID。

`CompanyID` 是一个与所在公司对应的 ID。其设有三个取值范围：

- 0-63：**预留给 Audiokinetic 使用**，用户不可使用。
- 64-255：**无限制**，供内部使用。 此范围之内的 Company ID 不可用于外部分发。
- 256-4095：**有限制**，供商用插件使用。 Audiokinetic 将其分配给官方的第三方开发人员使用。如果您是官方的第三方开发人员之一，则可以使用 56-4095，而非 64-255 范围中的值。否则请勿使用这些值。

`PluginID` 是一个介于 0-32767 之间的唯一数字 ID，其与某一公司内部所用的插件对应。

比如，若您开发仅供内部使用的插件，则可在 64 ~ 255 之间任选一个 `CompanyID`，并在 0 ~ 32767 之间任选三个 PluginID。三个数字不需要连续。

CompanyID 和 PluginID 需要传给声音引擎插件声明宏 `AK_IMPLEMENT_PLUGIN_FACTORY` 。

|  |  |
| --- | --- |
|  | **注意:** 重要注意事项：  - *一定不要更改现有插件的* CompanyID 或 PluginID。否则使用该插件的工程将无法识别插件。CompanyID 和 PluginID 始终与各个插件实例保持一致，可用于在加载文件时重新创建所需插件的实例。 - 如果同一个 CompanyID 具有两个或两个以上的相同 PluginID，Wwise 将在启动时显示错误消息。如果发生这种情况，则需更改新插件的 ID。 - 若自研插件基于 Audiokinetic 提供的示例插件（参见 [示例插件](samplecode.html#samplecode_plugins) 章节），请不要忘记将 CompanyID 和 PluginID 改为适当的值。如果您有一个指定的官方 CompanyID，则使用它；如果没有，可以使用介于 64 与 255 之间的一个数。请确保该 CompanyID 的 PluginID 不重复。 |

有关 ID 的更多详细信息，请参阅 [Wwise 插件 ID](plugin_ids.html) 章节。

## PluginInfo 元素

<PlatformSupport>

<Platform Name="Windows">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

<Platform Name="Mac">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

<Platform Name="iOS">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

<Platform Name="XboxOne">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

<Platform Name="PS4">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

</PlatformSupport>

`PluginInfo/PlatformSupport` 部分定义了插件支持的平台。它能包含一个或更多 `Platform` 要素，其中每个都指定了每个平台上插件支持的不同特性。可指定以下功能：

- `CanBeInsertOnBusses` 确定效果器是否可用来控制和主导总线。通常这需要效果器支持环绕声音频配置。
- `CanBeInsertOnAuxBusses` 确定效果器是否可用来控制和主导辅助总线。通常这需要效果器支持环绕声音频配置。注意，如果已经设置 `CanBeInsertOnBusses，则效果器就已经可应用于辅助总线。`
- `CanBeInsertOnAudioObjects` 确定效果器是否可作为作用于音效的插入效果（必须支持单声道和立体声处理）。
- `CanBeRendered` 确定效果器是否可用于离线渲染。
- `CanSendMonitorData` 决定效果器是否可发送监控数据。有关详细信息，请参阅 `AK::Wwise::Plugin::Notifications::Monitor::NotifyMonitorData` 章节。
- `CanBeSourceOnSound` 决定源插件是否可为声音的音频源。
- `CanBeInsertEndOfPipeline` 决定效果器是否只能用在音频管线的末端，相当于顶层 Audio Bus 的最后一个效果器插槽（预留给 Audiokinetic 使用）。

在 Wwise 中，您的插件只可用于指定的平台。

另外，也可选择添加 Any 平台，而无需列出所有支持的平台。不过，这样的话会在 Wwise 中将此插件报告为适用于所有平台。若该插件没有提供匹配的运行时库，则用户只有在对应平台上设置端口时才会注意到。

<PlatformSupport>

<Platform Name="Any">

<CanBeInsertOnBusses>true</CanBeInsertOnBusses>

<CanBeInsertOnAudioObjects>true</CanBeInsertOnAudioObjects>

<CanBeRendered>true</CanBeRendered>

</Platform>

</PlatformSupport>

## Metadata PluginInfo Element

For a metadata plug-in, it is important to set the MenuPath="Metadata" attribute to the PluginInfo node as such:

<[PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823) MenuPath="Metadata">

<PlatformSupport>

<Platform Name="Any"></Platform>

</PlatformSupport>

</[PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823)>

## 属性要素

每个音频插件都可定义属性和引用。有关属性和引用的更多信息，请参照 [属性 XML 描述](plugin_xml_properties.html) 。

## 内部对象

`InnerTypes` 部分定义了插件内您可以实例化和使用的可能内部对象类型。可以在 `InnerTypes` 部分定义多个 `InnerType` 。每个 `InnerType` 必须具有唯一名称和插件 ID。`InnerType` 部分包含 `Properties` 部分，您可以使用定义插件属性的相同方式定义其属性。

当插件中需要多个对象实例时，Inner Types 非常实用。例如，当具有不定数量的 EQ Band 时，就可以为 EQ 插件定义 Inner Type `Band` 。每个 and 拥有相同的属性定义，但值不同。

<PluginModule>

<EffectPlugin ...>

<[PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823) ...>

...

</[PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823)>

<Properties>

...

</Properties>

<InnerTypes>

<InnerType Name="Band" CompanyID="X" PluginID="Y">

<Properties>

...

</Properties>

</InnerType>

</InnerTypes>

</EffectPlugin>

|  |  |
| --- | --- |
|  | **备注:** Inner Types 的属性不支持 RTPC。因此将不能使用 `SupportRTPCType` 属性和 `AudioEnginePropertyID` 元素。 |

|  |  |
| --- | --- |
|  | **备注:** 只有音频插件内支持 `InnerTypes` 。 |

若要在插件代码中操纵 Inner Type 实例 (Inner Object)，则需获取插件类中的 `AK::Wwise::Plugin::RequestObjectStore` ，并使用 `AK::Wwise::Plugin::ObjectStore` `m_objectStore` 成员，以此请求服务。 `AK::Wwise::Plugin::ObjectStore` 接口提供用于创建和删除 Inner Object 的函数（`AK::Wwise::Plugin::ObjectStore::CreatePropertySet` 和 `AK::Wwise::Plugin::ObjectStore::DeletePropertySet` ）。 Inner Object 的属性使用 PropertySet 接口操纵（参见 [Property Set](plugin_backend_model.html#wwiseplugin_propertyset) 章节）。

在创建对象后，须使用插入函数 (`AK::Wwise::Plugin::ObjectStore::InsertPropertySet`) 和移除函数 (`AK::Wwise::Plugin::ObjectStore::RemovePropertySet`) 将其存储到命名列表中。 例如，您可以创建类型为 `Band` 的内部对象，并将它存储在 `BandList` 中：

// Create a new band

[AK::Wwise::Plugin::PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html)\* pBand = m\_objectStore->CreatePropertySet("Band");

// 在“BandList”中插入新 band（位于末尾）

m\_objectStore->InsertPropertySet("BandList", (unsigned int)-1, pBand);

|  |  |
| --- | --- |
|  | **备注:** 每次只能将 Inner Object 存储到一个列表中。 |

工程 Work Unit 中数据的存留由 Wwise 自动处理。不过，用户须针对 SoundBank 和声音引擎数据实现 Inner Object 的序列化。须将 `AK::Wwise::Plugin::CustomData::GetPluginData` 和 `AK::Wwise::Plugin::AudioPlugin::GetBankParameters` 中的内部对象进行序列化。

在向对象库中添加内部对象时，Wwise 会自动创建相关的撤消机制， 您无需亲自实现撤消系统。但为了正常地支持撤消事件，您只需在收到框架通知时更新用户接口即可。

## Inner Object 通知

`AK::Wwise::Plugin::NotificationsObjectStore` 接口提供所要覆盖的处理程序，以便对与 Inner Object 相关的通知事件作出响应。这些主要是为了基于模型更改来更新自定义 GUI 元素。用户交互、撤消事件甚至 WAAPI 调用都可能会触发这类更改。

比如，在调用 `AK::Wwise::Plugin::ObjectStore::InsertPropertySet` 后，不要马上更新 UI。 而应等待您的插件上调用通知 `AK::Wwise::Plugin::NotificationsObjectStore::NotifyInnerObjectAddedRemoved。` 此通知告诉您对象已添加到列表或者已从列表中移除。

同样地，您也可以对 `AK::Wwise::Plugin::NotificationsObjectStore::NotifyInnerObjectPropertyChanged` 作出响应。在 Inner Object 中发生属性值更改时会调用此函数。

# 故障排除

如果您遇到任何问题，请参阅 [Wwise 源插件和效果器插件故障排除指南](plugin_troubleshooting.html) 。

[AK::SpeakerVolumes::Vector::Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)

AkForceInline void Max(AkReal32 \*in\_pVolumesDst, const AkReal32 \*in\_pVolumesSrc, AkUInt32 in\_uNumChannels)

**Definition:** [AkSpeakerVolumes.h:283](_ak_speaker_volumes_8h_source.html#l00283)

[AK.Wwise::Plugin::PluginInfo](namespace_a_k_1_1_wwise_1_1_plugin_a69141ebf4159597c1e76aad07862c823.html#a69141ebf4159597c1e76aad07862c823)

CPluginInfo PluginInfo

**Definition:** [PluginInstanceTypes.h:537](_plugin_instance_types_8h_source.html#l00537)

[AK::TempAlloc::Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)

Type

IDs of temporary memory pools used by the sound engine.

**Definition:** [AkTempAllocDefs.h:63](_ak_temp_alloc_defs_8h_source.html#l00062)

[AK.Wwise::Plugin::V2::PropertySet](class_a_k_1_1_wwise_1_1_plugin_1_1_v2_1_1_property_set.html)

Interface used to interact with property sets.

**Definition:** [HostPropertySet.h:92](_host_property_set_8h_source.html#l00091)

[AK::SpeakerVolumes::Vector::Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)

AkForceInline void Min(AkReal32 \*in\_pVolumesDst, const AkReal32 \*in\_pVolumesSrc, AkUInt32 in\_uNumChannels)

**Definition:** [AkSpeakerVolumes.h:291](_ak_speaker_volumes_8h_source.html#l00291)