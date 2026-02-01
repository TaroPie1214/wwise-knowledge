# Capture Log Options

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Capture Log](00-Capture-Log.md) > Capture Log Options

### Capture Log Options

Capture Log Options（捕获日志选项）视图允许根据条目类型、Wwise 对象名称和作用域等一系列筛选选项来在 Capture Log 中加入或移除条目。

| 界面元素 | 描述 |
| --- | --- |
| **Include 关系** | |
| Playback Relation（竖排圆点） | 显示播放关系。显示目标对象所在事件的所有通知，即使它们与目标对象没有直接联系。它会显示所有元素，用蓝点符号链接在一起。 |
| Include game object relations | 包括游戏对象关系。将包含发生在与所选对象具有相同的游戏对象的那些对象上发生的事情。例如，假定您已经选择了 Sound A 作为筛选后的对象，并且它是在已经播放了 Sound B 的某个游戏对象播放。它将在 Capture Log 视图中的该游戏对象上添加所有关于 Sound B 的播放关系。 |
| Include parents and busses（使用 Object Filter 时） | 包含父级和总线。将包含针对所选对象的所有父对象层级和子对象可能连通到的所有总线的通知。 |
| **Scope** | |
| Global | 全局。显示适用于所有游戏对象的条目。 |
| Game object | 游戏对象。仅显示适用于特定游戏对象的条目。 |
| **Types（类型）** | |
| Notifications | 通知。显示来自声音引擎的通知。通知包含声音引擎处理动作的状态。  例如：事件播放。开始延迟。 |
| Markers（标记） | 显示音频文件标记和音乐片段自定义提示。 |
| Event | 显示由 Wwise 或游戏引擎触发的动作事件和对话事件。 |
| Actions | 显示事件中的动作。 |
| Properties | 属性。显示对属性值所做的更改。 |
| States | 状态。显示状态更改。 |
| Switches | 切换开关。显示切换开关更改。 |
| SoundBanks | 显示与 SoundBank 有关的信息，包括 SoundBank 的名称。 |
| Events Preparation（事件准备） | 准备事件。显示使用 [`PrepareEvent()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a98b617d05618e6d18680d198845ff3d7.html)和 [`PrepareGameSyncs()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ad5fc8ab51eecee6511d5c61b03659fa4.html)函数准备的事件和游戏同步器。 |
| Error | 错误。显示声音引擎出现的任何错误。 |
| Messages | 消息。显示声音引擎发送的任何消息。消息通常会传达问题或特殊信息。这些消息可在游戏引擎中进行编程。  例如：未知事件名。主人公的脚步声。 |
| MIDI 事件 | MIDI 事件。显示声音引擎播放的所有 MIDI 事件。  Information derived from the MIDI file is displayed as per the MIDI Events, and especially the Filters, in the [MIDI properties](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/00-MIDI-category-Containers-hierarchy-objects.md#wwiseobject_sound_midi). 其中将显示通道数（1 - 16），MIDI 事件名（Note-on 音符开或 Note-off 音符关），键位以及力度。 |
| API Calls | 显示对声音引擎的 API 调用。这里显示了 API 的大致类别，可根据需要选择或排除，包括：  - [Event](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__events.html) - [RTPC](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__rtpc.html) - [Game](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__states.html)  [Game Syncs](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__switches.html) - [Game Objects](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__gameobjects.html) - [Listener Spatialization （空间定位）](https://www.audiokinetic.com/library/?source=SDK&id=soundengine__listeners.html) - [Positions（定位）](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__3dpos.html) - [Auxiliary Bus](https://www.audiokinetic.com/library/?source=SDK&id=quickstart__sample__integration__environments.html) - [Obstruction/Occlusion](https://www.audiokinetic.com/library/?source=SDK&id=soundengine__obsocc.html) - [Motion（振动）](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__motion.html) - [MIDI](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__midi.html) - [Dynamic Sequence （动态序列）](https://www.audiokinetic.com/library/?source=SDK&id=integrating__elements__dynamicdialogue.html) - [Spatial Audio](https://www.audiokinetic.com/library/?source=SDK&id=spatial__audio.html) - [其他](https://www.audiokinetic.com/library/?source=SDK&id=workingwithsdks__integratingelements.html)  列出的每个调用都将显示相应函数以及传递的参数（如果存在）。 |
|  | Resets the dialog to the default settings. |
|  | 选择列表中的所有类型。 |
|  | 清除列表中所有类型的选择。 |

**相关主题**

- [“筛选 Capture Log”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/05-筛选-Capture-Log.md "筛选 Capture Log")

---