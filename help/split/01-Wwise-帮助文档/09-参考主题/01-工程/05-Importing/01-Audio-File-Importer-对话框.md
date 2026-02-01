# Audio File Importer 对话框

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Importing](00-Importing.md)  > Audio File Importer 对话框

### Audio File Importer 对话框

在 Audio File Importer 中，您可以将 Sound SFX 和 Sound Voice 媒体文件导入 Wwise 工程，并且确定这些文件的整合方式及其在工程中的位置。您可以在不同的时间，出于不同原因导入文件：

- 将新文件导入工程并创建新的结构
- 替换现有文件
- 针对各语言版本进行本地化

To access the Audio File Importer:

- From Wwise menu bar, click **Views** > **Audio File Importer**.
- From the Wwise menu bar, click **Project** > **Import Audio Files**.
- Click **Shift + I**.
- Right-click an object in the Project Explorer and then select **Import Audio Files**.

在 Audio File Importer 中可以根据导入文件的使用方式，可以指定相应的导入模式。

在导入某个文件后，该文件已被验证为 Wwise 支持的格式。如果在导入过程中出现问题，您则可以在 Import Conflict Manager（导入冲突管理器）中查看错误，也许还可能解决一些问题。

#### Wwise 支持哪些文件？

支持以下音频文件属性和格式：

**PCM 音频格式**

- WAV 和 AMB

**声道配置**

- 0.1 至 13.1

**采样率**

- 最高 96 kHz

**位深**

- 16位
- 24位

|  |  |
| --- | --- |
| [备注] | 备注 |
| Wwise 还可以导入 32 位浮点式 PCM（脉冲编码调制）文件；但是，转码格式最高仅支持 24 位。此外，若在 [“Transport Control”一节](../../02-视图/10-Transport-Control.md "Transport Control") 中播放，文件将被转换成 16 位。 |

#### DC Offsets

直流偏置。有时使用直流偏置筛选器来消除直流偏置是很好的方法，因为直流偏置可影响 Wwise 中的音量并导致副作用。在某些情况下，您将无法消除直流偏置，例如，对于精确到采样点的容器。在其它情况下，例如在声音归一化为 0 dB 的情况下，您可能需要消除直流偏置，也可能不需要。This setting can be enabled in the Conversion Settings dialog.

|  |  |
| --- | --- |
| [注意] | 注意 |
| 对于循环声音，我们建议不要消除直流偏置。消除机制采用高通滤波器，因此不保证将以相同方法修改循环的第一个采样和最后一个采样，因为并不知道这两个样本将连续播放。这可能产生信号中断，导致听到爆音。 |

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Import Mode | - **Create new objects**：将文件作为当前 Wwise 工程中的新对象进行导入。 - **Replace audio files**：导入文件将替代当前 Wwise 工程中的媒体文件。 - **Localize languages**：将文件作为当前工程的本地化语音进行导入。 |
| Import as | - Sound SFX：将文件作为 Sound SFX 对象导入到工程层级中的指定位置。 - Sound Voice：将文件作为 Sound Voice 对象导入到工程层级中的指定位置。 |
| Destination language | 目标语言。指明导入的 Sound Voice 文件属于何种语言，下拉列表将显示 Language Manager 中指定的工程语言类型。 |
| Audio file destination | 音频文件的目标位置。为需要导入到 Original 路径中的文件和文件夹选择一个子文件夹。 |
| Object destination | 对象目标。允许选择游戏目录下的当前工程路径中的位置，媒体文件将导入其中并可在 Project Explorer - Browser（工程浏览器 —— 浏览器）中进行选择。 |
|  | Opens the File Open dialog where you can select files that you want to import. |
|  | Opens the Folder Open dialog where you can select folders that you want to import.  |  |  | | --- | --- | | [技巧] | 技巧 | | 您也可以将系统中的文件或文件夹拖拽至导入列表中。 | |
| Import Tab Delimited | 导入按制表符分割的文件...。导入用制表符分割好的文本文件，其中定义了要导入的音频文件以及要创建的结构。  有关详细信息，请参阅[“从用制表符分割的文本文件导入媒体文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/02-导入媒体文件/05-从用制表符分割的文本文件导入媒体文件.md "从用制表符分割的文本文件导入媒体文件")。 |
|  | 从导入列表中删除当前所选文件和文件夹。 |
| Audio File/Folder | 音频文件/文件夹。要导入的各个音频文件或文件夹的名称。 |
|  | Template selector（模板选择器）. 显示快捷菜单，用来浏览模板并选择最近使用的模板。在选择一个模板后，系统将使用当前的模板匹配模式，将音频文件名称与模板对象名称进行匹配。  |  |  | | --- | --- | | [技巧] | 技巧 | | 您可以从列表中选择多个条目并选择一个模板，来快速地将该模板同时应用于多个条目。 | |
| Template | 模板。为要导入的文件或文件夹显示相关的模板对象。有关详细信息，请参阅[“使用模板导入媒体文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/02-导入媒体文件/03-使用模板导入媒体文件.md "使用模板导入媒体文件")。 |
| Object Type/Action | Shows a list of the possible object types to create for the WAV file or folder. 而且，还会列出以下可能的操作：  - **No Object**（无对象）：选择此选项将不会为 WAV 文件或文件夹创建 Wwise 对象。请注意，为 WAV 文件选择此选项时，文件仍会被导入。You need to remove the entry from the list if you do not want to have the WAV file imported. 使用 DEL 键从列表中删除条目。 - **Use existing object**（使用现有对象）：选择此选项时，将不会为 WAV 文件或文件夹创建新的 Wwise 对象，而会复用工程中具有相同的名称的现有对象，并将现有内容与导入条目的子对象进行合并。此选项仅在导入目标路径中找到匹配对象时才可用。 - **Copy template**（复制模板）：选择此选项将复制相关模板对象（包括它的所有设置），并将导入的 WAV 文件用于复制的对象。此选项仅在关联模板时才可用。  |  |  | | --- | --- | | [技巧] | 技巧 | | 您可以从列表中选择多个条目并更改对象类型或操作，来快速地同时修改多个条目。 | |
| Object | 对象。显示导入的对象名称和类型。  对象名称颜色可能为：  - **White**，创建新对象时将显示为白色。 - **Yellow**，根据关联模板创建新对象时将显示为黄色。 - **Gray**，基于现有对象创建子对象时将显示为灰色。  |  |  | | --- | --- | | [备注] | 备注 | | 如果目标结构中出现名称冲突，所创建的对象则可能会使用不同的名称。如果目标位置已存在同名对象，则会附加数字后缀，按序递增。 | |
| Message | 消息。显示有关当前情况的详细信息。您可以查看这些消息，来确保导入正确完成。 |
| File Size | 媒体文件的大小（单位为 KB）。 |
| Date Modified | 修改日期。最后一次更改媒体文件的日期和时间。 |
| Template match mode | 模板匹配模式。设置使用模板时的匹配模式。  - **Match all**（匹配全部）：尝试使用字符串相似度和指派算法将各个音频文件和文件夹与模板对象进行匹配。音频文件名称和模板名称不需要相同。此方法在大多数情况下是有效的，但如果音频文件名称与模板名称差异过大，则有可能匹配失误。 - **Perfect matches only**（仅完全匹配）：仅将音频文件与相同名称的模板匹配。 |
| Auto Add/Checkout on Source Control | 自动添加/签出源文件。决定 Wwise 是否通过 Source Control 对导入的文件执行 Add 或 Checkout 操作。  |  |  | | --- | --- | | [备注] | 备注 | | 只有在 Project Settings 的 [“General 选项卡”一节](../08-Project-Settings/01-General-选项卡.md "General 选项卡")中选择了版本控制插件才会显示此选项。 | |
| **Custom Properties** 按钮 | 显示 Custom Properties 编辑器对话框，方便为导入的对象设置自定义属性。  |  |  | | --- | --- | | [备注] | 备注 | | 此选项仅在 Project Settings（工程设置）中设置了自定义属性时才可用。 | |
|  | Opens the Importing dialog where you can view the progress of the file import and stop the import if required. |
|  | Closes the Audio Importer dialog. |

**相关主题**

- [“导入媒体文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/02-导入媒体文件/00-导入媒体文件.md "导入媒体文件")
- [“导入用于音效的媒体文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/02-导入媒体文件/01-导入用于音效的媒体文件.md "导入用于音效的媒体文件")
- [“导入用于旁白的媒体文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/02-导入媒体文件/04-导入用于旁白的媒体文件.md "导入用于旁白的媒体文件")
- [“替换媒体文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/03-替换媒体文件.md "替换媒体文件")
- [“替换 Sound Voice 媒体文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/03-替换媒体文件.md#replacing_sound_voice_media_files "替换 Sound Voice 媒体文件")
- [“导入 SFX 文件”一节](../../../03-设置工程/05-管理工程中的媒体文件/03-替换媒体文件.md#replacing_sfx_files "导入 SFX 文件")
- [“管理文件导入问题”一节](../../../03-设置工程/05-管理工程中的媒体文件/04-管理文件导入问题.md "管理文件导入问题")
- [“为音轨添加内容”一节](../../../06-创建互动音乐/04-使用-Music-Track-和-Music-Segment/04-为音轨添加内容.md "为音轨添加内容")

---