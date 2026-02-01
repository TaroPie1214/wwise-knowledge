# Wwise 源插件和效果器插件故障排除指南

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise 源插件和效果器插件故障排除指南

**问题：启动时，Wwise 显示错误消息，指示两个插件具有相同的公司 ID 和插件 ID。**

- 每个插件必须具有唯一的公司 ID/插件 ID 组合。请参阅 [插件类型元素](plugin_xml.html#wwiseplugin_xml_effectplugin_sourceplugin_tags) 了解有关如何定义这些 ID 的详情。

**问题：用户在 Wwise 中无法使用我的插件。**

- 请检验您的插件描述文件中是否指定了正确的插件类型。对于源插件，此文件应使用 `SourcePlugin` 标记，而对于效果器插件则使用 `EffectPlugin` 。请参阅 [插件类型元素](plugin_xml.html#wwiseplugin_xml_effectplugin_sourceplugin_tags) 了解更多信息。在 XML 文件和引擎部分代码的 PluginRegistration 类中，必须匹配此类别。
- 请检验插件描述文件中是否指定了支持的相应平台。请参阅 [PluginInfo 元素](plugin_xml.html#wwiseplugin_xml_plugininfo_tag) 了解更多信息。
- 请检验插件 XML 文件中指定的公司 ID 和插件 ID 是否匹配 DLL 和 PluginRegistration 对象中的 `AkCreatePlugin()` 函数所用的相应 ID。请参阅 [声音引擎插件概述](soundengine_plugins.html#se_plugins_overview) 了解 PluginRegistration 的示例。有关更多详细信息，请参阅 [Wwise 插件 XML 描述文件](plugin_xml.html) 和 [编写音频插件的设计工具部分](effectpluginwwise.html) 章节。
- 若 Wwise 在启动时显示错误消息，指示两个插件具有相同的 ID，请参阅本页中的 [对应的问题](plugin_troubleshooting.html#plugin_troubleshooting_duplicate_ids) 章节。
- 请检验您的 XML 和 DLL 是否具有相同的名称
- 请检验 XML 和 DLL 文件是否位于 Plugins 文件夹中。

**问题：用户无法在 Mac 上使用我的插件，但在 PC 上可以。**

- 您的插件需为 64 位 DLL。在 Mac 中，Wwise 创作工具只能以 64 位格式运行。

**问题：我的插件用户界面中的一个控件显示为空或者被禁用。**

- 请检验在资源中，控件文本指定的属性名称（例如 *Prop=SineFrequency*）与插件描述文件中指定的名称（例如 *Property Name="SineFrequency"*）是否相同。请参阅 [“Prop”控件属性](wwiseplugin_dialog_guide.html#wwiseplugin_dialog_guide_controls_wwise_propname) 和 [属性要素](plugin_xml_properties.html#wwiseplugin_xml_properties_tag) 了解更多信息。
- 请检验控件类（例如 *Class=SuperRange*）是否适合属性的类型。请参阅 [“Class”控件属性](wwiseplugin_dialog_guide.html#wwiseplugin_dialog_guide_controls_wwise_class) 和 [属性要素](plugin_xml_properties.html#wwiseplugin_xml_properties_tag) 了解更多信息。

**问题：我的插件用户界面中的一个 Wwise 控件无法正常显示。**

- 请确保 `Class` 属性在对话框资源中设置正确。请参阅 [“Class”控件属性](wwiseplugin_dialog_guide.html#wwiseplugin_dialog_guide_controls_wwise_class) 了解更多详情。
- 请确保您的代码在对话框完整创建之前不会更改控件文本。在这种情况下，Wwise 将失去按需访问 `Class` 属性的权限。注意，您*不得更改绑定到属性控件上的文本。请参阅* [“Prop”控件属性](wwiseplugin_dialog_guide.html#wwiseplugin_dialog_guide_controls_wwise_propname) 了解更多信息。
- 请参阅 [其他控件属性](wwiseplugin_dialog_guide.html#wwiseplugin_dialog_guide_controls_wwise_attributes) 并验证各种控件属性设置正确。
- 请参阅 [如何向对话框中添加常规控件](wwiseplugin_dialog_guide.html#wwiseplugin_dialog_guide_controls_regular) 和 [如何向对话框中添加 Wwise 属性控件](wwiseplugin_dialog_guide.html#wwiseplugin_dialog_guide_controls_wwise) 了解有关插件对话框中可用的两类控件的更多信息。

**问题：我的插件无法识别 UI 中的属性变化。**

- 请确认插件定义文件中指定的 `AudioEnginePropertyID` 是否在 0-32767 范围之内（对于 wcustomproperties 文件，该范围为 0-150）请参阅 [属性要素](plugin_xml_properties.html#wwiseplugin_xml_properties_tag) 了解有关 `AudioEnginePropertyID` 标记的更多信息。
- 请检验插件定义文件中指定的 `AudioEnginePropertyID` 与您在 AK::IAkEffectParam::SetParam() 的实现中使用的 ID 是否匹配。 请参阅 [属性要素](plugin_xml_properties.html#wwiseplugin_xml_properties_tag) 了解有关 `AudioEnginePropertyID` 标记的更多信息，并请参阅 [AK::IAkPluginParam::SetParam()](soundengine_plugins.html#iakeffectparam_setparam) 了解有关实现 AK::IAkEffectParam::SetParam() 的详情。

**问题：我的插件在 Wwise 中能正常运行，但在游戏中无法运行。**

这存在两种可能性：

- 如果游戏静态地链接效果器，则请确保您链接了插件库，并在 CPP 文件之一中包含相应的工厂头文件。
- 如果游戏使用的是动态库（DLL、SO、PRX 等），请确保将您的效果器 DLL 复制到可执行文件所在的同一文件夹中。如果它们不在同一文件夹中，则应设置 [AkInitSettings::szPluginDLLPath](struct_ak_init_settings_a381f6978151d3e205f3b493523ed3b57.html#a381f6978151d3e205f3b493523ed3b57 "When using DLLs for plugins, specify their path. Leave NULL if DLLs are in the same folder as the gam...") 来添加 DLL 搜索路径。

**问题：我可以在工程中添加插件，但在 Wwise 中播放声音时无法听到应用插件后的效果。**

- 您可以在播放应用了插件的声音之前单击 Start Capture 来排查此问题的原因。假如 Capture Log（捕获日志）中显示 Plugin not registered（未注册插件），则可通过在设计工具端 DLL 代码的 cpp 文件中添加 [AK\_STATIC\_LINK\_PLUGIN(YourPlugin)](_i_ak_plugin_8h_a8e9fc150137c878499f2200e7e27a256.html#a8e9fc150137c878499f2200e7e27a256) 来解决此问题。

**Problem: My plug-in does not display debugging and/or diagnostic information.**

- To send debug or diagnostic information to Wwise Authoring, you can use `AK::IAkPluginContextBase::PostMonitorMessage()`, which is a method that can be called from the `AK::IAkEffectPluginContext` instance passed as an argument to your plug-in's `AK::IAkSourcePlugin::Init()` or `AK::IAkEffectPlugin::Init()` function.
- To output debugging information to the debugger (Visual Studio), you can use `AKPLATFORM::OutputDebugMsg()` or `AKPLATFORM::OutputDebugMsgV()`, found in AkPlatformFuncs.h.

**问题：我的插件在 Unity 中不能运行。**

以下是在 Unity 中验证新插件的几点注意事项。

- Wwise 加载到 Unity 中的插件必须复制到 \Assets\Wwise\Deployment\Plugins\[Platform]\DSP。通常这是 Release 版本。
- 插件必须是 Windows\x86、Windows\x86\_64 和 Mac 版本，才能在 Unity Editor 中运行。
- 标准的 Unity 集成将从 PluginInfo.xml 中检测插件使用情况，该文件在生成 SoundBank 时创建。PluginInfo.xml 中的“DLL”标记直接来源于 XML 文件中的“EngineDllName”标记，用于描述 Wwise Authoring 文件夹中的插件，请确保您的 DLL 具有相同的名称。

请参阅 [插件静态注册](soundengine_plugins.html#register_effects) 了解更多详情。