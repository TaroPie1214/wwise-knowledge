# 在 Blueprint 中使用回调

|  |
| --- |
| Wwise Unreal Integration Documentation |

在 Blueprint 中使用回调

Blueprint 中暴露了 Event 回调。它们通过自定义 Event 实现。

# Event 回调

C++ 声音引擎 API 中暴露的大多数回调也会暴露给 Blueprint。如需详细了解各种回调类型的作用，请参阅 [SDK 文档](https://www.audiokinetic.com/library/edge/?source=SDK&id=_ak_callback_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html)。

|  |  |
| --- | --- |
|  | **注記：** 因为 Blueprint 流程图需要在游戏线程上执行，所以对于要求修改 `AkCallbackInfo` 结构（如 `AK_SpeakerVolumeMatrix` ）的回调，无法将其暴露给 Blueprint。请使用 C++ 代码来实现。 |

## 使用 Event 回调

在订阅 Event 回调之前，需要先在 `Callback Mask` 输入引脚下拉菜单中予以选择。然后，便可通过自定义 Blueprint Event，在回调函数中实现所要执行的 Blueprint 流程图。

![](../../../../images/UsingBlueprintCallbacks.png)

## 订阅多种回调类型

若要订阅多种回调类型，请在 `Callback Mask` 输入引脚下拉菜单中选择多个值。

![](../../../../images/UsingMultipleCallbacks.png)

接着，在 Custom Event 流程图中，便可针对 `Callback Type` 变量使用 Switch，来确定当前回调类型。然后，将 `Callback Info` 类转换为合适的类型。

![](../../../../images/UsingMultipleCallbacks_Graph.png)

## 使用 MIDI 回调

MIDI Event 回调信息类会依据当前 MIDI Event 类型转译成不同的内容。为了简化 MIDI 回调信息的解析，提供了 Blueprint 宏 `SwitchOnMidiType` 。它会自动解析回调信息对象，并触发正确的执行引脚：

![](../../../../images/UsingMIDICallbacks.png)

|  |  |
| --- | --- |
|  | **注記：** MIDI Callback Info 类的 `Chan` 成员指向 MIDI 声道。取值范围为 1 ~ 16。 |