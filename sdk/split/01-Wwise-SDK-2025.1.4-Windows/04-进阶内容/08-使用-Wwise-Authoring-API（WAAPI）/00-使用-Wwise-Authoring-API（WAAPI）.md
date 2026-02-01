# 使用 Wwise Authoring API（WAAPI）

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

使用 Wwise Authoring API（WAAPI）

Wwise Authoring API 是用于与 Wwise 设计工具通信的。The functions available in the API allow the clients to perform several tasks, including:

- **Wwise 工程修改**，如：
  - 获取对象和它们的信息
  - 设置对象的信息
  - 创建新对象
- **常见操作**，如：
  - 导入音频文件
  - 生成 SoundBanks
  - 转码音频文件
  - 播放 Wwise 对象
- **用户界面的访问和控制**，如：
  - 打开视图
  - 访问当前选中内容并对它们进行改动
  - 察看对象
- **SoundEngine 方面的用途**，如：
  - 创建游戏对象并设置位置
  - 发送事件
  - 设置 Game Parameter（游戏参数）值、Switches（切换开关）和 States（状态）

# 用例示例

Wwise Authoring API 可以和以下项目集成：

- 游戏引擎
- 对话管理管线
- 用于声音设计、编辑、对话录音或音乐制作的 DAW
- 各种各样的脚本

The Wwise Authoring API 可以用于：

- 任务自动化，如导入音频文件或创建 Wwise 对象
- 在移动设备上远程控制 Wwise
- 实现自定义 Wwise 界面
- 向 Wwise 添加自定义功能。请参阅 [定义命令扩展](defining_custom_commands.html) 。

# 工作原理

WAAPI 是一种允许其他进程与 Wwise 设计工具进行通信的 API。WAAPI supports bidirectional communications, allowing processes to invoke remote procedure calls and to subscribe to their topics of interest so as to be notified when changes occur in Wwise.

WAAPI 允许访问三个不同层次的功能：

- Wwise 用户界面：视图、选项、命令等
- Wwise 设计工具核心：工程和对象、SoundBank、音频文件、走带等
- Wwise 声音引擎：Game Object、Post Event、RTPC Value 等

WAAPI 可通过各种编程语言来使用。如需查找最适合自身工作流的语言，请参阅 [编程语言](waapi_gettingstarted.html#waapi_languages) 。

# 详细了解 WAAPI

阅读更多关于特定话题的内容：

- [准备使用 Wwise Authoring API](waapi_prepare.html)
- [Wwise Authoring API (WAAPI) 快速入门](waapi_gettingstarted.html)
- [WAAPI 示例](waapi_samples.html)
- [查询 Wwise 工程](waapi_query.html)
- [Managing and Querying the Media Pool](waapi_mediapool.html)
- [订阅 Wwise Authoring API 中的话题](waapi_subscribe.html)
- [导入音频文件和创建架构](waapi_import.html)
- [在 Wwise 插件中使用 Wwise Authoring API](waapi_plugin.html)
- [Wwise Authoring API 示例索引](waapi_example_index.html)

参阅 Wwise Authoring API 参考文档中的以下话题：

- [Wwise Authoring API Reference](waapi_index.html)
- [Wwise 设计工具命令标识符](globalcommandsids.html)
- [Wwise Authoring Performance Monitor Counter Identifiers](globalcountersids.html)
- [Wwise Authoring View Identifiers](globalviewsids.html)
- [Wwise 对象参考](wobjects_index.html)