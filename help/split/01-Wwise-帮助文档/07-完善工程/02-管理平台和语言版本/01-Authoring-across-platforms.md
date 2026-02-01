# Authoring across platforms

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [完善工程](../00-完善工程.md) > [管理平台和语言版本](00-管理平台和语言版本.md) > Authoring across platforms

## Authoring across platforms

对于音频设计师，处理不同的平台通常意味着为各个平台创建不同的工程。在 Wwise 中，只用一个工程就可以全部做到。在创建工程时，您可以自动进行跨平台开发，如果您愿意，则甚至可以同时开发。在默认情况下，工程中的所有可用平台都是活跃的，但是您可以从工程中移除平台，以提高工作流程的效率。有关从工程中移除平台的信息，请参阅[“Removing platforms”一节](../../03-设置工程/02-管理多平台.md#removing_platform "Removing platforms")。

在创建工程并导入素材和音乐后，设置一系列的转码设置 ShareSet（可以针对各个平台进行自定义），另外根据各个平台的优点和限制定义如何使用素材。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在 Wwise 中，跨平台制作的前提是您有权针对这些平台进行开发。如果您后来得到了更多的平台权限，则需要更新安装包，以包含这些额外的平台。 |

Wwise 可以让您按照以下方式为各个激活的平台自定义工程：

- [“对音频文件做转码”一节](../01-管理输出/10-对音频文件做转码/00-对音频文件做转码.md "对音频文件做转码")
- [“Customizing object properties per platform”一节](01-Authoring-across-platforms.md#customizing_object_properties_per_platform "Customizing object properties per platform")
- [“Excluding project elements from a platform”一节](01-Authoring-across-platforms.md#excluding_project_elements_from_platform "Excluding project elements from a platform")
- [“Switching to a different platform”一节](01-Authoring-across-platforms.md#switching_to_different_platform "Switching to a different platform")
- [“Copying settings from one platform to another”一节](01-Authoring-across-platforms.md#copying_settings_from_one_platform_to_another "Copying settings from one platform to another")

### Customizing object properties per platform

在 Wwise 中为工程中的特定平台定义声音属性时，默认情况下这些属性设置会覆盖所有活跃的平台。这些属性被称为受到了跨平台链接（linked）。这可以简化跨平台创建工程的过程。但是，如果您想自定义特定平台的属性，则可以对该平台的属性取消链接，然后定义您想要的属性。在取消链接属性时，链接标志会变成橙色。

|  |
| --- |
|  |

在为平台定义属性时，您可以轻松地判断这些属性在另一平台上是否已经取消链接。链接/取消链接标志将部分变为橙色，表示属性已经部分地取消链接。

**对某个平台的某个属性取消链接的方法是：**

1. 右键点击您要取消链接的属性旁边的链接标志。

   此时将会显示快捷菜单。
2. 点击 **Unlink**。

   标志变成橙色，您定义的值将仅适用于当前平台。

   当您切换到该属性仍然链接的平台时，链接标志将显示此属性在另一个平台上未链接。

|  |  |
| --- | --- |
| [备注] | 备注 |
| To link the properties again, right-click the property indicator and select **Link** in the shortcut menu. |

### Selecting sources per platform

在 Wwise 中，对象可以拥有多个源。在默认情况下，当跨平台播放时，对象将使用同一个源。然而，您可以通过在 Contents Editor 中取消链接这些源来为各个平台指定不同的源。在为该平台生成 SoundBank 时，将使用您选择的源。

|  |
| --- |
|  |

|  |  |
| --- | --- |
| [备注] | 备注 |
| 对于 Sound Voice 对象，您可以为工程中的每种语言分别取消链接源 Use 属性。 |

例如，假设格斗游戏中的角色根据游戏的平台拥有不同的名称。游戏主角最初取名为 Max，但在 Windows 改名为 Arthur。特定 Sound Voice 对象因此将包含两种不同的音频源，各个音频源包含的每行对白几乎完全相同，但使用的是不同的名称。您可以在 Windows 版本中取消链接声音对象 Use 属性，以便该版本中的声音对象使用 Arthur 的对白而不是 Max 的对白。

在定义用于您平台的源时，您可以使用链接/取消链接标志来检查各个源的状态。当某个源在当前平台上被取消链接时，其链接/取消链接标志将完全变为橙色。然而，当该源在另一个平台上被取消链接时，其标志将部分变为橙色。

**为平台选择源的方法是：**

1. 在 Contents Editor 中，通过点击相应的 **Use** 选项选择您要使用的源。

   此时选定的源将应用于所有平台。
2. 如果您只想在当前平台上使用此音频源，请右键单击语言栏中的链接标志。

   此时将会显示快捷菜单。
3. 点击 **Unlink**。

   标志将变为橙色，您决定使用的音源只适用于当前平台和所选语言。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 要再次链接源 Use 属性，则右键点击属性标志并从快捷菜单中选择 **Link**。 |

### Excluding project elements from a platform

进行音频研发时，需要牢记游戏和游戏平台的内存需求。您还需要考虑哪些平台能够恰当地处理特定素材。为了优化各个平台，您可能需要启用或弃用特定对象。在弃用某个对象后，为该平台生成的 SoundBank 中不会包含该对象。

![](../../../../images/excluding_from_platforms.png)

|  |  |
| --- | --- |
|  | The check box is selected which means that the Parent Container will be included in SoundBanks that are generated. |
|  | The check boxes for the ExcludedLinked sound object and the Parent Container are not selected. These objects will be excluded from SoundBanks that are generated. All child objects of the Parent Container will also be excluded. |
|  | Link indicators that show if an object is linked, unlinked, or partially linked to other platforms.  For example, for the IncludedUnlinked sound object, the link indicator is completely orange, which means that it is unlinked on the current platform. The check box is selected, which means the object will be included in the SoundBanks for the current platform, but because the object is unlinked, the check box might be deselected on other platforms. |

Inclusion 复选框可以用来在平台中包含或排除特定对象、文件夹、事件或语言，在 Wwise 的多个视图中都可以看到：

- Project Explorer（对象、效果器、音频设备以及虚拟文件夹和工作单元左侧的无标题复选框）
- Property Editor（对象图标左侧的无标题复选框）
- Contents Editor（内容编辑器中的 **Inc. "Language"** 复选框，其中“Language”对应您工程中的任何语言）
- Event Editor（**Inclusion 复选框**）
- List View（**Inclusion 复选框**）
- Multi Editor（**Inclusion 复选框**）
- Query Editor（**Inclusion 复选框**）

在决定启用或弃用对象后，您可以在 Transport Control 中试听平台专有的音频。还可以使用 Soundcaster 和 Game Profiler 来帮助决定平台中要启用或弃用的对象。有关性能分析和模拟的详细信息，请参阅以下各节：

- [*性能分析*](../06-性能分析/00-性能分析.md "性能分析")
- [*创建模拟*](../03-创建模拟/00-创建模拟.md "创建模拟")

**要在 Wwise 视图中弃用工程元素，请执行以下操作：**

1. 在任何含有 Inclusion 复选框的 Wwise 视图中直接清除 Inclusion 复选框，或使用快捷菜单的 **Inclusion** > **Exclude Selection** 选项。

   该工程元素将不再包含于当前平台中。

|  |  |
| --- | --- |
| [技巧] | 技巧 |
| 您可以同时选择多个元素，以便批量启用或弃用元素。 |

**从所有平台中弃用工程元素的方法如下：**

1. 确保要弃用的工程元素的链接标志为灰色，即该元素已链接。

   - 如果链接标志为橙色，则选择 **Inclusion** > **Link**。
   - 如果链接标志只有顶部为橙色，请[切换当前平台](01-Authoring-across-platforms.md#switching_to_different_platform "Switching to a different platform")来查找未链接的平台（全橙）并将其全部改为链接。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 更多关于链接标志的信息，请参阅 [“Linking or unlinking property values”一节](../../08-使用-Wwise/03-了解-Property-Editor/11-使用-Property-Editor.md#linking_unlinking_property_values "Linking or unlinking property values")。 |
2. 重复[要在 Wwise 视图中弃用工程元素，请执行以下操作：](01-Authoring-across-platforms.md#list_exclude_elements "要在 Wwise 视图中弃用工程元素，请执行以下操作：")中的步骤。

### Switching to a different platform

由于 Wwise 工程包含所有活跃的平台版本，因此在开发周期中，您可以随时轻松地从一个平台切换到另一个平台。例如，您可以同时针对多个平台进行开发，而且还可以系统地为各个平台定义特定的对象属性。在您切换平台后，将显示当前的平台版本。

**在有效平台之间切换的方法是：**

1. 在工具栏左侧，单击箭头以显示 Platform Selector（平台选择器）列表。
2. 从 Platform Selector 列表中选择新的平台。

   |  |  |
   | --- | --- |
   | [技巧] | 技巧 |
   | 列表按字母顺序排列，其中每个平台均有对应的快捷方式。比如，若 Wwise 工程包含 A、B、C 三个平台，则按下 Alt+1 将打开平台 A 版本，按下 Alt+3 将打开平台 C 版本。您可以随时按下对应快捷键，以便选择不同平台版本的 Wwise 工程。 |

   此时将显示您选择的平台版本。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 只有已添加到工程中的平台会显示在 Platform Selector 列表中。For information on adding a platform, see [*管理多平台*](../../03-设置工程/02-管理多平台.md "管理多平台"). |

### Copying settings from one platform to another

Since Wwise allows platform-specific editing in your project, at some point you may want to copy these settings from one platform to another. For example, if you have been working on two platforms for some time and are now ready to add a third one, you might want to start with a copy of one of the platforms you have already customized.

The **Copy Platform Settings** dialog, accessed through the [“Platform Manager”一节](../../09-参考主题/01-工程/09-Platform-Manager/00-Platform-Manager.md "Platform Manager"), lets you do just that. 您只需指定源和目标平台，Wwise 就会将所有平台相关设置从源平台复制到目标平台。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 平台设置不同于 **Base Platform**。后者一旦选定用于某个平台之后便不会改变了。如果需要新的 **Base Platform**，则必须创建新平台。 |

**从源平台复制到目标平台的平台相关设置：**

- 取消链接的对象参数

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | 有一些例外情况：Project Settings 对话框 SoundBanks 和 External Sources 选项卡中的平台相关设置不会复制到目标平台。 |
- Inclusion/exclusion（启用/弃用）
- 取消链接的活跃音频源（Contents Editor 中为声音指定的源）
- 转码设置

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | 如果目标平台上不支持源平台上使用的转码格式，则使用目标平台的默认格式代替，并且日志中将显示警告。另外，如果目标平台上的格式不支持源平台上指定的采样率，则它将被修复，并且日志中将显示警告。 |
- Unlinked 3D Attenuation (specified in the Positioning category of the Property
  Editor)
- 取消链接的 3D 衰减曲线（在 Attenuation Editor 中定义）
- Unlinked Effects (specified in the Effects tab of the Primary Editor)

  |  |  |
  | --- | --- |
  | [备注] | 备注 |
  | If an Effect used on the source platform is not supported on the target platform, no effect will be set for the corresponding effect ID on the target platform. |
- 取消链接的对白事件路径目标对象

当设置在源平台上已经取消链接时，该设置在目标平台上也会取消链接，并复制到目标平台。当某设置在目标平台上被链接但在目标平台上已经取消链接时，则目标平台上将重新链接它。

---