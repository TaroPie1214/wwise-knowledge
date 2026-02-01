# Migrating your projects

[Wwise 帮助文档](../00-Wwise-帮助文档.md) > [完善工程](00-完善工程.md) > Migrating your projects

## Migrating your projects

在准备升级到新的 Wwise 大版本时，必须遵照协同规范来确保将之前版本中创建的工程顺利地迁移到更高版本。这样做的目的是避免对游戏产生任何形式的危害，所以一定要检查新版中执行的更改，并选择性、系统性地将修改应用到游戏代码中。

升级和迁移规范可能会因以下条件而有所不同：

- **处于版本控制之下的工程**：必须在关键点签入工程。
- **多个用户**：必须在本地系统上完成 Wwise 升级、工程迁移、SDK 升级和游戏代码更新，以便多个用户在工作站上统一对 Wwise 进行升级。
- **集成的游戏工程**：必须按照迁移说明中的规定修改游戏代码。

强烈建议迁移团队（由一名或两名指定人员组成）先在本地系统上执行以下任务：

- [“Preparing your projects for migration”一节](09-Migrating-your-projects.md#before_you_begin "Preparing your projects for migration")
- [“Upgrading Wwise and migrating your project”一节](09-Migrating-your-projects.md#upgrading_wwise "Upgrading Wwise and migrating your project")
- [“Upgrading Wwise and migrating your project”一节](09-Migrating-your-projects.md#upgrading_wwise "Upgrading Wwise and migrating your project")
- [“测试”一节](09-Migrating-your-projects.md#testing "测试")

在迁移团队执行这些任务之后，您可以执行以下操作：

- [“Upgrading Wwise on all workstations”一节](09-Migrating-your-projects.md#upgrading_wwise_on_all_workstations "Upgrading Wwise on all workstations").

有关处于版本控制之下的工程的升级和迁移工作流程，请参见下表：

![](../../../images/UpdateDiagram_Overview.png)

## Preparing your projects for migration

在升级到新的 Wwise 版本之前，必须针对工程作一些准备（尤其是在已将 Wwise 工程整合到游戏中的情况下）。具体来说，就是针对所要迁移的全部工程重复以下章节中所述的步骤。

迁移团队必须执行以下任务以便做好将工程迁移到最新版本的准备。

1. 提交所有工程：

   1. 对于处于版本控制之下的工程，请求团队其他成员一并提交所有更改。

      这样可以避免以后产生合并问题。
2. 获取所有最新版本的待迁移工程：

   1. 对于处于版本控制之下的工程，将所有工程全部导入到本地系统。
   2. 确保所有工程文件均具备读写权限。

      对于处于版本控制之下的工程，您可能需要从各个子文件夹中签出工程文件 (WPROJ) 和所有 Work Unit 文件 (WWU)。
3. 验证待迁移工程：

   1. 在当前 Wwise 版本中，打开准备迁移的各个 Wwise 工程并进行保存。
   2. 若 Project Load Log（工程加载日志）对话框显示消息和修复建议，请接受这些修复，然后保存更改并关闭工程。重复这一操作，直到不再显示任何消息。这样做的目的是排除所有工程错误以简化升级流程。
4. 标记待迁移工程：

   1. 对于处于版本控制之下的工程，提交并标记为升级之前最后版本的工程。

      若此时提交工程，则将保存迁移之前的所有更改。版本控制记录中，此后的其他更改都与迁移直接相关。

## Upgrading Wwise and migrating your project

即便对功能集进行了重大更改，工程迁移流程也可确保迁移后的工程具有与之前工程基本相同的声音效果。有关这些更改的详细信息，请参阅[当前 Wwise 版本的版本说明](https://www.audiokinetic.com/library/edge/?source=SDK&id=releasenotes.html)以及其中链接的对应重要迁移说明。

建议迁移团队先在本地系统上将 Wwise 工程迁移到新的 Wwise 版本。在迁移团队测试并提交已迁移的工程之前，所有其他用户不得修改工程。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在升级到新的版本时并不一定要迁移工程，具体因 Wwise 版本之间的更改类型而异。  - **大版本**：若版本的年份编号（即年份之后第一个小数位）发生变化，则表示该大版本可能存在多项重大更改。比如，2019.1 和 2019.2 都属于大版本。在使用 Wwise 2019.2 打开 Wwise 2019.1 中保存的工程时，Wwise 会提示迁移工程。若接受，则稍后将无法使用 2019.1 版本打开该工程。 - **小版本**：若版本的年份编号（即年份之后第一个小数位）保持不变，而后一小数位发生变化，则表示其为小版本。比如，2019.1.3 和 2019.1.4 都属于小版本，只存在些许更改。在使用 Wwise 2019.1.4 打开 Wwise 2019.1.3 中保存的工程时，无需实施迁移。 |

1. 升级 Wwise：

   1. Upgrade Wwise on your local system as described in [Installing Wwise and Its
      Components](https://www.audiokinetic.com/library/edge/?source=InstallGuide&id=installing_wwise_and_its_components).
2. 将工程迁移到新的版本：

   1. 确认当前 Wwise 工程中的所有文件均具备读写权限。
   2. 进行工程备份并将备份工程存储到系统或网络上的另一文件夹中。Wwise 会自动备份工程，但最好另外手动备份。
   3. 打开新的 Wwise 版本。在打开的 Project Launcher（工程启动器）对话框中，选择准备迁移的工程。

      Project Migration 对话框打开时会提示将工程迁移到更高的 Wwise 版本。

      |  |  |
      | --- | --- |
      | [备注] | 备注 |
      | The Migration dialog is only displayed when significant changes have been made to the project file between versions. 倘若工程不需要迁移，则 Wwise 会跳到迁移流程的下一步。 |
   4. 单击 **Migrate**（迁移）。

      这时 Wwise 会迁移工程。在迁移工程之后，Wwise 会检查现有工程缓存文件夹是否与当前 Wwise 版本兼容。若否，则 Wwise 将删除工程缓存文件夹。在删除工程缓存后，会显示以下消息框。

      ![](../../../images/cache_deleted_message.png)
   5. 单击 **OK**（确定）。
   6. 在 Wwise 菜单栏中，依次选择 **Views > Utilities > Logs**（视图 >实用工具 > 日志）。此时将打开 Logs 视图。
   7. 在 Logs（日志）视图中，选中 **Project Load**（工程加载）选项卡。这时 Project Load Log 会显示与迁移有关的消息，并指示有没有针对新版 Wwise 创建任何文件。

      ![](../../../images/Project_load_log.png)

      |  |  |
      | --- | --- |
      | [备注] | 备注 |
      | 此信息存储在工程文件夹内的 `projectname.wproj_migration.log` 文件中。在必要时，可单击 **Copy to clipboard**（复制到剪贴板）来保存此信息以供稍后参考。 |
   8. 若使用了版本控制系统，请将迁移过程中创建的所有新文件添加到版本控制系统。
   9. 关闭 Logs（日志）视图。
3. 生成 SoundBank（音频包）：

   1. 针对已迁移的工程生成 SoundBank 以便用来测试。

## Upgrading the Wwise SDK and updating game code

除了升级 Wwise 设计工具，还要执行以下任务来升级 Wwise SDK 并更新游戏代码。

1. 升级 Wwise SDK：

   1. 确认系统满足 Wwise SDK [平台要求](https://www.audiokinetic.com/library/edge/?source=SDK&id=reference_platform.html)。
   2. 可选择卸载之前的 Wwise SDK 版本。

      最好同时手动移除 C++ 示例工程创建的临时文件。
   3. 安装更高的 Wwise SDK 版本。参阅[通过 Launcher 安装 Wwise](https://www.audiokinetic.com/library/wwise_launcher/?source=InstallGuide&id=install_wwise_through_launcher)，并在 **Packages**（数据包）下选中 **SDK (C++)**。
   4. 确认 WWISESDK 环境变量指向更高版本的安装文件夹。（有关如何设置环境变量的详细信息，请参阅[选用多个 Wwise SDK 版本](https://www.audiokinetic.com/library/wwise_launcher/?source=InstallGuide&id=installing_or_upgrading_wwise_and_its_packages#working_with_multiple_versions_of_wwise_sdk)）。
2. 针对更高 Wwise SDK 版本更新游戏代码：

   1. 参阅 Wwise SDK 文档中的迁移说明，以便熟悉需要执行哪些修改。
   2. 若要迁移游戏代码，必须将 C++ 工程的现有功能从之前的版本移植到更高的 Wwise SDK 版本。在此过程中，可能需要修改或重构各个模块中的代码。另外，可能需要针对以下模块执行相应的更改以便更新游戏代码：

      - Sound Engine（声音引擎）
      - Memory Manager
      - Stream Manager
      - Communications Module

      |  |  |
      | --- | --- |
      | [备注] | 备注 |
      | 为了确保更高版本中的有些新功能不会对游戏产生不利影响，建议先升级游戏所需的组件。在确保游戏比较稳定后，则可根据需要集成这些新功能。 |
   3. 根据需要修改代码。

      |  |  |
      | --- | --- |
      | [技巧] | 技巧 |
      | 在修改代码时，最好重新构建 C++ 工程。 |
3. 构建游戏。

## 测试

在完成升级和迁移之前，必须测试已迁移的游戏。有可能您已经在工作当中创建了一套测试规范。不过作为补充，我们还是列出了一些简单的步骤以供您在测试时参考。建议迁移团队同时在 Wwise 设计工具和游戏中实施这些测试。

**测试已迁移的游戏工程，然后提交：**

1. 在游戏中，确认声音和音频行为。确认事项可能包括：

   - 基本的音频播放。
   - 受代码更改影响的行为。
   - 平台行为。
   - 与 Wwise 设计工具的通信。
2. 将已迁移的 Wwise 工程和代码更改提交到版本控制系统。

在完成测试后，倘若对结果满意，便可指导其他用户升级到最新 Wwise 版本。

## Upgrading Wwise on all workstations

在本地系统上升级 Wwise、成功迁移工程、执行 SDK 升级及游戏代码更改并完成测试之后，您可以指导其他用户在其工作站上升级 Wwise。

此次升级必须在使用 Wwise 的所有工作站上执行，其中包括：

- 编译机器
- 声音设计师所用工作站
- 开发人员所用工作站
- 所有其他 Wwise 用户工作站

确保包括了所有运行 Wwise 的工作站以便全部进行升级。

**在所有工作站上升级 Wwise：**

1. 可选择卸载所有 Wwise 组件。其中可能包括：

   - Wwise 设计工具
   - Wwise SDK

   有关如何卸载的详细信息，请参阅[卸载 Wwise](https://www.audiokinetic.com/library/wwise_launcher/?source=InstallGuide&id=uninstalling_wwise)。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 并不一定非要卸载 Wwise。在必要时，可在同一工作站上保留多个 Wwise 版本和内部版本。 |
2. 安装更高的 Wwise 版本。其中可能包括：

   - Wwise 设计工具
   - Wwise SDK
   - Wwise Game Simulator

   有关如何安装的详细信息，请参阅[安装 Wwise 及关联组件包](https://www.audiokinetic.com/library/wwise_launcher/?source=InstallGuide&id=installing_or_upgrading_wwise_and_its_packages)。

**在所有工作站上访问已迁移的 Wwise 工程：**

1. 在安装更高的 Wwise 版本后，检出已迁移的 Wwise 工程。
2. 打开 Wwise。

   此时将显示 End-User License Agreement（最终用户授权协议）。
3. 仔细阅读协议。若接受，请点击 **Accept**（接受）。

   此时将打开 Project Launcher 窗口。
4. 打开已迁移的工程。

   |  |  |
   | --- | --- |
   | [备注] | 备注 |
   | 若部分用户在本地存有 Wwise 工程中的 Work Unit 且未将其添加到版本控制系统，则会弹出消息并提示允许在新的 Wwise 版本中打开工程时迁移这些 Work Unit。 |

   在加载工程之前，Wwise 会检查并确保工程缓存文件夹与当前版本兼容。若否，则 Wwise 将删除工程缓存文件夹。在删除工程缓存后，会显示以下消息框。

   ![](../../../images/cache_deleted_message.png)
5. 单击 **OK**（确定）。

   在删除缓存后，便会将工程加载到 Wwise 中。

---