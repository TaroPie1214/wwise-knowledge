# Multi-Channel Creator window

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 工具](../../00-Wwise-工具.md) > [使用 Multi-Channel Creator](../00-使用-Multi-Channel-Creator.md) > [Multi-Channel Creator reference](00-Multi-Channel-Creator-reference.md) > Multi-Channel Creator window

### Multi-Channel Creator window

在 Multi-Channel Creator 窗口中，您可以指定源单声道或立体声文件的位置，这些文件将用于创建将导入到 Wwise 工程的多声道文件。您还可以指定保存新创建的多声道文件的输出文件夹。一旦指定 Input 文件夹，则 Output preview（输出预览）中会自动填入内容。Output preview 显示将与可能输出配置的列表一起创建的多声道文件。

要了解声道配置的详细信息，请参阅[“了解总线配置”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。

| 界面元素 | 描述 |
| --- | --- |
| Input folder | Input 文件夹。该文件夹包含源单声道和立体声音频文件，这些文件将被合并起来创建多声道文件。  Input 文件夹中的各个音频文件的名称必须包含特定前缀，这样 Multi-Channel Creator 才能轻松识别各个文件具有的声道。You can define these suffixes in the Settings dialog. |
|  | Opens the Browse for Folder dialog where you can navigate to the 'Input folder'. |
| Output folder | Output 文件夹。用于保存多声道文件的文件夹。 |
|  | Opens the Browse for Folder dialog where you can navigate to the 'Output folder'. |
| **Output Preview（输出预览）** | |
| |  | | --- | |  |  （选择） | 确定将生成的多声道文件。 |
| Output file name | 输出文件名。将生成的多声道文件的名称。  如果 Input 文件夹中的源文件分成子文件夹，则 Output 文件名将包含相对于输出文件夹的完整路径。 |
| Configuration | 配置。一系列可能的多声道配置。这些配置是根据 Input 文件夹中的各个源音频文件具有的声道建立的。  要了解声道配置的详细信息，请参阅[“了解总线配置”一节](../../../05-使用声音和振动来提升游戏体验/02-定义定位/11-了解总线配置.md "了解总线配置")。 |
|  | 在 Output preview 列表中选择要处理的所有多声道文件。 |
|  | 在 Output preview 列表中清除选择所有多声道文件。 |
|  | 启动所选输出文件的生成流程。 |

---