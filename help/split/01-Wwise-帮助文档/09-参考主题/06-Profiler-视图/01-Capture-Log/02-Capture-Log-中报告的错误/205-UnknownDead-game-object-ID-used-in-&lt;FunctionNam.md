# Unknown/Dead game object ID used in &lt;FunctionName&gt;. Make sure the game object is registered before using it and do not use it once it was unregistered.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > Unknown/Dead game object ID used in <FunctionName>. Make sure the game object is registered before using it and do not use it once it was unregistered.

#### Unknown/Dead game object ID used in <FunctionName>. Make sure the game object is registered before using it and do not use it once it was unregistered.

“<FunctionName> 中使用了未知/非活动游戏对象 ID。确保在使用前注册游戏对象，一旦注销了就不要再使用它。”对于需要 Game Object ID（游戏对象 ID）的 API 函数，如果使用无法识别的 ID 来调用，将出现此错误。提供了函数的名称，以便查找游戏代码。若某 Game Object 曾经活跃，则将其标记为 Dead Game Object（非活动游戏对象），同时在 Game Object 列中显示对象的原有名称。Game Object 的生存期从 [`AK::SoundEngine::RegisterGameObj`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html) 开始到 [`AK::SoundEngine::UnregisterGameObj`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_af53445c959103c84ea50c17d665f254a.html) 结束。若在这些调用之前或之后执行函数调用，则将发生此错误。

请注意，以下调用序列是合法的：  
  `AK::SoundEngine::RegisterGameObj(MyGameObjID);   
 AK::SoundEngine::PostEvent("Play_MySound", MyGameObjID);   
 AK::SoundEngine::UnregisterGameObj(MyGameObjID);`

|  |  |
| --- | --- |
| [备注] | 备注 |
| If you are using the Unity game engine, the lifetime of a Wwise Game Object follows the lifetime of the `AkGameObj` component. |

**可能的原因：**

- 在函数调用前从未注册 Game Object。
- 在函数调用前已注销 Game Object。
- Game Object ID 损坏。
- Unity 用户：Script Execution Order（脚本执行顺序）可能有误，导致出现以上情况之一。

**推荐的解决步骤：**

- 打开 [Profiler Settings](../../../01-工程/10-Profiler-Settings.md "Profiler Settings")（性能分析器设置），并启用 **API Calls**（API 调用）。然后，重现场景。在 Capture Log（捕获日志）中，该错误之前应显示出现问题的调用及所有参数。
- 在 Game Object 3D Viewer（游戏对象 3D 查看器）视图中，确认 Game Object 的生存期。
- 更改函数调用顺序，使其介于相关的 `RegisterGameObj` 和 `UnregisterGameObj` 之间。
- Unity 用户：查看 Unity 中的 Script Execution Order（脚本执行顺序）。

**另请参阅：**

- [`AK::SoundEngine::RegisterGameObj()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html)
- [`AK::SoundEngine::UnregisterGameObj()`](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_af53445c959103c84ea50c17d665f254a.html)
- [AkGameObj 类引用](https://www.audiokinetic.com/library/edge/?source=Unity&id=class_ak_game_obj.html)

---