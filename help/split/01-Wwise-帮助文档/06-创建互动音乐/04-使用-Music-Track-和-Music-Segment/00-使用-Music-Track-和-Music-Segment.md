# 使用 Music Track 和 Music Segment

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > 使用 Music Track 和 Music Segment

## 使用 Music Track 和 Music Segment

The Music Segment is the basic unit of interactive music. 它与多轨音序器类似，用于排列音乐轨和子音乐轨，为游戏创建多声部配乐。音乐轨（Music Track）可包含无限数量的子音乐轨，各条子音乐轨可包含不同的音乐片段。通过为各条音乐轨指定不同的播放行为，可以为游戏中的音乐增加变化。

为了帮助您轻松识别界面中音乐段落和音乐轨，Wwise 使用特定的图标来标识它们。

| 图标 | 代表 |
| --- | --- |
| |  | | --- | |  | | Music Track —— 音乐轨。每次播放其父段落时播放该音乐轨。 |
| |  | | --- | |  | | Random Music Track —— 随机音乐轨。每次在播放其父段落时，按随机顺序播放其子音乐轨。 |
| |  | | --- | |  | | Sequence Music Track —— 序列音乐轨。每次在播放其父段落时，按序播放其子音乐轨。 |
| |  | | --- | |  | | Switch Music Track —— 切换开关音乐轨。根据相关联的切换开关组播放其子音乐轨。 |
| |  | | --- | |  | | Music Segment —— 音乐段落。音乐轨的父对象。 |

指定段落中的所有音乐轨都显示在 Music Segment Editor 中。音乐轨包含音乐片段，可以对这些音乐片段进行查看和编辑。这些片段代表音频源，并以波形方式在 Music Segment Editor 时间线上显示。您可以编辑这些这些片段，并在时间线上的特定点给这些片段添加 cue （提示点）。您还可以创建自定义提示点（Custom Cue），以指示何时改变属性变化或进行过渡，或何时播放插播乐句（Stinger）。

其中一种最好用的提示便是 Event（事件）提示。利用这种提示，可将 Event 快速添加到 Music Segment 时间线中的特定时间点。

|  |
| --- |
|  |

Music Segment Editor 包含三个区域：

- Snap 按钮部分，用于将片段和提示点对齐至所选的元素。
- 音轨控制部分，用于编辑音轨的属性设置，以及单条轨道的静音和强制播放。
- 段落时间线部分，用于查看片段和提示点。

|  |
| --- |
|  |

## 向 Music Segment 添加 Music Track

您可以从 Wwise 中的以下位置将音乐轨（Music Track）添加至段落（Muisc Segment）：

- Project Explorer 的 Audio 选项卡
- Music Segment Editor（音乐段落编辑器）

|  |  |
| --- | --- |
| [备注] | 备注 |
| 默认情况下，新的音轨将使用 Normal 行为。要为音乐轨设置不同的行为，请参阅 [“定义 Music Track 的播放行为”一节](01-定义-Music-Track-的播放行为.md "定义 Music Track 的播放行为")。 |

**从 Audio 选项卡添加新音乐轨的方法如下：**

1. In the Containers hierarchy, right-click the segment to which you want to add a track and select **New Child > Music Track.**

   新音乐轨被添加到段落中，并显示在 Music Segment Editor 里。
2. 将默认名称替换为更适合音乐轨的名称。

**在 Music Segment Editor 中添加新音乐轨的方法如下：**

1. 将段落加载至 Music Segment Editor。
2. 在 Music Segment Editor 中，右键点击以打开快捷菜单，然后选择 **New Track**。

   这时会打开 New Music Track（新建音乐轨）对话框。
3. 将默认名称替换为更适合音乐轨的名称，然后点击 **OK**。

   新音乐轨将被添加至 Music Segment Editor。

---