# Migrating a pre-2021.1 Authoring Plug-in

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Migrating a pre-2021.1 Authoring Plug-in

In Wwise 2021.1, we introduced a new API for the Authoring part of plug-ins that included several changes. 本迁移指南将阐明这些改进并提供相关信息，来帮助您更新自己的插件代码以使用这一新的 API。

|  |  |
| --- | --- |
|  | **备注:** 新的设计工具插件 API 可在 `<Wwise>/SDK/include/AK/Wwise/Plugin` 下找到。 |

# 新功能

出于一些考虑，我们在 2021.1 中重写了插件 API。主要目的在于提供更好的默认设计，来将后端和前端实现之间涉及的一些内容分开，以此提升向后兼容能力并最大限度地降低创建插件时的要求。为此，我们采取了以下措施：

- 将插件的后端和前端作为单独的实体，并允许一个后端存在多个前端。在 Wwise 环境下，后端负责模型管理和 SoundBank 生成，前端负责实现图形用户界面 (GUI) 并将监控反馈提供给用户。这样的话，在命令行会话当中只需将插件的后端部分实例化即可。藉此，可进一步提升性能。倘若没有提供前端，在运行时会生成默认的前端。
- 依据一系列带有版本的细分接口对 `AK::Wwise::IAudioPlugin` 类进行拆分。插件现在可通过请求服务实例和实现特定接口来请求服务并将其提供给设计工具。由于减少了标准插件的依赖项且设计工具知晓所用接口版本，我们可以实现先前版本的适配器以在未来 Wwise 版本中提供相应的支持。倘若不再支持接口，系统会告知用户插件不受支持。如此一来，插件创建者便无需像之前一样为了支持新的 Wwise 版本而频繁更新插件。
- 设计工具插件 API 采用基于 C API 的架构，并不依赖特定于工具集和平台的结构（如 Windows SDK `VARIANT` ）。插件动态库暴露了简单的 C 结构，便于针对每个插件描述其组件并向实现提供指针。为方便起见，我们使用了 C++ API 再现原有 API 的功能，以此在编译时生成这些底层结构。
- 简化插件的注册并将其植入到插件容器中，同时利用这一结构包含库中所有插件的描述符。将插件类添加到此容器中，并在构建这一全局容器的过程中自动注册插件的声音引擎部分。只需使用少数几个宏来暴露设计工具插件（详见 [库插件容器](plugin_dll.html#wwiseplugin_container) 章节）。

除上述新增功能外，我们还对其中一些函数进行了修改以更加清楚地表明其用途。

|  |  |
| --- | --- |
|  | **备注:** 插件的声音引擎部分不采用上述设计，其仍沿用先前版本的实现方法。 |

# API 改进和移除

在 2021.1 中，我们从 API 里移除了一些被认为不再适用的方法。还有一些方法没有被移除，而是通过重新命名或更改参数进行了修改，确保更加便于理解或易于使用。

- `AK::Wwise::IAudioPlugin::SetPluginPropertySet()` ：已移除（弃用）
- `AK::Wwise::IAudioPlugin::SetPluginObjectStore()` ：已移除（弃用）
- `AK::Wwise::IAudioPlugin::SetPluginObjectMedia()` ：已移除（弃用）
- `AK::Wwise::IAudioPlugin::Destroy()` ：已移除（弃用）
- `AK::Wwise::IAudioPlugin::IsPlayable()` ：已移除（未使用）
- `AK::Wwise::IAudioPlugin::GetPluginMediaConverterInterface()` ：已移除。替换为独立的 `AK::Wwise::Plugin::MediaConverter` 接口。
- `AK::Wwise::IAudioPlugin::CopyInto()` -> `AK::Wwise::Plugin::CustomData::InitFromInstance()` ：已重命名，并更改参数。对相应逻辑实施了逆转以确保在相互排斥时与其他 `Init` 方法保持一致。
- `AK::Wwise::IAudioPlugin::Load()` -> `AK::Wwise::Plugin::CustomData::InitFromWorkunit()` ：已重命名
- `AK::Wwise::IAudioPlugin::Delete()` -> `AK::Wwise::Plugin::CustomData::OnDelete()` ：已重命名

此处未列出那些将非可选指针参数改为引用的方法。

# Changes to Plug-in Registration

In the original API, the Authoring part of the plug-in registered itself by calling `AK::Wwise::RegisterWwisePlugin`, which made the plug-in inject `g_pAKPluginList` into the loaded WwiseSoundEngine DLL.

In the new API, Wwise Authoring manages the registration process. Plug-in dynamic libraries now expose plug-ins as entries listed in a plug-in container that Wwise Authoring retrieves with the exported `GetPluginContainer${ContainerName}` function. Each plug-in entry in the container is an instance of `ak_wwise_plugin_info` that describes an Authoring plug-in and associates an Authoring plug-in class with a corresponding Sound Engine plug-in class.

As a result of this change, the Sound Engine plug-in part can no longer use the single `AkCreatePlugin` instantiation function. Instead, it must define one `AK::Registration` instance per plug-in, typically using the `AK_IMPLEMENT_PLUGIN_FACTORY` macro. A plug-in registration requires dedicated factory functions, so porting an `AkCreatePlugin` function requires it to be split into plug-in specific functions, for example `CreatePlugin1FX`, `CreatePlugin1Params`, `CreatePlugin2Source`, `CreatePlugin2Params`, and so on.

Refer to [库插件容器](plugin_dll.html#wwiseplugin_container) for instructions on how to set up the plug-in container in the Authoring plug-in part.

# 移植简单的插件

自研插件可能会使用设计工具插件 API 所提供的功能子集。以下各节分别阐述了与特定功能相关的改进。您可以根据插件所用 API 参考对应的章节。如需进一步了解设计工具插件 API 的高级功能，请参阅 [常见请求用例](plugin_21_1_migration.html#plugin_21_1_migration_porting_services) 章节。

|  |  |
| --- | --- |
|  | **备注:** 本节将 2021.1 版本的之前的 API 称为原有 API，将 2021.1 版本之后的 API 称为新的 API。 |

## AudioPlugin

在原有 API 中，`AK::Wwise::IAudioPlugin` 接口包含设计工具插件 API 的所有功能。 您可以针对各个方法的空实现直接创建 `AK::Wwise::DefaultAudioPluginImplementation` 子类，但类仍会定义所有这些未使用的方法。

在新的 API 中，设有类似的 `AK::Wwise::Plugin::AudioPlugin` 接口，但其只有 `AK::Wwise::Plugin::AudioPlugin::GetBankParameters()` 这一个方法。对于将典型属性写入 SoundBank 的简单插件，我们只需实现这一个接口即可。通过实现这一接口，还可表明实现类为后端类（相对前端类而言，详见 [实现前端](plugin_21_1_migration.html#plugin_21_1_migration_porting_backend_frontend) section 章节）。

具体来说，原有 API 和新的 API 之间在类方面存在如下区别：

**原有 API**

// MyAudioPlugin.h

class MyAudioPlugin: public AK::Wwise::DefaultAudioPluginImplementation

{

IPluginPropertySet\* m\_pPSet = nullptr;

public:

void Destroy() override { delete this; }

void SetPluginPropertySet(IPluginPropertySet\* in\_pPSet) override;

bool GetBankParameters(const GUID & in\_guidPlatform, AK::Wwise::IWriteData\* in\_pDataWriter) const override;

};

**新的 API**

// MyAudioPlugin.h

class MyAudioPlugin : public [AK::Wwise::Plugin::AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html)

{

public:

bool [GetBankParameters](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ae59a3955718ed3bbde0521da21cd8539.html#ae59a3955718ed3bbde0521da21cd8539)(

const GUID& in\_guidPlatform,

[AK::Wwise::Plugin::DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html)& in\_dataWriter

) const override;

};

我们可以看到，这里只剩一个要实现的方法：`GetBankParameters`。AK::Wwise::IAudioPlugin::Destroy() 函数也不再需要了，因为实例化和析构操作已完全交由插件 API 处理。我们可以使用标准的 C++ 析构函数来释放资源。

## 使用属性集

您可能注意到了，前面章节的代码示例中移除了 `AK::Wwise::IAudioPlugin::SetPluginPropertySet()` 函数。事实上，我们已不再需要该函数，因为 `AK::Wwise::Plugin::AudioPlugin` 接口可代为 *请求* 属性集组件。通过创建 `AK::Wwise::Plugin::RequestPropertySet` 子类，`AK::Wwise::Plugin::AudioPlugin` 接口可在插件描述中添加 `PropertySet` 组件要求，并在将插件实例化时由设计工具予以实现。同时还会添加成员变量 `m_propertySet`，并在实例化时将其自动设为 `PropertySet` 组件实例。如此一来，便无需手动创建此成员变量并实现与其对应的设置函数。

这样的话只需 `GetBankParameters` 便可实现简单的设计工具插件：

**原有 API**

// MyAudioPlugin.cpp

void MyAudioPlugin::SetPluginPropertySet(IPluginPropertySet\* in\_pPSet)

{

m\_pPSet = in\_pPSet;

}

bool MyAudioPlugin::GetBankParameters(const GUID & in\_guidPlatform, AK::Wwise::IWriteData\* in\_pDataWriter) const

{

CComVariant varProp; m\_pPSet->GetValue(in\_guidPlatform, L"Placeholder", varProp);

in\_pDataWriter->WriteReal32(varProp.fltVal);

return true;

}

**新的 API**

// MyAudioPlugin.cpp

bool MyAudioPlugin::GetBankParameters(const GUID& in\_guidPlatform, [AK::Wwise::Plugin::DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html)& in\_dataWriter) const

{

in\_dataWriter.[WriteReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a8d9b58e2ecba7f95721d4b89b7f9630f.html#a8d9b58e2ecba7f95721d4b89b7f9630f)(m\_propertySet.GetReal32(in\_guidPlatform, "Placeholder"));

return true;

}

一些关键区别：

- 将 `DataWriter` 参数改为了引用，因为其并非可选参数（不可为 NULL）。
- 通过继承的成员变量 `m_propertySet` 访问属性集。
- 传给 `AK::Wwise::Plugin::PropertySet::GetReal32()` 的属性名称字符串为 `const char*` 类型而非 `LPCWSTR` (const wchar\_t\*)。
- 在 `AK::Wwise::Plugin::PropertySet` 访问器的方法签名中以显式方式指定属性类型（此处为 Real32），以确保与 `AK::Wwise::Plugin::DataWriter` 保持一致。

所有这些改进可使此函数的实现更为简单、安全、便捷。

## 实现前端

通过实现 `AK::Wwise::Plugin::AudioPlugin` ，可以最简单的方式实现 SoundBank 生成。不过，要是只提供插件的这一部分，便不会显示任何自定义 GUI。在这种情况下，设计工具会默认生成类似于 Multi-Editor 视图的 GUI。

如前所述，`AudioPlugin` 类代表设计工具插件的后端：其可用在命令行上下文中（没有 GUI），并实现各种自定义数据或状态管理。若要显示自定义 GUI，则需创建新的类，并将其与同一插件标识符关联。该类与后端类分开进行实例化。

前端类通过创建前端接口子类实现。鉴于 GUI 自身的特性，必须针对不同的平台分别予以实现。为此，在将原来与前端相关的方法转到 `AK::Wwise::Plugin::GUIWindows` 接口后，可创建与之对应的子类来在 Windows 上提供自定义插件 GUI。

class MyFrontend : public [AK::Wwise::Plugin::GUIWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.html)

{

public:

bool [GetDialog](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a21b81136769b185c244ada93e6767f14.html#a21b81136769b185c244ada93e6767f14)(

[AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog,

uint32\_t& out\_uiDialogID,

[AK::Wwise::Plugin::PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html)\*& out\_pTable

) const;

bool [WindowProc](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a8ea33835cc026463f2f64b4327f89b17.html#a8ea33835cc026463f2f64b4327f89b17)(

[AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog,

HWND in\_hWnd,

uint32\_t in\_message,

WPARAM in\_wParam,

LPARAM in\_lParam,

LRESULT& out\_lResult

);

bool [Help](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a4923a0688cfc1bca88fcd33196c897a7.html#a4923a0688cfc1bca88fcd33196c897a7)(

HWND in\_hWnd,

[AK::Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d) in\_eDialog,

const char\* in\_szLanguageCode

);

};

|  |  |
| --- | --- |
|  | **备注:** 若想使用 MFC，同样也要先创建 `AK::Wwise::Plugin::PluginMFCWindows` 子类。藉此，来针对库初始化全局 `CWinApp`。 |

注意，已将 `eDialog` 和 `PopulateTableItem` 的副本添加到 `AK::Wwise::Plugin` 命名空间。 对于 `PopulateTableItem` ，还更新了相关的宏以反映其与前端接口的关系：

- `AK_BEGIN_POPULATE_TABLE()` -> `AK_WWISE_PLUGIN_GUI_WINDOWS_BEGIN_POPULATE_TABLE()`
- `AK_POP_ITEM()` -> `AK_WWISE_PLUGIN_GUI_WINDOWS_POP_ITEM()`
- `AK_END_POPULATE_TABLE()` -> [AK\_WWISE\_PLUGIN\_GUI\_WINDOWS\_END\_POPULATE\_TABLE()](_g_u_i_windows_8h_a286a575e82a4a1b002ff737b186d4c76.html#a286a575e82a4a1b002ff737b186d4c76 "Ends the declaration of a property-control bindings table.")

请参阅 [如何将常规控件绑定到属性](wwiseplugin_dialog_guide.html#wwiseplugin_dialog_guide_poptable) 了解更多详情。

在前端类中，*不得* 创建 `AK::Wwise::Plugin::AudioPlugin` 子类或实现任何与后端相关的逻辑。比如，实施影响 SoundBank 生成结果的属性值调整或操作。前端只负责直观地显示属性并监控数据，同时基于用户输入更新插件模型。

若后端无需对用户所提供的数值实施任何调整，则前端可直接通过创建 `AK::Wwise::Plugin::RequestPropertySet` 子类来请求 `PropertySet` 组件。倘若后端对属性实施任何数值调整（比如藉此实现动态属性范围），则应在后端予以实现。

若后端提供了一些前端所需的实现，则可通过创建 `AK::Wwise::Plugin::RequestLinkBackend` 子类来请求 `LinkBackend` 服务。藉此，可为前端类提供 `m_backend` 实例，并使用其来代表与之绑定的后端实例。

反过来，后端类也可通过创建 `AK::Wwise::Plugin::RequestLinkFrontend` 子类来请求 `LinkFrontend` 服务。对 `LinkFrontend` 来说，最大的区别在于一个后端可有多个前端。在这种情况下，所继承的 `m_frontend` 代表前端数组。您可以通过 `GetArray` 方法获取数组的大小，并使用 `ForEach` 函数列出与之对应的前端。

# 常见请求用例

`PropertySet` 组件请求由 `AK::Wwise::Plugin::AudioPlugin` 接口以隐式方式发送，其一般要用在 [AK::Wwise::Plugin::AudioPlugin::GetBankParameters()](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ae59a3955718ed3bbde0521da21cd8539.html#ae59a3955718ed3bbde0521da21cd8539 "Obtains parameters that will be written to a bank.") 中。其他组件和服务是可选的，并可通过创建 `AK::Wwise::Plugin::Request[...]` 子类来手动请求（参见 [请求组件和服务](plugin_dll.html#wwiseplugin_authoring_request) 章节）。在插件提供对设计工具的实现时，接口不加 `Request` 前缀。比如，对 `AK::Wwise::Plugin::Source` 、`AK::Wwise::Plugin::SinkDevices` 和 `AK::Wwise::Plugin::PropertyDisplayName` 来说便是如此。

下面列出了原有 API 中的常见用例以及在新的 API 中获取同样功能所需请求的对应服务。

## 监控数据

您可以通过 `NotifyMonitorData` 方法接收插件的声音引擎部分所发送的监控数据。 此方法已转到通知接口。您可以通过创建 `AK::Wwise::Plugin::Notifications::Monitor` 子类来实现该方法。

有关如何实现 `AK::Wwise::Plugin::Notifications::Monitor` 接口的详细信息，请参阅 [设计工具端的监控](wwiseplugin_frontend.html#wwiseplugin_dll_notifymonitordata) 章节。

## 插件授权

在原有 API 中，要想提供自定义句柄以供授权，必须实现 `AK::Wwise::IAudioPlugin::GetLicenseStatus` 。此函数已转到单独的接口：您可以通过创建 `AK::Wwise::Plugin::License` 子类来实现该方法。

有关如何实现 `AK::Wwise::Plugin::License` 的详细信息，请参阅 [管理授权](wwiseplugin_backend.html#wwiseplugin_dll_license) 章节。

## 对象媒体和媒体转换器

我们可以通过实现 `AK::Wwise::IAudioPlugin::SetPluginObjectMedia()` 和 `AK::Wwise::IAudioPlugin::GetPluginMediaConverterInterface()` ，来为要作为媒体进行处理的插件数据提供支持（这些媒体一般都是可在音频源转码过程中编码的音频文件）。这些以及媒体对象的管理现已统一整合到 `AK::Wwise::Plugin::ObjectMedia` 中。对象媒体方法直接在插件类内实现。媒体转换器（仍为可选）是一个要单独实现的接口：`AK::Wwise::Plugin::MediaConverter` 。

有关如何使用这些接口的详细信息，请参阅 [向音频插件中添加媒体](effectplugin_media.html) 章节。

## 自定义插件数据

所有不通过 PropertySet 或 ObjectMedia 组件管理的插件数据都已统一整合到通用接口 `AK::Wwise::Plugin::CustomData` 中。大部分方法都是一样的，只对 `CopyInto` 进行了修改，以便将逻辑逆转。

- `AK::Wwise::IAudioPlugin::GetPluginData()` -> `AK::Wwise::Plugin::CustomData::GetPluginData()`
- `AK::Wwise::IAudioPlugin::InitToDefault()` -> `AK::Wwise::Plugin::CustomData::InitToDefault()`
- `AK::Wwise::IAudioPlugin::CopyInto()` -> `AK::Wwise::Plugin::CustomData::InitFromInstance()`
- `AK::Wwise::IAudioPlugin::Load()` -> `AK::Wwise::Plugin::CustomData::InitFromWorkunit()`
- `AK::Wwise::IAudioPlugin::Save()` -> `AK::Wwise::Plugin::CustomData::Save()`
- `AK::Wwise::IAudioPlugin::Delete()` -> `AK::Wwise::Plugin::CustomData::OnDelete()`

这里的三个 `Init` 函数相互排斥：在初始化插件时，将依据加载情境调用其中的某个函数。

您可以通过创建 `AK::Wwise::Plugin::CustomData` 接口子类来实现这些方法。有关如何实现 `CustomData` 接口的详细信息，请参阅 [提供自定义数据](plugin_backend_model.html#wwiseplugin_complexproperty_provide) 章节。

|  |  |
| --- | --- |
|  | **备注:** 相较于通过 `AK::Wwise::IAudioPlugin::CopyInto()` 在原有 API 中初始化所提供的实例，`AK::Wwise::Plugin::CustomData::InitFromInstance()` 会通过自己的参数实现相应的实例。  在使用 Custom Data 将插件移植到 2021.1 设计工具插件 API 时，请务必应用此逻辑逆转。 |

[AK.Wwise::Plugin::eDialog](namespace_a_k_1_1_wwise_1_1_plugin_a5a9328b141630d1de228c92e81e9034d.html#a5a9328b141630d1de228c92e81e9034d)

eDialog

**Definition:** [PluginDef.h:138](_plugin_def_8h_source.html#l00137)

[AK.Wwise::Plugin::V1::DataWriter](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer.html)

Interface used to write data during sound bank generation.

**Definition:** [HostDataWriter.h:245](_host_data_writer_8h_source.html#l00244)

[AK.Wwise::Plugin::V1::GUIWindows::GetDialog](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a21b81136769b185c244ada93e6767f14.html#a21b81136769b185c244ada93e6767f14)

virtual bool GetDialog(eDialog in\_eDialog, uint32\_t &out\_uiDialogID, PopulateTableItem \*&out\_pTable) const

Retrieves the plug-in dialog parameters.

**Definition:** [GUIWindows.h:280](_g_u_i_windows_8h_source.html#l00280)

[AK.Wwise::Plugin::V1::DataWriter::WriteReal32](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_data_writer_a8d9b58e2ecba7f95721d4b89b7f9630f.html#a8d9b58e2ecba7f95721d4b89b7f9630f)

bool WriteReal32(float in\_value)

Writes a 32-bit, single-precision floating point value.

**Definition:** [HostDataWriter.h:427](_host_data_writer_8h_source.html#l00427)

[AK.Wwise::Plugin::PopulateTableItem](struct_a_k_1_1_wwise_1_1_plugin_1_1_populate_table_item.html)

**Definition:** [PluginDef.h:127](_plugin_def_8h_source.html#l00126)

[AK.Wwise::Plugin::V1::GUIWindows::Help](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a4923a0688cfc1bca88fcd33196c897a7.html#a4923a0688cfc1bca88fcd33196c897a7)

virtual bool Help(HWND in\_hWnd, eDialog in\_eDialog, const char \*in\_szLanguageCode) const

Called when the user clicks on the '?' icon.

**Definition:** [GUIWindows.h:323](_g_u_i_windows_8h_source.html#l00323)

[AK.Wwise::Plugin::V1::GUIWindows](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows.html)

Windows frontend plug-in API for Audio plug-ins.

**Definition:** [GUIWindows.h:200](_g_u_i_windows_8h_source.html#l00199)

[AK.Wwise::Plugin::V1::AudioPlugin](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin.html)

Wwise API for general Audio Plug-in's backend.

**Definition:** [AudioPlugin.h:133](_audio_plugin_8h_source.html#l00130)

[AK.Wwise::Plugin::V1::GUIWindows::WindowProc](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_g_u_i_windows_a8ea33835cc026463f2f64b4327f89b17.html#a8ea33835cc026463f2f64b4327f89b17)

virtual bool WindowProc(eDialog in\_eDialog, HWND in\_hWnd, uint32\_t in\_message, WPARAM in\_wParam, LPARAM in\_lParam, LRESULT &out\_lResult)

Window message handler for dialogs.

**Definition:** [GUIWindows.h:303](_g_u_i_windows_8h_source.html#l00303)

[AK.Wwise::Plugin::V1::AudioPlugin::GetBankParameters](class_a_k_1_1_wwise_1_1_plugin_1_1_v1_1_1_audio_plugin_ae59a3955718ed3bbde0521da21cd8539.html#ae59a3955718ed3bbde0521da21cd8539)

virtual bool GetBankParameters(const GUID &in\_guidPlatform, DataWriter &in\_dataWriter) const

Obtains parameters that will be written to a bank.

**Definition:** [AudioPlugin.h:228](_audio_plugin_8h_source.html#l00228)