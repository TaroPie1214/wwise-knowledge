# 效果器 – SoundBank 管理

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../00-使用声音和振动来提升游戏体验.md) > [管理效果器](00-管理效果器.md) > 效果器 – SoundBank 管理

## 效果器 – SoundBank 管理

效果器必须打包到 SoundBank 中并由游戏加载。如何将效果器打包到 SoundBank 中取决于其本身的用法。

- **Containers hierarchy:** Any SoundBank that packages an object in the Containers hierarchy also packages all Effects used by that object, unless specifically excluded in the SoundBank Editor.
- **Busses hierarchy:** Effects used by objects in the Busses hierarchy (Busses, Auxiliary Busses) are packaged in the Init SoundBank.
- **Devices hierarchy:** Effects used by Audio Device objects are packaged in the Init SoundBank.

|  |  |
| --- | --- |
| [备注] | 备注 |
| 在生成 SoundBank 的过程中，Wwise 会自动生成 Init SoundBank。 |

Although Busses and Audio Device Effects are automatically added to the Init SoundBank, some Effects, or parts of Effects, are not. 以下条目不会自动添加到 Init SoundBank：

- **效果器媒体：**Init SoundBank 不会打包任何媒体文件。效果器媒体必须打包到 User-defined SoundBank 并在使用效果器之前由游戏加载。
- **Effects loaded at runtime:** Your game can make use of the
  SDK functions to change a Bus or Audio Device effect at runtime. If the Effect
  to be loaded is in use by your project during SoundBank generation (that is,
  referred to by a Bus, Auxiliary Bus, or Audio Device) then it will be packaged
  in the Init SoundBank. Otherwise, the Effect must be packaged in a user-defined
  SoundBank and loaded by the game prior to being used.

有关 SoundBank 管理的详细信息，请参阅“[*管理 SoundBank*](../../07-完善工程/07-管理-SoundBank/00-管理-SoundBank.md "管理 SoundBank")”章节。

---