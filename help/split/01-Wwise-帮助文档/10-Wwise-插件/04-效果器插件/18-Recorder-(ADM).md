# Recorder (ADM)

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 插件](../00-Wwise-插件.md) > [效果器插件](00-效果器插件.md) > Recorder (ADM)

## Recorder (ADM)

|  |  |
| --- | --- |
| [注意] | 注意 |
| This plug-in is experimental. |

The Recorder (ADM) Effect plug-in records the signal passing through an audio object-format
bus. The content is saved to a WAV file in ADM format, which records multiple beds and
individual 3D objects with animation. The plug-in can be used both in Wwise Authoring and in
game.

The channel count of the WAV file is fixed for the duration of the recording. The channels
are allocated to main mix, passthrough mix, extra beds, and individual audio objects as
needed. Channels are reused for objects of the same type. For example, after an audio object
is destroyed, the channel it used is reused for the next audio object. Audio objects from
the bus are assigned to main mix, passthrough, or audio objects using rules similar to the
[“3D Audio Bed Mixer”一节](01-3D-Audio-Bed-Mixer.md "3D Audio Bed Mixer") or system audio output with 3D
enabled. The Recorder (ADM) honors the Wwise System Output Settings metadata. In addition to
the standard assignment rules, when **Preserve Extra Beds** is
enabled, objects with no 3D Spatialization and no speaker panning are not mixed.

The WAV file is created as soon as audio begins passing through the bus. By default, this
file is recorded to until silence is detected, and it's overwritten each time audio resumes.
However, when the **Hold** property is enabled, a single file
is created during a recording session, even if there are periods of silence. A Recorder(ADM)
ShareSet with **Hold** enabled can be used in combination with
the Set Effect and Reset Set Effect Event Actions. This makes it easy to control the
recording time. (See [“事件 Action 的类型”一节](../../04-与游戏互动/01-管理-Event/01-事件-Action-的类型.md "事件 Action 的类型") for details.)

**Known issues and limitations:**

- WAV files created by Recorder (ADM) cannot be imported into software that requires
  the Dolby Atmos Profile, such as ProTools or Nuendo. We recommend you use the EAR
  Production Suite in REAPER to load the recorded files.
- Only the following bed formats are supported:

  - Mono
  - Stereo
  - 3.0LCR
  - 5.0Surround (no LFE)
  - 5.1Surround
  - 7.1Surround
  - 7.1.4Surround

  2D objects in other formats, including ambisonics, are mixed into the main
  mix.

### Recorder (ADM) properties

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
| Channel Count | 声道数。定义要在 ADM 输出文件中写入多少个声道。该值在文件从头到尾都是固定的。在对象数超过可用声道数时，将在 Main Mix 中对对象实施混音。  Default value: 64  Range: 2 to 128 |
| Main Mix Channel Config | 主混音声道配置。定义 Main Mix (Bed) 的声道配置。在因超出可用声道数或所用选项与 ADM 对象不兼容而无法将对象写入为动态对象时，将在 Main Mix 中对其实施混音。  Default value: 7.1 |
| Enable Passthrough Mix | 启用直通混音。若启用，将在 ADM 输出文件中创建立体声 Passthrough Mix 对象。这种混音遵循与音频输出设备层级的直通信号相同的规则。  Default value: false |
| Preserve Extra Beds | 保留附加 Bed。若启用，则尽可能将 2D 对象保留为单独的 Bed 而不是发送到 Main Mix。  Default value: false |
| Apply Downstream Volume | 启用时，上层层级上的增益将作用于输出文件。 例如，如果 Main Audio Bus（主音频总线）的音量增加 10，子音频总线的音量减少 15，则子音频总线及其所有子音频总线将继承 -5 的总增益量。 虽然该增益始终能听见，但除非启用该选项，否则录音机输出的音频文件将不会包含这个增益。  Default value: false |
| Hold | 保持。在启用时，即便没有输入，Recorder 也会保持活跃状态。此属性可与 RTPC 控件一起用来确保不会在静音时段将录音重置。若要终止 Recorder，必须禁用此属性。  Default value: false |
| **Authoring Tool Output Path（设计工具输出路径）** | |
| Path | 路径。录音文件的完整或相对路径（相对于 Documents 文件夹）的名称和文件名。使用右侧的选择器按钮搜索文件或位置。通过向文件名添加 “%s” 可在调用效果器时在文件名中包含当前日期和时间。 |
| Status | 状态。指定好的文件完整路径。 如果没有问题，则会以黑色字体显示。 If there are errors, they are listed in square brackets and - except for blank filepaths - in red font. 错误类型包括：  - [Will not record in Authoring Tool]：文件名路径为空白。 - [Invalid Filename]：生成的文件名路径包含保留字符（<,>,:,",/,\,|,?,\*），或超出系统字符长度限制。 - [Directory Not Found] —— 目录路径：指定文件名路径中的目录不存在。 - [Write Access Denied] —— 目录路径：用户对指定的文件名路径没有写入权限。    |  |  | | --- | --- | | [备注] | 备注 | | 如显示任何上述问题，Authoring Tool Recoding Status（设计工具录音状态）将变为 Cannot Record（不能录音）。 | |
| **Game Output Path（游戏输出路径）** | |
| Path | 路径。相对于 SoundBank 位置的文件名。  **Caution**:Mac 路径必须使用正斜杠。Windows 会将正斜杠和反斜杠解释为文件夹分隔符，Mac 则会将反斜杠解释为部分文件名。 |
| Status | 状态。如果没出现任何问题，则会以黑色字体使用 $（Game base path）相对变量（即游戏基本路径）显示指定文件名的完整路径。 该变量对应于 SoundBank 的位置。 例如，在运行时，如果 soundbank 位于 \Game\Audio\Soundbanks\Linux 并且 Path 设置为 Recording.wav，则 $(Game base path)\Recording.wav 即表示 \Game\Audio\Soundbanks\Linux\Recording.wav。如果出现错误，则会用方括号列出错误（空白文件路径除外），并以红色字体显示。 错误类型包括：  - [Will not record in Game]：文件名路径为空。 - [Path Must Be Relative]：不允许使用绝对路径。 - [Invalid Filename]：生成的文件名包含无效的字符（Windows 上包括 <、>、:、"、/、\、|、?、\*；macOS 上包括 : ）。 |

---