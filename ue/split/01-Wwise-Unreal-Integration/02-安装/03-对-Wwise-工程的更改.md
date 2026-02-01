# 对 Wwise 工程的更改

|  |
| --- |
| Wwise Unreal Integration Documentation |

对 Wwise 工程的更改

在集成 Wwise 后首次打开 Unreal 工程时，若之前做了不同的设定，则 Wwise 工程中的某些设置会发生变化。

在打开 SoundBank Settings (**Project > Project Settings > SoundBanks**) 时，可以看到启用了以下设置：

- Copy Loose/Streamed Media
- Remove Unused Generated Files
- Generate Per Bank Metadata File（有可能同时启用 Generate All Banks Metadata File）
- Generate JSON Metadata
- Include in Metadata：
  - Object GUID
  - Object Path
  - Max Attenuation（强烈推荐）
  - Estimated Duration（强烈推荐）

![](../../../images/sbs_newproject.png)

在打开 **Project > Project Settings > Logs** 时，可以看到禁用了以下设置：

- Media is duplicated in several SoundBanks
- Media not found in any SoundBank