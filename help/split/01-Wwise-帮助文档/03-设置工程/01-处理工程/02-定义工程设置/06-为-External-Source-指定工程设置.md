# 为 External Source 指定工程设置

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [设置工程](../../00-设置工程.md) > [处理工程](../00-处理工程.md) > [定义工程设置](00-定义工程设置.md) > 为 External Source 指定工程设置

### 为 External Source 指定工程设置

若打算使用 [“External Source（外部源）”一节](../../../10-Wwise-插件/03-源插件/03-External-Source（外部源）/00-External-Source（外部源）.md "External Source（外部源）") 插件，则须指定 External Sources List 文件的存放位置。这个 XML 文件可用来指定以下设置：

- 可与 Wwise 中创建的 External Source 关联的外部音频文件的存放位置。
- 用于转换每个文件的 Conversion Settings。

您还必须指定保存经过转码后的源的文件夹，以便 Wwise 声音引擎在运行时可以使用它们。另外，输出文件夹路径中还可包含环境变量（如 `$(WWISESDK)` 或 `$(TEMP)`）。

您可以使用 SoundBank Manager（音频包管理器）的 User Settings（用户设置）覆盖这些工程设置。请参阅 [“为 External Source 指定用户设置”一节](../../../07-完善工程/07-管理-SoundBank/04-配置用户-SoundBank-设置.md#specifying_input_ouput_location_for_external_source_files "为 External Source 指定用户设置")。

**为 External Source 指定工程设置：**

1. 在菜单栏中，点击 **Project** > **Project Setting**。
2. 在 Project Settings（工程设置）对话框中，切换到 **[“External Sources 选项卡”一节](../../../09-参考主题/01-工程/08-Project-Settings/06-External-Sources-选项卡.md "External Sources 选项卡")**。
3. 在 **Input Path**（输入路径）分组框中，根据需要执行以下操作来指定要将 External Sources List（外部源列表）文件 (WSOURCES) 存储到哪个位置：

   - 点击 **External Sources List**，然后输入外部资源列表文件所在的路径。
   - 点击游戏平台的相应浏览按钮 [...]，前往该平台外部资源列表文件的文件夹，然后点击 **Open**。
4. 对工程中的各个有效平台重复执行步骤 **3**。
5. 在 **Output Path**（输出路径）分组框中，根据需要执行以下操作来指定要将转码后的 External Source（外部源）保存到哪个位置：

   - 点击 **External Sources Output Folder** 列表，并输入要保存音频文件的路径。
   - 单击与其中一个游戏平台对应的“浏览”按钮 [...] 来使用 [“Advanced Folder Picker”一节](../../../09-参考主题/01-工程/08-Project-Settings/09-Advanced-Folder-Picker.md "Advanced Folder Picker") 指定要将与该平台关联的转码音频文件保存到哪个文件夹，然后单击 **OK**（确定）。
6. 对各个平台执行步骤 **5**。
7. 单击 **OK**（确定）关闭 Project Settings（工程设置）对话框。

---