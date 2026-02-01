# Assigning Conversion Settings ShareSets to objects

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [完善工程](../../00-完善工程.md) > [管理输出](../00-管理输出.md) > [对音频文件做转码](00-对音频文件做转码.md) > Assigning Conversion Settings ShareSets to objects

### Assigning Conversion Settings ShareSets to objects

After you have created the Conversion Settings ShareSets for your project, you can start assigning them to the objects in your project hierarchy. Conversion settings ShareSets, like other object properties, are inherited from parent to child, which means that if you assign a Conversion Settings ShareSet to a Property Container, all containers and objects below it will automatically use the same ShareSet. 当然，您可以不沿用父对象使用的 ShareSet，以便对层级结构中的特定对象或源应用不同的转码设置。

在默认情况下，您创建的所有 Conversion Settings 初始都为 ShareSets。但是，您可以针对一个特定对象来调整 ShareSet。如果您不想在对象之间共享转码设置，则可以创建自定义转码设置。在使用自定义转码设置时，这些设置仅应用于当前对象。如果更改转码设置，则只有此对象将受到影响。

**将转码设置 ShareSet 指派到对象**

1. 将顶层对象加载到 Property Editor 中。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 如果对象不是顶层对象，则在设置转码设置选项前必须选择 Override Parent 选项。 |
2. Switch to the Conversion category.
3. In the **Conversion Settings** group, click the browse
   button.

   A list of Conversion Settings ShareSets that are currently available in the project is displayed.
4. 在列表中选择您要应用到对象的 ShareSet。
5. 如果您要为对象采用自定义转码设置，则从 **Mode** 列表中选择 **Define custom**。

   这份 Conversion Settings 的名称后会跟有单词“Custom”（自定义）。从现在开始，您对实例所做的更改将仅影响使用它的一个对象。
6. 点击 **Edit** 按钮以将 ShareSet 或自定义转码设置加载到 Conversion Settings Editor 中，您可以在其中优化各种转码设置。
7. 在 Audio Source 表中，检查一下将应用这些转码设置的音频源列表以确保列表正确。

   要完成此表中的信息，必须对音频源做转码。有关转换音频源的详细信息，请参阅[“对音频文件做转码”一节](04-对音频文件做转码.md "对音频文件做转码")。

---