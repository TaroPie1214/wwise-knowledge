# 创建音频设备 (Sink) 插件

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

创建音频设备 (Sink) 插件

# 音频设备插件接口实现

音频设备插件（Audio Device plug-in）是音频处理链的终端。自然音频设备是指操作系统原生支持的声音系统。倘若附加硬件或驱动程序允许，还可以有更多输出终端形式。Sink 插件的作用是将最终混音采样转码为兼容格式并传输至设备。

## 声音引擎组件

在声音引擎端编写音频设备插件的过程包括实现 `AK::IAkSinkPlugin` 接口。本节只介绍此接口专用的函数。请参阅 [创建声音引擎插件](soundengine_plugins.html) 了解与其他插件类型（AK::IAkPlugin 接口）共享的接口组件的信息。另请参阅与所述 AkSink 插件相关的示例代码（ [示例](samplecode.html) ）。

音频设备始终通过其所用插件 (Audio Device ShareSet) 和设备 ID 指定。此设备 ID 对 Wwise 声音引擎来说并无意义，只是为了方便插件实现类区分多个相同类型的设备。该 ID 由游戏通过 `AK::SoundEngine::Init` 和 `AK::SoundEngine::AddOutput` 中使用的 `AkOutputSettings::idDevice` 参数传递。比如，对于要访问 Windows 音频设备的音频设备插件，可能会识别出某台电脑上的多个 Windows 设备。

若所用设备无需与多个设备区分，则可忽略该参数。若需要区分，则还须支持“默认设备”概念（在 `idDevice` 参数为 `0` 时选择的设备）。插件参数决定在接收到 `0` 值时是选择第一个可用设备还是特定设备。

Sink 插件可以注册一个附加静态函数来实现对可用音频设备的枚举。此函数的作用是列出可能的设备，以便用户设计工具中选择，并允许通过调用 `AK::SoundEngine::GetDeviceList` 来在运行时枚举设备。此函数是可选的。若不使用该函数，则插件将在必要时初始化为默认输出。在必要时，需在插件参数创建函数之后提供该附加静态函数。如需进一步了解要为插件创建提供的其他静态函数，请参阅 [创建声音引擎插件](soundengine_plugins.html) 。

下面以虚构的 Sink 插件 MyPlugin 为例展示了如何实现设备枚举。注意，MyPlugin 命名空间中的函数和类皆为实际插件实现所对应的占位符。

`在` Wwise 调用插件设备枚举函数时，将采用所要列出的最大设备数以及 `AkDeviceDescription` 的预分配数组。设备名称的最大长度为 `AK_MAX_PATH` （256 个字符）。您必须修改计数 (`io_maxNumDevices`)，使其正确反映列出的设备描述数量。即便所提供的设备描述数组指针为 NULL，也要修改计数来反映所要填写的设备描述数量。这样调用方才能为 `out_deviceDescriptions` 分配相应数量的内存。

// ...

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) GetMyPluginDeviceList([AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)& io\_maxNumDevices, [AkDeviceDescription](struct_ak_device_description.html)\* out\_deviceDescriptions)

{

// For example, fetch the available devices

const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) deviceCount = MyPlugin::GetNumberOfDevices();

const MyPlugin::Device\* devices = MyPlugin::GetDevices();

// 处理设备计数请求：

// 若 out\_deviceDescriptions 为 NULL，则 io\_maxNumDevices 应设为设备计数

// 这样调用方才能确定要预留多少内存。

if (out\_deviceDescriptions == NULL)

{

io\_maxNumDevices = deviceCount;

return [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e);

}

// 否则，填写 out\_deviceDescriptions

// until all available devices are filled (i == deviceCount)

// or the end of the array is reached (i == io\_maxNumDevices)

int i = 0;

for (; i < deviceCount && i < io\_maxNumDevices; ++i)

{

[AKPLATFORM::SafeStrCpy](namespace_a_k_p_l_a_t_f_o_r_m_aebd4566f4b4cc51c94ab69c3272b5991.html#aebd4566f4b4cc51c94ab69c3272b5991)(out\_deviceDescriptions[i].deviceName, device[i]->deviceName, [AK\_MAX\_PATH](_platforms_2_windows_2_ak_types_8h_ac1096fa0921ee445f47e145c167eab4b.html#ac1096fa0921ee445f47e145c167eab4b));

out\_deviceDescriptions[i].[idDevice](struct_ak_device_description_a5e1be4d07a51040ccc6ff04a38e7d47c.html#a5e1be4d07a51040ccc6ff04a38e7d47c) = devices[i].idDevice;

out\_deviceDescriptions[i].[deviceStateMask](struct_ak_device_description_ac0acc1661266c664aae7d9fd983315eb.html#ac0acc1661266c664aae7d9fd983315eb) = devices[i].deviceStateMask;

out\_deviceDescriptions[i].[isDefaultDevice](struct_ak_device_description_aff286ff755788f1997fc4bf34846824f.html#aff286ff755788f1997fc4bf34846824f) = devices[i].isDefaultDevice;

}

// 设置数组中写入的设备数

io\_maxNumDevices = i;

return [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e);

}

// 静态初始化器对象将插件自动注册到声音引擎中。

[AK::PluginRegistration](class_a_k_1_1_plugin_registration.html) MyPluginRegistration([AkPluginTypeEffect](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4a2971cc4c818bf62c55175445d2be117d), AKCOMPANYID\_MYCOMPANY, EFFECTID\_MYPLUGIN, CreateMyPlugin, CreateMyPluginParams, GetMyPluginDeviceList);

|  |  |
| --- | --- |
|  | **备注:** 为了能够针对支持的所有平台实现设备枚举，并在运行时通过 `AK::SoundEngine::GetDeviceList` 调用相应的函数，此声音引擎实现替换了之前设计工具专用插件对应的 `AkGetSinkPluginDevices` 函数。 |

|  |  |
| --- | --- |
|  | **备注:** 此函数将针对所有平台进行编译。在处理特定于平台的设备枚举时，需使用相应的宏（如 `AK_WIN` 和 `AK_LINUX` ），并针对没有定义实现的平台返回 `AK_NotImplemented` 。 |

## 适用于音频设备插件的设计工具 DLL

Sink 插件跟其他插件一样需要对应的设计工具 DLL。有关插件通用 Wwise 设计工具组件的基本设置，请参阅“ [设计工具插件库格式](plugin_dll.html) ”。

|  |  |
| --- | --- |
|  | **备注:** `AkGetSinkPluginDevices` 现已弃用。有关如何实现设备枚举的信息，请参见上述 [声音引擎组件](soundengine_plugins_audiodevices.html#se_audiodevice_engine) 部分。 |

## 测试您的音频设备插件

在实现了插件的 Wwise 部件（ [编写音频插件的设计工具部分](effectpluginwwise.html) ）和声音引擎部件后，应该对您的新插件进行测试。以下是测试的步骤。

- 在您的 Wwise 工程中，根据新插件创建 Audio Device ShereSet（音频设备共享集）。为 ShareSet 指定名称，保证不重名。
- 生成 SoundBank。
- 确保已在游戏代码中注册插件。请参阅 [声音引擎插件概述](soundengine_plugins.html#se_plugins_overview) 。
- 在声音引擎初始化参数中指定要使用的音频设备ID。AkOutputSettings 中的 ID 为工程中 Audio Device ShareSet 名称的哈希值（由 `AK::SoundEngine::GetIDFromString` 给出）。

例如：

[AkInitSettings](struct_ak_init_settings.html) initSettings;

[AkPlatformInitSettings](struct_ak_platform_init_settings.html) platformInitSettings;

[AK::SoundEngine::GetDefaultInitSettings](namespace_a_k_1_1_sound_engine_a03381fc17e1b0ee16c2ab501c647ab9e.html#a03381fc17e1b0ee16c2ab501c647ab9e)( initSettings );

[AK::SoundEngine::GetDefaultPlatformInitSettings](namespace_a_k_1_1_sound_engine_aecdb9cd8f2d7f461ef1a58f5f5f5725d.html#aecdb9cd8f2d7f461ef1a58f5f5f5725d)( platformInitSettings );

initSettings.[settingsMainOutput](struct_ak_init_settings_a9c5254abf13a5c3bf60ddd27c48db4d7.html#a9c5254abf13a5c3bf60ddd27c48db4d7).[audioDeviceShareset](struct_ak_output_settings_af1ff3ac68f3fa137c847144117d01535.html#af1ff3ac68f3fa137c847144117d01535) = [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)("YourNewAudioDeviceSharesetNameHere");

[AK::SoundEngine::Init](namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a9a26da64092b97243844df77cbcdbf5f)( &initSettings, &platformInitSettings );

另外，也可结合 Audio Device 插件使用 `AK::SoundEngine::AddOutput。`

[AkOutputSettings](struct_ak_output_settings.html) outputSettings("YourNewAudioDeviceSharesetNameHere", 0 /\*Default device\*/)'

AK::SoundEngine::AddOutput(outputSettings);

您可以使用 `AK::SoungEngine::GetDeviceList` 来针对所用插件测试设备枚举。

const int maxNbDevices = 20;

[AkDeviceDescription](struct_ak_device_description.html) devices[maxNbDevices];

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) deviceCount = maxNbDevices;

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) res = [AK::SoundEngine::GetDeviceList](namespace_a_k_1_1_sound_engine_a3de19a0cdec459ebdc73fc1d0f8f276e.html#a3de19a0cdec459ebdc73fc1d0f8f276e)(

[AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)("YourNewAudioDeviceSharesetNameHere"),

deviceCount,

devices

);

有关更多信息，请参阅以下各节：

- [声音引擎插件概述](soundengine_plugins.html#se_plugins_overview)
- [编写音频插件的设计工具部分](effectpluginwwise.html)
- [示例](samplecode.html)

[AkInitSettings::settingsMainOutput](struct_ak_init_settings_a9c5254abf13a5c3bf60ddd27c48db4d7.html#a9c5254abf13a5c3bf60ddd27c48db4d7)

AkOutputSettings settingsMainOutput

Main output device settings.

**Definition:** [AkSoundEngine.h:208](_ak_sound_engine_8h_source.html#l00208)

[AK::SoundEngine::Init](namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a9a26da64092b97243844df77cbcdbf5f)

AKSOUNDENGINE\_API AKRESULT Init(AkInitSettings \*in\_pSettings, AkPlatformInitSettings \*in\_pPlatformSettings)

[AkPlatformInitSettings](struct_ak_platform_init_settings.html)

**Definition:** [AkWinSoundEngine.h:43](_ak_win_sound_engine_8h_source.html#l00042)

[AkDeviceDescription::isDefaultDevice](struct_ak_device_description_aff286ff755788f1997fc4bf34846824f.html#aff286ff755788f1997fc4bf34846824f)

bool isDefaultDevice

Identify default device. Always false when not supported.

**Definition:** [AkSoundEngineTypes.h:61](_ak_sound_engine_types_8h_source.html#l00061)

[AkOutputSettings](struct_ak_output_settings.html)

Platform-independent initialization settings of output devices.

**Definition:** [AkSoundEngineTypes.h:219](_ak_sound_engine_types_8h_source.html#l00218)

[AkDeviceDescription::deviceStateMask](struct_ak_device_description_ac0acc1661266c664aae7d9fd983315eb.html#ac0acc1661266c664aae7d9fd983315eb)

enum AkAudioDeviceState deviceStateMask

Bitmask used to filter the device based on their state.

**Definition:** [AkSoundEngineTypes.h:60](_ak_sound_engine_types_8h_source.html#l00059)

[AK::SoundEngine::GetDefaultInitSettings](namespace_a_k_1_1_sound_engine_a03381fc17e1b0ee16c2ab501c647ab9e.html#a03381fc17e1b0ee16c2ab501c647ab9e)

AKSOUNDENGINE\_API void GetDefaultInitSettings(AkInitSettings &out\_settings)

[AK::PluginRegistration](class_a_k_1_1_plugin_registration.html)

**Definition:** [IAkPlugin.h:1994](_i_ak_plugin_8h_source.html#l01993)

[AK\_MAX\_PATH](_platforms_2_windows_2_ak_types_8h_ac1096fa0921ee445f47e145c167eab4b.html#ac1096fa0921ee445f47e145c167eab4b)

#define AK\_MAX\_PATH

Maximum path length.

**Definition:** [AkTypes.h:140](_platforms_2_windows_2_ak_types_8h_source.html#l00140)

[AkPluginTypeEffect](_ak_enums_8h_af1a95e76b0e2a003e7edb2ad6f4043f4.html#af1a95e76b0e2a003e7edb2ad6f4043f4a2971cc4c818bf62c55175445d2be117d)

@ AkPluginTypeEffect

Effect plug-in: applies processing to audio data.

**Definition:** [AkEnums.h:285](_ak_enums_8h_source.html#l00285)

[AK::SoundEngine::GetDefaultPlatformInitSettings](namespace_a_k_1_1_sound_engine_aecdb9cd8f2d7f461ef1a58f5f5f5725d.html#aecdb9cd8f2d7f461ef1a58f5f5f5725d)

AKSOUNDENGINE\_API void GetDefaultPlatformInitSettings(AkPlatformInitSettings &out\_platformSettings)

[AKPLATFORM::SafeStrCpy](namespace_a_k_p_l_a_t_f_o_r_m_aebd4566f4b4cc51c94ab69c3272b5991.html#aebd4566f4b4cc51c94ab69c3272b5991)

void SafeStrCpy(wchar\_t \*in\_pDest, const wchar\_t \*in\_pSrc, size\_t in\_uDestMaxNumChars)

Safe unicode string copy.

**Definition:** [AkPlatformFuncs.h:251](_win32_2_ak_platform_funcs_8h_source.html#l00251)

[AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)

AKSOUNDENGINE\_API AkUInt32 GetIDFromString(const char \*in\_pszString)

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63)

AKRESULT

**Definition:** [AkEnums.h:32](_ak_enums_8h_source.html#l00031)

[AkDeviceDescription](struct_ak_device_description.html)

**Definition:** [AkSoundEngineTypes.h:57](_ak_sound_engine_types_8h_source.html#l00056)

[AkOutputSettings::audioDeviceShareset](struct_ak_output_settings_af1ff3ac68f3fa137c847144117d01535.html#af1ff3ac68f3fa137c847144117d01535)

AkUniqueID audioDeviceShareset

**Definition:** [AkSoundEngineTypes.h:241](_ak_sound_engine_types_8h_source.html#l00241)

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AkInitSettings](struct_ak_init_settings.html)

**Definition:** [AkSoundEngine.h:193](_ak_sound_engine_8h_source.html#l00192)

[AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e)

@ AK\_Success

The operation was successful.

**Definition:** [AkEnums.h:34](_ak_enums_8h_source.html#l00034)

[AK::SoundEngine::GetDeviceList](namespace_a_k_1_1_sound_engine_a3de19a0cdec459ebdc73fc1d0f8f276e.html#a3de19a0cdec459ebdc73fc1d0f8f276e)

AKSOUNDENGINE\_API AKRESULT GetDeviceList(AkUInt32 in\_ulCompanyID, AkUInt32 in\_ulPluginID, AkUInt32 &io\_maxNumDevices, AkDeviceDescription \*out\_deviceDescriptions)

[AkDeviceDescription::idDevice](struct_ak_device_description_a5e1be4d07a51040ccc6ff04a38e7d47c.html#a5e1be4d07a51040ccc6ff04a38e7d47c)

AkUInt32 idDevice

Device ID for Wwise. This is the same as what is returned from AK::GetDeviceID and AK::GetDeviceIDFro...

**Definition:** [AkSoundEngineTypes.h:58](_ak_sound_engine_types_8h_source.html#l00058)