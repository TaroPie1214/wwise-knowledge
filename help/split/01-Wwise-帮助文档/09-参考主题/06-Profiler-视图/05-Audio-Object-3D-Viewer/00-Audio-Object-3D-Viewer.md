# Audio Object 3D Viewer

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Profiler 视图](../00-Profiler-视图.md) > Audio Object 3D Viewer

## Audio Object 3D Viewer

Audio Object 3D Viewer（音频对象 3D 查看器）提供了 Audio Object 相对于听者位置和朝向的详细定位信息。同时，视图中还显示了散布范围（表示为围绕听者的球体）。此视图中显示的信息基于当前性能分析器光标时间。

Audio Object 3D Viewer 可与 [“Audio Object List”一节](../06-Audio-Object-List.md "Audio Object List") 结合使用。要想在 Audio Object 3D Viewer 中显示内容，必须在 Audio Object List（音频对象列表）中选择 Audio Object 情境。Audio Object 情境包括总线、游戏对象和效果器处理阶段。Audio Object 情境由 Audio Object List 中的 Visibility（可见性）图标 ![](../../../../images/enable_filter_icon.png) 表示。通过单击 Audio Object List 中的 Audio Object，可自动在 Audio Object 3D Viewer 中选择情境。

您可以使用以下控件在 3D 视图中进行浏览：

- 若要围绕中心调节摄像机位置，请单击、按住并拖动鼠标左键（仅可在 Perspective 摄像机模式下执行此操作）。
- 若要进行缩放，请使用鼠标滚轮慢慢调节，或者单击、按住并拖动鼠标右键。
- 若要更改摄像机预设，请使用工具栏上的摄像机菜单按钮。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若要在此视图中显示信息，则须在 [“Profiler Settings”一节](../../01-工程/10-Profiler-Settings.md "Profiler Settings") 中启用 **Audio Object Data** 以捕获数据，同时在捕获会话中选择时间点。 |

| 筛选器工具栏 | |
| --- | --- |
| This view includes a filtering toolbar, which allows you to reduce the amount of information displayed in the view so you can focus on specific elements. 有关更多详细信息，请参阅 [“在性能分析视图中筛选数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/03-在性能分析视图中筛选数据.md "在性能分析视图中筛选数据") 章节。 | |
|  | |
|  | **Unlink Filter**：禁止在多个筛选器视图之间同步。 |
|  | **Text Filter**：通过指定文本来筛选内容。系统会将您所指定的字词与内容中所含名称或字符串的开头进行匹配。键入的字词越多，显示的结果越细化。匹配项不区分大小写。有关高级用法的信息，请参阅“[“使用性能分析器筛选器表达式”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/04-使用性能分析器筛选器表达式.md "使用性能分析器筛选器表达式")”。 |
|  | **Object Filter**：通过指定 Wwise 对象来筛选内容。系统会将您所指定的 Wwise 工程对象与视图中的内容进行匹配。同时，还会依据对象关系（如父子对象关系和输出总线关系）对内容进行匹配。 |
|  | **Browse Object Filter**：显示 Project Explorer 浏览器，以便选择所要筛选的对象。 |
|  | **Mute/Solo Filtering**：若启用，则从结果中排除激活了 Mute 的对象，而只显示激活了 Solo 的对象。 |
|  | **Options**：显示其他操作。 |

| 界面元素 | 描述 |
| --- | --- |
|  | Click the View Settings icon in the upper right corner of the view to open the [“Profiler Settings”一节](../../01-工程/10-Profiler-Settings.md "Profiler Settings") dialog, where you can specify the type of data to capture. |
|  | 指示当前使用的摄像机选项。您可以选择以下任一选项：  - **Perspective**（透视）– 围绕中心点自由移动。 - **Top**（俯视）– 将摄像机放在听者上方。 - **Front**（前视）– 将摄像机放在听者前方。 - **Back**（后视）– 将摄像机放在听者后方。 |
|  | 将缩放比例重置为默认设置。在选择 **Perspective** 摄像机选项时，此按钮还会将摄像机恢复到默认位置。 |
|  | Opens the [“Audio Object 3D Viewer Options”一节](01-Audio-Object-3D-Viewer-Options.md "Audio Object 3D Viewer Options") dialog in which you can select the options that you want to appear in the Audio Object 3D Viewer. |
| Bus | 总线。与 Audio Object List 中所聚焦处理阶段关联的总线。 |
| Game Object | 游戏对象。与 Audio Object List 中所聚焦处理阶段关联的游戏对象。 |
| Stage | 阶段。指向 Audio Object List 中选择聚焦的处理阶段，并在 3D 查看器中显示相应的 Audio Object。 |
| Game Object 3D Viewer | 游戏对象 3D 查看器。以图形形式在三维空间中呈现 Audio Object 的相对位置。 |

**相关主题**

- [“了解基于对象的音频”一节](../../../03-设置工程/07-建立输出总线的结构/03-了解基于对象的音频/00-了解基于对象的音频.md "了解基于对象的音频")
- [“对 Audio Object 实施性能分析”一节](../../../07-完善工程/06-性能分析/12-对-Audio-Object-实施性能分析.md "对 Audio Object 实施性能分析")

---