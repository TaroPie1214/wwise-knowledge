# Building your interactive music hierarchies

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > Building your interactive music hierarchies

## Building your interactive music hierarchies

To provide a musical score for your game, you will need to manage many musical assets and it is very useful to organize these assets into groups. Just as you can group objects together and create parent/child relationships for the sounds in your project, you can also benefit from organizing all the music assets in your project. This structure not only organizes your music assets but allows you to define properties and behaviors for the groupings that you create. Both sounds and music are organized in the Containers hierarchy.

You can use a combination of the following music object types to group your audio assets and build a structure for your interactive music project:

- [“什么是 Music Segment？”一节](01-什么是-Music-Segment？.md "什么是 Music Segment？") —— 由若干 Music Track（音乐轨）组成，每个 Music Track 都包含 Music Clip（音乐片段）。这些片段可以在 Music Segment （音乐段落）内进行排列对齐。
- [“容器类型”一节](02-容器类型.md "容器类型") —— 包含一组 Music Segment 或其它音乐容器，并遵循特定的播放行为。音乐容器共有两种：

  - Music Switch Container（音乐切换容器）根据调用的 Switch（切换开关）或 State（状态）来播放音乐对象。
  - Music Playlist Container（音乐播放列表容器）会按随机或顺序方式播放音乐。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 也可以用 Virtual Folder（虚拟文件夹）将音乐对象分组，但与其它音乐对象不同，Virtual Folder 不具有任何属性或行为。 |

---