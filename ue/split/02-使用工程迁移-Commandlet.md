# 使用工程迁移 Commandlet

|  |
| --- |
| Wwise Unreal Integration Documentation |

使用工程迁移 Commandlet

Wwise Unreal 插件包含相应的 Commandlet，方便通过命令行将 Unreal 工程迁移到 Wwise 2022.1。

# Commandlet 用法和参数

Commandlet 用法：

<UnrealEditor.exe> <path\_to\_uproject> -run=AkMigration [ [-transfer-bank-waapi] OR [-generate-bank-definition=<Path/To/Save/FileName>.tsv] ][-ignore-bank-errors] [-transfer-bank-autoload] [-delete-banks] [-migrate-assets] [-update-settings] [-delete-deprecated-assets] [-generated-soundbanks-folder=<Path/To/Folder>]

以下参数执行 Migration Window 中可用的相同操作。有关这些操作的详细信息，请参阅 [将工程升级到 Wwise 2022.1](pg_important_migration_notes_2022_1_0.html) 页面。

- **transfer-bank-waapi**：（可选）通过 WAAPI 将 Unreal 工程中的 SoundBank 传输到 Wwise。此参数不可与 generate-bank-definition 结合使用。
- **generate-bank-definition**：（可选）在指定的路径创建 SoundBank 定义文件。使用绝对文件路径 (C:...)。之后须将文件手动导入到 Wwise 中来创建 SoundBank。此参数不可与 transfer-bank-waapi 结合使用。
  - **ignore-bank-errors**：（可选）忽略在通过 WAAPI 传输 SoundBank 期间或在写入到 SoundBank 定义文件时发生的错误并继续实施迁移。
- **transfer-bank-autoload**：（可选）将 AkAudioBank AutoLoad 属性传输到其中分组存放的素材。
- **delete-banks**：（可选）在完成传输后删除 Unreal 工程中的所有 SoundBank 素材。
- **delete-deprecated-assets**：（可选）删除所有还在工程中但已弃用的 Wwise 素材。
- **migrate-assets**：（可选）迁移工程中的 Wwise 素材。
- **update-settings**：更新 Wwise 和 Unreal 工程的设置。
  - **generated-soundbanks-folder**：（可选）与 update-settings 结合使用的 GeneratedSoundBanks 文件夹的路径。使用绝对文件路径 (C:/...)。此参数用于设定 Unreal 工程中的 Generated Sound Banks Folder 设置。
- **help**：（可选）输出消息来描述所有参数并马上终止 Commandlet。

## 使用示例

C:\UE\_5.0\Engine\Binaries\Win64\UnrealEditor-Cmd.exe C:\MyProjects\Demo\WwiseDemoGame.uproject -run=AkMigration -transfer-bank-waapi -transfer-bank-autoload -delete-banks -migrate-assets -delete-deprecated-assets -update-settings -generated-soundbanks-folder="C:/Project/WwiseProject/GeneratedSoundBanks"

|  |  |
| --- | --- |
|  | **TIP：** Commandlet 窗口会在执行命令后立即关闭。若要将命令的结果输出到文本文件，请在命令的末尾添加 `> log.txt`。这时会在当前目录下创建名为 `log.txt` 的文本文件并在其中包含相关错误或警告。 |

# 操作顺序

迁移操作的执行顺序跟编辑器内的迁移相同，其并不受命令行中的参数顺序影响。 顺序如下：

1. 生成 Bank
   1. 传输 Auto Load 属性
   2. 传输 Bank（WAAPI 或 SoundBank 定义文件）
   3. 删除弃用的 AkAudioBank 素材

# 迁移 Wwise 素材

1. 删除弃用的素材
2. 更新工程设置