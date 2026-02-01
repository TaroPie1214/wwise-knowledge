# Working with music objects

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [创建互动音乐](../00-创建互动音乐.md) > [Building your interactive music hierarchies](00-Building-your-interactive-music-hierarchies.md) > Working with music objects

## Working with music objects

The Containers hierarchy gives you the flexibility to organize the music objects in your project as you see fit to produce a full musical score. 在此，可使用快捷菜单和标准 Windows 快捷方式来重命名、剪切、复制和粘贴对象。

### 添加音乐对象

创建层级结构要从 Work Unit 开始。若单独操作（非多人协作），则可直接从 Default Work Unit（默认工作单元）开始创建层级结构；否则，需要先创建 Work Unit，然后再将音乐对象添加到 Work Unit 中。有关 Work Unit 和版本控制的详细信息，请参阅[*Working with a team*](../../03-设置工程/04-Working-with-a-team/00-Working-with-a-team.md "Working with a team")。

要实际构建音乐结构，可执行以下任一操作：

- 设置好您的工程结构，然后将音频文件导入该结构。
- 先导入音频文件，再将其组织到工程结构中。

  For more information on importing audio files and how they create new objects in the Containers hierarchy, see [*管理工程中的媒体文件*](../../03-设置工程/05-管理工程中的媒体文件/00-管理工程中的媒体文件.md "管理工程中的媒体文件").

**使用 Project Explorer 工具栏，创建子对象的方法是：**

1. 在 Project Explorer 的 Audio（音频）选项卡中，选择新音乐对象所在的工作单元。

   Project Explorer 工具栏中的一系列图标将被激活。
2. 从图标列表中，点击要添加的对象的图标。

   The object is added to the Containers hierarchy under the selected Work Unit.
3. 将默认名称替换为最适合该对象的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在 Wwise 中命名音乐对象时，不得使用以下字符：‘:<>%\*?”/\|.’ |

   然后可以将其它音乐对象添加到层级结构中。请提前花些时间理解一下对象之间的关系，以便根据关系相应地组织这些对象。在工程后续进程中，这样会帮您节省大量的时间。

**To create a child object in the Containers hierarchy:**

1. In the Containers hierarchy of the Audio tab of the Project Explorer, right-click the Work Unit in which you want to create your music object.
2. 从快捷菜单中，选择 **New Child**（新建子项）。

   子菜单中会显示您可以添加的对象列表。

   At this level of the hierarchy, you can add any one of the following objects that support interactive music:

   - Work Unit（工作单元）
   - Virtual Folder（虚拟文件夹）
   - Music Switch Container（音乐切换容器）
   - Music Playlist Container （音乐播放列表容器）
   - Music Segment （音乐段落）
3. From the list, select the object that you want to add.

   The object is added to the hierarchy.
4. 将默认名称替换为最适合该音乐对象的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在 Wwise 中命名对象时，不得使用以下字符：‘:<>\*?”%/\|.’ |

   接下来可以继续添加其它对象。请提前花些时间熟悉理解对象之间的关系，以便有依据地组织它们，在工程后续进程中，这样会帮您节省大量的时间。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在 Project Explorer 内，可使用预定义的键盘快捷方式快速创建父对象或子对象。比如，在默认情况下，按下 Shift+Alt+F 即可创建父文件夹。若要打开 Keyboard Shortcuts 视图并查找工程所用快捷方式，请在 Project 菜单中单击 **Keyboard Shortcuts...**。 |

### 添加父级音乐对象

After you have added the first object to your Work Unit, you can begin adding more objects and create parent-child relationships between them. 父对象包含其它对象，在创建一个父对象后，您可以将现有对象移到此新父对象之下。The benefit of creating parent-child relationships is that you can change properties and define behaviors for the parent that will affect the child objects below it. For more information about the properties of interactive music objects, refer to [“About the properties of music objects”一节](03-About-the-properties-of-music-objects.md "About the properties of music objects").

**使用 Project Explorer 工具栏创建父对象：**

1. In the Containers hierarchy in the Audio tab of the Project Explorer, select the music object to which you want to add a parent.
2. Press the **Shift** key to display the icons for the music objects that can be added as a parent of the selected object.
3. From the list, click the icon that represents the music object that you want to add.

   The object is added to the Containers hierarchy as the parent of the selected object.
4. 将默认名称替换为最适合该音乐对象的名称。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 在 Wwise 中命名对象时，不得使用以下字符：‘:<>\*?”%/\|.’ |

**创建父对象的方法是：**

1. In the Containers hierarchy in the Audio tab of the Project Explorer, right-click the object with which you want to create a parent relationship.
2. 从快捷菜单中，选择 **New Parent**（新建父项）。

   子菜单将会打开并显示您可添加的对象列表。

   Depending on the selected object's level in the hierarchy, you have the option of adding any of the following in relation to interactive music as new parent objects:

   - Work Unit（工作单元）
   - Virtual Folder（虚拟文件夹）
   - Music Switch Container（音乐切换容器）
   - Music Playlist Container （音乐播放列表容器）
   - Music Segment （音乐段落）
3. 从对象列表中，点击要添加的对象。

   The new parent object is added to the Containers hierarchy with a default name, based on its object type.
4. Type the name that best represents the music object.

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在 Wwise 中命名对象时，不得使用以下字符：‘:<>\*?”%/\|.’ |

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 在 Project Explorer 内，可使用预定义的键盘快捷方式快速创建父对象或子对象。比如，在默认情况下，按下 Shift+Alt+F 即可创建父文件夹。若要打开 Keyboard Shortcuts 视图并查找工程所用快捷方式，请在 Project 菜单中单击 **Keyboard Shortcuts...**。 |

### 移动音乐对象

| 操作 | Results |
| --- | --- |
| 移动音乐对象 | 如果将对象移动到层级结构中的新位置，该对象的属性和行为将受其新父对象影响。 |
| 如果您移动一个与某事件相关联的对象，则该对象仍与该事件有关联。 |

### 复制和粘贴音乐对象

| 操作 | Results |
| --- | --- |
| 复制音乐对象 | 如果将音乐对象复制并粘贴到新位置，该音乐对象的属性和行为将受其新父对象影响，其子对象也会被复制到新位置。 |
| 如果被复制的音乐对象与某事件相关联，复制后，新对象将与该事件无关。 |

### 剪切或删除音乐对象

| 操作 | 结果 |
| --- | --- |
| 剪切或删除音乐对象 | 如果剪切或删除某音乐对象，则其子对象也将被删除。 |
| 但是，与其关联的已转码音频文件不会被删除，不再与对象关联的已转码音频文件称为 Orphan File（落单文件）。要删除 Orphan File，您需要清除音频缓存。关于如何删除落单音频文件的详细信息，请参阅[“清除缓存”一节](../../03-设置工程/05-管理工程中的媒体文件/06-清除缓存.md "清除缓存")。 |
| 如果您删除或剪切一个与某事件相关联的对象，则将会导致事件中缺失对象。 |

---