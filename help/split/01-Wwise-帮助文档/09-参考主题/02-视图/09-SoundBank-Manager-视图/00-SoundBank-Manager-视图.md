# SoundBank Manager 视图

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [视图](../00-视图.md) > SoundBank Manager 视图

## SoundBank Manager 视图

SoundBank Manager（音频包管理器）会显示为工程创建的 SoundBank。它还会显示各个 SoundBank 的相关信息，包括其当前大小、剩余空间量，以及 SoundBank 的类型或内容。创建 SoundBank 之前，您可以自定义用户设置，并可以指定将为哪些平台和语言生成 SoundBank。

在 SoundBank Manager 中双击 SoundBank 时，会在 SoundBank Editor（音频包编辑器）中自动显示所选 SoundBank 的相关信息。

SoundBank Manager 会显示两个 SoundBank 列表：

- **User-Defined SoundBanks**：此列表显示在上部窗格中，其包含所有通过编辑工程创建的 SoundBank。这些 SoundBank 由用户创建并完全定义，并可通过手动创建来单独添加或通过导入定义文件来自动添加。有关详细信息，请参阅“[“手动创建 User-Defined SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/01-手动创建-User-Defined-SoundBank.md "手动创建 User-Defined SoundBank")”。
- **Auto-Defined SoundBanks**：此列表显示在下部窗格中，其包含所有 Wwise 可自动创建 SoundBank 的对象。对于每个对象，都会列明是否自动创建了 SoundBank。若未创建 SoundBank，则会在附加列中显示用于确定原因所需的信息。有关详细信息，请参阅“[“Auto-defined SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/02-SoundBank-管理策略/05-Auto-defined-SoundBank.md "Auto-defined SoundBank")”。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在编辑工程时，两个 SoundBank 列表会动态添加和移除行。不过，每行中显示的信息：  - 只在生成 SoundBank 后更新。 - 显示与当前活跃平台和语言对应的 SoundBank 信息。有关详细信息，请参阅“[“Switching to a different platform”一节](../../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md#switching_to_different_platform "Switching to a different platform")”和“[“Switching to a different project language”一节](../../../07-完善工程/02-管理平台和语言版本/02-Localizing-your-project.md#switching_to_different_language_version "Switching to a different project language")”章节。 |

| 界面元素 | 描述 |
| --- | --- |
| Show Hierarchy | 显示层级结构。更改条目在 SoundBank 列表中的显示方式。若选中，则按层级显示条目以及 Work Unit（工作单元）、文件夹和其他对象。若取消选中，则以简单列表形式显示条目。 |
|  | 影响 Auto-Defined SoundBank 列表内容的显示选项：  - **Show Events**（显示事件）：在 Auto-Defined SoundBank 列表中显示 Event。 - **Show Audio Busses**（显示音频总线）：在 Auto-Defined SoundBank 列表中显示 Audio Bus。 - **Show Generated Auto SoundBanks**（显示生成的自动定义的音频包）：在 Auto-Defined SoundBank 列表中显示自动定义了 SoundBank 的条目。 - **Show Non-Generated Auto SoundBanks**（显示生成的未自动定义的音频包）：在 Auto-Defined SoundBank 列表中显示未自动定义 SoundBank 的条目。  只要取消选中了列表中的选项，显示选项按钮就会显示为橙色。  |  |  | | --- | --- | | [备注] | 备注 | | 有关 Auto-Defined SoundBank 的更多详细信息，请参阅“[“Auto-defined SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/02-SoundBank-管理策略/05-Auto-defined-SoundBank.md "Auto-defined SoundBank")”章节。 | |
| [Platform] | [平台]。列出显示了 SoundBank 信息的当前活跃平台。若要更改活跃平台，请参阅“[“Switching to a different platform”一节](../../../07-完善工程/02-管理平台和语言版本/01-Authoring-across-platforms.md#switching_to_different_platform "Switching to a different platform")”章节。 |
| [Language] | [语言]。列出显示了 SoundBank 信息的当前活跃语言。若要更改活跃语言，请参阅“[“Switching to a different project language”一节](../../../07-完善工程/02-管理平台和语言版本/02-Localizing-your-project.md#switching_to_different_language_version "Switching to a different project language")”章节。 |
|  | 打开 Keyboard Shortcuts 对话框。在此，可在特定 Work Unit 下创建并命名新的 SoundBank。 |
|  | 显示 SoundBank Generation Log，其中包含与生成 SoundBank 过程中发现的已有问题或潜在问题相关的信息。  该按钮会显示情况严重的 SoundBank Generation Log 条目数。 |
|  | 生成选中项。打开 [“Generating SoundBanks 对话框”一节](04-Generating-SoundBanks-对话框.md "Generating SoundBanks 对话框") 对话框，并根据指定的设置为选定平台和语言生成所选 SoundBank 和对应文件。若自上次生成 SoundBank 后未作任何更改，则不重新生成 SoundBank。 |
|  | 全部生成。打开 [“Generating SoundBanks 对话框”一节](04-Generating-SoundBanks-对话框.md "Generating SoundBanks 对话框") 对话框，并根据指定的设置为所有平台和语言（无论是否选中）生成全部 SoundBank 和对应文件。若自上次生成 SoundBank 后未作任何更改，则不重新生成 SoundBank。 |
|  | SoundBank Settings：  - **Project SoundBank Settings**：打开 Project Settings 对话框并转到 SoundBanks 选项卡。您可以在此对话框中设定工程的 SoundBank 设置。Project SoundBank Settings 将应用于所有用户，除非在 User SoundBank Settings 中覆盖。 - **User SoundBank Settings**：打开 SoundBanks Settings 对话框。此对话框用于定义自定义用户设置，其会覆盖 Project SoundBank Settings 中的设置。  只要修改了此对话框中的选项，相应设置按钮就会显示为橙色。其表示 User SoundBank Settings 会覆盖 Project SoundBank Settings。 |
| **User-Defined SoundBank** | |
| User-Defined SoundBank | 用户定义的音频包。User-Defined SoundBanks 列表的第一列。该列包含 User-Defined SoundBank 的名称。有关详细信息，请参阅[“使用 User-defined SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/00-使用-User-defined-SoundBank.md "使用 User-defined SoundBank")。  在启用 **Show Hierarchy** 的情况下显示 SoundBank 时，此列会显示 Work Unit、文件夹和 SoundBank 的层级结构。在选择工作单元或文件夹时，还会自动选择所有子对象。在取消选择时，也会取消选择所有子对象。  若 SoundBank 存在问题，则其名称将显示为红色。这些问题可能是：  - 当前 Data Size 值超出 Max Size 中允许的最大内存值。 - SoundBanks 不包含某些所选语言版本的 Sound Voice 源文件。  |  |  |   | --- | --- |   | [备注] | 备注 |   | If **Use reference language as stand-in** is selected in the Language Manager, then the missing language voices will be output in the reference language; however, the SoundBank name will still be red. 详请参阅[*管理语言*](../../../03-设置工程/03-管理语言.md "管理语言")。 |    只会生成选中了对应复选框的 SoundBank。  若在 Project Settings 中选中 **Enable Auto-Defined SoundBanks**，将无法选择单个 SoundBank。这是因为 Wwise 会为 User-defined SoundBank 中没有包含的 Event 自动定义 SoundBank。您可以通过同时生成所有 SoundBank 来对此进行准确的评估。有关此 SoundBank 管理策略的详细信息，请参阅[“Auto-defined SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/02-SoundBank-管理策略/05-Auto-defined-SoundBank.md "Auto-defined SoundBank")。 |
| ID | 此 ID 用于在调用 SDK 函数时识别 SoundBank。注意，该 ID 使用 SDK 函数 [AK::SoundEngine::GetIDFromString](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html) 获取。  生成的元数据文件也包含 SoundBank 的 ID。有关详细信息，请参阅“[“SoundBanks 选项卡”一节](../../01-工程/08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡")”。 |
| On Disk | 磁盘上。显示行条目是否存在对应的 SoundBank 文件。若存在相应文件，则该列包含 SoundBank 文件 (.bnk) 图标。否则，该列为空。  每次生成 SoundBank 后都会更新此列中的信息。  若针对生成的文件启用并配置了版本控制系统，则该图标会指示文件的版本控制状态。 |
| Data Size（数据大小） | 数据大小。针对当前所选平台 SoundBank 将使用的游戏内存量。  若 SoundBank 包含 Sound Voice，则将根据当前所选语言同时更新 Data Size 列。  若超出最大限值，则 Data Size 值显示为红色。所显示的大小是上次生成 SoundBank 时得到的值；只有再次成功生成 SoundBank 之后才会更新。  **Units**：字节 |
| Decoded Size | 解码后大小。在当前所选平台下，包含解码后 Vorbis 或 Opus 媒体的 SoundBank 所要使用的游戏内存量。若 SoundBank 不含 Vorbis 或 Opus 媒体文件，则此值与 Data Size 相同。  若 SoundBank 包含 Sound Voice，则将根据当前所选语言同时更新 Decoded Size 列。  **Units**：字节 |
| Max Size | 最大大小。为该 SoundBank 分配的最大游戏内存量。  可以为该值取消链接，允许各个平台的最大内存不相同。  即使超出您指定的最大内存量，仍然可以成功生成 SoundBank。  值为 0 时表示该 SoundBank 的大小没有限制。此时，控件显示“Infinite”，而非“0”。  单位：字节  Default value: 0  Range: 0 to 2147483647 |
| Free Space | 剩余空间。SoundBank 中的剩余空间量。剩余空间是由 Max Size 减去 Data Size 得到的。若 Data Size 超出 Max Size，则 Free Space 值将显示为红色。  **Units**：字节 |
| Type | 显示相应 SoundBank 中包含的对象类型，如音效、语音和音乐。如果 SoundBank 包含所有四种对象，则该列将显示“All”（全部）。  若 SoundBank 中同时包含 Sound Voice 和其他类型的声音，则此列中的文本显示为红色。这是为了警告您数据将对每种生成的语言进行复制，对于语音以外的类型这是没有必要的。 |
| Date Updated | 更新日期。上一次更新 SoundBank 的日期和时间。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| **Auto-Defined SoundBank** | |
| Auto-Defined SoundBank | 自动定义的音频包。Auto-Defined SoundBanks 列表的第一列。该列包含 Wwise 可能自动定义 SoundBank 的对象的名称。  此列包含：  - Init SoundBank。每个工程仅包含一个 Init SoundBank，不管采用怎样的 SoundBank 设置。 - 可能自动定义 SoundBank 的各个对象。请参阅 [“Auto-defined SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/02-SoundBank-管理策略/05-Auto-defined-SoundBank.md "Auto-defined SoundBank") 了解详细信息。  在启用 **Show Hierarchy** 的情况下显示 SoundBank 时，此列会显示自动定义了 SoundBank 的对象及其层级结构（跟 Project Explorer 视图中显示的一样）。 |
| ID | 此 ID 用于在调用 SDK 函数时识别 SoundBank。注意，该 ID 使用 SDK 函数 [AK::SoundEngine::GetIDFromString](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html) 获取。  生成的元数据文件也包含 SoundBank 的 ID。有关更多详细信息，请参阅“[“SoundBanks 选项卡”一节](../../01-工程/08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡")”。 |
| On Disk | 磁盘上。显示行条目是否存在对应的 SoundBank 文件。若存在相应文件，则该列包含 SoundBank 文件 (.bnk) 图标。否则，该列为空。  每次生成 SoundBank 后都会更新此列中的信息。  若针对生成的文件启用并配置了版本控制系统，则该图标会指示文件的版本控制状态。 |
| Inc | 启用。显示是否设置了对象的 Inclusion 属性（如适用）。  对于具有 Inclusion 属性的对象，必须设置该属性才能包含自动定义的 SoundBank。  |  |  | | --- | --- | | [备注] | 备注 | | 每次生成 SoundBank 后都会更新此列中的信息。它*不会*在修改工程后动态更新。 | |
| In User-Defined | 为用户定义。显示哪个 User-defined SoundBank 包含相应对象（如适用）。  这可能决定对象是否包含自动定义的 SoundBank（取决于工程配置）。有关详细信息，请参阅[“使用 User-defined SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/00-使用-User-defined-SoundBank.md "使用 User-defined SoundBank")。  |  |  | | --- | --- | | [备注] | 备注 | | 每次生成 SoundBank 后都会更新此列中的信息。它*不会*在修改工程后动态更新。 | |
| Type | 显示相应 SoundBank 中包含的对象类型，如音效、语音和音乐。如果 SoundBank 包含所有四种对象，则该列将显示“All”（全部）。  若 SoundBank 中同时包含 Sound Voice 和其他类型的声音，则此列中的文本显示为红色。这是为了警告您数据将对每种生成的语言进行复制，对于语音以外的类型这是没有必要的。 |
| Date Updated | 更新日期。上一次更新 SoundBank 的日期和时间。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| **Platforms（平台）** | |
| Platforms（平台） | 平台。当前工程中可用并处于活动状态的平台列表。  将为选中的平台生成 SoundBank。  列表中只有针对当前工程授权的平台才可用。有关如何针对各个平台获取授权的详细信息，请参阅 Audiokinetic Launcher 文档的“故障排查”章节。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| **Languages（语言）** | |
| Languages（语言） | 语言。当前工程中使用的语言列表。  将为选中的语言生成 SoundBank。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |

**相关主题**

- [“手动创建 User-Defined SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/01-手动创建-User-Defined-SoundBank.md "手动创建 User-Defined SoundBank")
- [“通过导入定义文件创建并填充 SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/02-通过导入定义文件创建并填充-SoundBank.md "通过导入定义文件创建并填充 SoundBank")
- [“手动填充 SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/03-手动填充-SoundBank.md "手动填充 SoundBank")
- [“重命名 SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/05-重命名-SoundBank.md "重命名 SoundBank")
- [“在 SoundBank 之间移动工程元素”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/04-管理-SoundBank-内容/06-在-SoundBank-之间移动工程元素.md "在 SoundBank 之间移动工程元素")
- [“删除 SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/03-使用-User-defined-SoundBank/06-删除-SoundBank.md "删除 SoundBank")
- [“为工程生成 SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/05-为工程生成-SoundBank.md "为工程生成 SoundBank")
- [“使用脚本生成 SoundBank”一节](../../../07-完善工程/07-管理-SoundBank/05-为工程生成-SoundBank.md#using_scripts_to_generate_soundbanks "使用脚本生成 SoundBank")

---