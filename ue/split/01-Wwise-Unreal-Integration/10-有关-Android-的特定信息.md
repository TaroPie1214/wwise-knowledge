# 有关 Android 的特定信息

|  |
| --- |
| Wwise Unreal Integration Documentation |

有关 Android 的特定信息

此页面列出了在开发者针对 Android 使用 Unreal Integration 构建应用程序时的相关要求及特别注意事项。

# 升级到 Unreal 4.25 或更高版本

- Unreal Engine 4.25 中对 Android 工具链进行了改进。若要从较早版本迁移到 Unreal 4.25 或更高版本，必须更改 `ThirdParty` 文件夹内的 Android SDK 文件夹层级结构。为此，请按照说明将以下文件夹移动到 `Android` 文件夹中并相应地进行重命名：
  - 将 `Android_armeabi-v7a` 移动到 `Android/armeabi-v7a` 并重命名
  - 将 `Android_arm64-v8a` 移动到 `Android/arm64-v8a` 并重命名
  - 将 `Android_x86` 移动到 `Android/x86` 并重命名
  - 将 `Android_x86_64` 移动到 `Android/x86_64` 并重命名