# Primary Editor 和 Secondary Editor

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [使用 Wwise](../../00-使用-Wwise.md) > [使用 Object Tab 和 Object Tab Group](../00-使用-Object-Tab-和-Object-Tab-Group.md) > Primary Editor 和 Secondary Editor

## Primary Editor 和 Secondary Editor

每个 Object Tab 由上部窗格中的 Primary Editor（适用于大部分对象类型）和下部窗格中的 Secondary Editor 组成。

![](../../../../images/otg_editors.png)

The Primary Editor typically presents the Event Editor or the Audio Device Editor depending on the type of object selected. Secondary Editor 会为每个与当前选定对象密切相关的其他编辑器留出一个选项卡。单击窗格底部的选项卡名称可在这些编辑器之间切换。

![](../../../../images/otg_secondary_tabs.png)

下表列举了一些可包含在 Secondary Editor 中的选项卡以及可能导致其包含其内的条件。

| 选项卡名称 | 包含条件 |
| --- | --- |
| <Effect Name> | <效果器名称>。在对象上插入了效果器。A tab appears for each Effect inserted on the object, displayed from left to right. |
| Attenuation（衰减） | An attenuation instance (ShareSet or custom) has been defined in the Positioning Category of the Property Editor. |
| 内容 | 内容。大多数对象均默认包含该选项卡。 |
| Music | Included for music objects. |
| Source | 源。对象为声音对象且关联有源文件或带有源插件。 |

Buttons in the Property, Primary, and Secondary Editors provide the following
functionality:

|  |  |
| --- | --- |
|  | Minimizes the Property Editor (Ctrl+`). |
|  | Maximizes the Primary Editor (`) or the Secondary Editor (Shift+`) within the Object Tab. You can also maximize those editors by double clicking on one of their tabs. |
|  | For the Primary and Secondary Editors, duplicates the currently selected tab in a floating window. For the Property Editor, duplicates the editor in a floating window. |

**在所述编辑器中使用键盘快捷方式：**

- 在窗格上部或下部任意位置单击来将编辑器指定为活跃编辑器。活跃编辑器会显示较为突出的矩形框线。在 Secondary Editor 中有多个选项卡时，单击与要使用键盘快捷方式的编辑器对应的选项卡。

Any keyboard shortcuts that apply to the editor can be used, including the F1 key (or
Help button), which opens the reference topic pertaining to the active editor.

---