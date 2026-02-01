# 管理 File Package

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > 管理 File Package

## 管理 File Package

The File Packager is a standalone utility that groups a Wwise project's SoundBanks, loose media, and streamed media into one or more file packages. 文件包是将文件系统抽象化之后的独立单元，Loading a file package creates a lookup table in memory, which Wwise uses to locate the media in the package. By using file packages, you can avoid some of the limitations of a platform's file system, including the limit on the length of file names as well as the actual number of files. You can also use file packages to better manage language versions as well as downloadable content (DLC) that is made available after the game is released.

You can use the File Packager to create your file packages manually, or you can use the
command line to run the File Packager as part of the SoundBank generation process. You can
define the command line at the project level or as a custom SoundBank user setting. For more
information on using the command line to launch the File Packager after SoundBank
generation, see the following topics:

- [“定义工程的 SoundBank 设置”一节](../../03-设置工程/01-处理工程/02-定义工程设置/03-定义工程的-SoundBank-设置.md "定义工程的 SoundBank 设置")
- [“配置用户 SoundBank 设置”一节](../07-管理-SoundBank/04-配置用户-SoundBank-设置.md "配置用户 SoundBank 设置")
- [“在命令行中使用 File Packager 参数”一节](06-在命令行中使用-File-Packager-参数.md "在命令行中使用 File Packager 参数")

---