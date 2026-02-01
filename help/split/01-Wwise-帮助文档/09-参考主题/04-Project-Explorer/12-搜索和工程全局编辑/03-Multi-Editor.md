# Multi Editor

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [搜索和工程全局编辑](00-搜索和工程全局编辑.md) > Multi Editor

### Multi Editor

通过 Multi Editor（多项编辑器），用户可以一次定义和修改多个对象的属性。在以下情况下这可能非常有用，例如，您希望通过一条特定总线为多个容器指定通路，或您希望修改一系列对象和总线的音量。您可以在 Multi Editor 中快速轻松完成此任务。

您可以在 View 菜单中直接打开 Multi Editor（多项编辑器），然后再选择对象进行编辑。或者也可以先选择要编辑的对象，然后点击右键并从弹出的菜单中选择 **Show in Multi Editor**（在多项编辑器中显示）打开多项编辑器。

所选对象将会被加载至 Multi Editor 视图中。如果只有一个对象，其名称将显示在左上选项卡中。否则，该选项卡将显示所选对象的计数。虽然可以在不关闭视图的情况下对工程进行任意操作，但要注意 Multi Editor 会重新加载其他视图中选择的对象。

使用 Multi Editor 几乎可以修改所有 Wwise 对象的任何属性。基本上只有对象的 **Mute**、**Solo**、**Name** 和 **Notes** 属性不支持在 Multi Editor 中进行编辑。

Multi Editor 显示所选对象的相关属性。也就是说，显示的属性和行为取决于您选择的对象类型。举例来说，如果为 Switch Container 打开 Multi Editor，您将会在 Property Editor 中看到该 Switch Container 的属性；如果选择的是声音文件，Property Editor 则会显示该声音文件的属性；以此类推。

如果您为包含多种对象的选定项打开 Multi Editor，则某些显示的属性可能仅适用于一部分选定项。另外对于特定属性，只有所选对象均具有相同值，才会显示其值。通常会具有多个不同值，所以会显示一个小破折号“ - ”，表示无法显示单一值。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 要查看所选对象各个属性的描述，请参考相应 Property Editor 中的帮助。 |

除指定属性值并定义行为外，您还可以执行以下操作：

- **指定输入绝对值还是相对值**：在输入的值后面添加 + 或 -，即可指定应用到所选对象的属性值是相对的还是绝对的。您放置 + 或 - 符号的位置决定了您添加的是绝对值还是相对值 —— 符号放置在值之前表明指定的是绝对值；符号放置在值之后表明指定的是相对值。例如，为之前音量为 -17 dB 的对象输入绝对值 -23，会将所有对象的音量改为 -23 dB。而为音量设置为 -15 dB、-20 dB 和 -10 dB 的对象输入 6+ 这样的相对值，意味着将进行偏置，所有对象的音量将增加 6 dB。
- **关联/取消关联属性值**：您可以通过 Link 为所有平台使用同样的属性值，或是 Unlink 来为当前平台创建自定义属性值。
- **启用随机化器**：您可以启用 Randomizer 来为一个值设置其随机范围。Randomizer 在每次播放对象时修改对象的属性值，方法是从您指定的值范围中选择一个值。
- **添加 RTPC**：在 Multi Editor 中加载单个对象时，可通过 Game Parameter、MIDI 或 Modulator 对象添加新的 RTPC。在加载多个对象时，此选项不可用；不过，可使用 [“Paste Properties”一节](../../02-视图/11-Paste-Properties.md "Paste Properties") 视图将 RTPC 从一个对象复制到一个或多个其他对象。
- **Vew and edit effects:**

  1. Click  **View Settings** (Ctrl+Alt+H) in
     the title bar.
  2. In the [“Object Property Settings”一节](06-Object-Property-Settings.md "Object Property Settings") list, navigate to
     Audio > Effects, and choose the effect properties to view and click
     OK.
  3. An Effects folder appears under any appropriate object. Expand it to
     view the effects in rows and their properties in columns. This displays
     the same properties as the [“Effects tab: Containers hierarchy objects”一节](../01-Audio-tab/05-Common-tabs-and-categories-audio-structures/08-Effects-tab-Containers-hierarchy-objects.md "Effects tab: Containers hierarchy objects").
  4. To delete an effect, right-click it and select **Delete**.
  5. To move an effect, right-click it and select **Move Up** or **Move Down**,
     depending on its position.
- View object counts. For Effects and RTPC faders, a count is given in the Value
  column:

  - **count: n**: where *n* is a numeric
    value, indicates the quantity.
  - **mixed count: n-n**: where *n* is a
    numeric value, indicates the high and low quantities for more than one
    object.

| 界面元素 | 描述 |
| --- | --- |
|  | 点击视图右上角中的 View Settings 图标。  这时会打开 [“Object Property Settings”一节](06-Object-Property-Settings.md "Object Property Settings") 对话框。选择要为适用 Wwise 对象类型显示的各项属性。 |
|  | 有三个选项用来选择面板中属性的显示方式。  - **Tree view**：树形视图。在对象层级结构中显示相应对象属性。像其他层级结构视图一样，允许扩展和折叠父项来显示或隐藏子元素。 - **Flat view**： 扁平视图。在一个平铺列表中显示所有对象的属性，对象在层级结构中的位置完全由其路径名表示。在此视图中，只列出了可编辑的属性。其不可编辑的结构和层级元素只在路径名中可见。 - **Flat view (name only)**：扁平视图（仅显示名称）。在平铺列表中列出所有对象的属性，不指示其在层级中的位置。 |
|  | 根据当前选定对象的相对层级位置，打开一个三选项列表，用于更改选中对象，并在面板中编辑。每个选项都会显示相应的对象数量，以及对象类型（如果统一的话）。  - **All children - "#" objects**：所有子对象 - 对象个数。为所选对象的所有直接下级对象显示属性。 - **All descendants - "#" objects**：所有下属对象 - 对象个数。为所选对象的所有下级对象显示属性。 - **All parents - "#" objects**：所有父对象 -对象个数。为所选对象的所有直接上级对象显示属性。    |  |  | | --- | --- | | [备注] | 备注 | | 对于 Event，没有直接关联的属性。属性适用于 Event 的子项：Action。因此，批量编辑 Event 时，请务必选择 **All descendant** 或 **All children**。 | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
| Name | 名称。属性或行为的名称。此处列出的属性或行为将基于所选的对象。  |  |  | | --- | --- | | [备注] | 备注 | | Color 属性总是首先列出。该属性值显示与所选对象关联的颜色，通过单击可打开颜色选择器并[设置色块](../../../02-入门/04-个性化您的工作空间/03-设置颜色.md "设置颜色")。 | |
| Value | 值。您希望分配给所有所选对象的属性值。这可以包括数值，但也可以是用于启用或禁用某些行为或属性的复选框。  对于数值，您可以指定更改相对属性还是绝对属性。在值之后添加 + 或 - 符号，可为所选对象的属性创建偏置。在数值前添加符号，对象的属性将会改为绝对值。  对于 **Use Game-Defined Auxiliary Sends**（使用游戏定义辅助发送）这样的复选框，显示实心框（）则说明其适用于若干选定对象，但非全部。  |  |  | | --- | --- | | [备注] | 备注 | | 除非对象位于顶层或不沿用父对象，否则从其父对象继承的属性将无法在 Property Editor 中启用，如 **Use Game-Defined Auxiliary Send**。在 Multi Editor 中，只要多个所选对象中有一个允许启用，更改仍将影响所有对象。但是，在启用 Override parent 选项前，设置将不会生效。 |    根据情况，Value 列可能显示 Link、RTPC 标志，或者在字段的左侧显示 Randomizer 标志。由于 Multi Editor 能够编辑多个对象，其中每个都可能有不同设置，因此为 [Link Mixed、RTPC Mixed 和 Randomizer Mixed](../../../02-入门/03-Wwise-界面基础知识/01-理解-Wwise-中的视觉元素.md#property_value_indicators) 情况提供了特殊标志。 |

---