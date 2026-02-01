# Wwise Authoring API Reference - Topics

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Authoring API Reference - Topics

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。

[ak.wwise.core.audio.imported](ak_wwise_core_audio_imported.html)   
在“导入”操作结束时发送。

[ak.wwise.core.log.itemAdded](ak_wwise_core_log_itemadded.html)   
在条目被添加到日志中时发送。此项可用于检索被添加到 SoundBank 生成日志的条目。To retrieve the complete log, see [ak.wwise.core.log.get](ak_wwise_core_log_get.html).

[ak.wwise.core.object.attenuationCurveChanged](ak_wwise_core_object_attenuationcurvechanged.html)   
在 Attenuation 曲线发生更改时发送。

[ak.wwise.core.object.attenuationCurveLinkChanged](ak_wwise_core_object_attenuationcurvelinkchanged.html)   
在 Attenuation 曲线的 Link/Unlink 设置发生更改时发送。

[ak.wwise.core.object.childAdded](ak_wwise_core_object_childadded.html)   
在对象被作为子对象添加到另一对象时发送。See [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) to receive changes in batch.

[ak.wwise.core.object.childRemoved](ak_wwise_core_object_childremoved.html)   
在从另一对象的子对象移除对象时发送。See [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) to receive changes in batch.

[ak.wwise.core.object.created](ak_wwise_core_object_created.html)   
在创建对象时发送。See [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) to receive changes in batch.

[ak.wwise.core.object.curveChanged](ak_wwise_core_object_curvechanged.html)   
在一条或多条曲线发生更改时发送。

[ak.wwise.core.object.nameChanged](ak_wwise_core_object_namechanged.html)   
在对象被重命名时发送。发布被重命名的对象。See [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) to receive changes in batch.

[ak.wwise.core.object.notesChanged](ak_wwise_core_object_noteschanged.html)   
在对象的备注发生更改时发送。

[ak.wwise.core.object.postDeleted](ak_wwise_core_object_postdeleted.html)   
在对象被删除后发送。See [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) to receive changes in batch.

[ak.wwise.core.object.preDeleted](ak_wwise_core_object_predeleted.html)   
在对象被删除前发送。See [ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html) to receive changes in batch.

[ak.wwise.core.object.propertyChanged](ak_wwise_core_object_propertychanged.html)   
在对象的被监视属性发生更改时发送。

[ak.wwise.core.object.referenceChanged](ak_wwise_core_object_referencechanged.html)   
在对象引用发生更改时发送。

[ak.wwise.core.object.structureChanged](ak_wwise_core_object_structurechanged.html)   
Sent when the project structure changes. Publishes a summary of the changes. The publication is sent after the undo stack is modified. The changes are grouped in batch and redundant changes are collapsed.

[ak.wwise.core.profiler.captureLog.itemAdded](ak_wwise_core_profiler_capturelog_itemadded.html)   
在新的条目被添加到 Capture Log 中时发送。注意，将发送所有条目。不会像 Capture Log 视图一样应用筛选。

[ak.wwise.core.profiler.gameObjectRegistered](ak_wwise_core_profiler_gameobjectregistered.html)   
在注册游戏对象后发送。

[ak.wwise.core.profiler.gameObjectReset](ak_wwise_core_profiler_gameobjectreset.html)   
在重置游戏对象后发送（比如在执行性能分析时关闭与游戏的连接）。

[ak.wwise.core.profiler.gameObjectUnregistered](ak_wwise_core_profiler_gameobjectunregistered.html)   
在注销游戏对象后发送。

[ak.wwise.core.profiler.stateChanged](ak_wwise_core_profiler_statechanged.html)   
在 State Group 状态发生变化时发送。此订阅不需要启动 Profiler Capture Log。

[ak.wwise.core.profiler.switchChanged](ak_wwise_core_profiler_switchchanged.html)   
在 Switch Group 状态发生变化时发送。此函数不需要启动 Profiler Capture Log。

[ak.wwise.core.project.loaded](ak_wwise_core_project_loaded.html)   
在工程加载成功时发送。

[ak.wwise.core.project.postClosed](ak_wwise_core_project_postclosed.html)   
在工程完全关闭后发送。

[ak.wwise.core.project.preClosed](ak_wwise_core_project_preclosed.html)   
在工程开始关闭时发送。

[ak.wwise.core.project.saved](ak_wwise_core_project_saved.html)   
在工程成功保存后发送。

[ak.wwise.core.soundbank.generated](ak_wwise_core_soundbank_generated.html)   
在生成单个 SoundBank 后发送。可在 SoundBank 生成期间发送多次，针对生成的每个 SoundBank 以及平台。To generate SoundBanks, see [ak.wwise.core.soundbank.generate](ak_wwise_core_soundbank_generate.html) or [ak.wwise.ui.commands.execute](ak_wwise_ui_commands_execute.html) with one of the SoundBank generation commands. See [Wwise 设计工具命令标识符](globalcommandsids.html) for the list of commands.

[ak.wwise.core.soundbank.generationDone](ak_wwise_core_soundbank_generationdone.html)   
在生成所有 SoundBank 后发送。Note: This notification is only sent when SoundBanks have been generated, it is not a reliable way to determine when [ak.wwise.core.soundbank.generate](ak_wwise_core_soundbank_generate.html) has completed.

[ak.wwise.core.switchContainer.assignmentAdded](ak_wwise_core_switchcontainer_assignmentadded.html)   
在将指派添加到 Switch Container 时发送。

[ak.wwise.core.switchContainer.assignmentRemoved](ak_wwise_core_switchcontainer_assignmentremoved.html)   
在从 Switch Container 中移除指派时发送。

[ak.wwise.core.transport.stateChanged](ak_wwise_core_transport_statechanged.html)   
在走带对象的 State 发生变化时发送。

[ak.wwise.debug.assertFailed](ak_wwise_debug_assertfailed.html)   
在断言失败后发送。此函数仅在 Debug 版本中可用。

[ak.wwise.ui.commands.executed](ak_wwise_ui_commands_executed.html)   
在执行命令时发送。在发布当中发送与所执行命令对应的对象。

[ak.wwise.ui.selectionChanged](ak_wwise_ui_selectionchanged.html)   
在工程中所作选择发生更改时发送。