# Obs/Occ

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > [Advanced Profiler](00-Advanced-Profiler.md) > Obs/Occ

### Obs/Occ

Obs/Occ（声障/声笼）选项卡显示影响游戏对象的声障、声笼、衍射、透射损失、散布和开口等信息。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Game Object | 游戏对象的唯一 ID。 |
| Index/ID | 索引/ID。声音位置的索引和 Spatial Audio 声音路径的哈希 ID（如适用）。您可以使用  [`AK::SoundEngine::SetMultiplePositions()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ad63431938ab1e605a1f6e7fb013c0128.html) API 将索引（从 0 开始）传给游戏对象。若游戏对象只有一个位置，则此列将显示短横线 (-)。在 Spatial Audio 发声体启用衍射和透射时，将显示位置索引并后缀一串字符，以此向声音路径指派唯一标识符。这串字符是个由 Spatial Audio 生成和指派的唯一哈希值。通过结合 Voice Inspector（声部检视器）交叉引用该哈希值，可查看声音路径的音量和滤波贡献；通过结合 Game Object 3D Viewer（游戏对象 3D 查看器）交叉引用该哈希值，可查看声音路径及其虚拟位置。 |
| ListenerID | 听者的唯一 ID。 |
| Obstruction | 声障。针对与给定位置索引和听者对应的游戏对象显示的声障值（百分比）。 |
| Occlusion | 声笼。针对与给定位置索引和听者对应的游戏对象显示的声笼值（百分比）。 |
| Diffraction | 衍射。针对给定声音位置索引和听者显示的衍射系数，表示为百分比值 (0-100%)。 |
| Transmission Loss | 透射损失。针对给定声音位置索引和听者显示的透射损失系数，表示为百分比值 (0-100%)。 |
| Spread | 散布。由 Spatial Audio 指派给此游戏对象的声源散布值。声源散布依据 [`Radial Emitter`](https://www.audiokinetic.com/library/edge/?source=SDK&id=spatial_audio_radial_emitters.html) 的径向边界计算。若游戏对象为 Spatial Audio Room，则依据 Portal 相对于听者的边界计算。  |  |  | | --- | --- | | [备注] | 备注 | | 此处并不显示依据衰减曲线计算得出的散布值。若该值可用于游戏对象上播放的给定声音，则使用其覆盖此处显示的声源散布值。 |    |  |  | | --- | --- | | [技巧] | 技巧 | | 在启用 Obstruction/Occlusion 性能分析数据时，可在 [“Game Object 3D Viewer”一节](../11-Game-Object-3D-Viewer/00-Game-Object-3D-Viewer.md "Game Object 3D Viewer") 中查看给定声音的最终散布值。请参阅[“指定要捕获的信息类型”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/01-指定要捕获的信息类型.md "指定要捕获的信息类型") | |
| Aperture | 开口。开口值代表穿过发声体和听者之间声音路径的最小 Portal 开口，可用于限制特定声音的最大散布效果。每个声音的散布都将被限制在开口值范围之内，无论其是通过  [`AK::SpatialAudio::SetGameObjectRadius()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_spatial_audio_a8c2e8f50769b6ae29dcbcb636e9c33f2.html)  API 还是 Attenuation ShareSet 中的散布曲线定义。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从声音引擎捕获数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/00-从声音引擎捕获数据.md "从声音引擎捕获数据")
- [“使用 Performance Monitor 进行监控和故障排查”一节](../../../07-完善工程/06-性能分析/09-使用-Performance-Monitor-进行监控和故障排查.md "使用 Performance Monitor 进行监控和故障排查")

---