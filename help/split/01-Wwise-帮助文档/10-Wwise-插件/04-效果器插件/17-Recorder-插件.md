# Recorder 插件

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > Recorder 插件

## Recorder 插件

Recorder 插件效果器允许设计人员录制 AMB、WAV 或 WEM 文件。这包括除了能导致静音的定制（如虚声部等）之外的任何定制。 在 Wwise 创作工具或游戏中都能使用。

Be careful when choosing the hierarchical position of your Recorder. It can be applied to any single object in the Containers hierarchy. 音频信号进入 Recorder 后，将立即保存音频文件。随后播放期间，将在该文件中录音，直到对象播放完成（包括所有循环）。此后每次重新播放时（对象开始播放时），Recorder 都将重写该文件。It can also be applied to a bus, which implies that it will not output the file until the bus is unloaded, resulting in a typically larger AMB, WAV, or WEM. Note that if a recorder plug-in instance is added to a parent in the hierarchy (for example on a Property Container or a parent bus) then the file will be overwritten every time audio begins on one of the child objects or busses.

### Recorder properties

| 界面元素 | 描述 |
| --- | --- |
| Name | 名称。效果器实例的名称。  效果器实例是一组效果器属性设置。它们可以是两种类型之一：自定义或共享集。自定义实例只能由一个对象使用，然而共享集可在多个对象之间共享。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| Inclusion | 启用。决定是否在生成 SoundBank 时在其中包含相应元素。如勾选，则包含该元素。如未勾选，则不会包含该元素。  为了针对各个平台来优化声音设计，有时需在特定平台上弃用某些元素。在默认情况下，此复选框会应用于所有平台。使用复选框左侧的 [Link 标志](../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values") 来取消链接相应元素。然后，便可根据平台来自定义复选框的状态。  若取消选中此选项，则将禁用编辑器中的属性和行为选项。  Default value: true |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../09-参考主题/04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |
| Notes | 备注。Effect 的其它信息。 |
|  | 设置 Effect Editor 中选定标签页的显示方式。默认情况下，整体面板中仅显示一个选定标签页。不过，您可以通过单击分隔器按钮将面板沿横向或纵向一分为二，显示两个不同的标签页。当前所选选项将以高亮背景色显示。  |  |  | | --- | --- | | [备注] | 备注 | | 无法同时在两个面板中显示同一标签页。若选中的标签页已在另一面板中显示，则另一面板将自动显示另一标签页。 | |

|  |  |
| --- | --- |
| **File Attributes（文件属性）** | |
| Format | 文件格式：WAV，用于存储音频位流的行业标准 Waveform Audio File Format；或者 Wwise 描述文件 WEM。  Default value: WAV |
| Ambisonic Channel Ordering | Ambisonics 声道排序。对于 Ambisonics 声道配置，此设置可用于在 FuMa 排序和 ACN 排序 (AmbiX) 之间切换。  |  |  | | --- | --- | | [备注] | 备注 | | 对于 3 阶以上的 Ambisonics，会忽略此设置且文件将始终为 AmbiX，因为 FuMa 并没有 3 阶以上的定义。 |  |  |  | | --- | --- | | [备注] | 备注 | | 在默认情况下，若阶数低于或等于 3，则 Wwise 将导入的 Ambisonics 文件解释为 FuMa；若高于 3，则解释为 AmbiX。因此，在将此设置设为 FuMa 时，任何阶数的 Ambisonics 文件都可正确导入到 Wwise 中。 |  Default value: FuMa |
| **Authoring Tool Output Path（设计工具输出路径）** | |
| Path | 路径。录音文件的完整或相对路径（相对于 Documents 文件夹）的名称和文件名。使用右侧的选择器按钮搜索文件或位置。通过向文件名添加 “%s” 可在调用效果器时在文件名中包含当前日期和时间。 |
| Status | 状态。指定好的文件完整路径。 如果没有问题，则会以黑色字体显示。 如果出现错误，则会用方括号列出错误（空白文件路径除外），并以红色字体显示。 错误类型包括：  - [Will not record in Authoring Tool]：文件名路径为空白。 - [Invalid Filename]：生成的文件名路径包含保留字符（<,>,:,",/,\,|,?,\*），或超出系统字符长度限制。 - [Directory Not Found] —— 目录路径：指定文件名路径中的目录不存在。 - [Write Access Denied] —— 目录路径：用户对指定的文件名路径没有写入权限。    |  |  | | --- | --- | | [备注] | 备注 | | 如显示任何上述问题，Authoring Tool Recoding Status（设计工具录音状态）将变为 Cannot Record（不能录音）。 | |
| **Game Output Path（游戏输出路径）** | |
| Path | 路径。相对于 SoundBank 位置的文件名。  **Caution**:Mac 路径必须使用正斜杠。Windows 会将正斜杠和反斜杠解释为文件夹分隔符，Mac 则会将反斜杠解释为部分文件名。 |
| Status | 状态。如果没出现任何问题，则会以黑色字体使用 $（Game base path）相对变量（即游戏基本路径）显示指定文件名的完整路径。 该变量对应于 SoundBank 的位置。 例如，在运行时，如果 soundbank 位于 \Game\Audio\Soundbanks\Linux 并且 Path 设置为 Recording.wav，则 $(Game base path)\Recording.wav 即表示 \Game\Audio\Soundbanks\Linux\Recording.wav。如果出现错误，则会用方括号列出错误（空白文件路径除外），并以红色字体显示。 错误类型包括：  - [Will not record in Game]：文件名路径为空。 - [Path Must Be Relative]：不允许使用绝对路径。 - [Invalid Filename]：生成的文件名包含无效的字符（Windows 上包括 <、>、:、"、/、\、|、?、\*；macOS 上包括 : ）。 |
| Stereo Downmix | 可将具有两个以上声道的任何输入下混至立体声文件。 它激活以下 7.1 配置音量滑杆，以调整立体声下混中的不同输入声道（无论是哪些声道）的相对重要性。  |  |  | | --- | --- | | [备注] | 备注 | | 对于 Ambisonic 声道配置，Stereo 下混将不起作用。 |  Default value: true |
| Front | 前置。作用于前置扬声器的 [gain](../../14-词汇表.md#glossary_gain "Gain（增益）") 。  Default value: 0.0  Range: -96.3 to 0  Units: dB |
| Center | 中置。作用于中置扬声器的增益。  Default value: -3.0  Range: -96.3 to 0  Units: dB |
| Surround | 环绕声道。作用于环绕扬声器的增益。  Default value: -3.0  Range: -96.3 to 0  Units: dB |
| Back | 后置。作用于后置扬声器的增益。  Default value: -3.0  Range: -96.3 to 0  Units: dB |
| LFE | 作用于 LFE 声道上的增益。  Default value: -96.3  Range: -96.3 to 0  Units: dB |
| **Recorder Input（录音机输入）** | |
| Apply Downstream Volume | 启用时，上层层级上的增益将作用于输出文件。 例如，如果 Main Audio Bus（主音频总线）的音量增加 10，子音频总线的音量减少 15，则子音频总线及其所有子音频总线将继承 -5 的总增益量。 虽然该增益始终能听见，但除非启用该选项，否则录音机输出的音频文件将不会包含这个增益。  Default value: false |
| Import in Wwise | 导入 Wwise。提示点 [“Audio File Importer 对话框”一节](../../09-参考主题/01-工程/05-Importing/01-Audio-File-Importer-对话框.md "Audio File Importer 对话框") 以方便导入录音文件。 |
| |  |  | | --- | --- | | [备注] | 备注 | | 以下功能仅适用于 Windows 版的 Wwise。 | | |
| Authoring Tool Recording Status | 设计工具录音状态。录音过程的当前状态包含：  - Idle：当前未录音。 - Recording：当前正在录制适用的播放对象。 - Cannot Record：未录音，因为 Authoring Tool Output Path 的当前状态显示为错误。 |
| |  | | --- | |  | | 以峰值模式在时间线上显示 PCM（WAV 或 AMB）所有声道的内容。 |

---