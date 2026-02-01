# Switch Container tab: sound and motion objects

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Project Explorer](../../00-Project-Explorer.md) > [Audio tab](../00-Audio-tab.md) > [Common tabs and categories: audio structures](00-Common-tabs-and-categories-audio-structures.md) > Switch Container tab: sound and motion objects

#### Switch Container tab: sound and motion objects

In the Switch Container tab you can assign the objects within a Switch Container to a particular Switch or State. 请参阅 [“为 Switch 和 State 添加和移除对象”一节](../../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/03-定义-Switch-Container-的内容和行为.md#adding_and_removing_objects_from_switch_state "为 Switch 和 State 添加和移除对象")。

| Switch Container（切换容器） | |
| --- | --- |
| 界面元素 | 描述 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| (More Options) | Opens the following options:  - **Clear All**:   Removes all associations from the list. - **Automatically Assign   with Best Match**: Assigns objects to   matching groups. - **Expand All**:   Expands all groups in the Primary Editor. - **Collapse All**:   Collapses all groups in the Primary   Editor. |
| (Remove Selected Association(s)) | Click Remove Selected Association(s) to remove the selected associations from the list. |
| Assigned Object | 指派的对象。Switch Container 内指派到特定 Switch 或 State 的对象列表。通过指派对象，您可以定义针对各个 Switch 或 State 将播放的对象。If several objects are assigned to a Switch, they will all be played back simultaneously at runtime.  Click  to add objects to a group. |
| Waveform | The waveform of the Sound SFX or Sound Voice. |
| First Occurrence Only | 播放。确定是在游戏引擎每次触发 Switch Container 时播放对象，还是仅在切换 Switch 时播放对象。  若启用 First Occurrence Only 选项，则仅在 Switch 第一次改变后播放对象。随后触发同一 Switch Container 将不会播放对象。若禁用 First Occurrence Only 选项，则每次游戏引擎触发 Switch Container 时均播放对象。  Default value: false |
| Continue to play on Switch change | 切换开关改变时继续播放。决定在触发新的 Switch 时是否继续播放多个 Switch 中的音乐对象。  如果选择了此选项并且音乐对象位于两个 Switch 中，则音乐对象将继续播放，就像 Switch 没有发生切换一样。如果 Switch 发生切换但没有选择此选项，则音乐对象将在下一同步点停止播放，然后再从头开始播放。  Default value: true |
| Fade-in Time | 淡入。当 Switch 发生切换时对象淡入所需要的时间。  只有当 Switch 行为设为 Continuous 时，此选项才可用。  单位：s  Default value: 0  Range: 0 to 60 |
| Fade-out Time | 当 Switch 发生切换时对象淡出所需要的时间。  单位：s  Default value: 0  Range: 0 to 60 |

---