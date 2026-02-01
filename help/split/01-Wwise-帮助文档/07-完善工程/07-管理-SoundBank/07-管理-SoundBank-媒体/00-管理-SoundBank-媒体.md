# 管理 SoundBank 媒体

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理 SoundBank](../00-管理-SoundBank.md) > 管理 SoundBank 媒体

## 管理 SoundBank 媒体

生成的 SoundBank（音频包）不一定包含所有需要的媒体文件（具体取决于 Wwise 工程的结构）。有些媒体文件可能需要随 SoundBank 一起打包。

为便于理解，假设存在包含以下内容的示例工程：

- 一个导入的媒体文件 beep.wav，具有关联的 SFX 对象 sfx\_beep。
- 一个为播放 SFX 创建的 Event：play\_beep。
- 一个 SoundBank：sb\_beep。SoundBank 唯一包含的内容就是 play\_beep Event。
- 工程有一个目标平台：Windows。

原样导入的文件 beep.wav 包含在工程的 Originals 文件夹中。在生成 sb\_beep SoundBank 的过程中，Wwise 会对 beep.wav 进行处理。

- 该文件将依据 Conversion Settings（转码设置）进行转码。转码后的文件存储在工程的 .cache 文件夹中。有关详细信息，请参阅“[“定义工程的转码设置”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/02-定义工程的转码设置.md "定义工程的转码设置")”。

  转码后的文件指派有 Media ID（媒体 ID）。该 Media ID 是一个随机指派的 32 位整数值。有关详细信息，请参阅[“管理媒体素材 ID”一节](../../../03-设置工程/05-管理工程中的媒体文件/10-管理媒体素材-ID.md "管理媒体素材 ID")。

在完成 SoundBank 生成后，Wwise 会在配置的输出文件夹中创建 sb\_beep.bnk 文件。假设为转码后的文件指派的 Media ID 为 123。sb\_beep.bnk 文件包含 play\_beep Event，其引用 123.wem媒体文件。若满足以下条件，Wwise 会将 123.wem 打包到 sb\_beep.bnk 中：

- 没有将声音配置为流播放。有关更多详细信息，请参阅“[“流播放媒体”一节](../../../05-使用声音和振动来提升游戏体验/01-定义对象播放行为/01-定义对象的播放行为/00-定义对象的播放行为.md#streaming_media "流播放媒体")”。
- 没有将 SoundBank 配置为排除媒体文件。有关更多详细信息，请参阅“[“SoundBank Editor 视图”一节](../../../09-参考主题/04-Project-Explorer/03-SoundBanks-选项卡/01-SoundBank-Editor-视图/00-SoundBank-Editor-视图.md "SoundBank Editor 视图")”。

若 SoundBank 没有包含媒体文件，Wwise 会尝试在磁盘上查找文件。磁盘上的媒体文件一般都放在特定的位置。有关详细信息，请参阅“[“SoundBank 输出文件夹布局”一节](../06-SoundBank-输出文件夹布局.md "SoundBank 输出文件夹布局")”和“[“管理输出文件夹中的零散媒体文件”一节](01-管理输出文件夹中的零散媒体文件.md "管理输出文件夹中的零散媒体文件")”章节。

---