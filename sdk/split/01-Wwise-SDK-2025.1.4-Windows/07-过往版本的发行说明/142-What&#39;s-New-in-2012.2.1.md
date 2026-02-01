# What&#39;s New in 2012.2.1

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

What's New in 2012.2.1

2012.2.1 属于补丁发布. The following sections list and describe the changes made to Wwise between version 2012.2 and version 2012.2.1.

# Important behavior change

- **WG-21660** Fixed: WiiU output is twice too loud (+6dB). The output gain of the WiiU was mistakenly set to 2x for a long time. This can cause the output to clip or distort even if your project uses a Peak Limiter or the ML1 limiter. This patch brings the gain to 1 (i.e. no gain), therefore you might need to adjust your bus volumes up to compensate.

# Platform SDK changes

- Wii U: Cafe SDK 2.07.03 Patch 5

# Optimizations

- **WG-21544** Optimize Auxiliary send bus creation system to not create auxiliary busses when the send level is under the volume threshold.
- **WG-21583** Improved performance of 3d positioning calculations.
- **WG-21597** (XBox only) Tuning of compiler optimization flags.

# 漏洞修复

- **WG-21327** Fixed: (VitaHW) Wrong seek behavior when using "Seek" action.
- **WG-21467** Fixed: (Mac) AAC decoder crash on OS X Lion.
- **WG-21506** Fixed: (WiiU) AkIOThread m\_hIOThread member doesn't respect 8 byte alignment. Makes WiiU crash if IO thread is restarted.
- **WG-21507** Fixed: (WiiU) Use the hardware setting for the audio config of the DRC. Support Mono output on TV.
- **WG-21508** Fixed: (WiiU) Crash in deferred IO for WiiU.
- **WG-21517** Fixed: (VitaHW) Too many markers notifications triggered.
- **WG-21543** Fixed: (WiiU) Link warnings with WiiU compiler.
- **WG-21553** Fixed: (VitaHW) Aux bus volume are not updated while sounds are playing.
- **WG-21555** Fixed: (WiiU) Network cannot be reinitialized.
- **WG-21558** Fixed: (WiiU) Resampling algorithm doesn't interpolate on the Right channel (but does on the Left!). Noise is induced.
- **WG-21570** Fixed: Tooltips are not behaving properly in Wwise Authoring on Windows 8.
- **WG-21573** Fixed: Stereo delay channel crossfeed results in unstable feedback.
- **WG-21596** Fixed: (WiiU) DRC Virtual Surround mode always process 6 channels, even when the game doesn't support it.
- **WG-21632** Fixed: (WiiU) Race condion when switching to background. One audio frame might still be processed causing crash in Roomverb.
- **WG-21639** Fixed: (WiiU) Can't rumble on all Wiimotes when the DRC is connected.
- **WG-21640** Fixed: (WiiU) Hang on exit when using the power button on WiiU.
- **WG-21660** Fixed: (WiiU) Output is twice too loud (+6dB).
- **WG-21667** Fixed: (WiiU) Deadlock triggered by CPU starvation.
- **WG-21716** Fixed: (WiiU) Race condition on initialisation of AX voices and AX Callback.
- **WG-21736** Fixed: (32 bit Windows and Mac) Silent output (NaN) in rare cases.
- **WG-21738** Fixed: NaNs in volume computation when using 2D positioning RTPC with some interpolation curves. Output is silent.
- **WG-21741** Fixed: NaN created in 3D User Defined positioning code, when multiple listener used, with No Follow Listener. Output is silent.