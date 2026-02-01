# Wwise Authoring API 示例索引

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Authoring API 示例索引

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。

# 示例

[Adding a Blend Track assignment.](ak_wwise_core_blendcontainer_addassignment_example_adding_a_blend_track_assignment.html)   
Equivalent to performing a drag-and-drop operation in the Blend Tracks Editor.

[Adding a Blend Track to a Blend Container](ak_wwise_core_blendcontainer_addtrack_example_adding_a_blend_track_to_a_blend_container.html)   
Equivalent to clicking New Blend Track in the Blend Track Editor.

[将 Custom Cue 添加到现有 Music Segment](ak_wwise_core_object_create_example_adding_a_custom_cue_to_an_existing_music_segment.html)   
按照给定名称和时间（毫秒）在现有 Music Segment 内创建 Custom Cue。

[Adding a Marker to an Audio Source](ak_wwise_core_object_set_example_adding_a_marker_to_an_audio_source.html)   
In the "Markers" list of an audio source, appends a Marker using the given Time and Label properties.

[Adding a Metadata shareset to an existing Sound SFX](ak_wwise_core_object_create_example_adding_a_metadata_shareset_to_an_existing_sound_sfx.html)   
Creates a Metadata entry in the Metadata object list inside an existing Sound SFX. The Metadata is a shareset with the specified GUID.

[Adding a State Group to a Sound](ak_wwise_core_object_setstategroups_example_adding_a_state_group_to_a_sound.html)   
Adds a State Group to a Sound.

[Adding a message to the logs](ak_wwise_core_log_additem_example_adding_a_message_to_the_logs.html)   
Adds a message to the logs on channel 'general'.

[Adding a new files to source control.](ak_wwise_core_sourcecontrol_add_example_adding_a_new_files_to_source_control.html)   
Add two new audio files to the SFX directory and the source control.

[Adding a warning to the SoundBank Generation channel](ak_wwise_core_log_additem_example_adding_a_warning_to_the_soundbank_generation_channel.html)   
Adds a warning to the logs on channel 'soundbankGenerate'.

[Adding an RTPC with curve to an object](ak_wwise_core_object_set_example_adding_an_rtpc_with_curve_to_an_object.html)   
In an object's "RTPC" list, this function creates an RTPC on a property using the specified `ControlInput` and curve points. The `ControlInput` is the game parameter, Modulator, or MIDI object assigned to the x axis of the RTPC. If you use a game parameter, you are passing a reference, and therefore the game parameter that you want to link to `ControlInput` must be created before you pass it to the parameter.

[Adding an RTPC with curve to an object and creates a new Custom ControlInput](ak_wwise_core_object_set_example_adding_an_rtpc_with_curve_to_an_object_and_creates_a_new_custom_controlinput.html)   
在对象的 "RTPC" 列表中，使用给定 ControlInput 和曲线控制点在属性上创建 RTPC。

[将对象添加到 Inclusion 列表](ak_wwise_core_soundbank_setinclusions_example_adding_an_object_to_the_inclusion_list.html)   
将对象添加到 SoundBank 的 Inclusion 列表。未考虑 'media' 筛选器。

[将 Switch Container 的子对象指派给 State](ak_wwise_core_switchcontainer_addassignment_example_assigning_a_switch_container_s_child_to_a_state.html)   
相当于将 Switch Group 的子对象拖到 Assigned Objects 视图中所列的 State。

[开始某个 Undo Group](ak_wwise_core_undo_begingroup_example_beginning_an_undo_group.html)   
开始某个 Undo Group。

[将当前所连 Wwise 调到前台](ak_wwise_ui_bringtoforeground_example_bringing_the_currently_connected_wwise_to_foreground.html)   
将当前所连 Wwise 调到前台。

[取消某个 Undo Group](ak_wwise_core_undo_cancelgroup_example_canceling_an_undo_group.html)   
取消某个 Undo Group。

[Changing the playlist of a Random Sequence object](ak_wwise_core_object_set_example_changing_the_playlist_of_a_random_sequence_object.html)   
The playlist added to the Random Sequence object is composed of the '1st number' object followed by two times '2nd Number'.

[检查是否启用了某项属性](ak_wwise_core_object_ispropertyenabled_example_checking_if_a_property_is_enabled.html)   
检查是否启用了某项属性。

[Clearing an attenuation reference](ak_wwise_core_object_set_example_clearing_an_attenuation_reference.html)   
Clears the attenuation reference on the specified object by setting a null GUID.

[Clearing the general log.](ak_wwise_core_log_clear_example_clearing_the_general_log.html)   
Clears the entire log on the channel 'general'.

[清理 Inclusion 列表](ak_wwise_core_soundbank_setinclusions_example_clearing_the_inclusion_list.html)   
通过 'replace' 操作和空白 'inclusions' 列表清理 SoundBank 的 Inclusion 列表。

[Closing a view](ak_wwise_ui_layout_closeview_example_closing_a_view.html)   
Closes view using its GUID.

[Closing the current project](ak_wwise_console_project_close_example_closing_the_current_project.html)   
关闭当前工程。

[关闭当前工程](ak_wwise_ui_project_close_example_closing_the_current_project.html)   
关闭当前工程。

[Combining multiple filters with a custom return in the Media Pool](ak_wwise_core_mediapool_get_example_combining_multiple_filters_with_a_custom_return_in_the_media_pool.html)   
Searches the 'Project Originals' database for stereo files with 'wind' in the name, and returns their path and channel configuration.

[Commiting a file modification in the source control.](ak_wwise_core_sourcecontrol_commit_example_commiting_a_file_modification_in_the_source_control.html)   
The modification and the message on it is sent to the source file.

[连接到《Cube》](ak_wwise_core_remote_connect_example_connecting_to_cube.html)   
在同一电脑上连接到《Cube》游戏。

[连接到性能分析会话](ak_wwise_core_remote_connect_example_connecting_to_a_profile.html)   
通过给定完整路径连接到所保存性能分析会话（.prof 文件）。

[针对某个平台对 External Source 进行转码](ak_wwise_core_soundbank_convertexternalsources_example_convert_external_sources_for_a_platform.html)   
在默认输出路径针对 Linux 对 External Source 进行转码。

[针对多个平台和输出路径对 External Source 进行转码](ak_wwise_core_soundbank_convertexternalsources_example_convert_external_sources_for_several_platforms_and_output_paths.html)   
按照给定的各个 wsources 文件在可选和默认输出路径针对多个平台对 External Source 进行转码。

[Convert a WwiseObject](ak_wwise_core_audio_convert_example_convert_a_wwiseobject.html)   
Converts the audio file of the specified object onto specified platforms and languages.

[将对象复制到给定父对象](ak_wwise_core_object_copy_example_copying_an_object_to_the_given_parent.html)   
复制由 "object" ID 指定的对象，并将副本作为 "parent" 的子对象。若 "parent" 已经包含同名子对象，则对相应对象进行重命名。

[Creating a Media Pool Database](ak_wwise_core_object_set_example_creating_a_media_pool_database.html)   
Creates a Media Pool Database with the specified name and path to an audio file directory. The GUID for the `'User` Databases' folder is always `'{8452BD49-9264-4A56-A3BB-047FA7F119BE}'`.

[Creating a Music Playlist Container with segment and playlist](ak_wwise_core_object_set_example_creating_a_music_playlist_container_with_segment_and_playlist.html)   
Creates a new Music Playlist Container, import a wav file in a Music Segment and create a playlist.

[为 Sound 对象创建 Play Event](ak_wwise_core_object_create_example_creating_a_play_event_on_a_sound.html)   
在 'WAAPI' 虚文件夹下创建 'Play\_SFX' Event，并为 SFX 声音对象添加 Play 动作。See [Action](wwiseobject_action.html) for the list of possible event properties and action types.

[Creating a Property Container](ak_wwise_core_object_create_example_creating_a_property_container.html)   
在 Default Work Unit 下创建新的 'Guns' Virtual Folder。若已存在同名的文件夹，则自动命名为唯一名称。

[创建 Random Container 并添加两个 Sound 对象](ak_wwise_core_object_create_example_creating_a_random_container_with_two_sound_objects.html)   
在给定父对象下创建 'Boom' Random Container，并在其中添加 'A' 和 'B' Sound 对象。

[创建 Sound 对象](ak_wwise_core_object_create_example_creating_a_sound_object.html)   
在给定父对象下创建新的 'Boom' Sound 对象。

[Creating a Sound with Source Plug-in](ak_wwise_core_object_set_example_creating_a_sound_with_source_plug_in.html)   
Creates a new Sound with a Synth One Source Plug-in.

[创建 Virtual Folder](ak_wwise_core_object_create_example_creating_a_virtual_folder.html)   
在 Default Work Unit 下创建新的 'Guns' Virtual Folder。若已存在同名的文件夹，则自动命名为唯一名称。

[Creating a music hierarchy](ak_wwise_core_object_set_example_creating_a_music_hierarchy.html)   
In one operation, create a Music Switch Container, a Music Playlist Container, a Music Segment, and a Music Track with one imported WAV file.

[Creating a new SFX with no file and setting a value to a property](ak_wwise_core_audio_import_example_creating_a_new_sfx_with_no_file_and_setting_a_value_to_a_property.html)   
在 "objectPath" 下创建新的 SFX，将其音量属性设为 1。

[Creating a new project](ak_wwise_console_project_create_example_creating_a_new_project.html)   
Creates the .wproj project specified by path.

[Creating a new project](ak_wwise_ui_project_create_example_creating_a_new_project.html)   
Creates the .wproj project specified by path.

[Creating a new project for Android platform](ak_wwise_ui_project_create_example_creating_a_new_project_for_android_platform.html)   
Creates the .wproj project specified by path.

[Creating a new project for Windows and Android platforms](ak_wwise_console_project_create_example_creating_a_new_project_for_windows_and_android_platforms.html)   
Creates the .wproj project specified by path.

[创建走带对象](ak_wwise_core_transport_create_example_creating_a_transport_object.html)   
针对给定 Wwise 对象创建走带对象。

[Creating multiple child hierarchies of objects in batch](ak_wwise_core_object_set_example_creating_multiple_child_hierarchies_of_objects_in_batch.html)   
在多个对象下一并创建子对象层级结构：#1. 在给定父对象下创建新的 'Boom' Sound 对象。#2. 在 Default Work Unit 下创建新的 'Guns' Virtual Folder。若已存在同名的文件夹，则自动命名为唯一名称。#3. 在 'WAAPI' 虚文件夹下创建 'Play\_SFX' Event，并为 SFX 声音对象添加 Play 动作。#4. 在给定父对象下创建 'Boom' Random Container，并在其中添加 'A' 和 'B' Sound 对象。#5. 按照给定名称和时间（毫秒）在现有 Music Segment 内创建 Custom Cue。参见有关 [ak.wwise.core.object.create](ak_wwise_core_object_create.html) 的示例来对比两种架构。

[Creating new Source Plug-ins for a Voice](ak_wwise_core_object_set_example_creating_new_source_plug_ins_for_a_voice.html)   
针对 "English(US)" 和 "French" 语言为使用 Silence 和 SoundSeed Grain 插件的 Voice 创建两个新的 Source 对象。

[Customizing the return values in the Media Pool](ak_wwise_core_mediapool_get_example_customizing_the_return_values_in_the_media_pool.html)   
Searches for files and returns only their filename, duration, and sample rate.

[定义对象的 Attenuation 曲线](ak_wwise_core_object_setattenuationcurve_example_defining_an_attenuation_curve_of_an_object.html)   
通过设置一系列 "points" 来为 "object" 定义 "curveType" 类型的 Attenuation 曲线。

[Deleting a new file to source control.](ak_wwise_core_sourcecontrol_delete_example_deleting_a_new_file_to_source_control.html)   
Remove an existing file to the SFX directory and the source control.

[按照 GUID 删除对象](ak_wwise_core_object_delete_example_deleting_an_object_by_guid.html)   
删除由 GUID 指定的对象。

[按照路径删除对象](ak_wwise_core_object_delete_example_deleting_an_object_by_path.html)   
删除由路径指定的 MyTone 对象。

[销毁走带对象](ak_wwise_core_transport_destroy_example_destroying_a_transport_object.html)   
销毁给定走带对象。

[禁用性能分析器数据](ak_wwise_core_profiler_enableprofilerdata_example_disabling_profiler_data.html)   
禁用 "Voices Data"。

[与游戏断开连接](ak_wwise_core_remote_disconnect_example_disconnecting_from_a_game.html)   
与当前所连游戏或进程断开连接。

[Docking a floating view in a layout](ak_wwise_ui_layout_dockview_example_docking_a_floating_view_in_a_layout.html)   
Docks a floating view, using its GUID, in a specific panel of a layout.

[启用 ak.wwise.core.profiler.getVoiceContributions 所需的性能分析器数据](ak_wwise_core_profiler_enableprofilerdata_example_enabling_profiler_data_required_for_ak_wwise_cbdbd1e2db8fd6680100c9bbc6a5e3eb8.html)   
针对 enable 属性使用默认值 (true) 启用 "Voices Data" 和 "Voice Inspector Data"。

[启用性能分析器数据](ak_wwise_core_profiler_enableprofilerdata_example_enabling_the_profiler_data.html)   
启用 "Voices Data"。

[结束某个 Undo Group](ak_wwise_core_undo_endgroup_example_ending_an_undo_group.html)   
结束某个 Undo Group。

[Execute Lua file from path](ak_wwise_core_executeluascript_example_execute_lua_file_from_path.html)   
Executes a Lua script from a file path. This is the traditional way to execute Lua scripts and is preferred for longer, more complex scripts. Custom arguments can be passed and accessed via `wa_args` within the script file.

[Execute Lua string with arguments](ak_wwise_core_executeluascript_example_execute_lua_string_with_arguments.html)   
Executes Lua code that accesses custom arguments passed via `wa_args`. All additional arguments in the WAAPI call are accessible as fields in the `wa_args` table within the Lua code.

[Execute Lua string with conditional logic](ak_wwise_core_executeluascript_example_execute_lua_string_with_conditional_logic.html)   
Executes Lua code with control flow logic. The `luaString` can contain multiple lines and use standard Lua control structures like if/else, loops, and functions.

[Execute Lua string with wa\_call](ak_wwise_core_executeluascript_example_execute_lua_string_with_wa_call.html)   
Executes Lua code that calls WAAPI functions using `wa_call`. This demonstrates how to interact with the Wwise API from within the Lua code, such as adding a log message.

[Execute a simple Lua string](ak_wwise_core_executeluascript_example_execute_a_simple_lua_string.html)   
Executes Lua code provided as a string and returns a simple value. This is useful for quick inline scripts without creating a file.

[执行不需要对象参数的命令](ak_wwise_ui_commands_execute_example_executing_a_command_not_requiring_the_object_s_parameter.html)   
执行 "ResetAllMutes" 命令。

[执行需要对象参数的命令](ak_wwise_ui_commands_execute_example_executing_a_command_requiring_the_object_s_parameter.html)   
针对由 "objects" 的 GUID 定义的对象执行 "ConvertCurrentPlatform"。

[Filtering files by duration in the Media Pool](ak_wwise_core_mediapool_get_example_filtering_files_by_duration_in_the_media_pool.html)   
Retrieves audio files that are longer than 5 seconds.

[Filtering files by regular expression in the Media Pool](ak_wwise_core_mediapool_get_example_filtering_files_by_regular_expression_in_the_media_pool.html)   
Retrieves all files ending with '\_01.wav' or '\_02.wav' using a regex filter on the filename.

[在 Project Explorer 中查找并选中对象](ak_wwise_ui_commands_execute_example_finding_and_selecting_objects_in_project_explorer.html)   
在 Project Explorer 视图中查找并选中给定对象 (Selection Channel 1)。

[Finding files by audio description in the Media Pool](ak_wwise_core_mediapool_get_example_finding_files_by_audio_description_in_the_media_pool.html)   
Searches for files that match the description 'a powerful explosion with debris'.

[Finding files by audio similarity in the Media Pool](ak_wwise_core_mediapool_get_example_finding_files_by_audio_similarity_in_the_media_pool.html)   
Searches for audio files that sound similar to a specified file.

[通过指定 Inclusion 来生成新的 SoundBank](ak_wwise_core_soundbank_generate_example_generating_a_new_soundbank_by_specifying_inclusions.html)   
通过示例调用来导入并生成新的 SoundBank，但不会将 SoundBank 保存到工程中。See [ak.wwise.core.soundbank.generated](ak_wwise_core_soundbank_generated.html) to learn how to retrieve the SoundBank data.

[通过指定 Inclusion 来在磁盘上生成新的 SoundBank](ak_wwise_core_soundbank_generate_example_generating_a_new_soundbank_on_disk_by_specifying_inclusions.html)   
导入并生成新的 SoundBank，然后将其写入到磁盘上的 SoundBank 生成文件夹。

[Generating a short sine tone WAV file](ak_wwise_debug_generatetonewav_example_generating_a_short_sine_tone_wav_file.html)   
Generates a 1 second mono WAV file that contains a sine waveform, with a very short attack and release.

[生成多个现有 SoundBank 而不将其写入到磁盘中](ak_wwise_core_soundbank_generate_example_generating_several_existing_soundbanks_without_writing_them_to_disk.html)   
生成多个已存在于工程中的 SoundBank，并通过 WAAPI 对 SoundBank 数据进行流传输。See [ak.wwise.core.soundbank.generated](ak_wwise_core_soundbank_generated.html) to learn how to retrieve the SoundBank data.

[获取 State Group 的状态](ak_soundengine_getstate_example_get_the_state_of_a_state_group.html)   
通过 GUID 获取 "PlayerHealth" State Group 的当前状态。

[获取 Game Object 的 Switch 的状态](ak_soundengine_getswitch_example_get_the_state_of_a_switch_for_a_game_object.html)   
获取 "Footstep" Game Object 的 "Surface" Switch Group 的状态。

[获取有关 Curve 的信息](ak_wwise_core_object_get_example_gets_information_for_a_curve.html)   
使用 "points" 访问器获取曲线的控制点。

[获取有关 RTPC 的信息](ak_wwise_core_object_get_example_gets_information_for_an_rtpc.html)   
使用属性/引用访问器 @ 获取 RTPC 的 "PropertyName" 属性及 "ControlInput" 和 "Curve" 引用。

[获取声音的 "RTPC" 列表的 RTPC ID](ak_wwise_core_object_get_example_gets_the_rtpc_ids_from_a_sound_s_rtpc_list.html)   
使用列表访问器 @ 引用 "RTPC" 列表。注意，RTPC 未命名。

[Getting a Blend Track's assignment list.](ak_wwise_core_blendcontainer_getassignments_example_getting_a_blend_track_s_assignment_list.html)   
Getting a Blend Track's assignment list.

[获取走带对象的 State](ak_wwise_core_transport_getstate_example_getting_a_transport_object_s_state.html)   
获取给定走带对象的 State。

[Getting all Conversion Plug-ins](ak_wwise_core_object_get_example_getting_all_conversion_plug_ins.html)   
Using a WAQL query in order to retrieve all Conversion Plug-ins.

[Getting all files from a specific database in the Media Pool](ak_wwise_core_mediapool_get_example_getting_all_files_from_a_specific_database_in_the_media_pool.html)   
Query the media with FootStep database id.

[Getting all files from the Project Originals database](ak_wwise_core_mediapool_get_example_getting_all_files_from_the_project_originals_database.html)   
Query the media with Project Originals database id.

[获取所有包含 Sound 对象的对象](ak_wwise_core_object_get_example_getting_all_objects_containing_a_sound_object.html)   
检索至少有一个子对象为 Sound 对象的对象的 ID。可使用 "distinct" 转换来滤掉重复项。

[获取所有平台](ak_wwise_core_object_get_example_getting_all_platforms.html)   
检索平台的 ID 和名称。

[Getting all the fields from the Media Pool](ak_wwise_core_mediapool_getfields_example_getting_all_the_fields_from_the_media_pool.html)   
Get all the fields available in the Media Pool.

[获取对象的 Attenuation 曲线](ak_wwise_core_object_getattenuationcurve_example_getting_an_attenuation_curve_of_an_object.html)   
从由 "object" 指定的对象获取 "curve"。

[获取对象的名称](ak_wwise_core_object_get_example_getting_an_object_s_name.html)   
返回对象的“名称”属性。

[获取可用主机](ak_wwise_core_remote_getavailableconsoles_example_getting_available_consoles.html)   
获取可用主机以连接声音引擎。

[获取有关 Wwise 的信息](ak_wwise_core_getinfo_example_getting_information_about_wwise.html)   
获取有关当前所连 Wwise 的信息。

[统一获取各个声道的峰值](ak_wwise_core_audiosourcepeaks_getminmaxpeaksinregion_example_getting_peaks_across_channels.html)   
获取 Audio Source 对象的峰值。

[统一获取各个声道的峰值](ak_wwise_core_audiosourcepeaks_getminmaxpeaksintrimmedregion_example_getting_peaks_across_channels.html)   
在修剪区域内获取 Audio Source 对象的峰值。

[单独获取每个声道的峰值](ak_wwise_core_audiosourcepeaks_getminmaxpeaksinregion_example_getting_peaks_per_channel.html)   
获取 Audio Source 对象的峰值。

[单独获取每个声道的峰值](ak_wwise_core_audiosourcepeaks_getminmaxpeaksintrimmedregion_example_getting_peaks_per_channel.html)   
在修剪区域内获取 Audio Source 对象的峰值。

[获取声音对象的活跃音频源](ak_wwise_core_object_get_example_getting_the_active_source_of_a_sound_object.html)   
使用 "activeSource" 访问器获取声音的活跃音频源。

[获取 Switch Container 的指派](ak_wwise_core_switchcontainer_getassignments_example_getting_the_assignments_of_a_switch_container.html)   
获取包含 Switch Container 指派的列表。

[获取连接状态](ak_wwise_core_remote_getconnectionstatus_example_getting_the_connection_status.html)   
检索当前连接状态。在本例中，Wwise 被连接到了 Integration Demo。

[Getting the current output bus](ak_wwise_core_object_get_example_getting_the_current_output_bus.html)   
Returns the output bus that the object is currently using. The bus returned in the result is either inherited from a parent at a higher level in the hierarchy or is an override (the result does not distinguish between inherited or overridden busses).

[获取与筛选器匹配的下级对象](ak_wwise_core_object_get_example_getting_the_descendant_objects_matching_a_filter.html)   
From all the descendants in the Containers, return the objects whose names start with 'My'. 此项使用 '^My' 正则表达式。

[获取有关当前 Project 的信息](ak_wwise_core_getprojectinfo_example_getting_the_information_about_the_current_project.html)   
获取有关当前所打开工程的信息。

[获取包含所有对象类型的列表](ak_wwise_core_object_gettypes_example_getting_the_list_of_all_object_types.html)   
检索包含所有对象类型的列表。

[Getting the objects using an effect](ak_wwise_core_object_get_example_getting_the_objects_using_an_effect.html)   
Uses the referencesTo and owner accessors to get the list of objects using the effect ShareSet.

[获取工程名称、路径和未同步状态](ak_wwise_core_object_get_example_getting_the_project_name_path_and_dirty_state.html)   
检索工程名称、文件路径和未同步状态。注意，工程名称在 WPROJ MXL 中定义，其有可能跟文件名不一致。For using WAAPI on Mac, please see [在 Mac 上使用 WAAPI](waapi_prepare.html#waapi_path_on_mac) .

[获取对象的属性和引用](ak_wwise_core_object_get_example_getting_the_properties_and_references_of_an_object.html)   
返回对象的声部音量和输出总线。

[Getting the selected files](ak_wwise_ui_getselectedfiles_example_getting_the_selected_files.html)   
Retrieves the absolute file paths of the current view.

[获取选定对象](ak_wwise_ui_getselectedobjects_example_getting_the_selected_object.html)   
检索选定对象的 GUID。

[Getting the source control status of a file](ak_wwise_core_sourcecontrol_getstatus_example_getting_the_source_control_status_of_a_file.html)   
Returns the source control status and owner of the file.

[获取对象的音量](ak_wwise_core_object_get_example_getting_the_volume_of_an_object.html)   
Returns the volume of the Main Audio Bus.

[从文件导入 SoundBank Definition](ak_wwise_core_soundbank_processdefinitionfiles_example_import_soundbank_definitions_from_file.html)   
从给定文本文件导入 SoundBank Definition。

[Importing Base64 content to create a Sound SFX object](ak_wwise_core_object_set_example_importing_base64_content_to_create_a_sound_sfx_object.html)   
Creates a Source SFX object and an audio file source object and imports the specified base64 content as a WAV file.

[Importing WAV files into Impacter source plug-in](ak_wwise_core_object_set_example_importing_wav_files_into_impacter_source_plug_in.html)   
Creates a Sound and an Impacter source plug-in, then imports WAV files.

[Importing a MIDI file into a Music Segment to create a Music Track](ak_wwise_core_object_set_example_importing_a_midi_file_into_a_music_segment_to_create_a_music_track.html)   
Creates a Music Segment from the imported MIDI file. A Music Track and a Music Clip are also created.

[Importing a WAV file into Soundseed Grain source plug-in](ak_wwise_core_object_set_example_importing_a_wav_file_into_soundseed_grain_source_plug_in.html)   
Creates a Sound and a Soundseed Grain source plug-in, then imports a WAV file.

[Importing a WAV file into a Convolution Reverb effect plug-in](ak_wwise_core_object_set_example_importing_a_wav_file_into_a_convolution_reverb_effect_plug_in.html)   
Creates a Sound and a Convolution Reverb effect plug-in, then imports a WAV file as an impulse response.

[Importing a WAV file into a Music Track to create a Music Clip](ak_wwise_core_object_set_example_importing_a_wav_file_into_a_music_track_to_create_a_music_clip.html)   
Creates a Music Segment, a Music Track, and imports its WAV file. A Music Track is also created.

[Importing a WAV file into a Sound Voice](ak_wwise_core_object_set_example_importing_a_wav_file_into_a_sound_voice.html)   
Creates a Sound Voice object and an audio file source object and imports its wave file for English localization.

[Importing a WAV file into a new Sound SFX and creating the associated Event](ak_wwise_core_object_set_example_importing_a_wav_file_into_a_new_sound_sfx_and_creating_the_associated_event.html)   
Creates a new Sound object, imports a WAV file into it, and then creates an Event with a Play action on the Sound.

[Importing a WAV file into an Audio File Source](ak_wwise_core_object_set_example_importing_a_wav_file_into_an_audio_file_source.html)   
Creates a Sound SFX object and its audio source. The property field Sound object is also set.

[Importing a WAV file to create a Sound SFX object](ak_wwise_core_object_set_example_importing_a_wav_file_to_create_a_sound_sfx_object.html)   
Creates a Source SFX object and an audio file source object and imports its wave file.

[导入音频文件](ak_wwise_core_audio_importtabdelimited_example_importing_an_audio_file.html)   
通过制表符分隔文件导入音频文件。

[Importing an audio file to create a Sound SFX using a relative object path](ak_wwise_core_audio_import_example_importing_an_audio_file_to_create_a_sound_sfx_using_a_relative_object_path.html)   
Imports files using the importLocation, a relative objectPath, and an objectType.

[Importing an audio file to create a Sound SFX using an absolute object path](ak_wwise_core_audio_import_example_importing_an_audio_file_to_create_a_sound_sfx_using_an_absolute_object_path.html)   
Imports files using an absolute objectPath that includes the object type.

[Importing an audio file to create a Sound Voice for English](ak_wwise_core_audio_import_example_importing_an_audio_file_to_create_a_sound_voice_for_english.html)   
Imports files using an absolute objectPath and specifying the English language.

[Importing an audio file to create a Sound Voice for French](ak_wwise_core_audio_import_example_importing_an_audio_file_to_create_a_sound_voice_for_french.html)   
Imports files using an absolute objectPath and specifying the French language.

[Importing an audio files to create Sound Voices for English and French](ak_wwise_core_audio_import_example_importing_an_audio_files_to_create_sound_voices_for_english_and_french.html)   
Imports files using an absolute objectPath and specifying the language for each entry.

[Importing audio files and creating multiple Sound SFX](ak_wwise_core_audio_import_example_importing_audio_files_and_creating_multiple_sound_sfx.html)   
将由 "audioFile" 指定的文件导入到 "objectPath" 下。

[Importing audio files to create Sound SFX and Audio File Sources](ak_wwise_core_audio_import_example_importing_audio_files_to_create_sound_sfx_and_audio_file_sources.html)   
Imports files using an absolute objectPath that includes the object type for the Sound SFX and the Audio File Source.

[Importing two WAV files into a Music Segment to create two Music Tracks](ak_wwise_core_object_set_example_importing_two_wav_files_into_a_music_segment_to_create_two_music_tracks.html)   
Creates a Music Segment, and imports two WAV files. Two new Music Tracks and two Music Clips are also created.

[Importing two WAV files to create two Sound SFX objects](ak_wwise_core_object_set_example_importing_two_wav_files_to_create_two_sound_sfx_objects.html)   
Creates two Sound SFX objects and two audio file source objects and imports their wave files.

[针对 Event 执行 Stop 动作](ak_soundengine_executeactiononevent_example_launching_a_stop_action_on_event.html)   
针对给定 Event 执行 Stop 动作，在 5 秒内按照 log1 曲线淡出。

[Limiting the number of results in the Media Pool](ak_wwise_core_mediapool_get_example_limiting_the_number_of_results_in_the_media_pool.html)   
Searches for 'footstep' but limits the returned results to the first 3 matches.

[Load a Work Unit.](ak_wwise_core_workunit_load_example_load_a_work_unit.html)   
Load a Work Unit that was previously unloaded.

[Moving a layout splitter backward](ak_wwise_ui_layout_movesplitter_example_moving_a_layout_splitter_backward.html)   
Moves a splitter to the left or the top, by a delta given in pixels.

[Moving a layout splitter forward](ak_wwise_ui_layout_movesplitter_example_moving_a_layout_splitter_forward.html)   
Moves a splitter to the right or the bottom, by a delta given in pixels.

[将对象移动到新的父对象](ak_wwise_core_object_move_example_moving_an_object_to_a_new_parent.html)   
移动由 "id" 定义的对象，并将其作为 "parent" 的子对象。若 "parent" 已经包含同名子对象，则无法移动对象。

[将对象移动到包含同名子对象的父对象](ak_wwise_core_object_move_example_moving_an_object_to_a_parent_containing_a_child_of_the_same_name.html)   
移动由 "id" 定义的对象，并将其作为 "parent" 的子对象。若 "parent" 已经包含同名子对象，则对相应对象进行重命名。

[Mute a WwiseObject](ak_wwise_core_audio_mute_example_mute_a_wwiseobject.html)   
Mutes the object specified by "object".

[将给定对象静音](ak_wwise_ui_commands_execute_example_muting_the_specified_object.html)   
执行 "Mute" 命令并指定 Mute 状态。

[Opening a project](ak_wwise_console_project_open_example_opening_a_project.html)   
打开由路径指定的 .wproj 工程。

[打开工程](ak_wwise_ui_project_open_example_opening_a_project.html)   
打开由路径指定的 .wproj 工程。

[粘贴列表](ak_wwise_core_object_pasteproperties_example_pasting_a_list.html)   
将存在差异的属性、引用和列表从源对象粘贴到目标对象。只会粘贴选定 "RTPC" 列表，不会粘贴存在差异的属性或引用。

[粘贴列表和所有属性及引用](ak_wwise_core_object_pasteproperties_example_pasting_a_list_and_all_properties_and_references.html)   
将存在差异的属性、引用和列表从源对象粘贴到目标对象。只会随所有属性和引用一起粘贴 "RTPC" 列表。源对象只包含 "RTPC" 和 "Metadata" 列表。

[粘贴属性和所有列表](ak_wwise_core_object_pasteproperties_example_pasting_a_property_and_all_lists.html)   
将存在差异的属性、引用和列表从源对象粘贴到目标对象。只会随源对象的所有列表一起粘贴 "Volume" 属性。源对象只包含 "RTPC" 和 "Metadata" 列表。

[粘贴默认项](ak_wwise_core_object_pasteproperties_example_pasting_with_defaults.html)   
将存在差异的属性、引用和列表从源对象粘贴到目标对象。将粘贴所有差异项。

[不粘贴排除项](ak_wwise_core_object_pasteproperties_example_pasting_with_exclusion.html)   
将存在差异的属性、引用和列表从源对象粘贴到目标对象。为列表选择非默认 Paste Mode 并粘贴 "Volume" 属性和 "RTPC" 列表以外的所有条目。

[粘贴包含项](ak_wwise_core_object_pasteproperties_example_pasting_with_inclusion.html)   
将存在差异的属性、引用和列表从源对象粘贴到目标对象。仅粘贴 "Volume" 属性和 "RTPC" 列表。

[Performing a redo](ak_wwise_core_undo_redo_example_performing_a_redo.html)   
Performs a redo.

[执行“撤销”操作](ak_wwise_core_undo_undo_example_performing_an_undo.html)   
执行“撤销”操作。

[播放走带对象](ak_wwise_core_transport_executeaction_example_playing_a_transport_object.html)   
播放给定走带对象。

[按照 GUID 发送 Trigger](ak_soundengine_posttrigger_example_posting_a_trigger_by_guid.html)   
按照 GUID 发送给定 "trigger" 以作用于 "gameObject"。

[按照名称发送 Trigger](ak_soundengine_posttrigger_example_posting_a_trigger_by_name.html)   
按照名称发送给定 "trigger" 以作用于 "gameObject"。

[按照 Short ID 发送 Event](ak_soundengine_postevent_example_posting_an_event_by_short_id.html)   
使用 Event 的 Short ID 将 Event 发送到声音引擎。

[按照名称发送 Event](ak_soundengine_postevent_example_posting_an_event_by_name.html)   
使用 Event 的名称将 Event 发送到声音引擎。

[按照对象 GUID 发送 Event](ak_soundengine_postevent_example_posting_an_event_by_object_guid.html)   
使用 Event 的 GUID 将 Event 发送到声音引擎。

[准备 Event](ak_wwise_core_transport_prepare_example_preparing_an_event.html)   
准备对象及其依赖项以供播放并用于走带对象。

[查询在 1 分钟或之前注册的游戏对象](ak_wwise_core_profiler_getgameobjects_example_query_game_objects_registered_at_or_before_1_minute.html)   
获取注册时间为 60,000 毫秒或更早的游戏对象。

[Querying the CPU usage at a point in time.](ak_wwise_core_profiler_getcpuusage_example_querying_the_cpu_usage_at_a_point_in_time.html)   
Queries the CPU usage in the current capture session at the latest capture time.

[Querying the Loaded Media at a point in time.](ak_wwise_core_profiler_getloadedmedia_example_querying_the_loaded_media_at_a_point_in_time.html)   
Queries the active Loaded Media in the current capture session at the latest capture time.

[Querying the Performance Monitor at a point in time.](ak_wwise_core_profiler_getperformancemonitor_example_querying_the_performance_monitor_at_a_point_in_time.html)   
Queries the Performance Monitor Counters in the current capture session at the latest capture time. For the purposes of this example only a subset of the returned counters are displayed.

[在某个时间点查询 RTPC 值及 ID](ak_wwise_core_profiler_getrtpcs_example_querying_the_rtpc_id_and_value_at_a_point_in_time.html)   
在当前捕获会话的 30 秒（30,000 毫秒）位置查询活跃的 RTPC。

[Querying the Streamed Media at a point in time.](ak_wwise_core_profiler_getstreamedmedia_example_querying_the_streamed_media_at_a_point_in_time.html)   
Queries the active Streamed Media in the current capture session at the latest capture time.

[在某个时间点查询总线名称](ak_wwise_core_profiler_getbusses_example_querying_the_bus_names_at_a_point_in_time.html)   
在当前捕获会话的 30 秒（30,000 毫秒）位置查询总线。

[通过 Capture Time Cursor 查询 Audio Object 的游戏对象属性](ak_wwise_core_profiler_getaudioobjects_example_querying_the_game_object_properties_of_audio_object_from_the_capture_time_cursor.html)   
指定 Capture Time Cursor 作为处理调用时捕获会话的最新时间来查询 Audio Object。

[通过 Capture Time Cursor 查询声部的游戏对象属性](ak_wwise_core_profiler_getvoices_example_querying_the_game_object_properties_of_voices_from_the_capture_time_cursor.html)   
指定 Capture Time Cursor 作为处理调用时捕获会话的最新时间来查询声部。

[在某个时间点查询 Audio Object 的 Instigator ID (Pipeline ID)](ak_wwise_core_profiler_getaudioobjects_example_querying_the_instigator_id_pipeline_id_for_the_audio_objects_at_a_point_in_time.html)   
在当前捕获会话的 30 秒（30,000 毫秒）位置查询 Audio Object 的 Instigator ID (Pipeline ID)。

[在某个时间点查询声部名称](ak_wwise_core_profiler_getvoices_example_querying_the_sound_names_at_a_point_in_time.html)   
在当前捕获会话的 30 秒（30,000 毫秒）位置查询声部。

[Register a new temporary layout](ak_wwise_ui_layout_setlayout_example_register_a_new_temporary_layout.html)   
Registers a new layout from a JSON format

[Registering a bus for metering](ak_wwise_core_profiler_registermeter_example_registering_a_bus_for_metering.html)   
Registers a specific bus for metering. This is necessary to obtain the bus meter value with [ak.wwise.core.profiler.getMeters](ak_wwise_core_profiler_getmeters.html).

[将命令注册为 Edit in Visual Studio Code](ak_wwise_ui_commands_register_example_registering_a_command_to_edit_in_visual_studio_code.html)   
注册要在新的 Extra 菜单中显示的命令。

[将命令注册为 Edit in Wavosaur](ak_wwise_ui_commands_register_example_registering_a_command_to_edit_in_wavosaur.html)   
注册只在上下文菜单中显示的命令。

[将命令注册为 Programless registration](ak_wwise_ui_commands_register_example_registering_a_command_with_no_program.html)   
注册不含任何程序的命令。通常用作 WAAPI 中的回调。最简单的示例。

[注册游戏对象](ak_soundengine_registergameobj_example_registering_a_game_object.html)   
注册 "MyGameObjectName" 游戏对象。

[Removing a Blend Track assignment.](ak_wwise_core_blendcontainer_removeassignment_example_removing_a_blend_track_assignment.html)   
Equivalent to deleting an entry in the Blend Tracks Editor.

[从 Switch Container 中移除指派](ak_wwise_core_switchcontainer_removeassignment_example_removing_an_assignment_from_a_switch_container.html)   
相当于在 Assigned Objects 视图中选中并删除指派给 State 的子对象。

[对 WwiseObject 进行重命名](ak_wwise_core_object_setname_example_renaming_a_wwiseobject.html)   
将由 "object" 指定的对象重命名为 "value"。

[使用 GUID 重置 RTPC 值](ak_soundengine_resetrtpcvalue_example_resetting_an_rtpc_value_using_its_guid.html)   
针对 "gameObject" 使用 GUID 将 "rtpc" 的值重置为默认值。

[使用名称重置 RTPC 值](ak_soundengine_resetrtpcvalue_example_resetting_an_rtpc_value_using_its_name.html)   
针对 "gameObject" 使用名称将 "rtpc" 的值重置为默认值。

[Retrieve all audio files in a specific folder](ak_wwise_core_sourcecontrol_getsourcefiles_example_retrieve_all_audio_files_in_a_specific_folder.html)   
Returns the absolute path of audio files in a folder.

[Retrieve all audio files in the projet](ak_wwise_core_sourcecontrol_getsourcefiles_example_retrieve_all_audio_files_in_the_projet.html)   
Return the absolute path of audio files that are not used by a Wwise object and all folders under the Originals folder.

[Retrieve unused audio files in the projet](ak_wwise_core_sourcecontrol_getsourcefiles_example_retrieve_unused_audio_files_in_the_projet.html)   
Return the path of audio files that are not used by a Wwise object.

[检索 SoundBank 的 Inclusion 列表](ak_wwise_core_soundbank_getinclusions_example_retrieving_a_soundbank_s_inclusion_list.html)   
获取 SoundBank 的 Inclusion 列表。

[Retrieving all factory layout names](ak_wwise_ui_layout_getlayoutnames_example_retrieving_all_factory_layout_names.html)   
Returns a list of all factory layout names.

[Retrieving all instantiated views in a layout](ak_wwise_ui_layout_getviewinstances_example_retrieving_all_instantiated_views_in_a_layout.html)   
Returns a list of all instantiated views in a given layout.

[Retrieving all view types](ak_wwise_ui_layout_getviewtypes_example_retrieving_all_view_types.html)   
Returns a list of all available view types (just a few are listed in this example).

[检索有关对象属性的信息](ak_wwise_core_object_getpropertyinfo_example_retrieving_information_about_an_object_property.html)   
检索有关对象属性的信息。

[Retrieving or creating a new view](ak_wwise_ui_layout_getorcreateview_example_retrieving_or_creating_a_new_view.html)   
Gets a view, if it exists in the current layout, or creates a new one.

[检索 SoundBank 日志](ak_wwise_core_log_get_example_retrieving_the_soundbank_log.html)   
使用 'soundbankGenerate' 通道来检索最新的 SoundBank 生成日志。

[Retrieving the current allocation for a layout element](ak_wwise_ui_layout_getelementrectangle_example_retrieving_the_current_allocation_for_a_layout_element.html)   
Returns the current allocated rectangle of a layout element, identified by its GUID.

[Retrieving the current layout's name](ak_wwise_ui_layout_getcurrentlayoutname_example_retrieving_the_current_layout_s_name.html)   
Returns the current layout's name as a string.

[检索包含对象属性和引用名称的列表](ak_wwise_core_object_getpropertyandreferencenames_example_retrieving_the_list_of_property_and_reference_names_of_an_object.html)   
检索包含对象属性和引用名称的列表。

[检索包含走带对象的列表](ak_wwise_core_transport_getlist_example_retrieving_the_list_of_transport_objects.html)   
检索包含走带对象的列表。

[Retrieving the meter values after registering a bus for meter](ak_wwise_core_profiler_getmeters_example_retrieving_the_meter_values_after_registering_a_bus_for_meter.html)   
Gets the meter values for all registered busses. In this example, one of the busses is configured in 7.1 and is registered with [ak.wwise.core.profiler.registerMeter](ak_wwise_core_profiler_registermeter.html).

[返回属性和列表差异](ak_wwise_core_object_diff_example_returning_the_property_and_list_differences.html)   
返回 2 个对象之间的属性和列表差异。

[Reverting a file modification in the source control.](ak_wwise_core_sourcecontrol_revert_example_reverting_a_file_modification_in_the_source_control.html)   
The modification is canceled and the contents of the file return to what was before the checkout.

[Saving a profiler capture](ak_wwise_core_profiler_savecapture_example_saving_a_profiler_capture.html)   
Saves the current profiler capture to the file "capture.prof".

[保存当前工程](ak_wwise_core_project_save_example_saving_the_current_project.html)   
保存当前工程。

[按照文本搜索对象](ak_wwise_core_object_get_example_searching_objects_by_text.html)   
搜索名称中包含 'gun' 的对象。

[搜索特定类别的对象](ak_wwise_core_object_get_example_searching_objects_of_a_certain_category.html)   
Retrieves the id and name of objects with "Tone" in their text properties and filters the results to retrieve only those within the category "Containers".

[搜索特定类型的对象](ak_wwise_core_object_get_example_searching_objects_of_a_certain_type.html)   
检索“文本”属性中带有 "Tone" 的对象的 ID、名称和备注，并对结果进行筛选来仅获取 "Sound" 类型的对象。See [Wwise 对象参考](wobjects_index.html) for the types available.

[Searching the Media Pool for files with a specific keyword](ak_wwise_core_mediapool_get_example_searching_the_media_pool_for_files_with_a_specific_keyword.html)   
Performs a text search for the keyword 'Concrete' in the Media Pool.

[寻址到时长的 35%](ak_soundengine_seekonevent_example_seeking_to_35_of_duration.html)   
在时长的 35% 位置对 "event" 的 Play 动作中引用的 "gameObject" 进行寻址。

[寻址到 1 秒位置](ak_soundengine_seekonevent_example_seeking_to_position_1_s.html)   
在 1 秒位置对 "event" 的 Play 动作中引用的 "gameObject" 进行寻址。

[将消息发送到 Profiler](ak_soundengine_postmsgmonitor_example_sending_a_message_to_the_profiler.html)   
将 "message" 发送到 Profiler。

[Serializing a specific layout](ak_wwise_ui_layout_getlayout_example_serializing_a_specific_layout.html)   
Returns a layout serialized in a JSON format.

[Set Game Parameter range](ak_wwise_core_gameparameter_setrange_example_set_game_parameter_range.html)   
Equivalent to clicking the Edit button for Min or Max and setting the range of a Game Parameter.

[Set conversion plugin.](ak_wwise_core_audio_setconversionplugin_example_set_conversion_plugin.html)   
Changes an object's or project's conversion plug-in to the one specified (Vorbis).

[Set state properties to a Sound](ak_wwise_core_object_setstateproperties_example_set_state_properties_to_a_sound.html)   
Sets BypassEffects and Volume state properties to a Sound.

[Setting a Metadata plug-in](ak_wwise_core_object_set_example_setting_a_metadata_plug_in.html)   
Sets the Metadata of a Sound to a newly created Wwise System Output Settings plug-in.

[设置游戏对象的听者列表](ak_soundengine_setlisteners_example_setting_a_list_of_listeners_for_a_game_object.html)   
将 "listeners" 设为 "gameObject" 的活跃听者列表。

[使用 GUID 设置 RTPC 值](ak_soundengine_setrtpcvalue_example_setting_an_rtpc_value_using_its_guid.html)   
针对 "gameObject" 使用 GUID 将 "rtpc" 的值设为 "value"。

[使用名称设置 RTPC 值](ak_soundengine_setrtpcvalue_example_setting_an_rtpc_value_using_its_name.html)   
针对 "gameObject" 使用名称将 "rtpc" 的值设为 "value"。

[Setting an effect plug-in](ak_wwise_core_object_set_example_setting_an_effect_plug_in.html)   
Sets the effects of a Sound to a newly created Custom RoomVerb Effect plug-in.

[设置对象引用](ak_wwise_core_object_setreference_example_setting_an_object_reference.html)   
为给定对象设置 Output Bus。

[为游戏对象设置多个位置](ak_soundengine_setmultiplepositions_example_setting_multiple_positions_for_a_game_object.html)   
按照 "positions" 中的定义为 "gameObject" 设置多个位置以模拟一个在播声音对应的多个声源。

[设置 RTPC 的 "Curve" 引用](ak_wwise_core_object_set_example_setting_the_curve_reference_of_an_rtpc.html)   
设置给定 RTPC 的曲线控制点。

[设置游戏对象的 Auxiliary Bus](ak_soundengine_setgameobjectauxsendvalues_example_setting_the_auxiliary_busses_for_a_game_object.html)   
设置 "listener" 对应 "emitter" 的 Auxiliary Bus，分别为其指定总线名称和数值。

[使用 Short ID 将 State Group 设为另一 State](ak_soundengine_setstate_example_setting_the_state_group_to_another_state_using_short_ids.html)   
将 "stateGroup" 设为 "state"。

[使用名称将 State Group 设为另一 State](ak_soundengine_setstate_example_setting_the_state_group_to_another_state_using_names.html)   
将 "stateGroup" 设为 "state"。

[使用 Short ID 将 Switch Group 设为另一 State](ak_soundengine_setswitch_example_setting_the_switch_group_to_another_state_using_short_ids.html)   
针对 "gameObject" 将 "switchGroup" 设为 "switchState"。

[使用名称将 Switch Group 设为另一 State](ak_soundengine_setswitch_example_setting_the_switch_group_to_another_state_using_names.html)   
针对 "gameObject" 将 "switchGroup" 设为 "switchState"。

[为 Sound 对象的 Volume 属性设置 Randomizer 值](ak_wwise_core_object_setrandomizer_example_setting_the_volume_randomizer_values_of_a_sound_object.html)   
为由 "object" 定义的对象的 "Volume" 属性设置 Randomizer 值。

[为 Sound Voice 设置活跃音频源](ak_wwise_core_sound_setactivesource_example_setting_the_active_source_for_a_sound_voice.html)   
为 Sound Voice 设置活跃音频源。Sound 有一个主要音频源和一个备用音频源。

[设置听者对应发声体的输出总线音量](ak_soundengine_setgameobjectoutputbusvolume_example_setting_the_emitter_s_output_bus_volume_for_the_listener.html)   
使用倍数控制值将听者对应发声体的输出总线音量放大。

[设置默认听者列表](ak_soundengine_setdefaultlisteners_example_setting_the_list_of_default_listeners.html)   
将 "listeners" 设为默认听者列表。

[设置听者空间化](ak_soundengine_setlistenerspatialization_example_setting_the_listener_spatialization.html)   
使用 "volumeOffsets" 设置 "listener" 的空间化以将声像摆位到左侧。

[设置对象的备注](ak_wwise_core_object_setnotes_example_setting_the_notes_of_an_object.html)   
为由 "object" 定义的对象设置备注。

[设置游戏对象的声障和声笼电平](ak_soundengine_setobjectobstructionandocclusion_example_setting_the_obstruction_and_occlusion_level_of_a_game_object.html)   
设置 "listener" 对应 "emitter" 的 "obstructionLevel" 和 "occlusionLevel"。

[设置游戏对象的位置](ak_soundengine_setposition_example_setting_the_position_of_a_game_object.html)   
按照给定朝向将 "gameObject" 的位置设为 "position/position"。

[设置游戏对象的缩放系数](ak_soundengine_setscalingfactor_example_setting_the_scaling_factor_of_a_game_object.html)   
将 "gameObject" 的缩放系数设为 "attenuationScalingFactor" (200%)。

[Setting the trigger of a MusicStinger.](ak_wwise_core_object_set_example_setting_the_trigger_of_a_musicstinger.html)   
The object field contains the id of the MusicStinger we want to change.

[针对给定平台设置给定属性的值](ak_wwise_core_object_setproperty_example_setting_the_value_of_a_specified_property_on_the_specified_platform.html)   
将由 "object" 定义的对象的 "Volume" 属性设为 "Value"。

[设置名称、备注、属性和引用的值](ak_wwise_core_object_set_example_setting_the_values_of_the_name_notes_a_property_and_a_reference.html)   
设置 "object" 所定义对象的名称、备注、"Volume" 属性和 "OutputBus" 引用。参见有关 [ak.wwise.core.object.setName](ak_wwise_core_object_setname.html) 、 [ak.wwise.core.object.setNotes](ak_wwise_core_object_setnotes.html) 、 [ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html) 和 [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) 的示例来对比两种架构。

[设置音量](ak_wwise_core_object_setproperty_example_setting_the_volume.html)   
将由 "object" 定义的对象的 "Volume" 属性设为 "Value"。

[Solo a WwiseObject](ak_wwise_core_audio_solo_example_solo_a_wwiseobject.html)   
Solos the object specified by "object".

[停止播放当前在播内容](ak_soundengine_stopplayingid_example_stopping_a_current_content_playing.html)   
停止播放与 "playingId" 关联的内容，在 "transitionDuration" 内按照线性曲线淡出。

[停止播放当前在播内容](ak_soundengine_stopall_example_stopping_a_currently_playing_content.html)   
停止播放所有与 "gameObject" 关联的内容。

[停止播放所有走带对象](ak_wwise_core_transport_executeaction_example_stopping_all_transport_objects.html)   
停止播放所有走带对象。

[Switching the current layout](ak_wwise_ui_layout_switchlayout_example_switching_the_current_layout.html)   
Activates a new layout, identified by its name.

[切换走带对象的播放状态（暂停/继续）](ak_wwise_core_transport_executeaction_example_toggling_playback_pause_resume_on_a_transport_object.html)   
切换给定走带对象的播放状态（暂停/继续）。

[切换走带对象的播放状态（播放/停止）](ak_wwise_core_transport_executeaction_example_toggling_playback_play_stop_on_a_transport_object.html)   
切换给定走带对象的播放状态（播放/停止）。

[切换给定对象的 Mute 状态](ak_wwise_ui_commands_execute_example_toggling_the_mute_state_on_the_specified_object.html)   
执行 "Mute" 命令但不指定值，以此来切换当前状态。

[Undock a view from a layout](ak_wwise_ui_layout_undockview_example_undock_a_view_from_a_layout.html)   
Creates a floating view, at the given position, from a docked view in a layout.

[Unload a Work Unit.](ak_wwise_core_workunit_unload_example_unload_a_work_unit.html)   
Unload a Work Unit.

[Unmute all objects](ak_wwise_core_audio_resetmute_example_unmute_all_objects.html)   
Unmute all muted objects in Wwise.

[Unregister a temporary layout](ak_wwise_ui_layout_removelayout_example_unregister_a_temporary_layout.html)   
Unregisters a temporary layout, previously registered with "setLayout".

[Unregistering a bus for metering](ak_wwise_core_profiler_unregistermeter_example_unregistering_a_bus_for_metering.html)   
Unregisters a specific bus for metering.

[注销游戏对象](ak_soundengine_unregistergameobj_example_unregistering_a_game_object.html)   
注销 "gameObject"。

[注销一系列命令](ak_wwise_ui_commands_unregister_example_unregistering_a_list_of_commands.html)   
注销 ak.wwise.ui.commands.register 示例中的所有命令。

[Unsolo all objects](ak_wwise_core_audio_resetsolo_example_unsolo_all_objects.html)   
Unsolo all soloed objects in Wwise.

[Verify the status of WAAPI](ak_wwise_core_ping_example_verify_the_status_of_waapi.html)   
Make sure that WAAPI can be used before making a call to it.