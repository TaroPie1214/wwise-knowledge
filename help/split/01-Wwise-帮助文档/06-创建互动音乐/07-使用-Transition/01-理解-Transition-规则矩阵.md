# 理解 Transition 规则矩阵

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [使用 Transition](00-使用-Transition.md) > 理解 Transition 规则矩阵

## 理解 Transition 规则矩阵

Transitions（过渡）选项卡的中间是 Transition Matrix（过渡矩阵）。您可以使用其创建一系列规则并定义 Music Switch Container（音乐切换容器）或 Music Playlist Container（音乐播放列表容器）内的各个对象如何过渡到容器内的其他各个对象。在使用过渡时，可为容器内的各对象创建特定的规则，也可创建适用于多个对象的通用规则。以下元素均可作为过渡规则的 Source（源）或 Desitination（目标）：

- **Music object：**音乐对象，可以是 Music Segment（音乐段落）、Music Playlist Container，也可以是 Music Switch Container。
- **Virtual Folder：**虚拟文件夹，Music Switch Container 内的音乐对象可组织到虚拟文件夹中。将 Virtual Folder 选为音乐过渡的 Source 或 Destination 时，过渡规则将对该文件夹内的所有音乐对象生效。
- **Any：**任意对象，表示容器中的任何音乐对象都可用作 Source 或 Destination。
- **Nothing：**无对象，表示 Source 或 Destination 为空，即不播放任何音乐对象。

过渡时，Wwise 将从规则列表底部开始向上搜索，直至找到与当前情形匹配的过渡规则。如果未找到匹配的过渡，则 Wwise 则将使用默认的“Any to Any”过渡。

### 添加过渡规则

Music Switch Container（音乐切换容器）或 Music Playlist Container（音乐播放列表容器）的过渡矩阵中至少包含一条过渡规则：Any to Any（任意到任意）。若想创建更有针对性的过渡规则，则须自行将其添加到过渡矩阵。

**向 Music Switch Container 或 Music Playlist Container 添加自定义过渡：**

1. 将 Music Switch Container 或 Music Playlist Container 加载至 Property Editor 中。
2. In the Transitions tab of the Secondary Editor, click **Add**.
3. 这时会将新建的 Any to Any（任意到任意）过渡规则添加到过渡矩阵。
4. 在 **Source**（源）列中，单击**选择器**按钮 **[>>]**，并根据需要选择以下选项：

   - **Any**任意源。为任何未指定的源音乐对象创建过渡。
   - **Nothing**无对象。创建没有源对象（即不播放任何音乐对象）的过渡。
   - **Browse**，浏览并选择特定音乐对象或含有对象的虚拟文件夹，过渡规则会将其作为源对象。这时会打开 Project Explorer - Browser（工程资源管理器 - 浏览器）。在此，可选择 Source（源）。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 另外，也可直接从 Project Explorer 将音乐对象拖到过渡矩阵中。但要注意，对于加载到 Property Editor 中的容器，只有作为其子对象的音乐对象才能添加到矩阵中。 |
5. 在 **Destination**（过渡目标）列中，点击 **选择按钮** (**>>**)，并选择下列选项之一：

   - **Any**任意对象。过渡将适用于任意目标音乐对象。
   - **Nothing**无对象。创建没有目标对象（即不播放任何音乐对象）的过渡。
   - **Browse**，浏览并选择特定音乐对象或含有对象的虚拟文件夹，过渡规则会将其作为目标对象。这时会打开 Project Explorer - Browser（工程资源管理器 - 浏览器）。在此，可选择 Destination（目标）。

   新建的自定义过渡规则将被添加到过渡矩阵。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 您可以通过选中过渡矩阵中的过渡规则并上下拖动来更改它们的顺序。红线指示会将过渡规则放在哪里。“Any to Any”将是 Wwise 检查的最后一个过渡规则，因此无法从矩阵顶部下移。 |

在 Transitions 选项卡中，还可右键单击现有 Transition 并依据其 **Source** 或 **Destination** 来添加新的 Transition；在其 **Source** 或 **Destination** 未设为 Any 时，可利用 New Transition 快捷菜单选项来复制 **Source** 或 **Destination** 并创建新的 Transition。

### 复制和粘贴过渡规则

您可以轻松复制粘贴矩阵内的过渡规则来加快 Transition（过渡）的创建流程。

**从 Music Playlist Container（音乐播放列表容器）或 Music Switch Container（音乐切换容器）中复制自定义过渡规则的方法如下：**

1. 将 Music Switch Container 或 Music Playlist Container 加载至 Property Editor 中。
2. Switch to the Transitions tab of the Secondary Editor.
3. 在过渡矩阵中，右键单击要复制的过渡规则并从菜单中选择 **Copy**（复制）。
4. 在列表中，右键单击要粘贴过渡规则的位置并从菜单中选择 **Paste**（粘贴）。

   这时会将过渡规则的副本添加到过渡矩阵中的选定位置。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 另外，也可使用快捷键（Ctrl+C、Ctrl+V）在矩阵内复制粘贴过渡规则。 |

### 对过渡规则排序

在需要实施过渡时，Wwise 会自下至上检索过渡矩阵来寻找与当前情形匹配的过渡规则。一旦找到匹配的过渡规则就会停止检索，无论找到的过渡规则是否最为合适。为确保应用最为适合的过渡规则，可按从通用到特定的顺序对过渡矩阵中定义的规则进行排序（如下例所示）。

![](../../../../images/music_transition_matrix.png)

与 Source（源）或 Destination（目标）使用特定音乐对象的过渡规则相比，使用 **Any**（任意）或 **Nothing**（无）的过渡规则应该排在列表前面。这样可以确保 Wwise 在检索通用规则前就能找到特定规则。

### 移除过渡规则

若不再需要过渡矩阵中定义的过渡规则，则可轻松将其移除。在移除过渡规则时，不会删除 Source（源）和 Destination（目标）音乐对象。

**从 Music Playlist Container（音乐播放列表容器）或 Music Switch Container（音乐切换容器）中移除自定义过渡规则的方法如下：**

1. 将 Music Switch Container 或 Music Playlist Container 加载至 Property Editor 中。
2. Switch to the Transitions tab of the Secondary Editor.
3. 在过渡矩阵中，选择要移除的过渡规则。
4. 单击 **Remove**（移除）或按下 **Delete** 键。

   这时会从过渡矩阵中移除所选过渡规则。

---