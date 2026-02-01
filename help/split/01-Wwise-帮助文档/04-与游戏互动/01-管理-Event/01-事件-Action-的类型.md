# 事件 Action 的类型

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [与游戏互动](../00-与游戏互动.md) > [管理 Event](00-管理-Event.md) > 事件 Action 的类型

## 事件 Action 的类型

Wwise 自带多种动作（Action），这些动作可用于驱动游戏中声音、音乐和振动。动作按类别进行分组，每个类别都包含一系列供您选择的动作。

![](../../../../images/Event_actions_list.png)

每个动作还有一组属性（例如延迟和淡变），可用于更好地管理输入和输出的对象。下表介绍了所有的事件动作。

|  |  |
| --- | --- |
| [备注] | 备注 |
| 以下为一般描述，没有考虑每个 Action 的 Scope 设置。Scope 可以是 Game Object 或 Global，用于指定存在多个游戏对象时，动作的作用范围。 |

| 事件动作类型 | 描述 |
| --- | --- |
| Empty Event | 不包含动作或对象。 |
| Play | 播放关联对象。 |
| Stop > Stop | 停止播放关联对象。 |
| Stop > Stop All | 停止所有对象的播放，但可以添加例外。 |
| Pause > Pause | 暂停关联对象的播放。 |
| Pause > Pause All | 停止所有对象的播放，但可以添加例外。 |
| Resume > Resume | 恢复播放之前暂停了的关联对象。 |
| Resume > Resume All | 恢复所有暂停对象的播放，但可以添加例外。 |
| Break | 停止播放循环声音或连续容器，同时允许当前对象完成播放。 |
| Seek > Seek | 更改关联 Wwise 对象的播放位置。此操作不会影响当前未播放的对象。 |
| Seek > Seek All | 更改所有 Wwise 对象的播放位置，但可以添加例外。此操作不会影响当前未播放的对象。 |
| Post Event | 从事件内触发别的事件。 |
| Bus Volume > Set Voice Volume | 更改关联总线的音量电平。 |
| Bus Volume > Reset Volume | 将关联总线的音量复位至其原始电平。 |
| Bus Volume > Reset Volume All | 将所有总线的音量复位至其原始值，但可以添加例外。 |
| Voice Volume > Set Voice Volume | 更改关联对象的音量电平。 |
| Voice Volume > Reset Volume | 将关联对象的音量恢复至其原始电平。 |
| Voice Volume > Reset Volume All | 将所有对象的音量复位至其原始值，但可以添加例外。 |
| Voice Pitch > Set Voice Pitch | 更改关联对象的音高。 |
| Voice Pitch > Reset Pitch | 重置音高，将关联对象的音高复位至其原始值。 |
| Voice Pitch > Reset Voice Pitch All | 将所有对象的音高复位至其原始值，但可添加例外。 |
| Voice Low-pass Filter > Set Voice Low-pass Filter | 更改作用于关联 Wwise 对象的低通滤波器效果量。 |
| Voice Low-pass Filter > Reset Voice Low-pass Filter | 将作用于关联 Wwise 对象的低通滤波器效果量复位至其原始值。 |
| Voice Low-pass Filter > Reset Voice Low-pass Filter All | 将所有 Wwise 对象的 Low-Pass Filter 复位至其原始值，但可以添加例外。 |
| Voice High-pass Filter > Set Voice High-pass Filter | 更改应用于关联 Wwise 对象的高通滤波器数量。 |
| Voice High-pass Filter > Reset Voice High-pass Filter | 将应用于关联 Wwise 对象的高通滤波器恢复至其原始值。 |
| Voice High-pass Filter > Reset Voice High-pass Filter All | 将所有 Wwise 对象的 High-Pass Filter 复位至其原始值，但可以添加例外。 |
| Mute > Mute | 将关联对象静音。 |
| Mute > Unmute | 将关联对象恢复为其原始“静音前”音量电平。 |
| Mute > Unmute All | 将所有对象复位至静音前的原始电平，但可以添加例外。 |
| Game Parameter > Set Game Parameter | 更改游戏参数值。 |
| Game Parameter > Reset Game Parameter | 恢复游戏参数的原始值。 |
| States > Set State | 激活特定状态。 |
| States > Enable State | 在应用 Disable State Action 后，为相关 Wwise 对象重新启用 State。 |
| States > Disable State | 为关联 Wwise 对象禁用状态。 |
| Set Switch | 激活特定切换开关。 |
| Trigger （触发器） | 调用 Trigger，以启动 Stinger。 |
| Bypass Effect > Enable Bypass | 旁通作用于关联 Wwise 对象的效果器。 |
| Bypass Effect > Disable Bypass | 删除效果器旁通会将效果器重新作用于关联 Wwise 对象。 |
| Bypass Effect > Reset Bypass Effect | 重置旁通效果器。将关联对象的旁通效果器选项复位至其原始设置。 |
| Bypass Effect > Reset Bypass Effect All） | 将所有 Wwise 对象的旁通效果选项复位至其原始值，但可以添加例外。 |
| Release Envelope | 释放与 Wwise 对象关联的包络。 |
| Reset Playlist | 将指定随机容器/序列容器的播放列表重置为初始状态。这不会影响连续模式播放，也不会影响当前播放的声音。 |
| Set Effect > Set Effect | 设置效果器。覆盖指派给 Wwise 对象上的单个效果器插槽的效果器。 |
| Set Effect > Reset Effect | 重置“设置效果器”。将被 "Set Effect" Action 覆盖的某个对象的给定效果器插槽重置。 |
| Set Effect > Reset Set Effect All | 重置所有“设置效果器”。将被 "Set Effect" Action 覆盖的所有对象的给定效果器插槽重置。 |

---