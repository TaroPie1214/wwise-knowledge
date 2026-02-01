# Voice Inspector

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [参考主题](../00-参考主题.md) > [Profiler 视图](00-Profiler-视图.md) > Voice Inspector

## Voice Inspector

The Voice Inspector provides detailed information about Volume, LPF, HPF and DSF (the "value") for selected voice paths processed by a sound. The information displays the values of all contributors to the hierarchy, from the source to the Main Audio Bus, and the runtime value modifications, such as Event Actions, transitions, distance attenuation, and cone angles.

为了在视图中加载信息，必须确保已捕获相应信息，并选择了捕获的时间点。然后，[Voices Graph](04-Voice-Inspector.md#panel_voices_graph) 和 [Contribution List](04-Voice-Inspector.md#panel_contribution) 面板才会显示对应的声部信息。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 有两种类型的数据必须加以分析：Voices 和 Voice Inspector。若不启用前者，则 [“Voice Monitor”一节](09-Voice-Monitor.md "Voice Monitor") 和 [“Voice Inspector”一节](04-Voice-Inspector.md "Voice Inspector") 均不显示任何数据。若不启用后者，则 Voice Inspector 将仅显示以下消息：“This view needs "Voice Inspector Data". Enable it in the [“Profiler Settings”一节](../01-工程/10-Profiler-Settings.md "Profiler Settings").”。为此，可通过单击消息中的链接或视图标题栏中的 View Settings（视图设置）按钮，快速打开 Profiler Settings（性能分析器设置）视图。 |

| 界面元素 | 描述 |
| --- | --- |
|  | 通过单击视图右上角的 View Settings 图标，可打开 [“Profiler Settings”一节](../01-工程/10-Profiler-Settings.md "Profiler Settings")，并指定要捕获的数据类型。若要在 Voice Inspector 中查看信息，必须启用 Voice Inspector Data（声部检视器数据）。 |
| Voice Graph  声部图。此面板显示的内容与 Advanced Profiler（高级性能分析器）的 [“Voices Graph 选项卡”一节](03-Advanced-Profiler/01-Voices-Graph-选项卡.md "Voices Graph 选项卡") 选项卡相同，其中包括经过优化的总线层级结构、每个声部在运行时使用的底层引擎以及声音引擎管理的播放实例。不过，在此并不能按照对象或通过输入文字来筛选结果。 | |
| 视图 | 单击 **View** 选择按钮来显示或隐藏视图中的以下元素：  - **Game Objects**：在视图中显示或隐藏游戏对象。 - **Events**:：在 Graph 视图中显示或隐藏事件。 - **Targets**：在视图中显示或隐藏目标。  目标是指事件要播放的目标对象，目标对象播放时会触发其子音源。在目标为 Random Container 时，启用此选项将同时显示作为事件目标的 Random Container 及其播放的源对象。 - **Virtual Voices**：在视图中显示或隐藏虚声部。 - **Devices**：在视图中显示或隐藏最终输出设备。 - **Volumes**：在视图中显示或隐藏音量值。 - **LPF**：在视图中显示或隐藏 LPF 值。 - **HPF**：在视图中显示或隐藏 HPF 值。 - **DSF**: Displays or hides the DSF values in the graph view. |
| 坐标图视图 | 显示声音引擎生成的各个声部的结构和内容。有关详细信息，请参阅 Voices Graph 选项卡参考文档的 [“坐标图视图”一节](03-Advanced-Profiler/01-Voices-Graph-选项卡.md#graph_view "坐标图视图") 章节。 |
| **Contribution List** | |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Name | 名称。影响选定声部最终值的对象的名称。  The first row always displays **Σ Final Value** for the sum total of the Volume, LPF, HPF and DSF of the selected voice.  下面的分行会显示 Wwise 对象（如总线、容器和声音）的节点。节点下会进一步显示子对象的详细信息，包括 Attenuation 和发声体-听者对。最后一级子节点下会显示 Driver 所改动的对象属性的名称（如 Bus Volume 和 Voice Volume）。 |
| Driver | The cause of a possible change in the Final Value for the voice's Volume, LPF, HPF or DSF. 它可以是游戏参数，也可以是 Wwise 元素（广义来说包括对象、属性和设置）。  **可能的驱动因素：**   - **Music Segment Envelope**（如 Music Track 包含音量曲线） - **Background Music Mute** - **Cone Attenuation** - **Distance Attenuation（距离衰减）** - **闪避** - **Events/Actions**（包括 Set Volume Action、LPF 和 HPF） - **Fade in/out**（包括 Event 产生的所有淡入/淡出） - **HDR Gain**（HDR 窗口更改音量时） - **Live Edit**（用户在连接游戏的情况下执行修改时） - **Modulator**（显示 Modulator 名称和图标 – 可为 LFO、Time 或 Envelope） - **Mute**（在触发 Mute Action 后显示。在 Unmute 后隐藏） - **Obstruction**（显示在 Attenuation 节点下） - **Occlusion**（显示在 Attenuation 节点下） - **Pause**（在触发 Pause Action 后显示。在 Resume 后隐藏） - **Project Value**（Property Editor 中显示的属性值。仅用在执行本地性能分析时） - **Randomizer（随机化器）** - **RTPC**（显示 RTPC 名称） - **SoundBank Value**（从 SoundBank 获取） - **State**（显示 State Group 名称） - **Normalization** (Either loudness normalization or downmix normalization.) - **Switch（切换开关）** - **Diffraction Tapering** - **Smoothing** - **Portal Transition** - **Propagation Path Gain**（Spatial Audio 所作的调节。比如，导入/淡出影响的路径） - **Room Send**（由 Spatial Audio 设置的 Game-Defined Auxiliary Send） - **SetEarlyReflectionsVolume** - **SetGameObjectAuxSendValues** - **SetGameObjectOutputBusVolume** - **Transmission Loss** - **Diffraction** - **User-Defined Sends**  |  |  | | --- | --- | | [技巧] | 技巧 | | For further information on these drivers, see [“有关特定属性显示方式的说明”一节](../../07-完善工程/06-性能分析/10-使用-Voice-Inspector-分析声部.md#voice_inspector_notes_on_properties "有关特定属性显示方式的说明"). | |
| Driver Value | 驱动因素值。特定驱动因素的对应值。 |
| Volume | 音量。驱动因素对声部音量的影响 (dB)，将舍入为最近似的整数值。 |
| LPF | 低通滤波。驱动因素对声部低通滤波器截止频率的影响，以百分比表示。如需了解对应频率，请参阅 [“Wwise 中 LPF 和 HPF 值与截止频率的对应关系”一节](../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系")。 |
| HPF | 高通滤波。驱动因素对声部高通滤波器截止频率的影响，以百分比表示。如需了解对应频率，请参阅 [“Wwise 中 LPF 和 HPF 值与截止频率的对应关系”一节](../../03-设置工程/06-Building-your-sound-and-motion-hierarchies/04-工程层级结构中的属性介绍/02-定义相对属性（音量、音高、LPF、HPF）/01-Low-pass-和-High-pass-Filter-值与截止频率的关系.md#wwise_lpf_value_cutoff_frequencies "Wwise 中 LPF 和 HPF 值与截止频率的对应关系")。 |
| DSF | The impact of the drivers to establish a dual-shelf filter gain (in dB) on the voice. |

**相关主题**

- [设置 Voice Inspector：](../../07-完善工程/06-性能分析/10-使用-Voice-Inspector-分析声部.md#setting_up_voice_inspector "设置 Voice Inspector：")
- [“使用 Voice Inspector 分析声部”一节](../../07-完善工程/06-性能分析/10-使用-Voice-Inspector-分析声部.md "使用 Voice Inspector 分析声部")
- [“有关特定属性显示方式的说明”一节](../../07-完善工程/06-性能分析/10-使用-Voice-Inspector-分析声部.md#voice_inspector_notes_on_properties "有关特定属性显示方式的说明")
- [“筛选 Capture Log”一节](../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/05-筛选-Capture-Log.md "筛选 Capture Log")

---