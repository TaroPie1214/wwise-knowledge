# 为工程指定 Default Object Value

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [设置工程](../00-设置工程.md) > [处理工程](00-处理工程.md) > 为工程指定 Default Object Value

## 为工程指定 Default Object Value

在 Wwise 中，可为工程指定特定的 Default Object Value。这些默认值会被应用于您创建的每个新对象，除非新建的对象被创建为另一对象的子对象。在这种情况下，对象会沿用指派给其父对象的音频输出和 Conversion Settings ShareSet。

建议在工程中提早指定 Default Object Value 以便在创建新的对象时予以应用。

在工程开发期间更改 Default Object Value 时，只会影响执行所述更改之后创建的对象。也就是说，您可以在创建某种对象（如 SFX 对象）之前设置 Default Object Value，并在创建另一种对象（如 Voice 对象）之前更改 Default Object Value。

每个用户都可指定 Default Object Value。Wwise 会将其保存到 `<project directory>/<project_name>.<user_name>.wsettings` 路径下的 XML 文件中。

**指定 Default Object Value：**

1. 在菜单栏中，依次单击 **Project > Default Object Values**（工程 > 默认对象值）或按下 Shift+D。
2. 在 Default Object Values（默认对象值）对话框中，指定默认值。有关详细信息，请参阅下表。
3. 单击 **OK**（确定）。

   这时会关闭 Default Object Values 对话框并保存所指定的值。

| 界面元素 | 描述 |
| --- | --- |
| **Routing（信号通路）** | |
| Audio Output | The default Audio Bus within the Busses hierarchy through which new sound and music objects will be routed. |
|  | 打开 Project Explorer - Browser，以选择默认音频总线。 |
| **Sound Object** | |
| Voice Volume（声部音量）。 | 声部音量。所有新声音对象的默认层级或振幅。  默认值：0 范围：-200 至 0 单位：dB |
| **Default Conversion Settings（默认转码设置）** | |
| Override Project Settings | 不沿用工程设置。该项方便选择另一个默认 Conversion Settings 共享集。  |  |  | | --- | --- | | [备注] | 备注 | | 默认 Conversion Settings 共享集适用于新创建的 Wwise 对象。更改此项后并不会替换先前应用的 Conversion Settings 共享集。 | |
| (Conversion Setting ShareSet) | ShareSet 的名称将用于默认 Conversion Settings。  每次在工程中创建新的顶级父对象时都会使用默认 Conversion Settings 共享集。若将新对象创建为另一对象的子对象，则其将继承指派给父对象的 Conversion Settings 共享集。  在生成 SoundBank（音频包）时，不会使用用户默认 Conversion Settings。 |
|  | 打开 Project Explorer - Browser（工程资源管理器 - 浏览器）。在此，可浏览并选择不同的默认 Conversion Settings 共享集。 |
|  | 确定。关闭 Default Object Values 对话框并保存设置。 |
|  | 取消。关闭 Default Object Values 对话框而不保存设置。 |

---