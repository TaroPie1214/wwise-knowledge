# 在导入时创建 Wwise 对象

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [设置工程](../../00-设置工程.md) > [管理工程中的媒体文件](../00-管理工程中的媒体文件.md) > [导入的过程](00-导入的过程.md) > 在导入时创建 Wwise 对象

### 在导入时创建 Wwise 对象

After you have verified that the files that you want to import are supported by Wwise, you can determine what kind of object you want to create with the files.

Wwise 会区别对待 Sound SFX、Sound Voice，和 Music Track 对象。这样的话就可在 Wwise 中以不同的方式处理可能翻译为不同语言的 Sound Voice 对象。此外，还存在其他对象结构，例如 Container 和 Music Segment，可以用来对基础对象进行分组和组织。为了帮助区分这些对象，Wwise 使用不同的图标来表示每个对象类型。

| 图标 | 代表 |
| --- | --- |
| |  | | --- | |  | | **SFX** - The default object type when you import media files into the Containers hierarchy. |
| |  | | --- | |  | | **Voice** —— 语音。为游戏中的对白而创建的对象，这些对白可能会翻译为多种语言的版本。  |  |  | | --- | --- | | [技巧] | 技巧 | | Hold Ctrl and Shift while dragging a WAV file to the Containers hierarchy to automatically set the **Import As:** list value to **Sound Voice**, as opposed to the default **Sound SFX**, for the Reference Language. | |
| |  | | --- | |  | | **Random Container** - Created, by default, when dragging a folder into the Containers hierarchy. 但是在弹出的 Audio File Importer 窗口中，可以在 **Object Type/Action**（对象类型/动作）下拉菜单中为文件选择其他选项：  - **Object（对象）** - **Virtual Folder（虚拟文件夹）** - **Property Container** - **Sequence Container （序列容器）** - **Switch Container（切换容器）** - **Blend Container（混合容器）** - **Sound SFX（音效声）**    |  |  | | --- | --- | | [技巧] | 技巧 | | Hold the Ctrl key while dragging a folder to the Project Explorer in the Containers hierarchy to automatically create a Random Container with Sound SFX objects for every WAV file found in the folder. | |
| |  | | --- | |  | | **Music Track** - Created when dragging a source file (WAV or AMB) onto the Containers hierarchy under a Music Segment.  |  |  | | --- | --- | | [技巧] | 技巧 | | Hold the Ctrl key while dragging a WAV file on top of Music Segment in the Containers hierarchy of the Project Explorer to automatically create a Music Track object. | |
| |  | | --- | |  | | **Music Segment** - Created, by default, when dragging a folder or a source file (WAV or AMB) onto the Containers hierarchy under a Music Switch Container or Music Playlist Container.  但在弹出的 Audio File Importer 窗口中，可以在 **Object Type/Action** 下拉菜单中为文件选择其他选项：  - **Object（对象）** - **Virtual Folder（虚拟文件夹）** - **Music Switch Container（音乐切换容器）** - **Music Playlist Container （音乐播放列表容器）**    |  |  | | --- | --- | | [备注] | 备注 | | When dragging WAV files onto an existing Music Segment, Music Tracks are created for every WAV file dragged. | |

---