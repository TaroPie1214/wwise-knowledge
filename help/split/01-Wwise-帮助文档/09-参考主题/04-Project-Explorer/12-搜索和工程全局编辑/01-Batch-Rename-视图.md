# Batch Rename 视图

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [参考主题](../../00-参考主题.md) > [Project Explorer](../00-Project-Explorer.md) > [搜索和工程全局编辑](00-搜索和工程全局编辑.md) > Batch Rename 视图

### Batch Rename 视图

要打开下图所示的 Batch Rename 视图，可以在 **View** 菜单中选择或使用其快捷键方式（默认情况下为 Ctrl + F2）选择。它由 **Settings**（左侧）和 **Preview**（右侧）面板组成。浏览器（如 List 视图或 Project Explorer）中的任何可编辑对象都可以拖动到 **Preview** 面板进行重命名。

|  |
| --- |
|  |

您可以在 **Settings** 面板中输入您的搜索项和替换模式。此面板包含两个主要列：

- 左侧是 **Name** 列，用于识别选项。
- 右侧是 **Value** 列，给出条目。

下表详细介绍了这些选项。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| **Apply To** | 作用于。通过两种列表选项指定搜索和潜在重命名的目标。  - Name —— 将批量重命名作用于所列对象的名称。 - Notes —— 将批量重命名作用于所列对象的备注。 |
| **Replace** | 替换。启用此选项可激活以下替换设置。 |
| Find what | 查找什么。在所选对象的名称或说明中指定要替换的文本或正则表达式模式。 |
| Replace with | 换成。指定替换文本或正则表达式替换物。 |
| Match case | 匹配大小写。在禁用 **Use Regular Expression** 的情况下，指定 **Find what** 文本的匹配项是否区分大小写。 |
| Use Regular Expression | 指定 **Find what** 和 **Replace with** 字段是否识别正则表达式语法。  |  |  | | --- | --- | | [备注] | 备注 | | Wwise 使用 ECMAScript 正则表达式样式，[“正则表达式参考”一节](../../../02-入门/05-提供工作效率/01-使用批量重命名/04-正则表达式参考.md "正则表达式参考")中将详细进行介绍。 | |
| Occurrence | 出现点。指定要替换的匹配项。  - First —— 匹配文本的第一个匹配项。 - Last —— 匹配文本的最后一个匹配项。 - All —— 匹配文本的各个匹配项。  |  |  | | --- | --- | | [备注] | 备注 | | 此列表不适用正则表达式。 | |
| **Remove** | 删除。启用此选项会激活以下删除设置。 |
| Count | 字符数。指定要删除的字符数。可以直接在字段中输入值或使用滑杆（0 至 100，除非在字段中输入更大值）。 |
| At position | 所在位置。指定在删除之前要忽略的字符数。可以直接在字段中输入值，也可以使用滑杆输入值。 |
| From | 从何处开始。指定从对象名称或备注的 **beginning** 或 **end** 进行删除。 |
| **Insert** | 插入。启用此选项以激活以下插入设置。 |
| Insert what | 插入什么。指定如何解释 **To insert** 字段条目。共有两个选项：  - **Text**，仅插入 **To insert** 字段中输入的文本；或 - **Text with numbers**，插入根据 C++ printf 格式化数字模式定义的数字，并且能够进行任何适用的文本调整。选择器列表列出了常用的数字模式。 |
| # start at | 指定起始数值。对于 Batch Rename 中列出的按照 **Before** 列的字母顺序排序的各个对象，它们的编号将从此值开始以 1 递增。 |
| To insert | 指定插入文本或包含 C++ printf 格式化数字模式的文本的输入字段。  选择器（仅在 **Insert what** 设置为 **Text with number** 时才处于活跃状态）提供以下数值型 C++ printf 格式预定义列表选项：  - **Decimal (d%)**  —— 十进制数，基数为 10，格式（0-9） - **Decimal with zero padding (%02d)** —— 十进制数，基数为 10，个位数补零格式（00-09） - **Hexadecimal lower case (%X)** —— 十六进制数，基数为 16，格式中使用小写字母（0-f）表示值 10 至 15 - **Hexadecimal upper case (%X)** —— 十六进制数，基数为 16，格式中使用大写字母（0-F）表示值 10 至 15 - **Hexadecimal upper case (%X)** —— 十六进制数，基数为 16，格式中使用大写字母表示值 10 至 15，并且最多为四个字符进行补零至四位 (0x0000-0x000F)。 |
| At position | 插入位置。指定在插入之前要跳过的字符数。 |
| From | 指定 **At position** 开始计数的字符位置：  - **Beginning** —— 在名称或备注的第一个字符之前开始计数。例如，在对象“car engine”中将 **At position** 设为 3，则将在“r”之后插入数字，得到“car1 engine”。 - **End** —— 在名称或备注的最后一个字符之后开始计数。例如，在对象“car engine”中将 **At position** 设为 3，则将在“i”之前插入数字，得到“car eng1ine”。 |
|  | 将以上选项重置为默认的空状态。使用 Ctrl+Z 撤消重置操作。 |

右侧的 **Preview** 面板列出将包含在批量重命名过程中的对象。要添加对象，请将其从其他视图（如 Project Explorer）拖到 **Preview**面板。要添加更多对象，请在拖拽添加对象时按住 Shift 键；否则，将将视图中的对象拖动到 **Preview** 面板将替换其中列出的所有对象。要删除对象，请选中它们，然后按 Delete 键或在其快捷菜单中选择 **Remove From List**。除了全选（使用 Ctrl+A 或仅靠手动选择）并删除它们，单击 **Remove All** 也可清除 **Preview** 面板中的内容。

| 界面元素 | 描述 |
| --- | --- |
|  | 打开搜索框，在其中输入标准字母和数字会筛选掉视图中不相匹配的元素。阅读 [“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格") 了解详细信息。  点击搜索图标左侧的 Close（关闭）图标，以关闭搜索字段并删除筛选器。  |  |  | | --- | --- | | [备注] | 备注 | | 搜索不包括[“List View（列表视图）”一节](02-List-View（列表视图）.md "List View（列表视图）"), [“Query Editor”一节](../07-Queries-选项卡/01-Query-Editor.md "Query Editor"), [“MIDI Keymap Editor 视图”一节](../01-Audio-tab/03-Containers-hierarchy-sound-and-motion-objects/06-Common-tabs-and-categories-Containers-hierarchy-ob/01-MIDI-category-Containers-hierarchy-objects/01-MIDI-Keymap-Editor-视图.md "MIDI Keymap Editor 视图"), and [“Reference View 视图”一节](05-Reference-View-视图.md "Reference View 视图")中折叠起来的节点。  The search is not included in the Settings for Source objects. | |
|  | 配置列…。右键单击表格标题来打开 **Configure Columns** 对话框以指定要显示的列及其顺序。详请参阅[“使用表格”一节](../../../02-入门/03-Wwise-界面基础知识/00-Wwise-界面基础知识.md#using_tables "使用表格")。 |
| Name | 名称。显示对象名称。  |  |  | | --- | --- | | [备注] | 备注 | | 当 **Apply to**设置为 **Name** 时，对象名称相当于 **Before** 列。因此，**Name** 列仅在 **Apply to** 设置为 **Notes** 时才显示。 | |
| Before | 改名前。显示未修改的对象名称或备注。 |
| After | 改名后。显示修改过的对象名称或备注。 |
| (类型 —— 颜色) | 针对显示的消息类型，显示三种可能的颜色方框之一。如果没有消息，则不显示任何方框。  绿色 —— 成功（仅在点击**Rename All** 之后才显示）。  黄色 —— 警告（仍可以重命名）。**No Change** 是在重命名之后可能显示的一条警告。  红色 —— 错误（无法重命名）。 |
| Message | 消息。显示三种可能类型的消息：成功、警告或错误。  成功消息：  - **Successfully renamed（重命名成功）**  警告消息：  - **No Replace match detected.（没有发现匹配的替换）** - **Insert text does not have a valid printf format number.（输入文本没有包含有效的 printf 格式表示的数字）** - **No change.（没有变化）**  错误消息：  - **Resulting name is already used by a sibling object or is otherwise reserved**（结果名称已被兄弟对象占用或者被禁用）. - **Resulting name would be blank.（结果名称会为空白。）** - **File path would exceed system limit of characters.（文件路径会超出系统字符上限）** - **Name would contain invalid characters (<>\*?:"/\|%) for this object type.（名称会包含无效字符 (<>\*?:"/\|%)）**  |  |  | | --- | --- | | [备注] | 备注 | | 如果对象具有多条适用消息，则仅显示最新找到的消息。 | |
| |  | | --- | |  | | 汇总错误和警告消息的数量。 |
|  | 从面板中删除所有对象。 |
|  | 对 Preview 面板中的所有对象应用批量重命名，无论它们是不是通过搜索筛选器从视图中筛选出来的。  |  |  | | --- | --- | | [技巧] | 技巧 | | 按住 Ctrl+Z 撤消该操作。 |  在重命名 Work Unit（工作单元）或 Physical Folder（实文件夹）时，会打开 **Source Control Operation**（版本控制操作）对话框。在此，必须确认是否继续操作，因为后续没有办法撤消。 |

---