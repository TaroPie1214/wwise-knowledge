# Changing Mastering Suite in game

[Wwise 帮助文档](../../../00-Wwise-帮助文档.md) > [Wwise 插件](../../00-Wwise-插件.md) > [Audio Device 效果器插件](../00-Audio-Device-效果器插件.md) > [Mastering Suite](00-Mastering-Suite.md) > Changing Mastering Suite in game

### Changing Mastering Suite in game

允许在游戏正在运行的时候动态更改 Mastering Suite。用户可添加、移除或替换 Mastering Suite ShareSet。不过，必须满足以下条件：

- **已经注册插件**：可在游戏代码中注册 Mastering Suite 插件。有关详细信息，请参阅[集成详情 – 插件](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_integration_plugins.html)。
- **已经加载 ShareSet**：必须在加载的 SoundBank 中创建 Mastering Suite ShareSet。若被 SoundBank 中的另一条目引用或将 ShareSet 以显式方式添加到了 SoundBank 中，则会将 Mastering Suite ShareSet 包含在 SoundBank 中。

若要在运行时更改 Mastering Suite ShareSet，最好的方法是使用 "Set Effect" Event Action。有关更多详细信息，请参阅“[“Event Action 列表”一节](../../../09-参考主题/04-Project-Explorer/02-Events-选项卡/01-Event-Editor/01-Event-Action-列表.md#event_action_set_effect)”。目标 Effect ShareSet 将自动打包到与 Event 相同的 SoundBank 中。

另外，还可通过调用 SDK 函数 [`SetOutputDeviceEffect`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_ad455f291883c352a87b5b03da64549aa.html) 来以编程方式更改 ShareSet。为此，须将每个要指派的 Mastering Suite ShareSet 手动添加到 SoundBank 并确保在发布调用前进行加载。

为了避免出现毛刺噪声，强烈建议不要在添加/移除了 Mastering Suite 的 Output Device 上播放声音。

---