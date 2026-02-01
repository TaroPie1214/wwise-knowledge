# WwiseProjectDatabase 模块

|  |
| --- |
| Wwise Unreal Integration Documentation |

WwiseProjectDatabase 模块

WwiseProjectDatabase 模块可用于未烘焙的工程（包括用在 Editor 中）。此模块提供基于内存的数据库视图，方便查看 Wwise 工程所生成 SoundBank 的当前状态。It uses the [Wwise Project Database Sample](https://www.audiokinetic.com/en/library/edge/?source=SDK&id=soundengine_project_database_samplecode.html) with its own Adapter Types: The Unreal Adapters.

# 访问信息：WwiseProjectDatabase 和 WwiseDataStructure

WwiseProjectDatabase 模块会通过其访问方法来处理查询。比如，您可以请求获取所有已知 SoundBank，也可请求获取特定的 SoundBank。数据本身保存在其 DataStructure 成员中。

通常，WwiseProjectDatabase 中一次只会加载一个平台以供烘焙和打包；不过，在必要时可以加载不止一个平台。

|  |  |
| --- | --- |
|  | **注記：** 在 Mac 上使用 Unreal Editor 处理工程时，只有 Mac 平台是必须加载的。 |