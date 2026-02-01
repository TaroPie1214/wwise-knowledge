# 定义工程的 SoundBank 设置

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [设置工程](../../00-设置工程.md) > [处理工程](../00-处理工程.md) > [定义工程设置](00-定义工程设置.md) > 定义工程的 SoundBank 设置

### 定义工程的 SoundBank 设置

在为每种平台和语言生成 SoundBanks 前，您需要定义 SoundBank 设置。以下 SoundBank 设置可以在工程级别定义：

- [“定义 SoundBank 工程设置”一节](03-定义工程的-SoundBank-设置.md#defining_soundbank_project_settings "定义 SoundBank 工程设置") —— 确定生成的 SoundBank 中所包含的信息。
- [“为已保存的 SoundBank 指定新位置”一节](03-定义工程的-SoundBank-设置.md#specifying_location_for_saved_soundbanks "为已保存的 SoundBank 指定新位置") —— 确定硬盘或网络中保存 SoundBank 的位置。
- [“定义要在生成 SoundBank 之前/之后执行的操作”一节](03-定义工程的-SoundBank-设置.md#defining_steps_to_be_performed_pre_post_soundbank_generation "定义要在生成 SoundBank 之前/之后执行的操作") —— 确定在刚要生成 SoundBank 前将执行的任务。
- [“定义要在生成 SoundBank 之前/之后执行的操作”一节](03-定义工程的-SoundBank-设置.md#defining_steps_to_be_performed_pre_post_soundbank_generation "定义要在生成 SoundBank 之前/之后执行的操作") —— 确定在刚刚生成 SoundBank 后将执行的任务。

虽然这些设置在工程级别定义，但您可以创建自定义用户设置，覆盖这些工程设置。有关不沿用 SoundBank 工程设置的详细信息，请参阅[“配置用户 SoundBank 设置”一节](../../../07-完善工程/07-管理-SoundBank/04-配置用户-SoundBank-设置.md "配置用户 SoundBank 设置")。

#### 定义 SoundBank 工程设置

在生成 SoundBanks 前，您需要确定哪些信息是生成过程的一部分、如何加入这些信息以及生成什么格式。您选择的设置将取决于游戏如何访问 SoundBanks 中的数据和媒体。

**定义 SoundBank 工程设置的方法是：**

1. 通过执行以下任一操作来打开 Project Settings 对话框：

   - 在 **Project**（工程）菜单中，选择 **Project Setting**。
   - 按 **Shift+K**。
2. 切换到 SoundBanks 选项卡。
3. 在 **SoundBank Settings**（音频包设置）分组框中，根据需要选择以下选项来为 SoundBank 定义自定义设置：

   - **Allow SoundBanks to exceed maximum size** -- 允许 SoundBanks 超出最大体积。即使超出指定的最大体积时，仍将生成 SoundBank。
   - **Generate SoundBank content file** -- 生成 SoundBank 内容文件。用于创建列出各个 SoundBank 的内容的文件。内容文件包括有关 Event、Buss、State 和 Switch 的信息，以及流播放音频文件和内存音频文件的完整列表。
   - **Generate header file** -- 生成头文件。创建将 Event、状态、切换开关和游戏参数名称映射到 ID 的头文件。
   - **Max attenuation** -- 最大衰减距离。在 SoundBanksInfo.xml 文件中包含各个 Event 的最大衰减距离信息。
   - **Estimated duration** -- 预计时长。在 SoundBanksInfo.xml 文件中包含各个 Event 的预计最大和最小时长，以及声音是无限循环播放还是只播放一次。
   - **Use SoundBank Name**: 使用 SoundBank 名称。使用 SoundBank 名称（勾选时）或 ID（不勾选时）来命名生成的 .bnk SoundBank 文件，以及在一个 SoundBank 中引用另一个 SoundBank。要了解详细信息，请参阅[“SoundBanks 选项卡”一节](../../../09-参考主题/01-工程/08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡")。
4. 如果选择生成头文件，则必须确定是否保存它。为此，请执行以下操作之一：

   - 点击文本框并直接在其中输入路径。
   - 双击文本框或单击浏览按钮 [...] ，在弹出的浏览器中前往要选择的位置。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 您可以使用完整路径或相对路径来指定保存头文件的位置。使用相对路径时，工程文件夹会作为路径的起始点。 |
5. 如果选择生成 SoundBank 内容文件，则可以选择所需的文本文件格式和 **SoundBank content file format** 选项。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 如果文件路径、对象名称或对象备注包含非 ANSI 字符，则应使用 Unicode 格式。 |
6. 点击 **OK** 以应用这些设置。

#### 为已保存的 SoundBank 指定新位置

在生成工程的 SoundBanks 时，默认保存文件夹为：

ProjectName\GeneratedSoundBanks\Platform\

如果此位置对您不方便，那么可将它改为电脑或网络中的任何目录。

在为保存的 SoundBank 指定位置时，可使用完整路径或相对路径。使用相对路径时，工程文件夹会作为路径的起始点。例如，下列完整路径和相对路径指定的位置是相同的：

- C:\Wwise Projects\My Project\GeneratedSoundBanks\Windows
- GeneratedSoundBanks\Windows\

**为已保存的 SoundBank 指定新位置的方法是：**

1. 通过执行以下任一操作来打开 Project Settings 对话框：

   - 在 **Project**（工程）菜单中，选择 **Project Setting**。
   - 按 **Shift+K**。
2. 切换到 SoundBanks 选项卡。
3. 在 **SoundBank Paths**（音频包路径）分组框中，根据需要执行以下操作来指定路径：

   - 直接在文本框中输入路径。
   - 单击 **Browse**（浏览）并使用浏览器前往所选的位置。
4. 点击 **OK** 以使您所做的任何更改生效。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若在工程设置中启用了 **Copy Loose/Streamed Media**，则此设置还会决定要将媒体文件复制到哪个位置。有关详细信息，请参阅“[“SoundBanks 选项卡”一节](../../../09-参考主题/01-工程/08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡")”。 |

#### 定义要在生成 SoundBank 之前/之后执行的操作

根据工作流程，在生成 SoundBank 之前或之后您可能需要立即执行特定步骤或任务。例如，在生成特定 SoundBank 文件前想从版本控制系统中 check out 它们；或者在生成后想立即将流播放文件复制到 SoundBanks 目录中。

在 Wwise 中，这些任务类型是通过创建命令行来定义的。Wwise 中有一个专门的命令行编辑器，方便您构建数目不限的命令行。为了进一步简化过程，编辑器中包含命令行中可使用的所有 Wwise 专用环境变量和其它 Windows 环境变量的列表。

可用于编写自定义命令行的专用 Wwise 变量如下：

| 命令行变量 | 描述 |
| --- | --- |
| `$(AllowExceedMaximum)` | 指定当 SoundBanks 超过指定最大大小时是否生成该 SoundBanks。  当选择了 **Allow SoundBanks to exceed maximum**（允许 SoundBanks 超过最大大小）选项时，此变量设为 True。 |
| `$(GenerateContentFile)` | 指定是否创建文件来列出各个 SoundBank 的内容。内容文件包括有关 Event、Buss、State 和 Switch 的信息，以及流播放音频文件和内存音频文件的完整列表。  当选择了 Generate SoundBank content files（生成 SoundBank 内容文件）选项时，此变量设为 True。 |
| `$(GenerateHeaderFile)` | 指定是否生成将 Event、状态、切换开关和游戏参数名称映射到 ID 的头文件。  当选择了 **Generate Header File**（生成头文件）选项时，此变量设为 True。 |
| `$(GenerateMaxAttenuationInfo)` | 指定是否为 Event 生成最大衰减距离信息。  当选择了 **Metadata Options**: **Max attenuation**选项时，此变量设为 True。 |
| `$(GenerateEstimatedDuration)` | 指定是否生成 Event 的预计最大和最小时长以及时长类型信息。  启用 **Metadata Options**: **Estimated Duration** 选项时，此变量将设置为 True。 |
| `$(HeaderFileFullFilePath)` | 头文件的完整路径，具体为：$(HeaderFilePath)\Wwise\_IDs.h |
| `$(HeaderFilePath)` | 保存头文件的路径或位置。  此路径来自 Header file path（头文件路径）文本框。 |
| `$(InfoFilePath)` | 当前平台的信息文件的完整文件名。 |
| `$(IsRunningFromCmdLine)` | 指定 Wwise 启动的命令行中是否带有`-generatesoundbanks` 选项。 |
| `$(LanguageList)` | 传送到命令行的语言的列表或者 SoundBank Manager 中的选定语言的列表。  |  |  | | --- | --- | | [备注] | 备注 | | 列表采用空格隔开。 | |
| `$(Platform)` | 当前平台的名称。 |
| `$(SoundBankList)` | 传送到命令行的 SoundBank 的列表或者 SoundBank Manager 中的选定 SoundBank 的列表。  |  |  | | --- | --- | | [备注] | 备注 | | 列表采用空格隔开。并用双引号括起整个参数中的列表。 | |
| `$(SoundBankListAsTextFile)` | 该文本文件中会列出传给命令行的 SoundBank 或 SoundBank Manager 中的选定 SoundBank。此选项在处理一长串 SoundBank 时可能会很有用。  |  |  | | --- | --- | | [备注] | 备注 | | 列表采用空格隔开。并用双引号括起整个参数中的列表。 | |
| `$(SoundBankPath)` | 保存当前平台的 SoundBanks 的路径或位置。 |
| `$(UseSoundBankNames)` | 指定选用 SoundBank 名称（设为 `true` 时）或 ID（设为 `false` 时）来用于命名生成的 SoundBank（BNK）文件，以及在 SoundBanks 中用于引用其它 SoundBank 中的媒体。  当选择了 Use SoundBank names （使用声音包名称）选项时，此变量设为 true。 |
| `$(WwiseExeDriveLetter)` | Wwise 可执行程序（Wwise.exe）所在的电脑盘符。 |
| `$(WwiseExePath)` | Wwise 可执行程序（Wwise.exe）的路径或位置。 |
| `$(WwiseExeProcessID)` | Wwise 可执行程序（Wwise.exe）的进程 ID （数字形式）。 |
| `$(WwiseProjectDriveLetter)` | Wwise 工程所在的电脑盘符。 |
| `$(WwiseProjectName)` | 当前工程的名称。 |
| `$(WwiseProjectPath)` | Wwise 工程的路径或位置。 |
| `$(WaapiWampPort)` | WAAPI 为 WAMP 协议使用的端口。 |
| `$(WaapiHttpPort)` | WAAPI 为 HTTP 协议使用的端口。 |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 另外，所有环境变量（如 `$(WWISESDK)`）都是可以使用的。 |

为了尽可能提高灵活性，Wwise 支持为以下类型的步骤指定命令行：

- **Global opening step** -- 全局初始步骤。适用于所有平台并且在任何其它步骤前执行的命令行。
- **Platform-specific pre-generation step** -- 针对平台的生成前步骤。适用于特定平台并且在生成 SoundBanks 前执行的命令行。
- **Platform-specific post-generation step** -- 针对平台的生成后步骤。适用于特定平台并且在生成 SoundBanks 后执行的命令行。
- **Global closing step** -- 全局结束步骤。适用于所有平台并且在所有其它步之后执行的命令行。

在默认情况下，各个工程都包含平台专有的生成后步骤（post-generation step）命令行，该命令行将流播放文件复制到 SoundBank 目录下。然而，您可以通过执行一个不同的命令行将任何类型的任务自动化。Wwise 还自带另一个出厂命令行，它使用 File Packager 来生成包含 SoundBank 中所有数据和媒体的文件包。有关 File Packager 的详细信息，请参阅[*管理 File Package*](../../../07-完善工程/08-管理-File-Package/00-管理-File-Package.md "管理 File Package")。有关加载出厂命令行的详细信息，请参阅[“加载出厂/自定义命令行”一节](03-定义工程的-SoundBank-设置.md#loading_factory_custom_command_lines "加载出厂/自定义命令行")。

您还可以将您创建的命令行保存到文件（WCMDLINE）中，以便今后在同一工程中使用，跨工程使用，或者与其它用户共享。有关保存命令的详细信息，请参阅[“将自定义命令行保存至文件”一节](03-定义工程的-SoundBank-设置.md#saving_custom_command_lines_to_file "将自定义命令行保存至文件")。

**定义要在生成 SoundBank 之前执行的操作：**

1. 通过执行以下任一操作来打开 Project Settings 对话框：

   - 在 **Project**（工程）菜单中，选择 **Project Setting**。
   - 按 **Shift+K**。
2. 切换到 SoundBanks 选项卡。
3. 要创建全局 Pre-Generation Step（生成前步骤），请点击浏览按钮 [...] 以打开 Global Opening Step Editor。

   Pre-Generation Step Editor（生成前步骤编辑器）打开。
4. 在 **Description** 文本框中，输入名称，名称要能清晰描述将要执行的步骤或任务。
5. 点击 **Commands** 文本框，开始创建您的命令行。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | **Commands** 文本框和与大多数其他文本编辑器一样，允许您按 Enter 键添加新的文本行，选择文本并按 Delete 键删除文本，等等。 |
6. 如果要在命令中插入内置宏和环境变量，则请执行以下操作：

   在 **Macros**（宏）分组框中，根据需要选择以下选项：

   - **Built-in Macros** -- 内置宏。显示可用于 Wwise 命令行中的一列 Wwise 专用变量。
   - **Environment Variables** -- 环境变量。显示可用于 Wwise 命令行中的一列 Windows 专用环境变量。

   要添加变量到命令行中的话，要执行以下操作中的一项：

   - 双击列表中的变量。
   - 从列表中选择变量，然后点击 **Insert**（插入）。

   根据需要，继续添加变量到命令行。
7. 如果需要执行第二个全局生成前步骤，则只需转到第一行末尾，按 **Enter** 键，然后即可开始创建新的命令行。
8. 点击 **OK** 保存命令行并关闭 Pre-Generation Step Editor。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果需要将命令行保存为文件，则在编辑器中点击 **Save As**（另存为）按钮。有关保存自定义命令行的详细信息，请参阅[“将自定义命令行保存至文件”一节](03-定义工程的-SoundBank-设置.md#saving_custom_command_lines_to_file "将自定义命令行保存至文件")。 |
9. 要创建针对平台的生成前步骤，针对各个平台重复步骤 3 至 8。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 您还可以通过点击 **Load** 按钮将出厂设定和先前保存的自定义命令行加载到 Editor 中。有关加载出厂设定/自定义命令的详细信息，请参阅[“加载出厂/自定义命令行”一节](03-定义工程的-SoundBank-设置.md#loading_factory_custom_command_lines "加载出厂/自定义命令行")/>。 |

**定义要在生成 SoundBank 之后执行的操作：**

1. 通过执行以下任一操作来打开 Project Settings 对话框：

   - 在 **Project**（工程）菜单中，选择 **Project Setting**。
   - 按 **Shift+K**。
2. 切换到 SoundBanks 选项卡。
3. 在 **Post-Generation Step**（生成后操作）分组框中，您会发现系统会默认添加 **Copy Streamed Files**（复制流播放文件）命令行。要修改此命令行或添加其他命令行，请单击相应的浏览按钮 [...]。

   此时将打开 Post-Generation Step Editor。
4. 在 **Description** 文本框中，输入名称，名称要能清晰描述将要执行的步骤或任务。
5. 在 **Commands** 文本框中，单击当前命令行的末尾，然后按**Enter**。现在可以开始创建新的命令行了。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | **Commands** 文本框和与大多数其他文本编辑器一样，允许您按 Enter 键添加新的文本行，选择文本并按 Delete 键删除文本，等等。 |
6. 如果要在命令中插入内置宏和环境变量，则请执行以下操作：

   在 **Macros**（宏）分组框中，根据需要选择以下选项：

   - **Built-in Macros** -- 内置宏。显示可用于 Wwise 命令行中的一列 Wwise 专用变量。
   - **Environment Variables** -- 环境变量。显示可用于 Wwise 命令行中的一列 Windows 专用环境变量。

   要添加变量到命令行中的话，要执行以下操作中的一项：

   - 双击列表中的变量。
   - 从列表中选择变量，然后点击 **Insert**（插入）。

   根据需要，继续添加变量到命令行。
7. 如果需要执行第二个全局生成前步骤，则只需转到第一行末尾，按 Enter 键，然后即可开始创建新的命令行。
8. 点击 **OK** 以保存命令行并关闭 Post-Generation Step Editor。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果需要将命令行保存为文件，则在编辑器中点击 **Save As**（另存为）按钮。有关保存自定义命令行的详细信息，请参阅[“将自定义命令行保存至文件”一节](03-定义工程的-SoundBank-设置.md#saving_custom_command_lines_to_file "将自定义命令行保存至文件")。 |
9. 对于全局结束步骤或其它各个平台，重复执行步骤 3 至 8。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 您还可以通过点击 **Load** 按钮将出厂设定和先前保存的自定义命令行加载到 Editor 中。有关如何加载出厂/自定义命令的详细信息，请参阅[“加载出厂/自定义命令行”一节](03-定义工程的-SoundBank-设置.md#loading_factory_custom_command_lines "加载出厂/自定义命令行")章节。 |

#### 加载出厂/自定义命令行

Wwise 附带一些已经创建的命令行，包括将流播放文件复制到 SoundBank 目录的命令行，以及将流播放文件和 SoundBanks 打包到一个文件包（package）的命令行。这些被称作出厂设定命令行。您可以加载这些出厂设定命令行或您先前保存到文件中的自定义命令行。

**加载出厂设定/自定义命令行的方法是：**

1. 在 Pre/Post Generation Step Editor（生成前/后操作编辑器）中，单击 **Load**（加载）。
2. 在快捷菜单中，点击以下某个选项：

   - **From Factory Folder** - 打开 Explorer / Finder 并转至 Wwise 出厂设定命令行所在的目录。
   - **From Last Location** - 打开 Explorer / Finder 并转至上次加载命令行的目录。

   这时会打开 Open（打开）对话框。
3. 选择您要加载的命令行并点击 **Open**。

   命令行将被加载到编辑器中。

#### 将自定义命令行保存至文件

您可以将您创建的自定义命令行保存为文件，以便今后在同一工程中使用，跨工程使用，或者与其它用户共享。

**保存命令行为文件的方法是：**

1. 在 Pre-Post Generation Step Editor 中，编写命令行。
2. 完成时，点击 **Save As**。

   这时会打开 Save As（另存为）对话框。
3. 前往您想保存命令行的文件夹，对它命名，然后按 **Save**。

   命令行将保存为 WCMDLINE 文件，可以随时复用。

---