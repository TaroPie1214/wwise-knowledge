# Available 选项卡

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [工程](../00-工程.md) > [Remote Connections](00-Remote-Connections.md) > Available 选项卡

### Available 选项卡

Remote Connections（远程连接）对话框的 Available（可用）选项卡会显示网络中自动发现的远程游戏主机。为了使 Wwise 自动检测并连接到某个游戏机，该游戏机必须与 Wwise 位于相同的网络子网中，并且必须在 Wwise 工程设置中以及在游戏中初始化通信模块时指定相同的“Game Discovery Broadcast Port”。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../../04-Project-Explorer/07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../../04-Project-Explorer/01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](../../04-Project-Explorer/12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。您将连接到的特定游戏机的名称。 |
| Platform | 游戏机的平台类型，从 [“Platform Manager”一节](../09-Platform-Manager/00-Platform-Manager.md "Platform Manager") 中定义的名称中进行选择。 |
| Base Platform | 基础平台。平台对应的 SDK，如 Android、iOS、PlayStation 4、Switch、Windows 或 Xbox One。 |
| Status | 远程游戏机的状态。状态可以是以下类型之一：  - **Ready** —— 就绪。游戏机处于就绪状态，可接受连接。 - **Busy** —— 忙碌。游戏机已连接到设备，因此无法再接受任何连接。状态为 Busy 时，会显示已连接到游戏机的设备名称。 - **Different Version** —— 版本不同。Wwise 的版本与运行在远程 PC 或游戏机上的游戏版本不兼容。 - **Not Available** —— 不可用。设备不再与网络相连。 |
| IP Address | IP 地址。游戏机的网络地址。 |
| Application Name | 应用名。在初始化声音引擎时提供的应用程序名称。 |
| Port | 检测到的通信动态端口。（仅通过 IP 连接时可用） |
| Ping | Ping。往返延迟（毫秒）。 |
|  | 更新有关列表中各个游戏机的信息。 |
|  | 连接到列表中当前选择的设备。 |
|  | 连接到 IP…。打开对话框以指定主机的 IP 地址。 |
|  | 连接到文件…。打开对话框以选择包含上一性能分析会话所有数据的 .prof 文件。 |
|  | 删除列表中当前所选设备的连接。 |
| Synchronization Method | 同步方式。指定如何处理与远程应用的同步：  - **Profile Only**: There is no synchronization with the   remote instance.  Note that playback in Wwise Authoring is unavailable when connected in **Profile Only** mode because objects and media are not synchronized   with the remote instance.  您可以使用该选项快速连接到远程应用来实施性能分析，同时避免因意外同步而导致声音引擎对工程作出更改。 - **Profile and Edit (Sync Inspected Objects Only)**: Only   objects that are currently inspected in the Transport Control are synchronized, in   addition to all necessary related objects, such as the Output Bus, Effects, and   Attenuation.  This means that changes to other objects in your Wwise project are not synchronized.   The sound engine plays back objects in the remote instance based on the behaviors defined   in the last generated SoundBanks, while also applying any changes made to the Wwise   project during the current remote connect session.  Modified media (sounds, MIDI, Convolution IR, etc.) that is currently in use by the   game is also transferred to the game. - **Profile and Edit (Sync All Modified Objects)**: All objects   that are modified in the Wwise project and are also loaded in the remote instance are   synchronized.  您可以使用此选项来在连接时自动同步所有加载的对象（在连接的情况下加载 SoundBank 时也会如此）。  Modified media (sounds, MIDI, Convolution IR, etc.) that is currently in use by the game is   also transferred to the game.  有关更多详细信息，请参阅“[“Editing while profiling a game”一节](../../../07-完善工程/06-性能分析/08-Editing-while-profiling-a-game.md "Editing while profiling a game")”。 |
| Start capture on connect | 连接上即开始捕获。决定何时开始捕获过程。如果勾选该选项，则捕获过程会在连接时开始。如果未勾选该选项，则捕获过程仅在您点击 Start Capture 按钮时开始。  新捕获过程每次启动时，Capture Log 中的所有现有数据都会清除。 |
| Status | 状态。显示您当前是否连接到远程游戏机。如果已连接，它就会显示远程游戏机的名称和 IP 地址。 |
|  | 关闭。关闭 Remote Connections 对话框，而不中断任何活跃连接。 |

**相关主题**

- [“连接至本地/远程游戏系统”一节](../../../07-完善工程/06-性能分析/06-连接至本地远程游戏系统.md "连接至本地/远程游戏系统")
- [“从已有的远程捕获会话加载数据”一节](../../../07-完善工程/06-性能分析/07-从声音引擎捕获数据/09-从已有的远程捕获会话加载数据.md "从已有的远程捕获会话加载数据")
- [“指定网络端口”一节](../../../03-设置工程/01-处理工程/02-定义工程设置/07-指定网络端口.md "指定网络端口")

---