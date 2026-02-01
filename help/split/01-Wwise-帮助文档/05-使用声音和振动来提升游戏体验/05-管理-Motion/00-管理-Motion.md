# 管理 Motion

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../00-使用声音和振动来提升游戏体验.md) > 管理 Motion

## 管理 Motion

为了使游戏更有代入感，最好添加某种振动反馈。

Wwise 为在游戏中创建和集成振动提供了一套完整的管线。Wwise 为振动实现了全面的、与音频创作相似的管线解决方案，您可以实现以下功能：

- 只需稍加学习，就可以创建复杂、真实的振动效果。
- 将振动轻松集成至游戏内，不会明显影响游戏或声音引擎的表现。
- 使用与音频相同的功能来构建和集成振动。
- 无需额外工作，为各种平台上的同类设备创建振动效果。
- 根据游戏要求，轻松添加或移除振动元素。

## 了解 Wwise 中振动的工作方式

为了尽可能简单地从音频过渡至振动，Wwise 使用相同的工作流程，很多原理和功能都同时适用于两者。与音频类似，振动对象可以在层级结构中进行组织、可输出至总线，并可使用事件在游戏中触发。同时，还可在 3D 空间化环境中定位，由工程中的各种游戏同步器控制，并打包到 SoundBank（音频包）中。播放方面的主要区别在于，振动是通过游戏控制器而非扬声器播放的。

## 支持的振动设备

For a list of supported motion devices, see the Game Setup section in the [Integrating Wwise Motion](https://www.audiokinetic.com/library/edge/?source=SDK&id=integrating_elements_motion.html) topic in the Wwise SDK.

You can connect to other device types if you install other third-party plug-ins for
motion.

## High-level workflow for creating motion

The table below is a high-level workflow for generating motion for the first
time.

| Step | 描述 |
| --- | --- |
| Step 1. Integrate Wwise Motion | See [Integrating Wwise Motion](https://www.audiokinetic.com/library/edge/?source=SDK&id=integrating_elements_motion.html) in the Wwise SDK documentation and [“Prerequisites for creating motion”一节](03-为游戏创建振动效果/00-为游戏创建振动效果.md#motion_prerequisites "Prerequisites for creating motion"). |
| Step 2. Install the Wwise Motion source plug-in. | From the Audiokinetic Launcher, install the Wwise Motion source plug-in. 请参阅 [“Prerequisites for creating motion”一节](03-为游戏创建振动效果/00-为游戏创建振动效果.md#motion_prerequisites "Prerequisites for creating motion")。 |
| Step 3. Add a device to the Project Explorer. | Add a device to the Devices Default Work Unit in the Project Explorer Audio tab. See [“Audio Devices”一节](../../09-参考主题/04-Project-Explorer/01-Audio-tab/01-Audio-Devices/00-Audio-Devices.md "Audio Devices") and [“为游戏控制器生成振动效果”一节](03-为游戏创建振动效果/03-创建专用对象来生成振动效果/01-为游戏控制器生成振动效果.md "为游戏控制器生成振动效果"). |
| Step 4. Create a Motion Bus. | Create an Audio Bus and in the Audio Device field select the motion device you added in the previous step. See [*建立输出总线的结构*](../../03-设置工程/07-建立输出总线的结构/00-建立输出总线的结构.md "建立输出总线的结构") and [“Adding a Motion Bus to a Wwise Project”一节](02-Adding-a-Motion-Bus-to-a-Wwise-Project.md "Adding a Motion Bus to a Wwise Project"). |
| Step 5. Decide what type of object you will use to generate motion. | You can create motion from existing sounds or by creating a motion-specific object. 参阅：  - [“使用现有音频信号生成振动信号”一节](01-生成振动效果的方法.md#generating_motion_source_from_an_existing_audio_signal "使用现有音频信号生成振动信号") - [“Generating motion from a motion-specific source”一节](01-生成振动效果的方法.md#generating_motion_using_motion_fx_object "Generating motion from a motion-specific source") |
| Step 6. Filter out high frequencies. | If you are generating sound from existing audio files, filter out high frequencies and boost or reduce the generated motion signal. 请参阅 [“调节由音频生成的振动信号”一节](03-为游戏创建振动效果/01-通过现有声音生成振动效果.md#boosting_reducing_motion_signal "调节由音频生成的振动信号")。 |

---