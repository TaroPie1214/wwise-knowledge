# 使用 Multi-Channel Creator

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [Wwise 工具](../00-Wwise-工具.md) > 使用 Multi-Channel Creator

## 使用 Multi-Channel Creator

Wwise Multi-Channel Creator 是一款独立的实用工具，可通过组合多个单声道或立体声音频文件创建多声道音频文件。您也可以使用该工具将特定单声道文件标记为 0.1 分量或独立 LFE 声道。然后可导入这些文件（从 0.1 到 13.1 标准声道，或最多至 255 个匿名声道），并在 Wwise 工程内使用。

这些源文件必须带有特殊识别前缀，然后将其放入用户定义的“Input”文件夹内。Multi-Channel Creator 扫描 Input 文件夹，以创建一系列可能的多声道配置。生成新的多声道文件前，必须选择所需的配置。Multi-Channel Creator 将新的多声道文件保存在用户定义的“Output”文件夹中。

您可以使用该工具创建单独的文件，也可批量处理多个多声道文件。

下图说明使用 Multi-Channel Creator 创建多声道文件的工作流程。

|  |
| --- |
|  |

## Supported audio formats and features

Multi-Channel Creator 支持多种标准声道配置，使用 Settings 对话框中指定的前缀标识声道（如 “FL”、“C”、“LFE”等）。它还支持匿名配置，其中声道按照用户规定的顺序排列。此类配置的前缀包含数字。Multi-Channel Creator 可生成最多 255 个声道的匿名多声道音频文件。

Multi-Channel Creator 仅支持 PCM 音频格式（.wav）的文件。如果您尝试使用其它不支持的文件格式，则在生成输出文件时将发生错误。生成日志中将显示这些错误。

Multi-Channel Creator 还会在原始源文件中保留所有标记和循环点的位置。如果在源文件中找到重复的标记或循环点，Multi-Channel Creator 将移除重复项，仅在输出文件中保留一份标记或循环点。

## 启动 Multi-Channel Creator

Multi-Channel Creator 在您安装 Wwise 安装于 Wwise 应用程序所在的同一文件夹中。Wwise Multi-Channel Creator 可通过 Audiokinetic Launcher 中 **Launch Wwise** 按钮旁的下拉菜单启动。完成创建多声道文件后，您可以退出该应用程序。

**启动 Multi-Channel Creator 的方法是：**

1. 执行以下操作之一：

   - 在 Start 菜单中，搜索 **Multi-Channel Creator**。
   - 在桌面上双击 **Multi-Channel Creator** 图标。

   此时将打开 **Multi-Channel Creator** 应用程序。

     

   |  |
   | --- |
   |  |

**退出 Multi-Channel Creator 的方法是：**

1. 在窗口标题栏中，点击 **Close** (**X**) 图标。

   此时 **Multi-Channel Creator** 应用程序将关闭。

## Defining the Multi-Channel Creator settings

在使用 **Multi-Channel Creator** 前，必须定义该应用程序的设置。这些设置按用户保存在应用程序数据文件夹中（Application Data > Audiokinetic > MultiChannelCreator）。

这些设置包含一组前缀，它们用于表示不同的声道或构成多声道音频文件的声道集合。在定义这些前缀后，必须将它们添加至各个源文件名的结尾，以便系统能够轻松识别哪些输入文件包含哪些声道。由于输入文件可以是单声道也可以是立体声文件，因此您可以定义单声道和立体声前缀。

例如，假设您要为您的 Wwise 工程创建名为“Bang.wav”的 5.1 爆炸声。每个声道有六种不同的单声道声音：

- 左前
- 右前
- 中置
- 左环绕
- 右环绕
- LFE

For the purposes of this example, the default suffixes will be used, but you can use any suffix you want as long as it is defined in the Settings dialog. 下表显示如何将前缀添加至源文件名。

| 声道 | 前缀 | 源文件名 |
| --- | --- | --- |
| 左前 | .L | Bang.L.wav |
| 右前 | .R | Bang.R.wav |
| 中置 | .C | Bang.C.wav |
| 左环绕 | .SL | Bang.SL.wav |
| 右环绕 | .SR | Bang.SR.wav |
| LFE | .LFE | Bang.LFE.wav |

在将前缀添加至文件名后，Multi-Channel Creator 可以为您提供一列可能的多声道配置，您可以从中选择您需要的配置。

Another option in the Settings dialog allows you to determine how the system will handle source files of different lengths. Multi-Channel Creator 可以通过两种不同的方法处理以上情形，一种方法是使用无声音源填补短文件，使它们具有相同的长度，另一种方法是取消多声道文件生成过程。

**定义 Multi-Channel Creator 设置的方法是：**

1. 在菜单栏中，点击 **Settings** > **Settings**。

   The Settings dialog opens.
2. 要处理不同长度的输入文件，请从 **When file lengths are different** 列表中选择以下选项之一：

   - **Abort operation**，以取消多声道文件生成过程。
   - **Pad shortest files with silence**，以向短文件的结尾添加无声音源，使所有源文件具有相同长度。
3. 要更改单声道或立体声声道文件的默认前缀，请在列表中选择任一声道，然后点击相应的前缀。

   前缀将以蓝色高亮显示。
4. 输入您想用于代表所选声道的一个或一系列字母。
5. 按 **Enter** 键。
6. 对列表中的其它声道重复步骤 3-5。
7. 点击 **OK**

   The changes you made to the settings are saved and the Settings dialog is closed.

## Creating Multi-Channel files from mono/stereo sources

在生成多声道文件前必须执行以下步骤准备源文件：

- 创建单声道或立体声源文件。
- Name them appropriately using the special suffixes defined in the Settings dialog.
- 将源文件放置在单独的“Input”文件夹中。Input 文件夹中的源文件可以分成子文件夹。

然后，您可以开始创建用于 Wwise 工程的多声道文件。

创建过程涉及以下步骤：

- 指定包含源单声道或立体声音频文件的 Input 文件夹。
- 指定用于保存多声道文件的 Output 文件夹。
- 选择要生成的多声道文件。
- 从一列适用的配置中选择某一多声道配置。
- 生成多声道文件。

**创建多声道文件的方法是：**

1. 要指定 Input 文件夹，执行以下任一操作：

   - 在 Input 文件夹字段中输入文件夹的完整路径。
   - 将文件夹从 Windows 资源管理器或 Mac Finder 中拖至 **Input** 文件夹字段。
   - 点击 Input 文件夹 **Browse** (...) 按钮，导航至包含源文件的文件夹，选择该文件夹，然后按下 **OK**。

   Multi-Channel Creator 将自动扫描文件夹，并在 Output preview 列表中显示内容。

   |  |
   | --- |
   |  |

   如果 Input 文件夹包含子文件夹，则输出文件名将包含文件夹结构。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果更改了 Input 文件夹的内容，您则可以手动更新 Output preview，方法是点击 Refresh > Refresh 或按 F5。 |
2. 要指定 Output 文件夹，请执行以下任一操作：

   - 在 Output 文件夹字段中输入文件夹的完整路径。
   - Click the Output folder **Browse** () button, navigate to the folder where you want the multi-channel files to be saved, select the folder, and then press **OK**.
3. 在 Output preview 表中，选择要作为多声道文件输出的文件。

   |  |
   | --- |
   |  |

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 您可以使用 Select All 或 Select None 按钮来选择所有文件或取消选择。 |
4. 对于要输出的各个文件，请从 Configuration 列表中选择多声道配置。

   |  |
   | --- |
   |  |
5. 点击 **Process** 开始生成您选定的多声道文件。

   The Log dialog is displayed showing you the status of each multi-channel file that is created.

   |  |
   | --- |
   |  |
6. Click **Close** to close the Log dialog.

   生成的多声道文件保存在 Output 文件夹中。

## Creating anonymous multi-channel audio files

匿名声道配置是指事先未确定声道角色的配置，如“左前”或“低频效果”。它们完全遵循用户规定的顺序。必须使用特殊插件才能在运行解释它们。匿名多声道文件最多可包含 255 个声道。

创建匿名多声道文件需要两个步骤：

1. 在 Settings 中为匿名配置设置分隔符（请参阅[“Defining the Multi-Channel Creator settings”一节](00-使用-Multi-Channel-Creator.md#defining_multi_channel_creator_settings "Defining the Multi-Channel Creator settings")）；
2. 使用具有相同名称的多个单声道音频文件，以该分隔符加数字为前缀。

单声道文件将按其前缀值排序，并将它们一并放入匿名多声道音频文件中。

例如，假设您可以使用 4 个单声道文件创建 4 声道匿名多声道音频文件。打开 Settings 对话框，并输入“.”作为 **Suffix Separator for Anonymous Audio Files**。然后，您可以将其命名为以下名称：

- MyFile.1.wav
- MyFile.2.wav
- MyFile.123.wav
- MyFile.9999.wav

标示为“4 (Anonymous)”的匿名配置将显示在主屏幕中。一旦生成，便将创建匿名多声道文件。声道将按前缀的升序排序（如上所述）。

---