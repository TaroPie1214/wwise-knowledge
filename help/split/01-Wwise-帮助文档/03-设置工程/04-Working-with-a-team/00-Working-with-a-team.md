# Working with a team

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [设置工程](../00-设置工程.md) > Working with a team

## Working with a team

在当今的游戏环境中，随着游戏日趋复杂并且面临着上市的压力，声音设计师、作曲家、音频集成师和音频程序员能够协同处理同一工程至关重要。在 Wwise 中，可使用 Work Unit（工作单元）和版本控制系统加以实现。

每款游戏只能使用一个 Wwise 工程。为了让多人高效地协同处理同一工程，必须将工程分解成多个部分。在 Wwise 中，这些部分被称为工作单元。

|  |
| --- |
|  |

之后，可通过版本控制系统来管理这些 Work Unit 文件。

|  |
| --- |
|  |

之后，团队中的各个成员可并行处理工程的同一或不同部分。

|  |
| --- |
|  |

在大多数情况下，为了避免出现棘手和频繁的合并问题，您需要不同的成员处理工程的不同部分。然而在某些情况下，两个或多个成员必须并行处理同一工作单元。当这些文件重新 check-in 到版本控制系统时，您很可能需要处理合并冲突。请参阅版本控制文档，了解有关如何妥善处理合并冲突的详细信息。

虽然 Wwise 不是一款版本控制系统，但是您可以使用它的开放架构轻松地集成现有版本控制系统。它可以让您直接在 Wwise 中管理工程素材并执行许多版本控制功能。有关 Wwise 版本控制插件的详细信息，请参阅[“利用版本控制插件管理工程文件”一节](05-利用版本控制插件管理工程文件.md "利用版本控制插件管理工程文件")。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 要创建版本控制插件，所用版本控制系统需支持利用其 API 进行第三方集成。Wwise 中安装了 Perforce 和 Subversion 插件。 |

## 什么是 Work Unit？

工作单元是独特的 XML 文件，其中包含与工程中特定部分或元素相关的信息。这些工作单元可帮助您组织和管理工程中的各种不同元素。如果是团队协作，还可通过版本控制系统来管理这些工作单元，以便其他团队成员同时来处理此工程。

When a project is created, a Default Work Unit is created for each of the following elements in Wwise:

- Containers hierarchy
- Audio Devices
- Attenuations
- Control Surface Session
- Conversion Settings（转码设置）
- Dynamic Dialogue
- Effects（效果器）
- Events（事件）
- Game Parameters
- Busses hierarchy
- Mixing Session
- Modulators（调制器）
- Presets（预设）
- Queries（查询）
- SoundBanks（声音库）
- Soundcaster Sessions（声音选角器会话）
- States（状态）
- Switches（切换开关）
- Triggers

这些默认工作单元位于工程目录下的相应文件夹中。每个都命名为“Default Work Unit.wwu”。默认 Work Unit 已经创建，这样您就可以直接新建对象、事件、状态等，而不必先为每个工程元素创建 Work Unit。

随着项目进展或者更多人员加入项目团队，您可能需要将不同的工程元素分成新的工作单元。例如，您可以为 StatesLevel1、StatesLevel2 和 StatesLevel3 状态创建三个不同的工作单元。

如果您决定创建新的工作单元，则可以将默认工作单元保留为空白。然而，Default Work Units 是关键的工程文件，不得重命名或删除。 如果您重命名或删除这些文件，Wwise 则将在您下次打开工程时重新创建它们。

工作单元可以按照实子文件夹来组织存储在磁盘上。Project Explorer 中将复制此实文件夹结构。

您可以为所有工程元素创建新的 Work Unit。

The following example shows how Work Units can be created and organized to divide up the sound structures in the Containers hierarchy.

![](../../../images/pe_work_units_and_folders.png)

|  |  |
| --- | --- |
|  | Physical Folder。 |
|  | "3D\_Audio\_Demo" Work Unit 及其内容。 |

您可以在 Project Explorer 中的不同选项卡中创建和管理工作单元的内容。For more information about organizing your project into Work Units, refer to [“将工程分成 Work Units”一节](01-将工程分成-Work-Units.md "将工程分成 Work Units").

---