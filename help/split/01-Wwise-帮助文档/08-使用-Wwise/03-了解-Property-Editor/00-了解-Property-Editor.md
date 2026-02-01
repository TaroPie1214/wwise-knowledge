# 了解 Property Editor

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用 Wwise](../00-使用-Wwise.md) > 了解 Property Editor

## 了解 Property Editor

You can use the Property Editor to view and change the properties of objects in the Wwise
Hierarchy. The Property Editor is visible:

- In its own window. From the menu bar, click **Views > Editors >
  Property Editor** (Ctrl+K).
- In the Object Tab Group of the Designer layout. See [*使用 Object Tab 和 Object Tab Group*](../09-使用-Object-Tab-和-Object-Tab-Group/00-使用-Object-Tab-和-Object-Tab-Group.md "使用 Object Tab 和 Object Tab Group") and [“处理布局”一节](../../02-入门/04-个性化您的工作空间/02-处理布局/00-处理布局.md "处理布局").

Select an object in the Project Explorer to view its properties in the Property Editor.
Properties are displayed according to the object's type.

You can filter properties as follows:

- **Predefined categories:** Each object's properties have an
  [“Object specific category”一节](01-Object-specific-category.md "Object specific category"). Choose which other categories are
  shown by clicking **Show/Hide Category Filters**
  ![](../../../images/btn_display_options_dots.png) and selecting or deselecting them. Then select a shown category
  to see the properties in it. You can multi-select categories from among those
  shown.

  Depending on the object type, the following categories might be also
  available:

  - [“General category”一节](02-General-category.md "General category")
  - [“Routing category”一节](03-Routing-category.md "Routing category")
  - [“Conversion category”一节](04-Conversion-category.md "Conversion category")
  - [“Positioning category”一节](05-Positioning-category.md "Positioning category") (for Containers hierarchy and most Busses hierarchy objects)
  - [“HDR category”一节](06-HDR-category.md "HDR category") (for Containers hierarchy objects and Audio Busses)
  - [“MIDI category”一节](07-MIDI-category.md "MIDI category") (for Containers hierarchy objects)
  - [“Advanced category”一节](08-Advanced-category.md "Advanced category")（仅适用于除 Auxiliary Bus 外的所有对象）
  - [“Sources category”一节](09-Sources-category.md "Sources category")
  - [“All category”一节](10-All-category.md "All category")
- **Favorites**: You can configure a custom category
  called Favorites. To populate it:

  - Click **Show/Hide Category Filters** and
    then click **Configure Favorites**.
  - Right-click a property, then select **Add to
    Favorites** or **Configure
    Favorites**.

  If you have configured a least one favorite, filter on favorites by clicking **Show/Hide Category Filters** and selecting **Favorites**. Properties in Favorites are grouped by
  category. You can change the display order of the groups by clicking and dragging
  the ![](../../../images/btn_drag_up_or_down_categories.png) title bar icon. To restore the default order, click **Show/Hide Category Filters** then click **Reset Favorites Order to Default**.
- **Search field**: You can filter on property titles
  by entering text in the search field.
- **Only Show Modified**: This is enabled by clicking ![](../../../images/btn_modified.png). Modified properties are marked with an orange band: ![](../../../images/btn_modified_property.png), as are groups and categories containing modified
  properties.

Properties are displayed in collapsible groups. Groups can be expanded or collapsed by
clicking on them or by clicking **More Options**
![](../../../images/btn_more_options_off.png) and then **Expand All** or **Collapse All**. Some groups contain additional properties you can
display by clicking ![](../../../images/icn_expand.png). To have them shown always, click **Show/Hide
Category Filters** and enable **Always Show Additional
Properties**.

Properties are also displayed in the Primary Editor. 请参阅 [“Primary Editor 和 Secondary Editor”一节](../09-使用-Object-Tab-和-Object-Tab-Group/03-Primary-Editor-和-Secondary-Editor/00-Primary-Editor-和-Secondary-Editor.md "Primary Editor 和 Secondary Editor")。

When a Game Sync is loaded into the Property Editor, various properties are displayed depending on the game sync type. 下表描述为各个 Game Sync 所显示的属性：

| Game Sync | Property Editor 内容 |
| --- | --- |
| Switch Group | Game Parameter 值映射的名称（Name）、备注（Notes）和 Switch。 |
| Switch | 名称和备注。 |
| State Group | Name, notes, and transition properties between States. |
| State（状态） | 名称、备注和 State 值副本。 |
| Game Parameter（游戏参数） | 名称；备注；要绑定的内置参数；游戏参数的最小值、最大值和默认值；以及插值模式值。 |
| Trigger （触发器） | 名称和备注。 |

---