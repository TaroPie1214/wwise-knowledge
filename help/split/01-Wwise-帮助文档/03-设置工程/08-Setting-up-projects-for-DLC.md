# Setting up projects for DLC

[Wwise 帮助文档](../00-Wwise-帮助文档.md) > [设置工程](00-设置工程.md) > Setting up projects for DLC

## Setting up projects for DLC

There are two important things to consider if you plan to add downloadable content (DLC) to
your game.

First, you need to manage your sound structures and media in such a way that one or more DLCs can be merged into the base game. Depending on the changes you make, you have to either repackage existing SoundBanks or add new ones. 有关详细信息，请参阅[“Requirements and best practices for DLC SoundBanks”一节](../07-完善工程/07-管理-SoundBank/08-SoundBank-相关技巧和窍门/01-Requirements-and-best-practices-for-DLC-SoundBanks.md "Requirements and best practices for DLC SoundBanks")。

Second, you need to plan for packaging so that DLC can be delivered separately from the base
game. Depending on the game engine you are using, packaging requirements and recommendations vary:

- If you are using the Wwise Unreal Integration or the Wwise Unity Integration, we
  recommend that you use the engine packaging options: bulk data packaging for Unreal, or
  Addressables for Unity. For more information, see [Packaging Wwise Assets as Bulk Data](https://www.audiokinetic.com/library/edge/?source=UE4&id=using_features_package_as_bulk_data.html) (Unreal) or [DLC Packaging Tutorial](https://www.audiokinetic.com/library/?source=Unity&id=pg_addressables_tutorial.html) (Unity).
- If you are using a different engine, you can use the Wwise File Packager, but make sure to follow the best practices for DLC. 有关详细信息，请参阅[“Packaging DLC files”一节](../07-完善工程/08-管理-File-Package/05-Packaging-DLC-files.md "Packaging DLC files")。

---