# Wwise Authoring API 参考 – 函数

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Authoring API 参考 – 函数

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。

[ak.soundengine.executeActionOnEvent](ak_soundengine_executeactiononevent.html)   
针对给定 Event 的 Play 动作中引用的所有节点执行相应动作。参阅 `AK::SoundEngine::ExecuteActionOnEvent` 章节。

[ak.soundengine.getState](ak_soundengine_getstate.html)   
获取 State Group 的当前状态。在 getState 之前使用 setState 时，允许有短暂的延迟（不超过 10 ms），以便在声音引擎中更新信息。

[ak.soundengine.getSwitch](ak_soundengine_getswitch.html)   
获取给定 Game Object 的 Switch Group 的当前状态。

[ak.soundengine.loadBank](ak_soundengine_loadbank.html)   
Load a SoundBank. See `AK::SoundEngine::LoadBank`.

[ak.soundengine.postEvent](ak_soundengine_postevent.html)   
按照 Event ID 将 Event 异步发送到声音引擎。参阅 `AK::SoundEngine::PostEvent` 章节。

[ak.soundengine.postMsgMonitor](ak_soundengine_postmsgmonitor.html)   
在 Profiler 的 Capture Log 视图中显示消息。

[ak.soundengine.postTrigger](ak_soundengine_posttrigger.html)   
发送给定 Trigger。参阅 `AK::SoundEngine::PostTrigger` 章节。

[ak.soundengine.registerGameObj](ak_soundengine_registergameobj.html)   
注册游戏对象。将游戏对象注册两次并没有什么作用。注销一次便可将其彻底注销，无论其之前被注册过多少次。参阅 `AK::SoundEngine::RegisterGameObj` 章节。

[ak.soundengine.resetRTPCValue](ak_soundengine_resetrtpcvalue.html)   
将 RTPC 的值重置为 Wwise 工程中指定的默认值。参阅 `AK::SoundEngine::ResetRTPCValue` 章节。

[ak.soundengine.seekOnEvent](ak_soundengine_seekonevent.html)   
在内部对给定 Event 的 Play 动作中引用的所有在播对象进行寻址。参阅 `AK::SoundEngine::SeekOnEvent` 章节。

[ak.soundengine.setDefaultListeners](ak_soundengine_setdefaultlisteners.html)   
为所有后续注册的游戏对象设置默认的活跃听者。参阅 `AK::SoundEngine::SetDefaultListeners` 章节。

[ak.soundengine.setGameObjectAuxSendValues](ak_soundengine_setgameobjectauxsendvalues.html)   
设置 Auxiliary Bus 以输出给定游戏对象。参阅 `AK::SoundEngine::SetGameObjectAuxSendValues` 章节。

[ak.soundengine.setGameObjectOutputBusVolume](ak_soundengine_setgameobjectoutputbusvolume.html)   
设置给定游戏对象的输出总线音量（直达声）。参阅 `AK::SoundEngine::SetGameObjectOutputBusVolume` 章节。

[ak.soundengine.setListeners](ak_soundengine_setlisteners.html)   
设置单个游戏对象的活跃听者。在默认情况下，所有新的游戏对象都没有活跃听者，不过可使用 `SetDefaultListeners()` 来改写此行为。非活跃听者不实施计算。参阅 `AK::SoundEngine::SetListeners` 章节。

[ak.soundengine.setListenerSpatialization](ak_soundengine_setlistenerspatialization.html)   
设置听者的空间化参数。这样方便定义各个音频声道的听者特定音量偏置。参阅 `AK::SoundEngine::SetListenerSpatialization` 章节。

[ak.soundengine.setMultiplePositions](ak_soundengine_setmultiplepositions.html)   
为单个游戏对象设置多个位置。通过为单个游戏对象设置多个位置，只需占用一个声部的资源就可模拟多个声源。我们可以采用这种方式来模拟墙壁开口、区域声音或在同一区域发出相同声音的多个对象。参阅 `AK::SoundEngine::SetMultiplePositions` 章节。

[ak.soundengine.setObjectObstructionAndOcclusion](ak_soundengine_setobjectobstructionandocclusion.html)   
设置游戏对象的声障和声笼电平。此函数用于影响对象应当如何被特定听者听到。参阅 `AK::SoundEngine::SetObjectObstructionAndOcclusion` 章节。

[ak.soundengine.setPosition](ak_soundengine_setposition.html)   
设置游戏对象的位置。参阅 `AK::SoundEngine::SetPosition` 章节。

[ak.soundengine.setRTPCValue](ak_soundengine_setrtpcvalue.html)   
设置 RTPC 的值。参阅 `AK::SoundEngine::SetRTPCValue` 章节。

[ak.soundengine.setScalingFactor](ak_soundengine_setscalingfactor.html)   
设置游戏对象的缩放系数。您可以修改此游戏对象的衰减计算结果，以便模拟具有更大或更小传播区域的声音。参阅 `AK::SoundEngine::SetScalingFactor` 章节。

[ak.soundengine.setState](ak_soundengine_setstate.html)   
设置 State Group 的 State。参阅 `AK::SoundEngine::SetState` 章节。

[ak.soundengine.setSwitch](ak_soundengine_setswitch.html)   
设置 Switch Group 的 State。参阅 `AK::SoundEngine::SetSwitch` 章节。

[ak.soundengine.stopAll](ak_soundengine_stopall.html)   
停止播放与给定游戏对象 ID 关联的当前内容。若未指定游戏对象，则停止播放所有声音。参阅 `AK::SoundEngine::StopAll` 章节。

[ak.soundengine.stopPlayingID](ak_soundengine_stopplayingid.html)   
停止播放与给定 Playing ID 关联的当前内容。参阅 `AK::SoundEngine::StopPlayingID` 章节。

[ak.soundengine.unloadBank](ak_soundengine_unloadbank.html)   
Unload a SoundBank. See `AK::SoundEngine::UnloadBank`.

[ak.soundengine.unregisterGameObj](ak_soundengine_unregistergameobj.html)   
注销游戏对象。将游戏对象注册两次并没有什么作用。注销一次便可将其彻底注销，无论其之前被注册过多少次。允许注销在使用的游戏对象，但是会失去对其参数的控制。比方说，与此游戏对象关联的声音是在 3D 空间内移动的声音。在注销游戏对象后其会停止移动，而且无法恢复对它的控制。参阅 `AK::SoundEngine::UnregisterGameObj` 章节。

[ak.wwise.console.project.close](ak_wwise_console_project_close.html)   
关闭当前工程。This operation is synchronous.

[ak.wwise.console.project.create](ak_wwise_console_project_create.html)   
Creates, saves and opens new empty project, specified by path and platform. The project has no factory setting WorkUnit. This operation is synchronous.

[ak.wwise.console.project.open](ak_wwise_console_project_open.html)   
打开由路径指定的工程。This operation is synchronous.

[ak.wwise.core.audio.convert](ak_wwise_core_audio_convert.html)   
Creates a converted audio file. When errors occur, this function returns a list of messages with corresponding levels of severity.

[ak.wwise.core.audio.import](ak_wwise_core_audio_import.html)   
创建 Wwise 对象并导入音频文件。This function does not return an error when something fails during the import process, please see the log for the result of each import command. 此函数使用 Audio File Importer 中 Tab Delimited import 提供的同一导入处理器。函数会返回包含所有创建、替换或重用的对象的数组。使用选项来指定如何返回对象。For more information, see [导入音频文件和创建架构](waapi_import.html).

[ak.wwise.core.audio.importTabDelimited](ak_wwise_core_audio_importtabdelimited.html)   
通过制表符分隔文件创建脚本化对象并导入音频文件。

[ak.wwise.core.audio.mute](ak_wwise_core_audio_mute.html)   
Mutes an object.

[ak.wwise.core.audio.resetMute](ak_wwise_core_audio_resetmute.html)   
Unmute all muted objects.

[ak.wwise.core.audio.resetSolo](ak_wwise_core_audio_resetsolo.html)   
Unsolo all soloed objects.

[ak.wwise.core.audio.setConversionPlugin](ak_wwise_core_audio_setconversionplugin.html)   
Changes the plug-in to use for audio file conversion.

[ak.wwise.core.audio.solo](ak_wwise_core_audio_solo.html)   
Solos an object.

[ak.wwise.core.audioSourcePeaks.getMinMaxPeaksInRegion](ak_wwise_core_audiosourcepeaks_getminmaxpeaksinregion.html)   
在音频源的给定区域以二进制字符串数组形式获取最小/最大峰值对（每个声道对应一个字符串）。字符串为 base-64 编码的 16 位有符号整数数组（交错存取最小值和最大值）。若 getCrossChannelPeaks 为 true，则仅有一个二进制字符串（代表所有声道的全局峰值）。

[ak.wwise.core.audioSourcePeaks.getMinMaxPeaksInTrimmedRegion](ak_wwise_core_audiosourcepeaks_getminmaxpeaksintrimmedregion.html)   
针对每个声道在音频源的整个修剪区域以二进制字符串数组形式获取最小/最大峰值对（每个声道对应一个字符串）。字符串为 base-64 编码的 16 位有符号整数数组（交错存取最小值和最大值）。若 getCrossChannelPeaks 为 true，则仅有一个二进制字符串（代表所有声道的全局峰值）。

[ak.wwise.core.blendContainer.addAssignment](ak_wwise_core_blendcontainer_addassignment.html)   
Adds a new assignment to a Blend Track. Equivalent to performing a drag-and-drop operation in the Blend Tracks Editor.

[ak.wwise.core.blendContainer.addTrack](ak_wwise_core_blendcontainer_addtrack.html)   
Adds a new Blend Track to a Blend Container. Equivalent to clicking New Blend Track in the Blend Track Editor. To get the list of Blend Tracks, use the function ak.wwise.core.object.get with {return = "blendTracks"}.

[ak.wwise.core.blendContainer.getAssignments](ak_wwise_core_blendcontainer_getassignments.html)   
Returns a list of a Blend Track assignments.

[ak.wwise.core.blendContainer.removeAssignment](ak_wwise_core_blendcontainer_removeassignment.html)   
Removes an assignment from a Blend Track. Equivalent to deleting an entry in the Blend Tracks Editor.

[ak.wwise.core.executeLuaScript](ak_wwise_core_executeluascript.html)   
Execute Lua code from a file path (using `luaScript`) or directly as a string (using `luaString`). Optionally, specify additional Lua search paths, additional modules, and additional Lua scripts to load prior to the main script. The script can return a value, which can be any of the Lua types, including tables. All WAAPI arguments will be passed to the Lua script in the `wa_args` global variable, as a Lua table. Define your own key-values in the WAAPI arguments and access them from the Lua code. Use `wa_call` to call a WAAPI function from the Lua script. See [ak.wwise.waapi.getFunctions](ak_wwise_waapi_getfunctions.html) and [ak.wwise.waapi.getSchema](ak_wwise_waapi_getschema.html) to learn more about the functions available and their schema before using `wa_call`. If both `luaScript` and `luaString` are provided, the script file will be executed first, followed by the string code. Note that the Lua environment is reset at each call to this function.

[ak.wwise.core.gameParameter.setRange](ak_wwise_core_gameparameter_setrange.html)   
Sets the Min and Max properties on a Game Parameter. Modifies the RTPC curves and blend tracks that use this Game Parameter for their X axis.

[ak.wwise.core.getInfo](ak_wwise_core_getinfo.html)   
检索全局 Wwise 信息。

[ak.wwise.core.getProjectInfo](ak_wwise_core_getprojectinfo.html)   
检索有关当前所打开工程的信息，包括平台、语言和工程目录。

[ak.wwise.core.log.addItem](ak_wwise_core_log_additem.html)   
Adds a new item to the logs on the specified channel.

[ak.wwise.core.log.clear](ak_wwise_core_log_clear.html)   
Clears the logs on the specified channel.

[ak.wwise.core.log.get](ak_wwise_core_log_get.html)   
检索特定通道的最新日志。See [ak.wwise.core.log.itemAdded](ak_wwise_core_log_itemadded.html) to be notified when an item is added to the log. The log is empty when used in WwiseConsole.

[ak.wwise.core.mediaPool.get](ak_wwise_core_mediapool_get.html)   
Retrieve files from Media Pool. Use the return options to specify which properties of the files to return.

[ak.wwise.core.mediaPool.getFields](ak_wwise_core_mediapool_getfields.html)   
Retrieve all fields present in the Media Pool. You can then use the fields to query the Media Pool. The Media Pool discovers some fields when it scans audio files. Others, such as WAV fields, are always available.

[ak.wwise.core.object.copy](ak_wwise_core_object_copy.html)   
将对象复制到给定父对象。Note that if a Work Unit is copied, the operation cannot be undone and the project will be saved.

[ak.wwise.core.object.create](ak_wwise_core_object_create.html)   
创建 'type' 类型的对象作为 'parent' 的子对象。See [导入音频文件和创建架构](waapi_import.html) for more information about creating objects. Also see [ak.wwise.core.audio.import](ak_wwise_core_audio_import.html) to import audio files to Wwise. To create Effect or Source plug-ins, use [ak.wwise.core.object.set](ak_wwise_core_object_set.html), and see [Wwise 对象参考](wobjects_index.html) for the classId.

[ak.wwise.core.object.delete](ak_wwise_core_object_delete.html)   
删除给定对象。Note that if a Work Unit is deleted, the operation cannot be undone and the project will be saved.

[ak.wwise.core.object.diff](ak_wwise_core_object_diff.html)   
将源对象的属性和列表与目标对象进行比对。

[ak.wwise.core.object.get](ak_wwise_core_object_get.html)   
按照选项中所作指定针对每个对象执行查询并在查询结果中返回数据。该查询可指定 'waql' 或 'from' 参数以及可选的 'transform' 参数。See [使用 Wwise Authoring Query Language (WAQL)](waql_introduction.html) or [查询 Wwise 工程](waapi_query.html) for more information. See [返回选项](waapi_query.html#waapi_query_return) to learn about options.

[ak.wwise.core.object.getAttenuationCurve](ak_wwise_core_object_getattenuationcurve.html)   
针对给定 Attenuation 对象获取给定 Attenuation 曲线。

[ak.wwise.core.object.getPropertyAndReferenceNames](ak_wwise_core_object_getpropertyandreferencenames.html)   
检索包含对象属性和引用名称的列表。

[ak.wwise.core.object.getPropertyInfo](ak_wwise_core_object_getpropertyinfo.html)   
检索有关对象属性的信息。注意，此函数并不返回属性的值。To retrieve the value of a property, see [ak.wwise.core.object.get](ak_wwise_core_object_get.html) and [返回选项](waapi_query.html#waapi_query_return).

[ak.wwise.core.object.getPropertyNames](ak_wwise_core_object_getpropertynames.html)   
[ak.wwise.core.object.getTypes](ak_wwise_core_object_gettypes.html)   
检索包含 Wwise 对象模型中注册的所有对象类型的列表。此函数返回 [Wwise 对象参考](wobjects_index.html) 的对应项。

[ak.wwise.core.object.isLinked](ak_wwise_core_object_islinked.html)   
Indicates whether a property, reference, or object list is bound to a particular platform or to all platforms.

[ak.wwise.core.object.isPropertyEnabled](ak_wwise_core_object_ispropertyenabled.html)   
若依据所基于的属性的值启用了属性，则返回 true。

[ak.wwise.core.object.move](ak_wwise_core_object_move.html)   
将对象移动到给定父对象。返回被移动的对象。

[ak.wwise.core.object.pasteProperties](ak_wwise_core_object_pasteproperties.html)   
将某一对象的属性、引用和列表粘贴到若干目标对象。仅粘贴源对象和目标对象之间存在差异的属性、引用和列表。See [Wwise 对象参考](wobjects_index.html) for more information on the properties, references and lists available on each object type.

[ak.wwise.core.object.set](ak_wwise_core_object_set.html)   
允许批量处理以下操作：在子对象层级结构下创建对象；在列表中创建对象；设置名称、备注、属性和引用。See [导入音频文件和创建架构](waapi_import.html) for more information about creating objects. Also see [ak.wwise.core.audio.import](ak_wwise_core_audio_import.html) to import audio files to Wwise.

[ak.wwise.core.object.setAttenuationCurve](ak_wwise_core_object_setattenuationcurve.html)   
针对给定 Attenuation 对象设置给定 Attenuation 曲线。

[ak.wwise.core.object.setLinked](ak_wwise_core_object_setlinked.html)   
Link or unlink a property/reference or object list to a particular platform.

[ak.wwise.core.object.setName](ak_wwise_core_object_setname.html)   
对对象进行重命名。

[ak.wwise.core.object.setNotes](ak_wwise_core_object_setnotes.html)   
设置对象的备注。

[ak.wwise.core.object.setProperty](ak_wwise_core_object_setproperty.html)   
针对特定平台设置对象的属性值。See [Wwise 对象参考](wobjects_index.html) for more information on the properties available on each object type. See [ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html) to set a reference to an object. See [ak.wwise.core.object.get](ak_wwise_core_object_get.html) to obtain the value of a property for an object.

[ak.wwise.core.object.setRandomizer](ak_wwise_core_object_setrandomizer.html)   
针对特定平台设置对象属性的 Randomizer 值。See [Wwise 对象参考](wobjects_index.html) for more information on the properties available on each object type.

[ak.wwise.core.object.setReference](ak_wwise_core_object_setreference.html)   
设置对象的引用值。See [Wwise 对象参考](wobjects_index.html) for more information on the references available on each object type.

[ak.wwise.core.object.setStateGroups](ak_wwise_core_object_setstategroups.html)   
Sets the State Group objects associated with an object. Note, this will remove any previously associated State Group.

[ak.wwise.core.object.setStateProperties](ak_wwise_core_object_setstateproperties.html)   
Set the state properties of an object. Note, this will remove any previous state property, including the default ones.

[ak.wwise.core.ping](ak_wwise_core_ping.html)   
Verify if WAAPI is currently available.

[ak.wwise.core.plugin.getList](ak_wwise_core_plugin_getlist.html)   
[ak.wwise.core.plugin.getProperties](ak_wwise_core_plugin_getproperties.html)   
[ak.wwise.core.plugin.getProperty](ak_wwise_core_plugin_getproperty.html)   
[ak.wwise.core.profiler.enableProfilerData](ak_wwise_core_profiler_enableprofilerdata.html)   
指定所要捕获的数据的类型。不沿用用户的 Profiler Settings。

[ak.wwise.core.profiler.getAudioObjects](ak_wwise_core_profiler_getaudioobjects.html)   
在特定性能分析器捕获时间点检索 Audio Object。

[ak.wwise.core.profiler.getBusses](ak_wwise_core_profiler_getbusses.html)   
在特定性能分析器捕获时间检索总线。

[ak.wwise.core.profiler.getCpuUsage](ak_wwise_core_profiler_getcpuusage.html)   
Retrieves CPU usage statistics at a specific profiler capture time. This data can also be found in the Advanced Profiler, under the CPU tab. To ensure the CPU data is received, see [ak.wwise.core.profiler.enableProfilerData](ak_wwise_core_profiler_enableprofilerdata.html). The returned data includes "Inclusive" and "Exclusive" values, where "Inclusive" refers to the time spent in the element plus the time spent in any called elements, and "Exclusive" values pertain to execution only within the element itself.

[ak.wwise.core.profiler.getCursorTime](ak_wwise_core_profiler_getcursortime.html)   
返回给定性能分析器光标的当前时间（毫秒）。

[ak.wwise.core.profiler.getGameObjects](ak_wwise_core_profiler_getgameobjects.html)   
在特定性能分析器捕获时间点检索游戏对象。

[ak.wwise.core.profiler.getLoadedMedia](ak_wwise_core_profiler_getloadedmedia.html)   
Retrieves the loaded media at a specific profiler capture time. This data can also be found in the Advanced Profiler, under the Loaded Media tab. To ensure the Loaded Media data is received, see [ak.wwise.core.profiler.enableProfilerData](ak_wwise_core_profiler_enableprofilerdata.html).

[ak.wwise.core.profiler.getMeters](ak_wwise_core_profiler_getmeters.html)   
Retrieves the Meter data for all registered busses, aux busses and devices. Only the Main Audio Bus is registered by default. Use [ak.wwise.core.profiler.registerMeter](ak_wwise_core_profiler_registermeter.html) for other busses, before retrieval of the meter data.

[ak.wwise.core.profiler.getPerformanceMonitor](ak_wwise_core_profiler_getperformancemonitor.html)   
Retrieves the Performance Monitor statistics at a specific profiler capture time. See [Wwise Authoring Performance Monitor Counter Identifiers](globalcountersids.html) for the available counters.

[ak.wwise.core.profiler.getRTPCs](ak_wwise_core_profiler_getrtpcs.html)   
在特定性能分析器捕获时间检索活跃的 RTPC。

[ak.wwise.core.profiler.getStreamedMedia](ak_wwise_core_profiler_getstreamedmedia.html)   
Retrieves the streaming media at a specific profiler capture time. This data can also be found in the Advanced Profiler, under the Streams tab. To ensure the Streams data is received, see [ak.wwise.core.profiler.enableProfilerData](ak_wwise_core_profiler_enableprofilerdata.html).

[ak.wwise.core.profiler.getVoiceContributions](ak_wwise_core_profiler_getvoicecontributions.html)   
检索影响声部路径的声部音量、高通滤波和低通滤波的所有参数（通过 Pipeline ID 进行解析）。

[ak.wwise.core.profiler.getVoices](ak_wwise_core_profiler_getvoices.html)   
在特定性能分析器捕获时间检索声部。

[ak.wwise.core.profiler.registerMeter](ak_wwise_core_profiler_registermeter.html)   
Registers a bus, an aux bus or device to receive meter data. Only the Main Audio Bus is registered by default. Use [ak.wwise.core.profiler.getMeters](ak_wwise_core_profiler_getmeters.html) to retrieve the meter data after registering. Every call to ak.wwise.core.profiler.registerMeter must have a matching call to [ak.wwise.core.profiler.unregisterMeter](ak_wwise_core_profiler_unregistermeter.html).

[ak.wwise.core.profiler.saveCapture](ak_wwise_core_profiler_savecapture.html)   
Saves profiler as a .prof file according to the given file path.

[ak.wwise.core.profiler.startCapture](ak_wwise_core_profiler_startcapture.html)   
开始捕获性能分析器数据，并在捕获开始时返回时间（毫秒）。

[ak.wwise.core.profiler.stopCapture](ak_wwise_core_profiler_stopcapture.html)   
停止捕获性能分析器数据，并在捕获结束时返回时间（毫秒）。

[ak.wwise.core.profiler.unregisterMeter](ak_wwise_core_profiler_unregistermeter.html)   
Unregisters a bus or device that was registered with [ak.wwise.core.profiler.registerMeter](ak_wwise_core_profiler_registermeter.html).

[ak.wwise.core.project.save](ak_wwise_core_project_save.html)   
保存当前工程。

[ak.wwise.core.remote.connect](ak_wwise_core_remote_connect.html)   
Connects the Wwise Authoring application to a Wwise Sound Engine running executable or to a saved profile file. 主机必须在运行代码且启用了通信。若仅提供了 "host"，则将 Wwise 连接到找到的第一个声音引擎实例。为了对不同的实例加以区分，还可提供所要连接的应用程序的名称。

[ak.wwise.core.remote.disconnect](ak_wwise_core_remote_disconnect.html)   
将 Wwise 设计工具与运行可执行文件的 Wwise 声音引擎断开连接。

[ak.wwise.core.remote.getAvailableConsoles](ak_wwise_core_remote_getavailableconsoles.html)   
检索所有可用主机以将 Wwise 设计工具连接到声音引擎实例。

[ak.wwise.core.remote.getConnectionStatus](ak_wwise_core_remote_getconnectionstatus.html)   
检索连接状态。

[ak.wwise.core.sound.setActiveSource](ak_wwise_core_sound_setactivesource.html)   
设置用于给定声音的音频源版本。使用 [ak.wwise.core.object.get](ak_wwise_core_object_get.html) 及 'activeSource' 返回选项获取声音的活跃音频源。

[ak.wwise.core.soundbank.convertExternalSources](ak_wwise_core_soundbank_convertexternalsources.html)   
按照 wsources 文件中所述对工程的外部源文件进行转码，并将其放在默认文件夹或由输出参数指定的文件夹中。External Source 是在 Wwise 里您可以放到声音对象中的一种特殊类型的源（Source）。它表明在运行时将采用真实声音数据。若 SoundBank 生成也会触发 External Source 转码，则可利用此操作来处理未包含在 Wwise 工程中的源。Please see Wwise SDK help page "Integrating External Sources".

[ak.wwise.core.soundbank.generate](ak_wwise_core_soundbank_generate.html)   
Generate a list of SoundBanks with the import definition specified in the WAAPI request. If you do not write the SoundBanks to disk, subscribe to [ak.wwise.core.soundbank.generated](ak_wwise_core_soundbank_generated.html) to receive SoundBank structure info and the bank data as base64. Note: This is a synchronous operation.

[ak.wwise.core.soundbank.getInclusions](ak_wwise_core_soundbank_getinclusions.html)   
检索 SoundBank 的 Inclusion 列表。

[ak.wwise.core.soundbank.processDefinitionFiles](ak_wwise_core_soundbank_processdefinitionfiles.html)   
从给定文件导入 SoundBank 定义。可指定多个文件。打开 WAAPI 日志查看状态消息。

[ak.wwise.core.soundbank.setInclusions](ak_wwise_core_soundbank_setinclusions.html)   
修改 SoundBank 的 Inclusion 列表。'operation' 参数决定 'inclusions' 参数如何修改 SoundBank 的 Inclusion 列表；可在 SoundBank 的 Inclusion 列表中添加/移除/替换 'inclusions'。

[ak.wwise.core.sourceControl.add](ak_wwise_core_sourcecontrol_add.html)   
Add files to source control. Equivalent to Mark for Add for Perforce.

[ak.wwise.core.sourceControl.checkOut](ak_wwise_core_sourcecontrol_checkout.html)   
Check out files from source control. Equivalent to Check Out for Perforce.

[ak.wwise.core.sourceControl.commit](ak_wwise_core_sourcecontrol_commit.html)   
Commit files to source control. Equivalent to Submit Changes for Perforce.

[ak.wwise.core.sourceControl.delete](ak_wwise_core_sourcecontrol_delete.html)   
Delete files from source control. Equivalent to Mark for Delete for Perforce.

[ak.wwise.core.sourceControl.getSourceFiles](ak_wwise_core_sourcecontrol_getsourcefiles.html)   
Retrieve all original files.

[ak.wwise.core.sourceControl.getStatus](ak_wwise_core_sourcecontrol_getstatus.html)   
Get the source control status of the specified files.

[ak.wwise.core.sourceControl.move](ak_wwise_core_sourcecontrol_move.html)   
Move or rename files in source control. Always pass the same number of elements in files and newFiles. Equivalent to Move for Perforce.

[ak.wwise.core.sourceControl.revert](ak_wwise_core_sourcecontrol_revert.html)   
Revert changes to files in source control.

[ak.wwise.core.sourceControl.setProvider](ak_wwise_core_sourcecontrol_setprovider.html)   
Change the source control provider and credentials. This is the same setting as the Source Control option in the Project Settings dialog in Wwise.

[ak.wwise.core.switchContainer.addAssignment](ak_wwise_core_switchcontainer_addassignment.html)   
将 Switch Container 的子对象指派给 Switch。此函数相当于将子对象拖放到 Assigned Objects 视图中所列的 State。对于每个 State，都会在末尾添加子对象。

[ak.wwise.core.switchContainer.getAssignments](ak_wwise_core_switchcontainer_getassignments.html)   
返回包含 Switch Container 子对象和 State 之间的指派的列表。

[ak.wwise.core.switchContainer.removeAssignment](ak_wwise_core_switchcontainer_removeassignment.html)   
移除 Switch Container 的子对象和 State 之间的指派。

[ak.wwise.core.transport.create](ak_wwise_core_transport_create.html)   
针对给定 Wwise 对象创建走带对象。可使用返回的走带对象来播放、停止、暂停和继续播放 Wwise 对象（通过另一走带函数实现）。

[ak.wwise.core.transport.destroy](ak_wwise_core_transport_destroy.html)   
销毁给定走带对象。

[ak.wwise.core.transport.executeAction](ak_wwise_core_transport_executeaction.html)   
针对给定走带对象或所有走带对象（如未作任何指定）执行某项动作。

[ak.wwise.core.transport.getList](ak_wwise_core_transport_getlist.html)   
返回包含走带对象的列表。

[ak.wwise.core.transport.getState](ak_wwise_core_transport_getstate.html)   
获取给定走带对象的 State。

[ak.wwise.core.transport.prepare](ak_wwise_core_transport_prepare.html)   
准备对象及其依赖项以供播放。在通过 IAkGlobalPluginContext 调用 PostEventSync 或 PostMIDIOnEventSync 之前使用此函数。

[ak.wwise.core.undo.beginGroup](ak_wwise_core_undo_begingroup.html)   
开始某个 Undo Group。对于执行的每项 ak.wwise.core.beginUndoGroup 调用，确保仅调用 [ak.wwise.core.undo.endGroup](ak_wwise_core_undo_endgroup.html) 一次。可嵌套对 ak.wwise.core.undo.beginGroup 的调用。在关闭 WAMP 会话时，将检查并确认是否所有 Undo Group 均已关闭。若未全部关闭，则针对每个仍处于打开状态的分组调用 cancelGroup。

[ak.wwise.core.undo.cancelGroup](ak_wwise_core_undo_cancelgroup.html)   
取消最后一个 Undo Group。

[ak.wwise.core.undo.endGroup](ak_wwise_core_undo_endgroup.html)   
结束最后一个 Undo Group。

[ak.wwise.core.undo.redo](ak_wwise_core_undo_redo.html)   
Redoes the last operation in the Undo stack.

[ak.wwise.core.undo.undo](ak_wwise_core_undo_undo.html)   
撤消 Undo 堆栈中的最后一项操作。

[ak.wwise.core.workUnit.load](ak_wwise_core_workunit_load.html)   
Load a Work Unit that was previously unloaded. The Undo history will be cleared.

[ak.wwise.core.workUnit.unload](ak_wwise_core_workunit_unload.html)   
Unload a Work Unit. No object contained in the Work Unit will be available after this call. If the Work Unit is modified and not saved, the function will return error. The Undo history will be cleared.

[ak.wwise.debug.enableAsserts](ak_wwise_debug_enableasserts.html)   
启用 Debug 断言。每次使用 'false' 调用 enableAsserts 都会导致 ref 计数递增。若使用 true 调用，则 ref 计数递减。此函数仅在 Debug 版本中可用。

[ak.wwise.debug.enableAutomationMode](ak_wwise_debug_enableautomationmode.html)   
针对 Wwise 启用或禁用自动化模式。这样可以减少由消息框和对话框造成的潜在中断。比如，在启用自动化模式后，将自动允许迁移工程、保存工程加载日志、接受 EULA、工程许可协议和一般弹出消息框。

[ak.wwise.debug.generateToneWAV](ak_wwise_debug_generatetonewav.html)   
Generate a WAV file playing a tone with a simple envelope and save it to the specified location. This is provided as a utility to generate test WAV files.

[ak.wwise.debug.getWalTree](ak_wwise_debug_getwaltree.html)   
Retrieves the WAL tree, which describes the nodes that are synchronized in the Sound Engine. 仅限私人使用。

[ak.wwise.debug.restartWaapiServers](ak_wwise_debug_restartwaapiservers.html)   
Restart WAAPI servers. For internal use only.

[ak.wwise.debug.testAssert](ak_wwise_debug_testassert.html)   
仅限私人使用。

[ak.wwise.debug.testCrash](ak_wwise_debug_testcrash.html)   
仅限私人使用。

[ak.wwise.debug.validateCall](ak_wwise_debug_validatecall.html)   
Validate the arguments, options and result of a WAAPI function call. Does not actually call the function. 此函数仅在 Debug 版本中可用。

[ak.wwise.ui.bringToForeground](ak_wwise_ui_bringtoforeground.html)   
将 Wwise 主窗口调到前台。See SetForegroundWindow and AllowSetForegroundWindow on MSDN for more information on the restrictions. See ak.wwise.core.getInfo to obtain the Wwise process ID for AllowSetForegroundWindow.

[ak.wwise.ui.captureScreen](ak_wwise_ui_capturescreen.html)   
捕获相对于视图的部分 Wwise UI。

[ak.wwise.ui.commands.execute](ak_wwise_ui_commands_execute.html)   
执行命令。有些命令可将一系列对象作为参数。See [Wwise 设计工具命令标识符](globalcommandsids.html) for the available commands.

[ak.wwise.ui.commands.getCommands](ak_wwise_ui_commands_getcommands.html)   
获取命令列表。

[ak.wwise.ui.commands.register](ak_wwise_ui_commands_register.html)   
注册包含扩展命令的数组。保留注册的命令，直到 Wwise 进程终止。See [定义命令扩展](defining_custom_commands.html) for more information about registering commands. Also see [ak.wwise.ui.commands.executed](ak_wwise_ui_commands_executed.html).

[ak.wwise.ui.commands.unregister](ak_wwise_ui_commands_unregister.html)   
注销包含扩展 UI 命令的数组。

[ak.wwise.ui.getSelectedFiles](ak_wwise_ui_getselectedfiles.html)   
Retrieves the list of files currently selected by the user in the active view. Note that this function is not available in WwiseConsole.

[ak.wwise.ui.getSelectedObjects](ak_wwise_ui_getselectedobjects.html)   
检索用户当前在活跃视图中选中的一系列对象。Note that this function is not available in WwiseConsole.

[ak.wwise.ui.layout.closeView](ak_wwise_ui_layout_closeview.html)   
Requests to close a view by its unique id. The view might not yet be closed when returning from this function.

[ak.wwise.ui.layout.dockView](ak_wwise_ui_layout_dockview.html)   
Dock a floating view into a layout.

[ak.wwise.ui.layout.getCurrentLayoutName](ak_wwise_ui_layout_getcurrentlayoutname.html)   
Retrieves the current layout name.

[ak.wwise.ui.layout.getElementRectangle](ak_wwise_ui_layout_getelementrectangle.html)   
Retrieves the current allocated rectangle of a layout element. An empty rect is returned if the element is not found.

[ak.wwise.ui.layout.getLayout](ak_wwise_ui_layout_getlayout.html)   
Serializes a specific layout into a JSON format.

[ak.wwise.ui.layout.getLayoutNames](ak_wwise_ui_layout_getlayoutnames.html)   
Retrieves a list of the factory layout names.

[ak.wwise.ui.layout.getOrCreateView](ak_wwise_ui_layout_getorcreateview.html)   
Gets a view, if it exists in the current layout, or creates a new one.

[ak.wwise.ui.layout.getViewInstances](ak_wwise_ui_layout_getviewinstances.html)   
Retrieves a list of all view instances of a layout.

[ak.wwise.ui.layout.getViewTypes](ak_wwise_ui_layout_getviewtypes.html)   
Retrieves a list of all view types registered in Wwise.

[ak.wwise.ui.layout.moveSplitter](ak_wwise_ui_layout_movesplitter.html)   
Moves a splitter by a delta given in pixels.

[ak.wwise.ui.layout.removeLayout](ak_wwise_ui_layout_removelayout.html)   
Unregisters a temporary layout, previously registered with [ak.wwise.ui.layout.setLayout](ak_wwise_ui_layout_setlayout.html).

[ak.wwise.ui.layout.resetLayouts](ak_wwise_ui_layout_resetlayouts.html)   
Reset layouts to their default state.

[ak.wwise.ui.layout.setLayout](ak_wwise_ui_layout_setlayout.html)   
Registers a new layout from a JSON format.

[ak.wwise.ui.layout.switchLayout](ak_wwise_ui_layout_switchlayout.html)   
Switches the current layout.

[ak.wwise.ui.layout.undockView](ak_wwise_ui_layout_undockview.html)   
Undock a view from a layout.

[ak.wwise.ui.project.close](ak_wwise_ui_project_close.html)   
关闭当前工程。

[ak.wwise.ui.project.create](ak_wwise_ui_project_create.html)   
Creates, saves and opens new empty project, specified by path and platform. The project has no factory setting WorkUnit. Please see [ak.wwise.core.project.loaded](ak_wwise_core_project_loaded.html) for further explanations on how to be notified when the operation has completed.

[ak.wwise.ui.project.open](ak_wwise_ui_project_open.html)   
打开由路径指定的工程。Please see [ak.wwise.core.project.loaded](ak_wwise_core_project_loaded.html) for further explanations on how to be notified when the operation has completed.

[ak.wwise.waapi.getFunctions](ak_wwise_waapi_getfunctions.html)   
检索包含函数的列表。

[ak.wwise.waapi.getSchema](ak_wwise_waapi_getschema.html)   
检索 WAAPI URI 的 JSON 架构。

[ak.wwise.waapi.getTopics](ak_wwise_waapi_gettopics.html)   
检索包含客户端可订阅主题的列表。