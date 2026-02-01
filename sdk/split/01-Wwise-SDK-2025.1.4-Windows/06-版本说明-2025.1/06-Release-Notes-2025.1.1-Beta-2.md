# Release Notes 2025.1.1 Beta 2

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Release Notes 2025.1.1 Beta 2

The following sections list and describe the changes to Wwise between version 2025.1.0 and version 2025.1.1.  
此处提供了有关平台的特定信息：

[Windows 2025.1.1 Beta 2](windows_releasenotes_2025_1_1.html)

有关早期版本的信息，请参阅 [过往版本的发行说明](previousreleases.html) 章节。

- [New Features](whatsnew_2025_1_1.html#generic_feature_changes_2025_1_1)
- [API Changes](whatsnew_2025_1_1.html#generic_api_changes_2025_1_1)
- [Behavior Changes](whatsnew_2025_1_1.html#generic_behavior_changes_2025_1_1)
- [Miscellaneous Changes](whatsnew_2025_1_1.html#generic_misc_2025_1_1)
- [Bug Fixes](whatsnew_2025_1_1.html#generic_bugs_2025_1_1)
- [Fixes for Community-Reported Bugs](whatsnew_2025_1_1.html#generic_community_bugs_2025_1_1)
- [Documentation Improvements](whatsnew_2025_1_1.html#generic_documentation_improvements_2025_1_1)

# New Features

- **WG-25832** Added Mute and Solo buttons to the RTPC page.
- **WG-62401** Added option to create unit test infrastructure when creating a plug-in project.
- **WG-74681** Added new sound engine API `AK::SoundEngine::ResetBusConfig`. If you are using `AK::SoundEngine::SetBusConfig` in your game runtime, you can use the new API to revert the bus's channel config back to the value initially set when loading SoundBanks.
- **WG-75373** Increased the number of available bands for the Parametric EQ Effect from 3 to 8. Also added the ability to specify slopes for the Low Pass Filter and High Pass Filter, which are performed by running the filters multiple times in succession.
- **WG-75635** Added `SetOutputVolume`, `SetPanningRule`, and `SetSpeakerAngles` commands to Command Buffer API.
- **WG-76533** Added `SetEffect` and `SetBusConfig` commands to Command Buffer API.
- **WG-77247** The waveform column in the Media Pool now displays the waveform of multi-channel sounds as a mixdown.
- **WG-77838** Properties in the Reflect editor are now organized in groups, and there is a new Favorites category, similar to the Property Editor.
- **WG-77843** Added **Auto-Play on Selection** option to the Transport in Media Pool.
- **WG-77999** (Acoustics) When using the new automatic clustering feature, emitters are now clustered according to the room they reside in.
- **WG-78079** Added buttons to the Media Pool Databases tab to create databases and virtual folders.
- **WG-78508** Creating a new filter in the Media Pool now automatically displays the Filters page.

# API Changes

- **WG-72207** The DEFINEDUMMYASSERTHOOK macro has been deprecated and should be replaced by DEFINE\_PLUGIN\_ASSERT\_HOOK. By doing so, the AKASSERT macro in plug-ins will now call the sound engine assert handler.
- **WG-73894** Function definitions for managing `AkThread` and `AkThreadProperties` have been moved from inline functions in `AkPlatformFuncs.h` to the `AkSoundEngine` library. Plug-ins and other systems accessing the sound engine via dynamic linkage should now use the new `IAkPluginServicePlatformFuncs` from the `IAkGlobalPluginContext` to access this functionality.
- **WG-78949** Renamed the SDK function `AK::SoundEngine::SetActorMixerEffect` to `AK::SoundEngine::SetContainerEffect`.

# Behavior Changes

- **WG-78975** Double-clicking a file in the Media Pool no longer imports the file.
- **WG-79120** Changed the options in the Strata collection confirmation dialog.

# Miscellaneous Changes

- **WG-78751** (wp.py) The `bundle.json` format for Wwise Authoring plug-in packages now declares a dependency on triplets matching the Wwise installation packages. The `AuthoringDebug` package id has been replaced by triplets containing Debug, while `Authoring` remains in use by generic packages such as `Documentation`.
- **WG-78839** Increased the luminosity of disabled elements in the Property Editor.
- **WG-79095** The Sidechain Input meter on the Compressor and Expander Effects is now inactive when no Sidechain Mix is selected.

# Bug Fixes

- **WG-50389** Fixed: Cannot change the column size of the Game Object 3D Viewer property pane.
- **WG-57699** Fixed: No curve is shown in the Attenuation Editor if a curve is set to **Use Project Obstruction**, **Use Project Occlusion**, **Use Project Diffraction**, or **Use Project Transmission**.
- **WG-77565** Fixed: Path selection color only works in dark theme.
- **WG-77567** Fixed: Selection Properties pane in the Game Object 3D Viewer is missing tooltips and includes some properties that aren't useful while lacking properties that would be helpful.
- **WG-77662** Fixed: In the Game Object 3D Viewer, clicking the Display Options button opens the obsolete Game Object 3D Viewer Options dialog.
- **WG-77664** Fixed: Option names in the Game Object 3D Viewer toolbar are confusing.
- **WG-77924** Fixed positive DSF values not being reported in the voice inspector.
- **WG-78101** Fixed: In the Game Object 3D Viewer, can't select a game object from the game object list.
- **WG-78108** Fixed: The Media Pool view is unresponsive during search index maintenance.
- **WG-78122** Fixed: An Attenuation ShareSet used at the project level is not easily visualized from the Attenuation Editor.
- **WG-78322** Fixed: Field names in Media Pool filters are often truncated by an ellipsis.
- **WG-78364** Fixed: The **Render** check box for an Effect is sometimes wrongly enabled or disabled when using Effects that cannot be rendered, such as the Meter Effect.
- **WG-78535** 已修复：复制粘贴的对象数受限。
- **WG-78553** Fixed: (WAQL) Accessor "definedStates" does not provide which state it comes from.
- **WG-78765** Fixed: In the Media Pool, the left splitter doesn't fully collapse, and the bottom splitter collapses too much.
- **WG-78767** Fixed: Pressing the DEL key after selecting an object in the Property Editor doesn't delete the object.
- **WG-78825** Fixed: The Category buttons in the Property Editor do not have keyboard focus when clicked.
- **WG-78852** Fixed: Pinned Game Objects in the Game Object List of the Game Object 3D Viewer disappear after using the Game Object Filter.
- **WG-78855** Fixed: In the Game Object 3D Viewer, the parent row of the Game Object List can be filtered out.
- **WG-78857** Fixed: Category name that shows and hides text should be renamed Labels.
- **WG-78859** Fixed: Wrong or missing tooltips in Game Object 3D Viewer toolbar.
- **WG-78873** Fixed: Importing from Nuendo creates a sound object with no source and a missing audio file.
- **WG-78875** Fixed: The menu item **Edit in Nuendo** does nothing.
- **WG-78934** Fixed: Object visibility in the Game Object 3D Viewer doesn't persist when the object is unregistered.
- **WG-78946** 已修复：在导入或播放不符合制作规范的特定 ADM 文件时发生崩溃。
- **WG-79016** Fixed: It's possible to create Media Pool databases with invalid characters in their name.
- **WG-79022** Fixed: Reverb Zone Transition Region not visible in Game Object 3D Viewer until **Show Reverb Zone Transition Region** option is toggled.
- **WG-79043** Fixed: Adding an Effect to an object can cause a mismatch between the Effect Editor's content and the selected tab.
- **WG-79045** Fixed: (Spatial Audio) Selecting virtual positions does not automatically select the associated reflection and diffraction paths.
- **WG-79076** Fixed: Multi Playlist Container's Grid Frequency not displayed properly.
- **WG-79084** 已修复：在迁移由 Wwise 2023.1.0 以上版本创建的工程时可能会发生崩溃。
- **WG-79090** Fixed: (Spatial Audio) Objects cannot be selected when a cluster is drawn on top of them.
- **WG-79112** Fixed: Properties with exclusive RTPCs are prevented from editing dependent properties.
- **WG-79145** Fixed: Selection properties for virtual position and room objects in the Game Object 3D Viewer are the same.
- **WG-79198** Fixed: Show Game Object Voices and Show Portal Info buttons are the wrong color in dark theme.
- **WG-79219** 已修复：SoundBank 生成日志中报告的 Source Control 启用状态不正确。
- **WG-79223** Fixed: (Spatial Audio) Room distance calculations cause high CPU usage.
- **WG-79247** Fixed: Assert when opening Motion Source factory assets when using the Debug version of Wwise Authoring.
- **WG-79475** Fixed: All bands of the Parametric EQ Effect are enabled when an Effect is opened.

# Fixes for Community-Reported Bugs

- **WG-77558** 已修复：在使用无效的 Opus 转码声音文件生成 SoundBank 时可能会发生崩溃。
- **WG-78444** Fixed: Incorrect PerformanceCounter timestamps in stomp allocator metadata.
- **WG-78520** 已修复：在从物理上断开多个输出设备中的第一个时移除了错误的输出设备。
- **WG-78965** 已修复：在激活 ASAN (Address Sanitizer) 的情况下运行时显示编译警告。
- **WG-79036** 已修复：`WwiseAuthoringApi/cpp/SampleClient` WAAPI 示例编译失败，涉及 `std::chrono::high_resolution_timer` 相关错误。
- **WG-79134** Fixed: It's not possible to set up RTPCs for some properties of the Multiband Meter.

# Documentation Improvements

- **WG-62684** Added more information about the Game Object 3D Viewer selection properties.
- **WG-77809** Updated documentation around Room game object behavior.