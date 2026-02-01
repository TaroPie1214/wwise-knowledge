# Building sound and motion hierarchies

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [设置工程](../00-设置工程.md) > [Building your sound and motion hierarchies](00-Building-your-sound-and-motion-hierarchies.md) > Building sound and motion hierarchies

## Building sound and motion hierarchies

After you have created your project, you can start creating the structures for your assets in the Audio tab of the Project Explorer. You do this under the Containers hierarchy. You can add objects and create relationships by grouping them at different levels in the hierarchy. The following table lists the kinds of sound and motion objects you can add.

| Object（对象） | 图标 | 描述 |
| --- | --- | --- |
| Sound |  | 声音对象。该 Wwise 对象代表各音频素材，并链接到音频源。共有两种声音对象： |
| |  | | --- | |  | | **Sound SFX** —— 音效声。即音效对象。 |
| |  | | --- | |  | | **Sound Voice** —— 语音。即语音对象。 |
| 容器 |  | 容器。该对象可以包含 Sound 或其 Container，并且会根据特定行为播放整组对象。您可以设置 Container 属性，来影响其中的子对象。Container 分为四种： |
| |  | | --- | |  | | **Random Container** —— 随机容器。其中的对象/容器将随机播放。 |
| |  | | --- | |  | | **Sequence Container** —— 序列容器。其中的对象/容器将按照特定播放列表播放。 |
| |  | | --- | |  | | **Blend Container** —— 混合容器。其中的对象/容器将同时播放。此容器内的对象可以编入 Blend Track（混合轨），在其中，对象属性可以通过 RTPC（实时参数控制）映射到游戏参数，即由参数值来控制对象属性。Blend Track 内，两个对象间也可以基于游戏参数值来进行交叉淡变。 |
|  | |  | | --- | |  | | **Switch Containers** - A group of one or more objects and/or containers that are organized into a series of Switches or States that correspond to the different alternatives that exist for a particular element in the game. |
| Property Containers | |  | | --- | |  | | 角色混音器。一种高层对象，可以用来将其它对象编为一组。Properties that are applied to a Property Container affect the properties of the objects grouped under it.  You can also group objects within a Property Container using Virtual Folders. |
| 虚拟文件夹 | |  | | --- | |  | | 虚拟文件夹。一种高层元素，可以包含其它对象。Virtual Folder 不能作为Container 或 Sound 的子对象。 |
| Work Units | |  | | --- | |  | | 工作单元。一种高层元素，用来分割工程内容，以便多人同时处理同一工程。工程层级结构内的所有素材以及其它 Wwise 元素（例如状态、效果器和 SoundBanks）都位于 Work Unit 内。 |
| Physical Folders | |  | | --- | |  | | 实文件夹。一种高层元素，可以包含一组工程中其它的 Physical Folder 或 Work Unit。实文件夹不能作为容器或声音的子对象。 |

### Adding objects to the Containers hierarchy

创建层级结构要从 Work Unit 开始。您可以直接从 Default Work Unit（默认工作单元）开始创建层级结构,在团队中，更常见的方式是先新建 Work Unit，再添加对象至其中。有关 Work Unit 和版本控制的详细信息，请参阅[*Working with a team*](../04-Working-with-a-team/00-Working-with-a-team.md "Working with a team")。

构建对象结构时，可以采用以下方式之一：

- 先设置好工程结构，然后将音频文件导入其中。
- 先导入音频文件，之后再将导入的文件组织到工程结构中。

  For more information on importing audio files and how they create new objects in the Containers hierarchy, refer to [*管理工程中的媒体文件*](../05-管理工程中的媒体文件/00-管理工程中的媒体文件.md "管理工程中的媒体文件").

**使用 Project Explorer 工具栏，创建子对象的方法是：**

1. 在 Project Explorer（工程浏览器）的 Audio（音频）选项卡中，选择要新建对象的 Work Unit。

   Project Explorer 工具栏中的一系列图标将变为激活状态。
2. 从图标列表中，点击要添加的对象的图标。

   The object is added to the Containers hierarchy under the selected Work Unit.
3. 将默认名称替换为最适合该对象的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在 Wwise 中命名对象时，不得使用以下字符：‘:<>%\*?”/\|.’ |

   现在可以继续在层级结构中添加其它对象了。请提前花些时间熟悉理解对象之间的关系，以便有依据地组织它们，在工程后续进程中，这样会帮您节省大量的时间。

**To create a child object in the Containers hierarchy:**

1. 在 Project Explorer 的 Audio 选项卡中，右键点击要新建对象的 Work Unit。
2. 在快捷菜单中选择 **New Child**（新建子项）。

   子菜单将打开，并显示允许添加的对象列表。

   在此层级中，允许添加以下对象：

   - Virtual Folder（虚拟文件夹）
   - Property Container
   - Switch Container（切换容器）
   - Random Container（随机容器）
   - Sequence Container（序列容器）
   - Blend Container（混合容器）
   - Sound SFX（音效声）
   - Sound Voice（语音声）
3. 从对象列表中，点击要添加的对象。

   The object is added to the Containers hierarchy under the selected Work Unit.
4. 将默认名称替换为最适合该对象的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在 Wwise 中命名对象时，不得使用以下字符：‘:<>%\*?”/\|.’ |

   现在可以继续在层级结构中添加其它对象了。请提前花些时间熟悉理解对象之间的关系，以便有依据地组织它们，在工程后续进程中，这样会帮您节省大量的时间。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在 Project Explorer 内，可使用预定义的键盘快捷方式快速创建父对象或子对象。比如，在默认情况下，按下 Shift+Alt+F 即可创建父文件夹。若要打开 Keyboard Shortcuts 视图并查找工程所用快捷方式，请在 Project 菜单中单击 **Keyboard Shortcuts...**。 |

### 添加父对象

After you have added the first object to your Work Unit you can begin adding other objects to the Containers hierarchy and create parent-child relationships between them. 父对象包含其它对象，在创建一个父对象后，您可以将现有对象移到此新父对象之下。The benefit of creating parent-child relationships is that you can change properties and define behaviors for the parent that will affect the child objects placed below it. For more information about properties in the Containers hierarchy, refer to [“工程层级结构中的属性介绍”一节](04-工程层级结构中的属性介绍/00-工程层级结构中的属性介绍.md "工程层级结构中的属性介绍").

**使用 Project Explorer 工具栏创建父对象：**

1. 在 Project Explorer（工程浏览器）的 Audio（音频）选项卡中，选择要添加父级的对象。
2. 按住 **Shift** 键后，工具栏将显示所选对象允许添加的父级对象图标。
3. 从图标列表中，点击要添加的对象的图标。

   The object is added to the Containers hierarchy as the parent of the selected object.
4. 将默认名称替换为最适合该对象的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在 Wwise 中命名对象时，不得使用以下字符：‘:<>%\*?”/\|.’ |

**新建父对象的方法如下：**

1. 在 Project Explorer 的 Audio 选项卡中， 右键点击需要新建父级的对象。
2. 在快捷菜单中，选择 **New Parent**（新建父项）。

   子菜单将打开，并显示允许添加的对象列表。

   根据所选对象在层级结构中的层级，您可添加以下项作为新的父对象：

   - Switch Container（切换容器）
   - Random Container（随机容器）
   - Sequence Container（序列容器）
   - Blend Container（混合容器）
   - Virtual Folder（虚拟文件夹）
   - Property Container
3. 从对象列表中，点击要添加的对象。

   The new parent object is added to the Containers hierarchy with a default name, based on its object type.
4. 将默认名称替换为最适合该对象的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在 Wwise 中命名对象时，不得使用以下字符：‘:<>%\*?”/\|.’ |

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在 Project Explorer 内，可使用预定义的键盘快捷方式快速创建父对象或子对象。比如，在默认情况下，按下 Shift+Alt+F 即可创建父文件夹。若要打开 Keyboard Shortcuts 视图并查找工程所用快捷方式，请在 Project 菜单中单击 **Keyboard Shortcuts...**。 |

### Managing objects in the Containers hierarchy

In the Containers hierarchy you have access to shortcut menus and the standard Windows shortcuts for renaming, cutting, copying, and pasting objects. 在更改层级结构时，请牢记以下几点：

**移动对象**

- 如果更改某个对象在层级结构中的位置，则该对象将会受到其新父对象的属性和行为的影响。
- 如果您移动一个与某事件相关联的对象，则该对象仍与该事件有关联。

**复制和粘贴对象**

- 若将对象复制粘贴到新的位置，则其属性和行为将受新的父对象影响。其子对象也会受到影响。
- 如果复制的对象与某事件相关联，复制后，新对象将与该事件无关。

**剪切或删除对象**

- 若剪切或删除对象，则其子对象也将被删除。
- 但是，与其关联的已转码音频文件不会被删除，不再与对象关联的已转码音频文件称为 Orphan File（落单文件）。要删除这些落单文件，您需要清除音频缓存。关于删除落单音频文件的详细信息，请参阅[“清除缓存”一节](../05-管理工程中的媒体文件/06-清除缓存.md "清除缓存")。
- 如果您删除或剪切一个与某事件相关联的对象，则将会导致事件中缺失对象。

---