# Pre-Generation/Post-Generation Step Editor

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [工程](../../00-工程.md) > [Project Settings](../00-Project-Settings.md) > [SoundBanks 选项卡](00-SoundBanks-选项卡.md) > Pre-Generation/Post-Generation Step Editor

#### Pre-Generation/Post-Generation Step Editor

您可通过 Pre-Generation/Post-Generation Step Editor 创建和编辑全局打开和关闭命令行，以及基于平台的命令行。这些命令行用来在生成 SoundBank 前后执行自定义作业。例如，您可创建检查版本控制系统中特定文件的生成前步骤命令行，也可创建将 SoundBank 通过 File Packager 编组至包的生成后命令行。您可加载 Wwise 提供的现有命令行，也可将命令行保存至文件，以便跨工程使用它们。

由于使用同一编辑器为所有平台定义生成前和生成后步骤，因此在标题栏中会明确显示以下信息：

- 您创建的是生成前还是生成后步骤。
- 为其创建命令行的平台。
- 命令行是工程还是用户设置。

| 界面元素 | 描述 |
| --- | --- |
| 描述 | 名称或描述所执行命令类型的其它信息。 |
| Commands | 命令。一种命令行 shell 形式，您可创建全局和平台专用命令行。  通过创建多个全局和平台专用命令行，您可在 SoundBank 生成前或生成后执行多个不同的作业。 |
| **Macros（宏命令）** | |
| Built-in Macros | 内置宏。一组 Wwise 变量，可用于编写自定义命令行。  有关每种变量的说明，请参考 [“覆盖工程生成前和生成后操作”一节](../../../../07-完善工程/07-管理-SoundBank/04-配置用户-SoundBank-设置.md#defining_custom_user_steps_to_be_performed_pre_post_soundbank_generation "覆盖工程生成前和生成后操作")。 |
| Environment Variables | 环境变量。一组 Windows 环境变量，可用于编写自定义命令行。 |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。宏或环境变量的名称。 |
| Current Value | 当前值。相应宏或环境变量的当前值或设置。比如，若在 **SoundBank Settings** 分组框中选中了 **Use SoundBank names** 选项，则会将 `$(UseSoundBankNames)` 宏的当前值设为 `true`。 |
|  | 将所选的宏或环境变量添加至命令行。  变量将添加至指针所在位置，或替换命令行中的所选文本。  除点击 Insert 外，您只需双击列表中的变量便可将其添加至命令行。 |
|  | 加载…。打开 Windows 的 Open File 对话框以加载之前保存的命令行或出厂命令行。点击 Load 按钮时，您可选择以下选项：  - **From Factory Folder** – 打开对话框并转到保存出厂命令行的文件夹。 - **From Last Location** – 打开对话框并转到上次加载了命令行的文件夹。 |
|  | 将命令行数据保存为 .wcmdline 文件，这样之后便可在同一工程或跨工程使用创建的这些命令行。 |
|  | 确定。保存命令行并关闭对话框。 |
|  | 关闭 Pre-Generation/Post-Generation Editor，不保存命令行。 |

**相关主题**

- [“覆盖工程生成前和生成后操作”一节](../../../../07-完善工程/07-管理-SoundBank/04-配置用户-SoundBank-设置.md#defining_custom_user_steps_to_be_performed_pre_post_soundbank_generation "覆盖工程生成前和生成后操作")
- [“定义要在生成 SoundBank 之前/之后执行的操作”一节](../../../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md#defining_steps_to_be_performed_pre_post_soundbank_generation "定义要在生成 SoundBank 之前/之后执行的操作")

---