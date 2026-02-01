# 为插件创建 Factory Asset

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

为插件创建 Factory Asset

Factory Asset 便于通过插件提供预先制作的命名预设。工程根目录下 `FactoryAssets` 文件夹中的 `Manifest.xml` 指向 Wwise Work Unit 文件 (.wwu )。藉此，设计工具可查找所有插件预设。插件创建者需要自己创建此 Work Unit 文件。下面是完成插件开发后的例行操作。

1 – 创建新的 Wwise 工程。

2 – 在 Designer 布局下，打开 ShareSets 选项卡，然后展开 Effects 文件夹。

3 – 右键单击 Effects 文件夹，然后依次选择 **New Child** > **Work Unit**，并使用插件的名称来命名。

4 – 右键单击新建的 Work Unit，然后依次选择 **New Child** > <your plug-in>（列表末尾部分）。

5 – 使用预设的名称来命名，然后双击以打开 Effect Editor 并根据需要调节参数。

6 – 针对所要创建的每个预设重复步骤 4 和 5，然后保存工程。

7 – 复制 Wwise 工程的 Effects 文件夹中创建的文件（即 YourPluginName.wwu），然后保存到插件工程的 `FactoryAssets/Effects` 文件夹（必要时可自行创建 Effects 文件夹）。

8 - In the Manifest.xml file, make sure the name of your Work Unit file matches the **Manifest Name** field (without extension) and the name of your plug-in matches the **Plugin PluginName** field.

就这么简单！随后便可将 Factory Asset 与插件一并打包，并安装到 `Wwise/Authoring/Data/Factory Assets/YourPluginName` 中。