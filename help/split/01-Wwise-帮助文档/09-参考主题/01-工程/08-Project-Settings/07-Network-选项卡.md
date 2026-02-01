# Network 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Project Settings](00-Project-Settings.md) > Network 选项卡

### Network 选项卡

在 Project Settings（工程设置）对话框的 Network（网络）选项卡中，可指定 Wwise 设计工具与游戏通信时所要使用的端口号。

| 界面元素 | 描述 |
| --- | --- |
| **Game Discovery Broadcast Port (game side)（游戏探查广播端口（游戏端））** | |
| Communication Port Discovery Broadcast | 端口号。游戏端打开的端口。Wwise 设计工具将 Game Discovery（游戏探查）消息广播至该端口，因此游戏中和 Wwise 工程中应使用相同的端口，这点十分重要。由于游戏和Wwise 设计工具需要确定该端口，因此该端口不得为动态（不得设置为 0）。  Default value: 24024  Range: 1 to 65535 |
| **Game Discovery Response Port (authoring application side)（游戏探查响应端口（设计工具端））** | |
| Communication Port Discovery Response | 端口号。由设计工具打开的端口，当尝试找到您可连接的游戏时，会侦听在网络中广播的 Game Discovery 消息的响应。该端口号可以是动态的，这意味着操作系统需要时将选择随机端口号，而不是使用固定端口号。要使用动态端口号，请将该值设置为 0（这是默认值）。  Default value: 0  Range: 0 to 65535 |
|  | 确定。关闭 Project Settings 对话框并保存设置。 |
|  | 取消。关闭 Project Settings 对话框而不保存设置。 |

**相关主题**

- [“指定网络端口”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/07-指定网络端口.md "指定网络端口")
- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")

---