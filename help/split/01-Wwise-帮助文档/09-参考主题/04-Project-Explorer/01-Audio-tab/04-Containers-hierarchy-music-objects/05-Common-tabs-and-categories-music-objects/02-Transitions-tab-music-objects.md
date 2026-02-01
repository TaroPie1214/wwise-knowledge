# Transitions tab: music objects

[Wwise 帮助文档](../../../../../00-Wwise-帮助文档.md) > [参考主题](../../../../00-参考主题.md) > [Project Explorer](../../../00-Project-Explorer.md) > [Audio tab](../../00-Audio-tab.md) > [Containers hierarchy: music objects](../00-Containers-hierarchy-music-objects.md) > [Common tabs and categories: music objects](00-Common-tabs-and-categories-music-objects.md) > Transitions tab: music objects

##### Transitions tab: music objects

在 Transition 选项卡中可以定义音乐播放列表或 Music Switch Container 内的音乐对象之间的过渡。过渡指在当前播放的音乐对象切换到另一个音乐对象时用户指定使用的音乐行为。各个过渡都有一个源（Source）和一个目标（Destination）。源与目标之间可以使用额外的段落（被称为过渡段落）作为音乐连接。

The Transitions tab contains the transition matrix, which allows you to create a set of rules that define how each object transitions to every other object within the container. 用户可以为各个对象创建明确的规则，也可以创建作用于多个对象的一般规则。默认的“Any to Any”过渡规则作用于其它所有未被定义的过渡。

过渡列表将按降序显示在 Transitions 选项卡中。当需要一个过渡时，Wwise 将从列表底部开始搜索，直到发现一个适用于当前情形的过渡为止。如果未找到匹配的过渡，则 Wwise 则将使用默认的“Any to Any”过渡。

为了便于定义过渡，音乐开关容器的子级音乐对象可以用虚拟文件夹进行组织。然后即可选择虚拟文件夹作为过渡规则的源或目标。在过渡系统搜索要应用的规则时，如果文件夹内的任何音乐对象与源或目标匹配上了，则该源文件夹或目标文件夹将匹配。

| General | |
| --- | --- |
| 界面元素 | 描述 |
| [name] | 对象的名称。 |
| (Object Color) | 显示对象的颜色。单击图标可打开颜色选择器。    选择一种颜色并将其应用于对象。在为对象选择某种颜色时，会在选定方块上显示调色板图标，并在右下角标注黄色三角（如图所示）。  若要沿用父对象的颜色，请选中颜色选择器最左侧的方块。 |
| (Mute and Solo) | 控制对象的 Mute（静音）和 Solo（单独播放）状态，也会显示该对象是否处于被动静音和 Solo 状态。  将对象静音会使其在当前监听中无法听到。让对象 Solo 会使工程中的所有其它对象无声。  粗体的 **M** 或 **S** 表明已为对象主动设置了 Mute 或 Solo 状态。褪色的非粗体 **M** 或 **S** 表明对象的 Mute 或 Solo 状态是由于其它对象状态而被动设置的。  将对象静音会让其子对象被动静音。  让对象 Solo 会使同级对象被动静音，并让子对象和父对象被动 Solo。  |  |  | | --- | --- | | [技巧] | 技巧 | | 在点击 Solo 按钮的同时按住 Ctrl 键，可以强制仅 Solo 该 Solo 按钮所在的对象。 |  |  |  | | --- | --- | | [备注] | 备注 | | Mute 和 Solo 仅用于监视目的，而不会保存在工程中或存储在 SoundBank（声音包）中。 | |
| (Show references) | 指示工程中有多少元素包含对对象的直接引用。若存在对对象的引用，则图标显示为橙色；若不存在此类引用，则图标显示为灰色。  通过单击该按钮，可打开 [“Reference View 视图”一节](../../../12-搜索和工程全局编辑/05-Reference-View-视图.md "Reference View 视图")，并在 **References to:**（引用:）字段中查看对象的名称。 |

| Transitions（过渡） | |
| --- | --- |
| 界面元素 | 描述 |
| No. | 指定给过渡规则的编号。  当性能分析期间发生过渡时，Capture Log 中会显示过渡监视消息。过渡使用此编号进行标识。 |
| Source | 源。参与过渡的源音乐对象。  点击选择器按钮可访问以下选项：  - **Any**任意源。为任何未指定的源音乐对象创建过渡。 - **Nothing**无源。创建一个没有源的过渡，即不播放任何音乐对象。 - **Browse** 浏览。选择特定的音乐对象或包含音乐对象的虚拟文件夹作为源来创建过渡。  如果 Source 列中未指定音乐对象或文件夹，则 Wwise 将应用第一个具有源“Any”的过渡。 |
| Destination | 目标。参与过渡的目标音乐对象。  点击选择器按钮可访问以下选项：  - **Any**，为任何未指定的目标音乐对象创建一个过渡。 - **Nothing**，创建一个没有目标的过渡，即不播放任何音乐对象。 - **Browse**，选择特定的音乐对象或包含音乐对象的虚拟文件夹作为目标来创建过渡。  如果 Destination 列中未指定音乐对象或文件夹，Wwise 则将应用第一个具有目标"Any"的过渡。 |
|  | Adds a transition to the transition matrix. |
|  | Removes a selected transition from the transition matrix. |
| **Source** | |
| Exit source at | 退出源的时机。指示启动退出时源中所处的时刻。您可从以下选项中选择：  - **Immediate（立刻）：** 立即停止播放 Source。 - **Next Grid（下一网格线）：** 在下一个网格线停止播放 Source。网格是可对音乐对象进行虚拟分割的任意方法。 - **Next Bar（下一小节）：** 在下一小节停止播放 Source。 - **Next Beat：** 在下一拍停止源的播放。 - **Next Cue（下一提示点）：** 在下一个提示点停止播放 Source，可以是 Custom Cue，也可以是 Exit Cue（出口提示点）。 - **Next Custom Cue（下一自定义提示点）：** 在下一个 Custom Cue 停止播放 Source。如果当前段落不包含自定义提示点，则 Wwise 将继续播放下一个段落，直到发现一个自定义提示点为止。 - **Exit Cue（出口提示点）：** 在出口提示点处停止播放 Source。  |  |  | | --- | --- | | [备注] | 备注 | | 当选择“Next Cue”或“Next Custom Cue”时，您可以定义要匹配的自定义提示点名称。该名称必须完全匹配。如果未指定任何名称，则任何自定义提示点都将匹配。 |  此选项仅适用于 Music Switch Container。  Default value: Exit Cue |
| Match (exit source at) | 如果“Exit source at”选项设置为“Next Cue”或“Next Custom Cue”，则指定要匹配的自定义提示点的名称。如果未指定任何名称，则任何自定义提示点都将匹配。  该名称必须与源上的自定义提示点名称完全匹配。名称匹配是区分大小写的。 |
| Play post-exit | 播放后尾段。如果选择此选项，则源段落的后尾段将会播放。后尾段是指出口提示点右侧的区域。  仅当源在出口提示点处退出，或在出口提示点处或之后淡出时，才播放源的后尾段。否则，过渡期间绝不会播放后尾段。  Default value: true |
| Fade-out | 淡出。决定当源段落到达结尾时是否应用淡出。  Default value: false |
|  | 显示 [“Music Fade Editor”一节](../08-Music-Editor-视图/04-Music-Fade-Editor.md "Music Fade Editor")，您可以在其中编辑源的淡出。 |
| **Destination** | |
| Jump To | 同步到。确定音乐对象中目标开始播放的时刻。您可从以下选项中选择：  - **Start of Playlist**:播放列表的开头。跳到第一个播放列表项。 - **Specific Playlist Item**:特定播放列表项。跳到指定的播放列表项。若要指定所要跳到的播放列表项，请单击“浏览”按钮。此项仅在目标对象为 Music Playlist Container 时可用。 - **Last Played Segment**:上次播放的段落。跳到上次播放的段落。 - **Next Segment**:下一段落。跳到上次播放的段落之后的下一播放列表项。  Default value: Start of Playlist |
|  | 此时将会显示 Project Explorer —— Browser，您可以在此选择目标播放列表项。 |
| Sync to | 同步到。确定音乐对象中目标开始播放的时刻。您可从以下选项中选择：  - **Entry cue**:目标将在其入口提示点处开始播放。 - **Same time as playing segment**:目标将在与源段落相同的时间标记处开始播放。例如，如果源段落从头开始已经播放了 15 秒，则目标将从 15 秒处开始播放。 - **Random Cue**:在随机选择的提示点处开始播放目标。勾选了此选项，则可选择任何提示点，包括入口提示点或匹配筛选条件的任何自定义提示点。请参见 Match source cue name 和 Match (jump to destination)。 - **Random Custom Cue**:目标将在与筛选条件匹配的随机选择自定义提示点处开始播放。请参见Match source cue name 和 Match (specify cue name)。如果段落中没有自定义提示点，则使用入口提示点。 - **Last Exit Position**:根据上次 Destination 的段落播了多久施加相应的时间偏置，然后再开始播放 Destination。例如，若上次 Destination 的第三个段落播了 15 秒，则将从 15 秒处开始播放 Destination。  |  |  | | --- | --- | | [备注] | 备注 | | **Last Exit Position** 选项仅适用于同一播放实例期间父级 Music Container 的过渡。 |  Default value: Entry Cue |
| Match source cue name | 匹配源提示点名。确定哪些自定义提示点适合作为目标段落中的起始位置。只有名称与过渡源中使用的提示点名称匹配的自定义提示点才可能作为起始位置。例如，如果源在名为“A”的自定义提示点处退出，则目标将在名为“A”的自定义提示点处开始。  字符串比较不区分大小写，但它必须完全匹配（没有通配符）。  此选项仅在“Sync to”设置为“Random Cue”或“Random Custom Cue”时才能使用。  如果未找到任何匹配项，则将使用入口提示点。  此选项仅在以下情况时才能正常工作：  - “Exit Source At”设置被设为“Next Cue”或“Next Custom Cue”。 - “Source”对象不是“nothing”。  名称匹配仅会影响自定义提示点的选择；它不会影响入口提示点的适用性。如果使用“Random Cue”作为“Sync to”属性，则所选目标提示点要么会是名称与源退出时的提示点名称相匹配的自定义提示点，或者入口提示点。使用“Random Custom Cue”作为“Sync to”属性以从可能的目标中移除入口提示点。  **Match（指定提示点名称）** 决定哪些自定义提示点可以用作目标段落的起点位置。在自定义提示点中，只有名称与编辑框中的字符串相匹配的提示点才可能作为起始位置。如果未指定任何名称，则任何自定义提示点都将匹配。  字符串比较不区分大小写，但它必须完全匹配（没有通配符）。  此选项仅在“Sync to”设置为“Random Cue”或“Random Custom Cue”时才能使用。  如果未找到任何匹配项，则将使用入口提示点。  名称匹配仅会影响自定义提示点的选择；它不会影响入口提示点的适用性。如果使用“Random Cue”作为“Sync to”属性，所选目标提示点则将是名称与“Match”文本字段中输入的字符串相对应的自定义提示点，或者入口提示点。使用“Random Custom Cue”作为“Sync to”属性以从可能的目标中移除入口提示点。  Default value: Match specific name |
| Match (specify cue name) | 匹配源提示点名。确定哪些自定义提示点适合作为目标段落中的起始位置。在自定义提示点中，只有名称与编辑框中的字符串相匹配的提示点才可能作为起始位置。如果未指定任何名称，则任何自定义提示点都将匹配。  字符串比较不区分大小写，但它必须完全匹配（没有通配符）。  此选项仅在“Sync to”设置为“Random Cue”或“Random Custom Cue”时才能使用。  如果未找到任何匹配项，则将使用入口提示点。  名称匹配仅会影响自定义提示点的选择；它不会影响入口提示点的适用性。如果使用“Random Cue”作为“Sync to”属性，所选目标提示点则将是名称与“Match”文本字段中输入的字符串相对应的自定义提示点，或者入口提示点。使用“Random Custom Cue”作为“Sync to”属性以从可能的目标中移除入口提示点。 |
| Play pre-entry | 播放前导段。如果选择此选项，则将播放目标段落的前导段。前导段是指入口提示点左侧的区域。  只有在目标在其入口提示点处开始时，目标的前导段才会播放。在其他情况下，前导段将不会在过渡期间播放。  Default value: true |
| Fade-in | 淡入。决定当目标段落开始播放时是否应用淡入效果。  Default value: false |
|  | 显示 [“Music Fade Editor”一节](../08-Music-Editor-视图/04-Music-Fade-Editor.md "Music Fade Editor")，您可以在其中编辑过渡目标的淡入。 |
| **Transition Segment（过渡段落）** | |
| Use transition segment | 使用过渡段落。如果选择此选项，则在过渡期间会播放过渡段落。过渡段落是以音乐方式连接源对象和目标对象的一段短音乐。  Default value: false |
|  | 此时将会显示 Project Explorer Browser，您可以在此选择过渡段落。 |
| Play transition pre-entry | 播放过渡前导段。如果选择此选项，则将播放过渡段落的前导段。前导段是指入口提示点左侧的区域。  Default value: true |
| Fade-In | 淡入。如果选择此选项， 则在过渡段落开始播放时将应用淡入效果。  Default value: false |
|  | 此时将显示 Music Fade Editor，您可在此编辑过渡段落的淡入效果。 |
| Play transition post-exit | 播放过渡后尾段。如果选择此选项，则将播放过渡段落的后尾段。后尾段是指出口提示点右侧的区域。  Default value: true |
| Fade-out | 淡出。如果选择此选项，当过渡段落达到尾段时则将对过渡段落应用淡出效果。  Default value: false |
|  | 此时将显示 Music Fade Editor，您可在此编辑过渡段落的淡出效果。 |

**相关主题**

- [“添加过渡规则”一节](../../../../../06-创建互动音乐/07-使用-Transition/01-理解-Transition-规则矩阵.md#adding_transitions "添加过渡规则")
- [“移除过渡规则”一节](../../../../../06-创建互动音乐/07-使用-Transition/01-理解-Transition-规则矩阵.md#removing_transitions "移除过渡规则")
- [“设置 Source 和 Destination 属性”一节](../../../../../06-创建互动音乐/07-使用-Transition/02-设置-Source-和-Destination-属性.md "设置 Source 和 Destination 属性")
- [“使用 Transition Segment”一节](../../../../../06-创建互动音乐/07-使用-Transition/03-使用-Transition-Segment.md "使用 Transition Segment")

---