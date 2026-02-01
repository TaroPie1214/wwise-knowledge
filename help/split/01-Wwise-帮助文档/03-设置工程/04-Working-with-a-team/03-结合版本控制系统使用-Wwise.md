# 结合版本控制系统使用 Wwise

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [设置工程](../00-设置工程.md) > [Working with a team](00-Working-with-a-team.md) > 结合版本控制系统使用 Wwise

## 结合版本控制系统使用 Wwise

所有 Wwise 工程文件（包括各个 Work Unit）都基于 XML。所以，用户可使用版本控制系统轻松管理这些文件。建议将某些（并非全部）文件添加到版本控制系统。

File Manager（文件管理器）中的所有文件都可添加到版本控制系统。Wwise 会使用这些文件生成工程所需的其他文件。建议将以下内容添加到版本控制系统：

- **.wproj** —— Wwise 工程文件。这些文件存放在工程文件夹的根目录下。
- **.wwu** – Wwise Work Unit。这些文件存放在主工程文件夹的子目录下。
- **Originals 文件夹** – 原始媒体文件。这些文件可用于创建工程的最终音频素材。

总的来说，Wwise 生成的文件可以放在版本控制系统之外。因为没必要将它们添加到版本控制系统，而且在多用户环境下共享某些文件可能会导致同步问题。建议将以下内容放在版本控制系统之外：

- **.backup 文件夹** – 在使用新的 Wwise 大版本打开工程时，会对工程进行升级并生成 .backup 文件夹。这样是为了在需要时将工程恢复为升级之前的状态。若将工程添加到了版本控制系统，则可藉此恢复为升级之前的状态。为此，可将 .backup 文件夹放在版本控制系统之外。
- **.cache 文件夹** – 工程目录下的 .cache 文件夹是 Wwise 的本地工作文件夹。.cache 文件夹的内容不得添加到版本控制系统，因为这可能造成 Wwise 中发生异常行为。
- **.prof** – 这些文件在每次捕获时生成，其并非工程数据的一部分。
- **.validationcache** – 这些文件由 .wwu 文件生成，可放在版本控制系统之外。
- **.wsettings** – 此文件特定于本地用户和电脑。
- **IncrementalSoundBankData.xml** – 此文件用于根据 Wwise 工程的本地内容和本地 SoundBank 生成记录来追踪 SoundBank 的状态。
- **Authoring/Data/Models/sfxclap.dat**- This file syncs the
  Similar Sound Search model in the Media Pool. This file is large and requires a
  lot memory and CPU for media analysis. The Media Pool can be used without
  Similar Sound Search. Exclude this file if you are not using Similar Sound
  Search with the Media Pool.

注意，在创建新的工程时会包含 .gitignore 和 .p4ignore 文件。下面有个示例 .gitignore 文件：

```
# Wwise
.backup*
.cache*
*.akd
*.prof
*.validationcache
*.wsettings
IncrementalSoundBankData.xml
```

您可以随时通过工程来生成 SoundBank。不过，若有不使用 Wwise 的团队成员，则其需要这些生成的文件来在开发当中试玩游戏时试听声音。借助版本控制系统，团队成员可以访问这些文件。若有不止一个 Wwise 用户将 SoundBank 添加到版本控制系统，这些文件可能会不同步。为了避免这种情况，请将所有.bnk 和 .wem 文件添加到 soundbanks/ 路径下。鉴于 Wwise 与游戏引擎的集成方式各不相同，可能还要添加 .txt、.xml 和 .json 文件。

工程中的大文件可能还要进行特别处理以便节省时间（比如使用 Git LFS）。通过 Git LFS 放在版本控制系统之外的文件可能包括大的二进制文件（如 .wav、.aif、.png 和 .jpg）。

在游戏的整个开发过程中，都可在 File Manager 中查看工程文件 (.wproj)、Work Unit 文件 (.wwu) 和音频文件的状态。若使用 Perforce、Subversion 或别的版本控制插件，则可直接在 Wwise 中执行版本控制功能。有关如何在 Wwise 中使用版本控制插件的详细信息，请参阅[“利用版本控制插件管理工程文件”一节](05-利用版本控制插件管理工程文件.md "利用版本控制插件管理工程文件")。

在默认情况下，Wwise 会在保存 Work Unit 文件、SoundBank 文件和某些工程文件时应用 LF 行结束符。Wwise 也可在保存时为其应用 CRLF 结束符。详见 Project Settings 的 [“General 选项卡”一节](../../09-参考主题/01-工程/08-Project-Settings/01-General-选项卡.md "General 选项卡")中的 **Line Ending**。

若您是团队的一员且使用版本控制系统来管理工程文件，请时刻留意有无其他成员在处理这一工程，以及是否存在可能需要解决的合并冲突。因此，经常同步和合并您的工作，并频繁与团队成员沟通交流您正在做的工作非常重要。有关经验总结的完整列表，请参阅[“Source control tips and best practices”一节](06-Source-control-tips-and-best-practices.md "Source control tips and best practices")。

---