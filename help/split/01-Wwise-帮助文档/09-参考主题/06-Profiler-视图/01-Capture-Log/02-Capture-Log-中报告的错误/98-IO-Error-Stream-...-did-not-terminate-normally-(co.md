# I/O Error: Stream ... did not terminate normally (code ...). Memory leak detected.

[Wwise 帮助文档](../../../../00-Wwise-帮助文档.md) > [参考主题](../../../00-参考主题.md) > [Profiler 视图](../../00-Profiler-视图.md) > [Capture Log](../00-Capture-Log.md) > [Capture Log 中报告的错误](00-Capture-Log-中报告的错误.md) > I/O Error: Stream ... did not terminate normally (code ...). Memory leak detected.

#### I/O Error: Stream ... did not terminate normally (code ...). Memory leak detected.

This error happens when terminating the sound engine if there are streamed files that are still expecting transfers from the Low Level I/O systems.
This is a programming error that can happen if the game has a custom Low Level I/O implementing the IAkLowLevelIOHook interface. If your game does not have a custom I/O hook, or it uses Unreal or Unity, please contact Audiokinetic Support.

**可能的原因：**

- A call to [`AK::StreamMgr::IAkLowLevelIOHook::BatchRead`](https://www.audiokinetic.com/library/edge/?source=SDK&id=class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a9bc325405bc17c0a5105d0a53981b186.html) or [`AK::StreamMgr::IAkLowLevelIOHook::BatchWrite`](https://www.audiokinetic.com/library/edge/?source=SDK&id=class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a8f5041a24e395784437a62cdd2140505.html) did not answer all required transfers by calling in\_pTransferItems[i]->pTransferInfo->pCallback().
  All transfers must be answered by exactly one call, either when the operation completes successfully or an error is detected. If a transfer is not answered, that stream occupies one I/O slot until the game is terminated.
- An internal bug in the Wwise Stream Manager. Please contact Audiokinetic Support.

---