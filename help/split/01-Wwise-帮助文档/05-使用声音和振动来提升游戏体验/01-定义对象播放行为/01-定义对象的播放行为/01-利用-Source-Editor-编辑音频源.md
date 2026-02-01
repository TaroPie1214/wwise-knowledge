# 利用 Source Editor 编辑音频源

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../../00-使用声音和振动来提升游戏体验.md) > [定义对象播放行为](../00-定义对象播放行为.md) > [定义对象的播放行为](00-定义对象的播放行为.md) > 利用 Source Editor 编辑音频源

### 利用 Source Editor 编辑音频源

Source Editor（源编辑器）可用于编辑以下类型的对象：

- 音频源（WAV 或 AMB 文件）
- 源插件（Silence、Sine、Tone Generator 等）

The editing functions such as trimming, looping, and fades are not available for
the Audio Source objects of music objects, because these operations
are available as part of the Music Segment and Music Clip objects.

以下章节所述的操作都已存储到工程的 Work Unit（工作单元）中。这些操作会在对源素材实施转码的过程中执行并且都是非破坏性的。

有关 Source Editor 的参考信息，请参阅 [“Source Editor：音频源”一节](../../../09-参考主题/04-Project-Explorer/01-Audio-tab/06-Source-Editor：音频源.md "Source Editor：音频源")。

#### 对音频源的内容进行修剪

在修剪时，可移除 WAV 文件开头或结尾的无声内容以节省游戏所占的空间。在转码和播放的过程中，会弃用 Trim Start 和 Trim End 以外的内容。

**定义修剪位置：**

- 拖动 **Trim Start**（修剪起点）图柄（波形左下角的四方图柄）。
- 拖动 **Trim End**（修剪终点）图柄（波形右下角的四方图柄）。

#### 定义 Fade-in 和 Fade-out 区域

**定义 Fade-in 和 Fade-out 区域：**

- 拖动 **Fade-in**（淡入）图柄（波形左上角的三角图柄）。
- 拖动 **Fade-out**（淡出）图柄（波形右上角的三角图柄）。
- 右键单击图柄来选择淡变曲线。

#### 循环和交叉淡变

**调节循环点和使用交叉淡变：**

1. 在父级 Sound 对象中，启用 **Loop**（循环）。
2. 在 Source Editor（源编辑器）中，启用 **Override wav loop points**（不沿用 WAV 循环点）。这样就会不沿用 WAV 中的循环点。否则，会默认使用这些循环点。在下一步设置 Loop Start 时，会自动启用 Override wav loop points。
3. 向右拖动 **Loop Start**（循环起点）图柄（波形左上角的绿色图柄）。为避免循环时出现噼啪噪声，建议将循环点放在 PCM 数据的零交叉位置。
4. 向左拖动 **Loop End**（循环终点）图柄（波形右上角的红色图柄）。
5. 在侧面板中，定义 **Crossfade Duration**（交叉淡变时长）。这样可以让循环更流畅，同时还可移除噼啪噪声。

#### 添加和编辑文件标记

音频源文件可能包含标记，有时会被用作同步点或提示点。标记具有与文件位置绑定的唯一 ID。Wwise 可在 Source Editor 的坐标图中使用这些标记。另外，还可编辑这些标记或另外添加标记，但不会影响到原始文件。

您可以单击所需标记并将其拖放到要在源文件中标识的位置。比如，以此来显示文件哪里存在问题。或者提示即将发生的重要事件。比方说在对白中，可利用其来区分不同角色说话的时间点。所以，您可以根据具体需要自由地设置标记。

**在 Source Editor 的侧面板中，可选择 Marker Input Mode：**

- **Use File Markers**（使用文件标记）：使用源音频文件的标记。
- **Use Markers From Transients**（使用来自瞬态的标记）：通过自动检测瞬态起始点来放置标记。在移动 Marker Detection Sensitivity（标记检测灵敏度）滑杆时，才会显示这些标记。灵敏度越高，产生的标记越多。调整滑杆以使检测到的瞬态起始点尽可能靠近所需位置。然后，手动编辑这些标记。一旦编辑标记，标记模式就切换为 Manual Markers。
- **Manual Markers**（手动标记）：使用用户设置的标记。在选中 Manual Markers 时，并不会改变先前已有的标记位置。无论是文件标记还是来自瞬态的标记，用户都可以随时直接编辑。一旦进行编辑，标记选择就会设为 Manual Markers。

在 Source Editor 的坐标图内，可使用四个快捷菜单选项来快速编辑标记。

**标记专用的快捷菜单选项：**

- **Add Marker**（添加标记）：在 Source Editor 坐标图内的现有标记之外打开快捷菜单时，将显示此选项。它用于在坐标图时间线的指定时间点创建新的无标签的标记。
- **Delete All Markers**（删除所有标记）：在 Source Editor 坐标图内任意位置打开快捷菜单时，都会显示此选项。它用于移除来自源文件的所有标记。不过，这并不会影响原始文件标记。
- **Delete Marker**（删除标记）：只有在特定标记图柄位置打开快捷菜单时，才会显示此选项。它用于移除特定标记。它也不会影响原始文件标记。
- **Edit Marker Label...**（编辑标记标签...）：只有在特定标记图柄位置打开快捷菜单时，才会显示此选项。它会显示 Edit Label（编辑标签）对话框，其中显示所选标记的当前标签，便于根据需要更改标签。
- **Edit Markers in List View**（在列表视图中编辑标记）：在 Source Editor 坐标图内任意位置打开快捷菜单时，都会显示此选项。它会显示 List View（列表视图），其中有两个标记专用的列，用来查看和编辑所有源文件中的标记（包括 Wwise 中创建的标记）。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 除了使用“撤消”操作（依次选择 Edit > Undo 或按下 Ctrl+Z），还可通过将 **Marker Input Mode**（标记输入模式）改为 **Import From File**（从文件导入），来轻松恢复原始文件的标记。不过，一定要谨慎！在执行此操作后，所有手动输入的标记都将消失。 |

下图简要显示了 Wwise Source Editor 内的一些常用标记选项。

|  |
| --- |
|  |

**相关主题**

- [Wwise Fundamentals Module 2: Using a single WAV file for multiple
  applications](https://www.audiokinetic.com/en/courses/wwise101/?source=wwise101&id=single_sound_multiple_applications)

---