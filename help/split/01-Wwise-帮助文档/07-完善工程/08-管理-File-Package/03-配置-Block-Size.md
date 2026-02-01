# 配置 Block Size

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [管理 File Package](00-管理-File-Package.md) > 配置 Block Size

## 配置 Block Size

The Block size determines the number of bytes upon which the data in a package is aligned.
Empty data pads out entries in the package.

A block size of 1 is sufficient for most platforms. However, when using Wwise's Sample
low-level I/O hooks, Windows and Xbox platforms require a multiple of 4096 to match the
size of sectors used for unbuffered I/O. Other implementations of the low-level I/O hook
that your project uses might have different requirements.

You can set this value as part of the File Packager project settings or, if a project is not
being used, as a command-line argument (see [“在命令行中使用 File Packager 参数”一节](06-在命令行中使用-File-Packager-参数.md "在命令行中使用 File Packager 参数")).

For more information about how block sizes are used in the runtime, see [Low-Level I/O](https://www.audiokinetic.com/library/edge/?source=SDK&id=streamingmanager_lowlevel.html) in the SDK documentation.

---