# macOS 插件注意事项

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

macOS 插件注意事项

为了能够在 macOS 上使用 Wwise 设计工具，我们使用了适配层来允许在 Mac 系统上执行 Windows 二进制文件。相应地，设计工具插件二进制文件必须为 Windows DLL。如此一来，便无法以本机方式在 Mac 机器上构建插件的设计工具部分：您需要使用 Windows 机器或运行 Windows 的虚拟机，并安装相应的 Visual Studio 构建工具。

该限制仅针对插件的设计工具部分。换句话说，对于目标为 Apple 平台的声音引擎部分，要在运行 macOS 的 Mac 机器上加以构建。本机声音引擎插件库必须采用 Apple 的库格式（.dylib 或 .a），并与游戏一并分发或与之进行链接。

不过，正如前文所述，因为 Wwise 设计工具即便在 macOS 上也会使用 Windows 二进制文件，所以链接到设计工具插件以便进行试听的声音引擎部分必须为 Windows 库。

# 设计工具插件在 macOS 上的存放位置

在 macOS 上通过 Audiokinetic Launcher 安装 Wwise 设计工具时，会将相关文件存放在不同的位置。主应用程序包 `Wwise.app` 存放在安装时选定的安装目录下，其包含运行 Wwise 所需的适配文件。不过，实际的 Wwise 设计工具二进制文件会存放在全局位置：`/Library/Application Support/Audiokinetic`。这样在添加插件文件时才能避免修改 `Wwise.app`（出于安全原因，须保持只读模式）。

要想测试插件，只需通过 Launcher 添加打包好的插件即可。当然，也可手动将 DLL 和 XML 文件复制到设计工具插件的目录下：

`/Library/Application Support/Audiokinetic/Wwise <Version>/Authoring/x64/Release/bin/Plugins`

|  |  |
| --- | --- |
|  | **备注:** 要想使用新插件，必须重新启动 Wwise 设计工具。 |

# 在 macOS 上调试设计工具插件

因为插件的调试符号为 [Microsoft](namespace_microsoft.html) PDB 格式，所以不便将调试程序与进程绑定并逐步调试代码。不过，可通过启动脚本来启动 Wwise 设计工具，以此读取主机输出。

启动脚本存放在 `<Install Location>/Wwise.app/Contents/Tools/WwiseOpenProject.sh` 中，可使用完整的绝对路径从 Terminal 应用程序启动（前后加引号或手动转义空格）。

该脚本只需一项可选参数：所要打开的 Wwise 工程的路径。若未给定，则照常打开 Wwise。一旦启动，便会在主机中显示标准输出。您可以通过在插件的代码中添加 `printf` 调用来记录此输出。