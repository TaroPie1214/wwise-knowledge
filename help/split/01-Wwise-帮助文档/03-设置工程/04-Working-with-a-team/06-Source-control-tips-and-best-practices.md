# Source control tips and best practices

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [设置工程](../00-设置工程.md) > [Working with a team](00-Working-with-a-team.md) > Source control tips and best practices

## Source control tips and best practices

在结合 Wwise 使用版本控制系统前，最好仔细查看以下章节。您可以参照其中的技巧和窍门来在整个音频开发过程中更好地管理团队及工程文件。

### Planning your project

- Divide your project into smaller Work Units. 如果工程很庞大，并且您还将所有工程数据都保留在默认工作单元中的话，那么不仅会延长 Wwise 的响应时间，而且每当团队中有人做出更改后，其他团队成员则都需要进行合并，这可能会令发生合并问题和冲突的概率激增。通过使用工作单元将工程划分成小块，可以提高人们的工作效率，加快访问信息的速度，处理不同的领域，从而降低发生合并问题的可能性。
- 为全局默认工作单元指定负责人。因此好办法是让一个人管理或者至少其他人清楚对这些工程元素所做的更改。

### Basic workflow

- Manage global project elements effectively. 当您重命名或删除某个全局工程元素（例如状态或游戏参数）时，注意，您可能修改了工程中的许多其他对象，包括使用这些元素的所有声音对象和容器。当保存和登入这些更改时，您可能会影响其他人正在处理的众多工程文件。为限制此类更改的影响，应该尽早定义全局工程元素，此后再尽力避免更改这些元素。如果在初始设置后需要更改，则应执行以下操作：

  - 警告团队成员全局元素已被更改。
  - 要求团队全体成员登入他们的更改。
  - check-in 您的文件
  - 要求团队全体成员更新他们的工程文件。
  - 通过执行此流程，团队成员只需更新就可以获得新文件，无需合并。
- 检查工程文件状态。在开始处理某个工作单元前，使用 File Manager 验证哪些文件是只读文件。如果您更改的是只读工作单元，则将无法把该特定文件保存到工程中。
- 定期备份本地文件。虽然中央资源库中的文件可能是预定备份计划的一部分，但本地机器上的副本不是。为防止数据丢失，定期备份工程文件是个好办法，特别是当您对文件做了大量更改时，尤其如此。
- 在登入前生成完好度报告。在登入特定工作单元前，生成完好度报告是确保没有任何工程错误的好办法。If errors exist, you can quickly resolve them and then check the Work Unit in.

### Syncing your files

- Sync before new work sessions. 您应该先将您的工程文件与服务器进行同步，然后再启动新的工作会话，以便您获得最新的修改。
- 同步前关闭 Wwise。在将工程文件与服务器机型同步之前，应关闭 Wwise 以防止丢失信息的可能性。如果 Wwise 一直是打开状态，则副本将保留在内存中。同步时磁盘中的文件将被修改，但工程的旧版本仍将保留在内存中。如果您保存当前已打开的工程，则会覆盖磁盘中已保存的其他人的更改。

  以上所述仅在未使用版本控制插件的情况下适用。在使用版本控制插件进行同步时，系统会自动提示重新加载最新版本的工程。

### Checking in your files

- Submit often. 如果您有大更改，影响到团队的其他成员，应该经常将工程文件提交到服务器，以使其他成员可以使用您所做的更改。如果您等待太久，则还会增加发生冲突的概率。通过提交较小的、有针对性的更改，在必要时就容易恢复到工程的旧版本，并且容易在出现冲突时加以解决。
- 添加有用的注释。When you commit or check-in your files, make sure to fully describe the changes that you made.

### Source control system

- Understand your source control system. 在使用版本控制系统管理 Wwise 工程文件之前，应充分了解它的工作原理。了解版本控制系统的复杂性可帮助您避免问题，构建高效的制作管线。

### Project inconsistencies

- Become familiar with the Wwise project XML structure. 在合并文件前，花一点时间熟悉 Wwise 工程文件的 XML 结构。在一些情况下，您可能必须更新 XML 代码。如果您没有正确理解它，可能会毁坏您的工程。如果您的确要修改 XML，请确保在 Wwise 中打开工程，然后将文件重新登入到版本控制系统中。这将确保您对 XML 的更改是有效的，并且是您所需的。

### Communication

- 建议经常进行坦诚的沟通。无论在怎样的团队环境中，与团队的其他成员经常进行坦诚的沟通都很关键。经常、坦诚的沟通可以减少冲突，缩短合并文件的时间，建立一个更加高效的制作管线。For example, before making changes to a Work Unit that affects other members of your team, you should ask them to check in their changes and wait for your word before syncing and resuming their work.

### File usage

- Before deleting any files that are marked **Unused** in the **Usage** column of the File Manager, it is good practice to close and re-open the project to make sure the information is completely up to date.

### SoundBanks

- SoundBanks are configured in Work Units in the SoundBanks tab of the Project Explorer.
  The Work Unit files are in the `<project>\SoundBanks\`
  directory, and are XML files with the extension `.wwu`. You can
  reduce the frequency of changes to these files by populating them with
  objects such as Containers instead of, for example, individual Sound
  SFX.
- Generated SoundBanks are created by Wwise, by default in the `<project>\GeneratedSoundBanks\` directory. They are binary files with the extension `.bnk`. Since they can always be generated from the project, we recommend you exclude them from source control. 参见[“结合版本控制系统使用 Wwise”一节](03-结合版本控制系统使用-Wwise.md "结合版本控制系统使用 Wwise")。

---