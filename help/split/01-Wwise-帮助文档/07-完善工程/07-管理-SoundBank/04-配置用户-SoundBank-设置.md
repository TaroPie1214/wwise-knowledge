# 配置用户 SoundBank 设置

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [管理 SoundBank](00-管理-SoundBank.md) > 配置用户 SoundBank 设置

## 配置用户 SoundBank 设置

工程层级的 SoundBank（音频包）设置决定生成过程中包含哪些内容、如何包含这些内容以及以何种格式生成这些内容。请参阅 [“定义工程的 SoundBank 设置”一节](../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md "定义工程的 SoundBank 设置")。

您可以使用用户 SoundBank 设置来覆盖工程设置。这些用户设置只有您自己可以使用，并且只会影响您生成的 SoundBank。

### 配置用户 SoundBank 常规设置

**配置自定义 SoundBank 用户设置：**

1. 在 SoundBank Manager（音频包管理器）工具栏中，单击 **SoundBank Settings**（音频包设置）工具：

   ![](../../../../images/btn_gear_dropdown.png)

   若用户已经覆盖相应设置，则工具将显示橙色背景色。
2. 在菜单中，选择 **User SoundBank Settings**（用户音频包设置）。
3. 在 SoundBanks（音频包）选项卡中，选择 **Override Project SoundBank Settings**（覆盖工程音频包设置）。
4. 选中或取消选中相应选项来为 SoundBank（音频包）配置自定义设置。有关所有这些设置的参考信息，请参阅 [“SoundBanks Settings — SoundBanks 选项卡”一节](../../09-参考主题/02-视图/09-SoundBank-Manager-视图/01-SoundBanks-Settings-对话框/01-SoundBanks-Settings-—-SoundBanks-选项卡.md "SoundBanks Settings — SoundBanks 选项卡")。
5. 单击 **OK**（确定）。这时会应用所述设置。除非取消选中 **Override Project SoundBank Settings**，否则这些设置会一直有效。

### 覆盖工程 SoundBank 路径

SoundBank 保存在 [“SoundBanks 选项卡”一节](../../09-参考主题/01-工程/08-Project-Settings/03-SoundBanks-选项卡/00-SoundBanks-选项卡.md "SoundBanks 选项卡")的 SoundBank Paths 分区中指定的位置。不过，您可以使用用户设置来覆盖工程设置。

**覆盖工程 SoundBank 设置：**

1. 在 SoundBank Manager（音频包管理器）工具栏中，单击 **SoundBank Settings**（音频包设置）工具：

   ![](../../../../images/btn_gear_dropdown.png)

   若用户已经覆盖相应设置，则工具将显示橙色背景色。
2. 在菜单中，选择 **User SoundBank Settings**（用户音频包设置）。
3. 在 SoundBanks（音频包）选项卡中，选择 **Override Project SoundBank Settings**（覆盖工程音频包设置）。
4. 选中 **Override SoundBank Paths**（覆盖音频包路径）。有关所有这些参数的参考信息，请参阅 [“SoundBanks Settings — SoundBanks 选项卡”一节](../../09-参考主题/02-视图/09-SoundBank-Manager-视图/01-SoundBanks-Settings-对话框/01-SoundBanks-Settings-—-SoundBanks-选项卡.md "SoundBanks Settings — SoundBanks 选项卡")的 SoundBank Paths 分区。
5. 单击 **OK**（确定）。这时会应用所述设置。除非取消选中 **Override Project SoundBank Settings** 或 **Override SoundBank Paths**，否则这些设置会一直有效。

### 覆盖工程生成前和生成后操作

鉴于自身工作流程，在生成 SoundBank（音频包）之前或之后可能要马上执行特定的操作或任务。比如，您可能想在生成前从版本控制系统签出特定 SoundBank 文件，或者想在生成后马上将流播放文件复制到 SoundBank 目录下。虽然这些信息通常是在工程层级手动配置的，但有时候并不希望沿用它们，而是想配置自己的自定义设置。

在 Wwise 中，可通过创建命令行来配置这些类型的任务。Wwise 中有一个专门的命令行编辑器，方便您构建数目不限的命令行。为了进一步简化过程，编辑器中包含命令行中可使用的所有 Wwise 专用环境变量和其它 Windows 环境变量的列表。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 若外部工具返回错误或无法找到，构建过程可能会中断。通过在日志设置中将相应日志严重性级别设为 **Fatal Error** 来完成这一点。要了解详细信息，请参阅[“管理在日志中出现的消息”一节](../../03-设置工程/01-处理工程/02-定义工程设置/04-管理在日志中出现的消息.md "管理在日志中出现的消息")。  在自定义 **Global opening step** 失败时，整个构建过程都会中断且不会生成 SoundBank。不过当针对特定平台的自定义步骤失效时，则将只跳过该平台。然而，由于进程运行不完全成功，因此将跳过 **Global closing step**。外部进程必须返回非零值才会被视为失效。 |

可用于编写自定义命令行的专用 Wwise 变量如下：

| 命令行变量 | 描述 |
| --- | --- |
| `$(AllowExceedMaximum)` | 指定当 SoundBanks 超过指定最大大小时是否生成该 SoundBanks。  当选择了 Allow SoundBanks to exceed maximum（允许 SoundBanks 超过最大大小）选项时，此变量设为 True。 |
| `$(GenerateContentFile)` | 指定是否生成相应文件来列出各个 SoundBank 的内容。内容文件包括有关 Event、Buss、State 和 Switch 的信息，以及流播放音频文件和内存音频文件的完整列表。  当选择了 Generate SoundBank content files（生成 SoundBank 内容文件）选项时，此变量设为 True。 |
| `$(GenerateHeaderFile)` | 指定是否生成将 Event、状态、切换开关和游戏参数名称映射到 ID 的头文件。  当选择了 Generate Header File（生成头文件）选项时，此变量设为 True。 |
| `$(GenerateMaxAttenuationInfo)` | 指定是否为 Event 生成最大衰减距离信息。  当选择了 **Metadata Options**: **Max attenuation**选项时，此变量设为 True。 |
| `$(GenerateEstimatedDuration)` | 指定是否为 Event 生成预计最大和最小时长以及时长类型信息。  当选择了 **Metadata Options**: **Estimated Duration** 选项时，此变量设为 True。 |
| `$(HeaderFileFullFilePath)` | 头文件的完整路径，即 $(HeaderFilePath)\Wwise\_IDs.h。 |
| `$(HeaderFilePath)` | 保存头文件的路径或位置。  此路径来自 Header file path（头文件路径）文本框。 |
| `$(InfoFilePath)` | 当前平台的信息文件的完整文件名。 |
| `$(IsRunningFromCmdLine)` | 指定 Wwise 启动的命令行中是否带有“-generatesoundbanks” 选项。 |
| `$(LanguageList)` | 传送到命令行的语言的列表或者 **SoundBank Manager** 中的选定语言的列表。  |  |  | | --- | --- | | [备注] | 备注 | | 列表采用空格隔开。 | |
| `$(Platform)` | 当前平台的名称。 |
| `$(SoundBankList)` | 传送到命令行的 SoundBank 的列表或者 **SoundBank Manager** 中的选定 SoundBank 的列表。  |  |  | | --- | --- | | [备注] | 备注 | | 列表采用空格隔开。并用双引号括起整个参数中的列表。 | |
| `$(SoundBankListAsTextFile)` | 该文本文件中会列出传给命令行的 SoundBank 或 SoundBank Manager 中的选定 SoundBank。这在处理一长串 SoundBank 时会很有用。  |  |  | | --- | --- | | [备注] | 备注 | | 列表采用空格隔开。并用双引号括起整个参数中的列表。 | |
| `$(SoundBankPath)` | 保存当前平台的 SoundBanks 的路径或位置。 |
| `$(UseSoundBankNames)` | 指定选用 SoundBank 名称（设为 true 时）或 ID（设为 false 时）来用于命名生成的 SoundBank BNK 文件，以及在 SoundBanks 中用于引用其它 SoundBank 中的媒体。  当选择了 Use SoundBank names（使用声音包名称）选项时，此变量设为 True。 |
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
| 环境变量自动进行映射，例如 $(WWISESDK)。 |

为了尽可能提高灵活性，Wwise 支持为以下类型的操作配置不同的命令行：

- **Global opening step** -- 全局初始步骤。适用于所有平台并且在任何其它步骤前执行的命令行。
- **Platform-specific pre-generation step** -- 针对平台的生成前步骤。适用于特定平台并且在生成 SoundBanks 前执行的命令行。
- **Platform-specific post-generation step** -- 针对平台的生成后步骤。适用于特定平台并且在生成 SoundBanks 后执行的命令行。
- **Global closing step** -- 全局结束步骤。适用于所有平台并且在所有其它步之后执行的命令行。

在默认情况下，各个工程都包含平台专有的生成后步骤（post-generation step）命令行，该命令行将流播放文件复制到 SoundBank 目录下。然而，您可以通过执行一个不同的命令行将任何类型的任务自动化。Wwise 还自带另一个出厂命令行，它使用 File Packager 来生成包含 SoundBank 中所有数据和媒体的文件包。有关 File Packager 的详细信息，请参阅[*管理 File Package*](../08-管理-File-Package/00-管理-File-Package.md "管理 File Package")。有关加载出厂命令行的详细信息，请参阅[“加载出厂/自定义命令行”一节](../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md#loading_factory_custom_command_lines "加载出厂/自定义命令行")。

您还可以将您创建的命令行保存到文件（WCMDLINE）中，以便今后在同一工程中使用，跨工程使用，或者与其它用户共享。有关保存命令的详细信息，请参阅[“将自定义命令行保存至文件”一节](../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md#saving_custom_command_lines_to_file "将自定义命令行保存至文件")。

**覆盖工程生成前操作：**

1. 在 SoundBank Manager（音频包管理器）工具栏中，单击 **SoundBank Settings**（音频包设置）工具：

   ![](../../../../images/btn_gear_dropdown.png)

   若用户已经覆盖相应设置，则工具将显示橙色背景色。
2. 在菜单中，选择 **User SoundBank Settings**（用户音频包设置）。
3. 在 SoundBanks（音频包）选项卡中，选择 **Override Project SoundBank Settings**（覆盖工程音频包设置）。
4. 选择 **Override Project Pre-Generation Step**（不沿用工程预生成步骤）选项。
5. 若要添加或修改 Project Settings（工程设置）对话框中配置的要在生成前执行的 Global opening step（全局开始步骤），请单击对应的 **Edit**（编辑）按钮 (...)。

   Pre-Generation Step Editor（生成前步骤编辑器）打开。
6. 在 **Description** 文本框中，输入名称，名称要能清晰描述将要执行的步骤或任务。
7. 在 **Commands** 文本框中，根据需要编写新的命令行或者编辑现有的命令行。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | **Commands** 文本框和与大多数其他文本编辑器一样，允许您按 Enter 键添加新的文本行，选择文本并按 Delete 键删除文本，等等。 |
8. 如果要在命令中插入内置宏和环境变量，则请执行以下操作：

   在 **Macros**（宏）分组框中，根据需要选择以下选项：

   - **Built-in Macros** -- 内置宏。显示可用于 Wwise 命令行中的一列 Wwise 专用变量。
   - **Environment Variables** -- 环境变量。显示可用于 Wwise 命令行中的一列 Windows 专用环境变量。

   要添加变量到命令行中的话，要执行以下操作中的一项：

   - 双击列表中的变量。
   - 从列表中选择变量，然后点击 **Insert**（插入）。

   根据需要，继续添加变量到命令行。
9. 如果需要添加另一个预生成步骤，则只需转至第一行的末尾，按 **Enter**，然后开始创建新的命令行即可。
10. 点击 **OK** 保存命令行并关闭 Pre-Generation Step Editor。

    |  |  |
    | --- | --- |
    | [备注] | 备注 |
    | 如果需要将命令行保存为文件，则在编辑器中点击 Save As（另存为）按钮。有关保存自定义命令行的详细信息，请参阅[“将自定义命令行保存至文件”一节](../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md#saving_custom_command_lines_to_file "将自定义命令行保存至文件")。 |
11. 要添加或修改现有平台专用的预生成步骤，则对各个平台重复执行步骤 3 至 8。

    |  |  |
    | --- | --- |
    | [备注] | 备注 |
    | 您还可以通过点击 Load 按钮将出厂设定和先前保存的自定义命令行加载到 Editor 中。有关加载出厂设定/自定义命令的详细信息，请参阅[“加载出厂/自定义命令行”一节](../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md#loading_factory_custom_command_lines "加载出厂/自定义命令行")。 |

**覆盖工程生成后操作：**

1. 在 SoundBank Manager（音频包管理器）工具栏中，单击 **SoundBank Settings**（音频包设置）工具：

   ![](../../../../images/btn_gear_dropdown.png)

   若用户已经覆盖相应设置，则工具将显示橙色背景色。
2. 在菜单中，选择 **User SoundBank Settings**（用户音频包设置）。
3. 选择 **Override Project Post-Generation Step** 选项。
4. 若要添加或修改 Project Settings（工程设置）对话框中配置的要在生成后执行的现有操作，请单击其中一个 **Edit**（编辑）按钮。

   此时将打开 Post-Generation Step Editor。
5. 在 **Description** 文本框中，输入名称，名称要能清晰描述将要执行的步骤或任务。
6. 在 **Command** 文本框中，根据需要编写新的命令行或编辑当前命令行。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | **Commands** 文本框和与大多数其他文本编辑器一样，允许您按 Enter 键添加新的文本行，选择文本并按 Delete 键删除文本，等等。 |
7. 如果要在命令中插入内置宏和环境变量，则请执行以下操作：

   在 **Macros**（宏）分组框中，根据需要选择以下选项：

   - **Built-in Macros** -- 内置宏。显示可用于 Wwise 命令行中的一列 Wwise 专用变量。
   - **Environment Variables** -- 环境变量。显示可用于 Wwise 命令行中的一列 Windows 专用环境变量。

   要添加变量到命令行中的话，要执行以下操作中的一项：

   - 双击列表中的变量。
   - 从列表中选择变量，然后点击 **Insert**（插入）。

   根据需要，继续添加变量到命令行。
8. 如果需要添加另一个预生成步骤，则只需转至第一行的末尾，按 **Enter**，然后开始创建新的命令行即可。
9. 点击 **OK** 以保存命令行并关闭 Post-Generation Step Editor。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果需要将命令行保存为文件，则在编辑器中点击 Save As（另存为）按钮。有关保存自定义命令行的详细信息，请参阅[“将自定义命令行保存至文件”一节](../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md#saving_custom_command_lines_to_file "将自定义命令行保存至文件")。 |
10. 对于全局结束步骤或其它各个平台，重复执行步骤 3 至 8。

    |  |  |
    | --- | --- |
    | [备注] | 备注 |
    | 您还可以通过点击 Load 按钮将出厂设定和先前保存的自定义命令行加载到 Editor 中。有关加载出厂设定/自定义命令的详细信息，请参阅[“加载出厂/自定义命令行”一节](../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md#loading_factory_custom_command_lines "加载出厂/自定义命令行")。 |

### 为 External Source 指定用户设置

若打算使用 [“External Source（外部源）”一节](../../10-Wwise-插件/03-源插件/03-External-Source（外部源）/00-External-Source（外部源）.md "External Source（外部源）") 插件，则须指定运行时所用外部音频文件的存放位置。您还必须指定保存转码后的源的文件夹，以便在玩游戏时 Wwise 能够使用它们。在工程层级，可在 Project Settings 的 [“External Sources 选项卡”一节](../../09-参考主题/01-工程/08-Project-Settings/06-External-Sources-选项卡.md "External Sources 选项卡") 中执行此操作。参见[“为 External Source 指定工程设置”一节](../../03-设置工程/01-处理工程/02-定义工程设置/06-为-External-Source-指定工程设置.md "为 External Source 指定工程设置")。

您可以使用 SoundBank Manager（音频包管理器）的 User Settings（用户设置）覆盖这些工程设置。

**为 External Source 指定用户设置：**

1. 在 SoundBank Manager（音频包管理器）工具栏中，单击 **SoundBank Settings**（音频包设置）工具：

   ![](../../../../images/btn_gear_dropdown.png)

   若用户已经覆盖相应设置，则工具将显示橙色背景色。
2. 在菜单中，选择 **User SoundBank Settings**（用户音频包设置）。
3. 在 SoundBank Settings（音频包设置）对话框中，切换到 External Sources（外部源）选项卡。有关此选项卡中字段的参考信息，请参阅 [“SoundBanks Settings - External Sources 选项卡”一节](../../09-参考主题/02-视图/09-SoundBank-Manager-视图/01-SoundBanks-Settings-对话框/02-SoundBanks-Settings-External-Sources-选项卡.md "SoundBanks Settings - External Sources 选项卡")。
4. 单击 **OK**（确定）。这时会应用所述设置。除非取消选中相应的选项，否则这些设置会一直有效。

---