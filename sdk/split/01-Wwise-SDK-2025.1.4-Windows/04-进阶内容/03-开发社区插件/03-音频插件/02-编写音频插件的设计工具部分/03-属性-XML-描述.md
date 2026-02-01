# 属性 XML 描述

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

属性 XML 描述

Wwise 的开放架构支持三种插件，它们分别是用于生成声音的源插件、用于增强声音的效果器插件和支持在 Wwise 中使用版本控制软件的版本控制插件。前两种插件使用了 XML 插件描述文件，可以让您快速更改包括插件默认属性值在内的一些设置，而无需重新编译代码。Wwise 插件 DLL 可以包含多个插件，相关 XML 文件中必须对每个插件进行描述。每个 Wwise 插件 DLL 的 XML 描述文件具有与 DLL 相同的名称，而扩展名可以不同。例如，如果您的 DLL 命名为“MyPlugin.dll”，那么插件描述文件必须命名为“MyPlugin.xml”。

Wwise 开放性架构也可以用于定义 Wwise 对象的自定义属性。就像定义插件一样，Wwise 属性也通过 XML 描述进行控制。请参阅 [定义自定义属性](defining_custom_properties.html) 了解更多信息。

# 属性要素

<Properties>

...

</Properties>

`Properties` 字段定义了您的插件的属性和引用。`Property` 和 `Reference` 要素在用户界面中和 XML 中的排序一样。

- 这些属性对应于插件用户界面中允许操纵的控件，例如滑块和复选框，以及声音引擎插件代码可用来执行运算的值。
- 引用对应一个字段，这个字段包含对 Wwise 对象的引用。比如，一个引用可能指向一个在工程中定义的 Game Parameter 对象。

`Property（属性）通常定义如下：`

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

引用通常定义如下：

<Reference Name="OutputGameParameter" DisplayName="Output Game Parameter">

<AudioEnginePropertyId>1</AudioEnginePropertyID>

<Restrictions>

<TypeEnumerationRestriction>

<[Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9) Name="GameParameter" />

</TypeEnumerationRestriction>

</Restrictions>

</Reference>

`Property` 和 `Reference` 要素可以包含几个属性：

- `Name [Property, Reference]` (type:string, mandatory)：这是在 Wwise 插件中用于标识属性的字符串 ID。它用在以下两个位置：
  - Binding of properties to controls：您必须在插件对话框资源中指定此名称（Prop=<Property Name>），来将控件绑定至此属性。
  - Persistence：这是出现在 Wwise Project 文件里 `Property` 要素中的名称，用于保存和该属性相关的数据。

    |  |  |
    | --- | --- |
    |  | **注意:** 切勿更改现有属性的名称。否则工程中使用您插件的用户将可能丢失对该属性设置的值、随机化器或 RTPC。 |
  - in\_szPropertyName parameter in:
    - `AK::Wwise::Plugin::Notifications::PropertySet::NotifyPropertyChanged()`
    - `AK::Wwise::Plugin::Notifications::ReferenceSet::NotifyReferenceChanged()`
    - `AK::Wwise::Plugin::PropertyDisplayName::DisplayNameForProp()`
    - `AK::Wwise::Plugin::PropertyDisplayName::DisplayNamesForPropValues()`

  |  |  |
  | --- | --- |
  |  | **备注:** `Property Name`（属性名）称不是显示在 UI 中的名称，但您应该取一个有意义的名称，因为用户在工程文件中可以看到它。显示在 UI 中的名称由 `DisplayName` 属性指定。 |

  |  |  |
  | --- | --- |
  |  | **备注:** 在定义自定义属性时，`Name` 属性必须以“Custom:”为前缀。请参阅 [定义自定义属性](defining_custom_properties.html) 了解更多信息。 |
- `DisplayName [Property, Reference]` (**type:** string, **default:** empty)：定义在 Wwise 中多处出现的 Property 的显示名称。此属性将取代 `AK::Wwise::Plugin::PropertyDisplayName::DisplayNameForProp` 函数。
- `DisplayGroup [Property, Reference]` (**type:** string, **default:** empty)：定义 Tree 中用于组织属性或引用的斜杠分隔路径。例：“Audio/HDR”
- `IsVisible [Property, Reference]` (**type:** boolean, **default:** true, optional)：默认值是 `true` 。如果使用默认设置，在普通编辑器中可以查看此属性。当属性和它的数值对用户无意义时，或者您不想让用户看见它或在普通编辑器（比如在 List View中）中改动它时，则要将 `IsVisible` 设置为 `false` 。
- `Type [Property]` (mandatory)：这是属性类型。Possible values are:

  - `bool:` Boolean
  - `int16:` 16-bit integer
  - `Uint16:` 16-bit unsigned integer
  - `int32:` 32-bit integer
  - `Uint32:` 32-bit unsigned integer
  - `int64:` 64-bit integer
  - `Uint64:` 64-bit unsigned integer
  - `Real32:` Single-precision float (32-bit)
  - `Real64:` Double-precision float (64-bit)
  - `string:` UTF-8, null-terminated character string

  Plug-ins write properties to SoundBanks using the `AK::Wwise::Plugin::DataWriter` service, which supports writing any of the types listed above. Strings are serialized as null-terminated UTF-8 c-strings. Bool values are serialized as 1-byte values, where 1 stands for true and 0 for false.   
  In the case of custom properties added to a Wwise project, the values supported in SoundBanks are restricted to:

  - `int32:` 32-bit integer
  - `Real32:` Single-precision float (32-bit)

  The bool type can still be used as custom properties, however values are interpreted as int32 where 1 stands for true and 0 for false. However, custom properties typed as Strings are not exported to SoundBanks because they cannot be represented numerically.
- `SupportLink [Property, Reference]` (**type:** boolean, **default:** false, optional)：定义 `Property` 或 `Reference` 是否支持 Link/Unlink 功能。
- `SupportStates [Property]` (**type:** boolean, **default:** true, optional)：定义 `Property` 是否支持 State 映射来控制其值。注意，只有属性同时将 `SupportRTPCType` 定义为 `Additive` 或 `Boolean` 才支持 State 映射。
- `SupportRTPCType [Property]` (**type:** string, **default:** undefined, optional)：若未指定，则属性不支持 RTPC。若指定，则可能值为：
  - `Additive：将把通过` RTPC 曲线计算得出的值加上对象的基础属性值以及同一属性的其他 RTPC。
  - `Multiplicative：将把通过` RTPC 曲线计算得出的值乘以对象的基础属性值以及同一属性的其他 RTPC。
  - `Exclusive：将使用通过` RTPC 曲线计算得出的值全权控制属性值，并完全忽略对话框内属性控件中设定的值（此时将禁用该控件，以此告知 Wwise 用户其不会对属性产生任何影响）。
  - `Boolean：应用等效逻辑运算以启用或禁用布尔值属性。在` RTPC 类型为 `Additive` 或 `Boolean` 时，此属性还会启用 State 映射来影响属性的值。
- `ForceRTPCCurveSegmentShape [Property]` (**type:** string, **default:** undefined, optional, used with `SupportRTPCType`)：限制可能在此属性上的 RTPC 曲线中使用的线段形状。如果不指定，那么用户可以自由地更改曲线中任何段落的形状。如果指定，可能值是：
  - `Constant` ：曲线中的所有片段将使用恒定的插值（两个相邻点之间，Y 值与最左边点的 Y 值相同）。当属性表示离散值（例如布尔型或枚举）时使用此值。
- `DataMeaning [Property]` (**type:** string, **default:** undefined, optional)：如果已定义，则指定该属性代表一些特殊种类的数据，比如分贝。

  可能值是：

  - `Decibels` ：此属性以分贝表示。在默认情况下，RTPC 曲线将使用分贝刻度，但用户可以在分贝刻度和线性刻度之间切换。分贝度量将影响点与点之间的插值方式。例如，假设您有 0 dB 和 -96.3 dB 两个点，当使用线性度量时，在两点连线的中点值将为 -48.15 dB，当使用分贝刻度时中点值将约为 -6 dB（相当于振幅的一半）。
  - `Frequency` ：此属性代表频率，单位：Hz。频率度量影响点与点之间的插值方式。例如，假设有 1000 Hz 和 4000 Hz 两个点（两个八度音阶以上），当使用线性刻度时，在两点连线的中点値将为 2500 Hz，而使用频率度量时中点值为 2000 Hz（高一个八度）。
- `AudioEnginePropertyID [Property, Reference]` (**type:** integer in the range 0-32767): If defined, this is passed as the `AkPluginParamID` parameter to `AK::IAkPluginParam::SetParam()`. Make sure that your AudioEnginePropertyIDs are kept in sync between your implementation of `AK::IAkPluginParam::SetParam()` and your plug-in description file. Note that in a wcustomproperties file, the value must be in the range 0-150. When this element is used on a Reference, the value that is sent to `AK::IAkPluginParam::SetParam()` is the ShortID of the referenced object.
- `Temporary [Property]` (**type:** boolean, default: false, optional): If set, prevents the property from being saved and persisted in the Wwise Project. 这对有些只打算在 Wwise 与声音引擎相连时使用的属性来说非常有用。

|  |  |
| --- | --- |
|  | **备注:** 如果您希望 Wwise 用户来设置插件产生的声音或效果，并且在游戏期间不发生改变，则不要让其支持 RTPC。 |

`DefaultValue` 要素为属性指定默认值。此默认值即为创建新实例时的初始值，也是用户按住 CTRL 键的同时单击属性控件时属性的复位值。此值必须匹配属性类型（由`Property` 要素中的 `Type` 属性指定）和属性的范围（见下文）。

|  |  |
| --- | --- |
|  | **技巧:** XML 文件可以通过文本或 XML 编辑器进行编辑。它们位于插件 DLL 所在的路径，该文件夹位于主 Wwise 安装路径下的“plugins”文件夹中。Wwise 用户可以编辑插件的 XML 文件来更改自定义插件属性的默认值，而无需重新编译插件。因而无需研发，就可以执行此更改。 |

# UserInterface

`UserInterface` 元素定义与用户界面行为和外观相关的属性。以下属性均为可选，在 `UserInterface` 元素上设置它们：

- `DisplayName` (**type:** string, **default:** empty)：（已弃用）规定属性的显示名称，此名称将在 Wwise 中的多个位置显示。该属性会被 `Property` 或 `Reference` 要素中定义的 DisplayName 属性替代。
- `Decimals` (**type:** integer, **default:** 0)：定义小数点后显示的位数。此值必须是非负整数。如果设为 0，则不会显示小数和小数点。
- `Step` (**type:** float, **default:** 1)：定义移动滑块时数值的变化量。此值可以是整数或小数，具体取决于控件所绑定的属性类型。
- `Fine` (**type:** float, **default:** 1)：定义在按住 SHIFT 键并移动滑块时数值的变化量。此值可以是整数或小数，具体取决于控件所绑定的属性类型。
- `SliderType` (**type:** integer, **default:** 0)：定义滑块范围内的数值的映射。

  - 0：线性（默认）
  - 1：伪对数，介于 -96.3 dB 到 0 dB 之间
  - 2：伪对数，介于 -96.3 dB 到 96.3 dB 之间
  - 4：伪对数，介于 20 Hz 到 20000 Hz 之间
  - 5：伪对数，介于 20 Hz 到 12000 Hz 之间
  - 6：伪对数，介于 -96.3 dB 到 12 dB 之间
  - 11：伪对数，介于 0.02 Hz 到 20000 Hz 之间
  - 12：伪对数，介于 0.02 Hz 到 20 Hz 之间
  - 15：伪对数，介于 -24 dB 到 24 dB 之间
  - 16：伪对数，介于 -96.3 dB 到 24 dB 之间
- `Mid` (**type:** float, **default:** 0)：被视为中间值，介于 [最小值，最大值]范围内。此值将影响滑块控件的绘制。
- `UIMin` (**type:** float, **default:** Range's Min)：定义使用滑块可以设置的最小值。如果此值大于使用`Min` 属性设置的值，则用户可通过输入一个小于此属性指定值的值来强制将它设为更小值，从而扩大控制范围。
- `UIMax` (**type:** float, **default:** Range's Max)：定义使用滑块可以设置的最大值。如果此值小于使用`Max` 属性指定的值，则用户可通过输入一个比此属性指定值更大的值来强制将它设为更大值，从而扩大控制范围。
- `AutoUpdate` (**type:** boolean, **default:** false)：定义在移动滑块时是否可以更新此值。如果频繁更新此值会导致音频性能出现故障问题，请将此属性设为 `false` 。
- `LRMixDisplay` (**type:** boolean, **default:** false)：定义此值是否以左右范围平衡的特殊样式显示。该值必须介于 -100 ~ +100 之间，并映射至 Left to Right 平衡/混音（其中 0 代表 Center）。
- `ControlClass` (**type:** string, **default:** empty)：定义要用于 List View 或 the Multi Editor 等视图中的属性的用户界面控件。可能值是：

  - ColorPicker：颜色选择器。
  - ReadOnlyText：该属性值在用户界面中为只读形式。
- `DropDown` (**type:** string, **default:** empty)：在结合使用数字枚举（如 int16 类型的 `Enumeration` ）时，可使用此元素来指定如何在菜单中显示 `Enumeration` 值。可能值是：

  - Menu：针对相应的 Enumeration 值显示快捷菜单而非下拉菜单。菜单的路径由 `Enumeration` 中 `Value` 的 `DisplayName` 定义。比如，值 /Bus Volume/Reset Bus Volume 的 `DisplayName` 会显示 Bus Volume 菜单和 Reset Bus Volume 子菜单。在单击后，将把属性值设为 14。
  - CurveIn：在值为 0 ~ 8 时，将针对以下函数显示相应的正斜率曲线：Logarithmic (Base 3)、Sine、Logarithmic (Base 1.41)、Inverted S-Curve、Linear、S-Curve、Exponential (Base 1.41)、Reciprocal Sine 和 Exponential (Base 3)。
  - CurveOut：在值为 0 ~ 8 时，将针对以下函数显示相应的负斜率曲线：Logarithmic (Base 3)、Sine、Logarithmic (Base 1.41)、Inverted S-Curve、Linear、S-Curve、Exponential (Base 1.41)、Reciprocal Sine 和 Exponential (Base 3)。

|  |  |
| --- | --- |
|  | **技巧:** 属性范围很大的情况下，`UIMin` 和 `UIMax` 旨在让控件滑块的初始范围变得更加便于使用。如果某个属性具有较大的理论范围，但用户一般使用较小的范围，则使用 `Min/Max 属性设置` *实际范围，并使用* `UIMin/UIMax 属性设置滑块的初始范围。` |

# 限制

Wwise XML 描述可以指定 [属性限制](plugin_xml_properties.html#wwiseplugin_xml_restrictions_properties) 和 [引用限制](plugin_xml_properties.html#wwiseplugin_xml_restrictions_references) 。

## 属性限制

也可以为属性的数据值设置以下 2 个限制中的一个。

在`Range` 限制（Restrictions/ValueRestriction/Range 部分）中，您可以定义数值属性的范围。

<Restrictions>

<ValueRestriction>

<Range [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="Real64">

<[Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)>0</[Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)>

<[Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)>100</[Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)>

</Range>

</ValueRestriction>

</Restrictions>

在 `Enumeration` 限制（Restrictions/ValueRestriction/Enumeration 部分）中，您可以定义可能值列表和每个值的显示名称。

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

`bool` 和 `string` 属性不需要范围。Wwise 中的多个位置（例如 RTPC Curve Editor）都将使用此值域来定义坐标图 Y 轴的范围。

**Plugin.xsd** XML Schema 文件正式描述了此文件的格式，该 XML Schema 文件位于主 Wwise 安装路径下的“/Authoring/Data/Schemas”文件夹中。

## 引用限制

引用可以任意选择由以下被引用对象的限制所组成的清单：

**TypeEnumerationRestriction：为引用定义有效的** Wwise 对象类型清单。

<Restrictions>

<TypeEnumerationRestriction>

<[Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9) Name="GameParameter" />

...

</TypeEnumerationRestriction>

</Restrictions>

Type Name can be: PropertyContainer, RandomSequenceContainer, SwitchContainer, BlendContainer, Sound, Bus, Event, SwitchGroup, Switch, State, GameParameter, MidiParameter, SoundBank, Effect, MusicSegment, MusicTrack, MusicTrackSequence, MusicPlaylistContainer, MusicSwitchContainer, Trigger, Attenuation, DialogueEvent, MotionBus, MotionFX, Conversion, AuxBus, ModulatorLfo, ModulatorEnvelope.

**CategoryEnumerationRestriction：为引用定义有效的** Wwise 对象类别清单。

<Restrictions>

<CategoryEnumerationRestriction>

<Category Name="AudioObjects" />

...

</CategoryEnumerationRestriction>

</Restrictions>

Category Name 可以是：Busses、AudioObjects、Events、Switches、States、SoundBanks、GameParameters、Effects、AudioDevices、Presets、SoundcasterSessions、MixingSessions、Queries、InteractiveMusic、Triggers、Attenuations、DynamicDialogue、Conversions、Modulators、ControlSurfaceSessions。

**PlayableRestriction：定义对象是否必须可播放。**

<Restrictions>

<PlayableRestriction />

</Restrictions>

**NotNullRestriction：定义对象是否不能为** null。

<Restrictions>

<NotNullRestriction />

</Restrictions>

# 相关性

属性或引用可以没有依赖，也可以有很多依赖。相关性可将属性链接在一起，从而可以根据一个属性的值来启用或禁用另一属性。

请注意目前只有以下情况下会用到相关性：

- Property Editor - All Properties 标签页
- Effects（而不是 sources）的 Default User Interface
- 列表视图
- Multi Editor（多项编辑器）
- 查询视图 -Reference 视图

如果您通过在 `AK::Wwise::Plugin::AudioPlugin::GetDialog()` 中提供对话来实现自己的用户界面，则依赖不会被使用。启用或禁用 States 必须在插件的用户界面中实现。

以下示例将相关性从“GainBand1”添加到“OnOffBand1”。当“OnOffBand1”设为“True”时，将启用“GainBand1”属性。

<Property Name="GainBand1" ...>

<...>

<Dependencies>

<PropertyDependency Name="OnOffBand1" Action="Enable">

<Condition>

<Enumeration [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="bool">

<Value>True</Value>

</Enumeration>

</Condition>

</PropertyDependency>

</Dependencies>

</Property>

`Condition` 元素可以包含 `Enumeration` 元素或 `Range` 元素。`PropertyDependency` 元素中指定的 `Action` 属性必须是“Enable”。它表明当条件匹配时将启用此属性。

`Enumeration` 条件：

<Enumeration [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="int32">

<Value>0</Value>

<Value>1</Value>

</Enumeration>

`Range` 条件：

<Range [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="Real32">

<[Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)>-24</[Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)>

<[Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)>24</[Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)>

</Range>

另外，还可为 `PropertyDependency` 设置 `Context` 属性，以此更改要评估 `Condition` 的对象。同时，可将 `Context` 属性设为 Parent 或 Self；若未明确指定，则默认设为 Self。

接着前面的例子，假如将 context 添加到 `PropertyDependency` ，那么在针对**当前对象的父对象**将 OnOffBand1 设为 True 时，将会启用 GainBand1 属性。

<Property Name="GainBand1" ...>

<...>

<Dependencies>

<PropertyDependency Name="OnOffBand1" Action="Enable" Context="Parent">

<Condition>

<Enumeration [Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)="bool">

<Value>True</Value>

</Enumeration>

</Condition>

</PropertyDependency>

</Dependencies>

</Property>

[AK::SpeakerVolumes::Vector::Max](namespace_a_k_1_1_speaker_volumes_1_1_vector_a5cf5edb6e0760f5bd0ef29d98c322d9c.html#a5cf5edb6e0760f5bd0ef29d98c322d9c)

AkForceInline void Max(AkReal32 \*in\_pVolumesDst, const AkReal32 \*in\_pVolumesSrc, AkUInt32 in\_uNumChannels)

**Definition:** [AkSpeakerVolumes.h:283](_ak_speaker_volumes_8h_source.html#l00283)

[AK::TempAlloc::Type](namespace_a_k_1_1_temp_alloc_a94c6067317869a80ec86af6994a0ebd9.html#a94c6067317869a80ec86af6994a0ebd9)

Type

IDs of temporary memory pools used by the sound engine.

**Definition:** [AkTempAllocDefs.h:63](_ak_temp_alloc_defs_8h_source.html#l00062)

[AK::SpeakerVolumes::Vector::Min](namespace_a_k_1_1_speaker_volumes_1_1_vector_a8661f38fe4c56e23ffd967dc427bcde2.html#a8661f38fe4c56e23ffd967dc427bcde2)

AkForceInline void Min(AkReal32 \*in\_pVolumesDst, const AkReal32 \*in\_pVolumesSrc, AkUInt32 in\_uNumChannels)

**Definition:** [AkSpeakerVolumes.h:291](_ak_speaker_volumes_8h_source.html#l00291)