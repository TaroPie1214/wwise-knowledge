# 定义 Music Playlist Container 的播放行为

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [定义音乐对象播放行为](00-定义音乐对象播放行为.md) > 定义 Music Playlist Container 的播放行为

## 定义 Music Playlist Container 的播放行为

为了让工程中数量有限的音乐得到充分利用，可将 Music Segment（音乐段落）分组存放到 Music Playlist Container（音乐播放列表容器）中。Music Playlist Container 用途广泛，允许以多种方式将段落编组，各 Group（编组）都可以有不同的播放行为，播放模式和类型。播放类型决定了该编组将随机播放还是顺序播放，而播放模式决定了该编组每次播放的段落数量。

下图举例展示了如何使用 Music Playlist Container 对工程中的 Music Segment 进行分组。

|  |
| --- |
|  |

### 在 Music Playlist Container 内创建分组

您可以通过将 Music Segment 分组存放到 Music Playlist Container 中来构建复杂的音乐结构。可以建立多个 Group（编组），将其重新排列、删除、剪切、复制和粘贴，再将 Music Segment 添加到编组中。关于为 Music Playlist Container 添加内容的详细信息，请参阅[“为 Music Playlist Container 添加内容”一节](02-定义-Music-Playlist-Container-的播放行为.md#populating_music_playlist "为 Music Playlist Container 添加内容")。

**在 Music Playlist Container 中新建编组的方法如下：**

1. 将音乐播放列表容器加载到 Property Editor。

   顶层组会自动在音乐播放列表编辑器中加以创建。
2. 要在播放列表层级结构中添加新编组，请点击 **New Group**（新编组）。

   层级结构中所选父对象下面将添加新的编组。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 要从播放列表中删除某个编组，请右键点击并选择 **Delete**（删除），或选择编组并按 Delete 键。整个编组的全部内容都会从播放列表中删除。 |
3. 继续向播放列表中按需添加编组。

   您随时都可以定义播放列表内各个分组的行为。

### 定义 Music Playlist Container 内各个分组的行为

对于 Music Playlist Container 内的各个分组，可根据需要选用两种播放模式和播放类型。播放类型决定组是以随机方式还是以顺序方式播放。播放模式决定每次播放组时将会播放组的段落数量。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 您选择的播放模式和类型将决定各编组有哪些行为选项可用。 |

**在 Music Playlist Container 中定义 Random Group（随机编组）的方法如下：**

1. 将 Music Playlist Container 加载到 Property Editor（属性编辑器）。

   顶层组会自动在音乐播放列表编辑器中加以创建。
2. In the Primary Editor, from the Group/Segment list, select one of the following
   options to define the playback behavior of the top-level group:

   - **Random Continuous** - Plays all music objects in the group one after the other in random order each time the group is played.
   - **Random Step** -- 随机步进。每次播放编组时，仅随机播放其中的一个音乐对象。
3. 从 Random Type（随机类型）列表中，选择以下选项之一：

   - **Standard** -- 标准模式，始终保持对象池完整。一个音乐对象播放后，该对象将不会从对象列表中删除，因此可能重复播放。
   - **Shuffle** -- 洗牌模式，音乐对象播放后，会从对象池中删除。一个音乐对象播放后，会等到编组中所有其他音乐对象都已播放完毕，才可能重复播放该音乐对象。
4. 可以在 Avoid Repeat（避免重复）文本框中键入数量，这样一个音乐对象播放后，将先播放该数量的其他音乐对象，之后才可能重复播放该音乐对象。
5. 在 Loop Count（循环次数）文本框中，指定整个组将播放的次数或将要播放的步进数。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在循环某个步进组时，您可以定义每次播放组时将要播放的组内对象数。 |

**在 Music Playlist Container 中定义 Sequence Group（序列编组）的方法如下：**

1. 将音乐播放列表容器加载到 Property Editor。

   顶层组会自动在音乐播放列表编辑器中加以创建。
2. In the Primary Editor, from the Group/Segment list, select one of the following
   options to define the playback behavior of the top-level group:

   **Sequence Continuous** - Plays all music objects in the group in sequential order each time the group is played.

   **Sequence Step** -- 顺序步进。每次播放编组时，仅播放其中的一个音乐对象，而下次将播放下一个音乐对象。
3. 在 Loop Count 文本框中，指定整个编组的循环播放的次数（或步进数）。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 对于 Step Group（步进编组），Loop Count 将决定其每次会播放几个对象。比如，若 Sequence Step 分组包含六个段落且 Loop Count 被设为了 2，则在第一次播放分组时会播放段落 1 和 2，在第二次播放分组时会播放段落 3 和 4…以此类推。 |

### 为 Music Playlist Container 添加内容

Just like the Sequence Container in the Containers hierarchy, you must specify which segments within the Music Playlist Container will be added to the playlist and in which order. Each segment must belong to a group that defines the playback behavior of the segments within the group. 关于定义编组播放行为的详细信息，请参阅[“定义 Music Playlist Container 内各个分组的行为”一节](02-定义-Music-Playlist-Container-的播放行为.md#defining_group_behaviors_within_music_playlist_containers "定义 Music Playlist Container 内各个分组的行为")。

**为 Music Playlist Container 添加内容的方法如下：**

1. 将音乐播放列表容器加载到 Property Editor。
2. 在 Content Editor（内容编辑器）中，将若干段落拖拽到音乐播放列表内的编组中。

   所选段落将被添加到编组中。
3. 对于 Random Step（随机步进）或 Random Continuous（随机连续）编组，可以在 Weight（权重）文本框中为各对象设置权重。权重可以让某些音乐对象的优先级高于其它对象。
4. 在 Loop Count（循环次数）文本框中，指定各段落将播放的次数。
5. 继续将段落拖到 Music Playlist Container（音乐播放列表容器）内的各个分组。

---