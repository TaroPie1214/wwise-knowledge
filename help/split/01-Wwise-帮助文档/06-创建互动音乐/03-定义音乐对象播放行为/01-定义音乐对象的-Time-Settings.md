# 定义音乐对象的 Time Settings

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [定义音乐对象播放行为](00-定义音乐对象播放行为.md) > 定义音乐对象的 Time Settings

## 定义音乐对象的 Time Settings

在为游戏创作互动音乐时，最好让音乐的变换时机与当前音乐的曲速和节拍协调一致。原始音乐导入 Wwise 后，可以用 Time Settings（时间设置）来指定音乐对象速度和节拍。这些设置作为 Wwise 中音乐对象的标记，可以让您轻松地设置音乐的同步点和过渡点。

除了曲速和拍号，还可使用 Grid（网格）设置来指定如何划分时间网格，从而将 Music Segment（音乐段落）划分成特定长度的虚拟段落。这将为音乐段落添加另一个划分精度，让您在为音乐过渡、状态更改和插播乐句定义同步点时，有更大的灵活性。

您可以为 Music Segment、Music Playlist Container（音乐播放列表容器）和 Music Switch Container（音乐切换容器）设置 Time Settings。

**为音乐对象设置 Time Settings 的方法如下：**

1. 将音乐对象加载到 Property Editor（属性编辑器）。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果不是顶层对象，须先选择 Override parent（不沿用父项）选项，然后才能定义 Time Settings。 |
2. 在 Tempo（速度）文本框中，键入原始音乐的速度（单位为每分钟节拍数，即 bpm）。
3. 在 Time Signature（拍号）文本框中，键入原始音乐每小节的拍数和长度。
4. 在 Frequency（网格频率）下拉菜单中，选择用多长的网格来划分 Music Segment，例如 4 bars（每 4 小节）、beat（每拍）、whole note（每个全音符）等。
5. 若要为频率值设定偏置，请从列表中选择预定义选项，或者通过选择 Custom（自定义）并在对应 Offset（偏置）文本框中键入数值（单位为毫秒）来创建自定义偏置。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | Grid 设置中的 Frequency 和 Offset 让音乐对象多了一种划分精度，在给音乐过渡、状态更改和插播乐句设置同步点时，将会更加灵活。 |

---