# Using Sidechain Mixes with Effects

[Wwise 帮助文档](../../00-Wwise-帮助文档.md) > [使用声音和振动来提升游戏体验](../00-使用声音和振动来提升游戏体验.md) > [管理效果器](00-管理效果器.md) > Using Sidechain Mixes with Effects

## Using Sidechain Mixes with Effects

You can use Wwise Sidechain Mixes to generate or use audio signals across the Containers and Busses hierarchies as a part of their runtime audio processing, in addition to other properties and the inline audio signals the Effects process.

For example, you can use a Sidechain Mix to ensure that audio for certain gameplay sound effects remains clearly audible even if there is a lot of ambient noise in your environment. In this case, you could configure your Busses and Effects in the following way:

1. Create an Audio Bus that combines all gameplay sound effects, and that has an Effect that send the combined audio signal to a Sidechain Mix.
2. Create a separate Audio Bus for the ambient noise, with an Effect that acts as a dynamic range compressor to reduce the ambient noise volume. Configure the Effect to read the audio signal from the Sidechain Mix to drive the compression.

With this type of configuration, the volume of the ambient noise decreases as the volume of the gameplay sound effects sent to the Sidechain Mix increases. Because you are using a Sidechain Mix, you can share the audio of the gameplay sound effects across the two Busses and Effects even though the Effects are not connected and the Busses are on different branches in the Busses hierarchy.

An alternative approach to side-chaining that uses Meters, RTPCs, and other Effects, is described in [“Using RTPCs to fine-tune the audio mix”一节](../../04-与游戏互动/05-使用-RTPC/08-Using-RTPCs-to-fine-tune-the-audio-mix.md "Using RTPCs to fine-tune the audio mix"). However, because Sidechain Mixes can share a complete audio signal across Effects, you can use them for methods of audio processing that are higher fidelity, richer, or more complex than methods that use RTPCs alone.

Compared to RTPCs, Effects that support Sidechain Mixes can benefit in several ways:

- Improved precision in time, because Effects can read per-sample audio data instead of one parameter for an entire audio processing pass
- Measurement of the full audio spectrum of a signal, instead of just a peak amplitude.
- Ability to read multiple channels of audio data, instead of a single data point.

Each Effect defines its own behavior and support for Sidechain Mixes, and Effects can
generate or use Sidechain Mixes in different ways. For information about how individual
Effects work with Sidechain Mixes, refer to each Effect’s respective
documentation.

The following built-in Wwise Effects support Sidechain Mixes:

- [“Sidechain Send”一节](../../10-Wwise-插件/04-效果器插件/22-Sidechain-Send.md "Sidechain Send")
- [“Sidechain Receive”一节](../../10-Wwise-插件/04-效果器插件/21-Sidechain-Receive.md "Sidechain Receive")
- [“Compressor（压缩器）”一节](../../10-Wwise-插件/04-效果器插件/04-Compressor（压缩器）.md "Compressor（压缩器）")
- [“扩展器（Expander）”一节](../../10-Wwise-插件/04-效果器插件/06-扩展器（Expander）.md "扩展器（Expander）")
- [“Parametric EQ（参数均衡器）”一节](../../10-Wwise-插件/04-效果器插件/14-Parametric-EQ（参数均衡器）.md "Parametric EQ（参数均衡器）")

### Creating a Sidechain Mix ShareSet

Multiple Sidechain Mixes can be active at one time. Sidechain Mix ShareSets provide unique identification that Effects use to send audio to or receive audio from the correct Sidechain Mix. Each Sidechain Mix ShareSet can be created in your Wwise Project in the Project Explorer, or via the Property Editor or other Views wherever Sidechain Mixes are used by Effects.

To create a Sidechain Mix ShareSet:

- 执行以下操作之一：

  - In the ShareSets tab in the Project Explorer, select a Work Unit
    and click Create new Sidechain Mix.
  - In the Property Editor of an Effect that supports Sidechain Mixes,
    locate the Sidechain Mix area and click the Selector button [>>],
    then click New.

  A Sidechain Mix ShareSet is created in the Sidechain Mixes hierarchy.

### Configuring Sidechain Mixes

You can select the channel configuration of the Sidechain Mix. Although Sidechain Mixes do not require very many CPU and memory resources, we recommend a small channel configuration to minimize resource usage. A 1.0 signal is sufficient in most cases, unless you are using an Effect that benefits from a wider channel configuration.

It is also possible for the channel configuration of a Sidechain Mix to match the configuration of the Primary Output Device. The “Same as Primary Main Mix” and “Same as Primary Passthrough Mix” options are similar to the “Same as Main Mix” and “Same as Passthrough Mix” options available on Busses. The difference is that the Sidechain Mix specifically refers to the Primary Output Device to determine its configuration:

- “Same as Primary Main Mix” uses the channel configuration of the Main Mix of the Primary Output Device.
- “Same as Primary Passthrough Mix” uses the channel configuration of the Passthrough Mix of the Primary Output Device. If the Primary Output Device does not have a Passthrough Mix, then the Primary Output Device’s Main Mix channel configuration is used instead.

Sidechain Mixes operate independently of the Busses hierarchy, so it is not possible for a Sidechain Mix to mimic the configuration of a specific Bus, such as when a Bus uses a configuration of “Same as Parent”.

The Sidechain Mix view includes a Meter. When remotely connected to a Wwise runtime, the Meter displays the peaks of the monitored Sidechain Mix.

Sidechain Mixes do not support an Audio Objects channel configuration: a Sidechain Mix is always defined as only one multi-channel audio signal. When multiple audio signals contribute to a Sidechain Mix, they are always mixed together into one signal.

### Sending Audio to a Sidechain Mix

Audio for Sidechain Mixes must first be generated by an Effect. The “Sidechain Send” Effect is the only Effect provided by default in Wwise that generates audio data for Sidechain Mixes. However, it is possible for other Effect plug-ins by third-party developers to generate audio data as well.

The Sidechain Send Effect performs the following:

1. Reads any audio signal being input to the Effect.
2. Downmixes the audio signal to match the channel configuration of the specified Sidechain Mix Destination and applies the specified volume change.
3. Sends the downmixed audio directly to the Sidechain Mix.
4. Sends the input audio signal to the output audio signal without any data modification.

If multiple Effects send audio signals to a Sidechain Mix, all of the audio signals are
mixed together. In this way, multiple Effects that contribute to a single Sidechain
Mix can be active across the voice graph, instead of multiple Aux Bus connections
from many separate Audio Busses to a single Bus.

It is also possible to use this Effect to direct the audio used for a certain part of your
mix directly to a Sidechain Mix, without having to first send the audio to a
separate Bus. However, the Sidechain Send Effect is not an Object Processor, and if
the Sidechain Mix has a multi-channel configuration, the Effect might not correctly
mix down audio objects with positioning data to the destination Sidechain Mix.
Therefore, it is not recommended to use the Sidechain Send Effect on a Bus that
might operate in an Audio Objects configuration.

有关详细信息，请参阅[“Sidechain Send”一节](../../10-Wwise-插件/04-效果器插件/22-Sidechain-Send.md "Sidechain Send")。

### Receiving Audio from a Sidechain Mix

After audio is sent to a Sidechain Mix, another Effect can then receive the Sidechain Mix as a part of its processing.

The "Sidechain Receive" Effect fetches a Sidechain Mix’s audio signal and uses it as the
output audio for an Effect. The Sidechain Receive Effect performs the following:

1. Receives a Sidechain Mix audio signal.
2. Upmixes the Sidechain Mix to match the intended channel configuration
   of the Effect.
3. Replaces the input audio signal of the Effect with the upmixed audio
   from the Sidechain Mix.

The Sidechain Receive Effect is intended to be used for inspecting and debugging a Sidechain Mix. For example, you can use it to easily monitor the result of a given Sidechain Mix, instead of as a component of a full audio mix.

For more information, see [“Sidechain Receive”一节](../../10-Wwise-插件/04-效果器插件/21-Sidechain-Receive.md "Sidechain Receive")

The Compressor, Expander, and Parametric EQ Effects can also receive a Sidechain Mix signal
as a part of their processing.

When no Sidechain Mix is specified as a Sidechain Input, the Compressor, Expander, and
Parametric EQ Effects use the input audio signal for the analysis of any dynamics
involved in the execution of the effect. However, when a Sidechain Mix is specified
as a Sidechain Input, the Sidechain Mix audio signal is used for the analysis of any
dynamics involved in the execution of the Effect.

In this way, a Compressor can use a Sidechain Mix generated from one part of the Busses
hierarchy to duck the audio of another part of the hierarchy instead of compressing
the dynamic range of the input audio signal by itself.

For more information, see [“Compressor（压缩器）”一节](../../10-Wwise-插件/04-效果器插件/04-Compressor（压缩器）.md "Compressor（压缩器）"), [“扩展器（Expander）”一节](../../10-Wwise-插件/04-效果器插件/06-扩展器（Expander）.md "扩展器（Expander）"), and [“Parametric EQ（参数均衡器）”一节](../../10-Wwise-插件/04-效果器插件/14-Parametric-EQ（参数均衡器）.md "Parametric EQ（参数均衡器）").

### Sidechain Mix Scopes

When Effects send audio to a Sidechain Mix or receive audio from a Sidechain Mix, the
Effects must specify what Sidechain Mix to send to or read from. However, an Effect
must also specify the Scope of a Sidechain Mix. Scopes are IDs for the Sidechain Mix
system that allow for the same Sidechain Mix definition to be used across multiple
scenarios simultaneously with mutually exclusive audio. Typically, Scope IDs
correspond to Game Object IDs. You can use Scopes in combination with Wwise Effects
to restrict Sidechain Mix audio signals to specific Listener Game Objects, as
required in some multiplayer audio environments. For the Sidechain Send, Sidechain
Receive, Compressor, Expander, and Parametric EQ Effects, you can do this by setting
the Scope on the Effect to “Game Object” instead of “Global”.

### Sidechain Mix Delay

The Sidechain Mix system makes it possible for any Effect on any Bus to both send audio data to, and receive audio data from, a Sidechain Mix. Although the Sidechain Mix system is flexible, it does include a disadvantage in the form of a slight delay when receiving audio from a Sidechain mix. The delay has a duration of a single audio rendering pass in Wwise, or approximately 10.6 ms by default, although the exact duration might be different if your sound engine execution is configured with a different number of samples per frame.

In most cases, the delay is not a major problem. However, if there is extremely tight synchronization between sending and receiving Sidechain Mix audio data, the delay might be noticeable.

In music production, for example, you can use the sound of a kick drum to instantaneously duck another bass instrument on the track. To do so, you can send the sound of the kick drum to a Sidechain Mix, use a separate Compressor Effect on the bass instrument to read the audio signal from the Sidechain Mix, and set the attack to 1 millisecond. However, because of the delay before the Compressor Effect receives the Sidechain Mix, the attack for the bass instrument is effectively delayed by 10.6 milliseconds, which might cause the two instruments to overlap.

In such cases, you can compensate for the delay in different ways. 例如：

- Enable the "Delay output" property on the Sidechain Send Effect, which delays its output audio signal by one audio rendering pass. The output audio of the Effect can then be synchronized with any other Effect that receives audio from the same Sidechain Mix. However, be careful if you are working with content that requires low-latency audio playback, such as sound effects that are critical for user interaction and gameplay, or if the same audio is used for multiple Sidechain Send Effects in serial order.
- Depending on the situation, you could add another sound to compensate. In the example above, you could use a Tone Generator to create a loud noise just before or at the same time as the kick drum plays, send it exclusively to a Sidechain Mix, and then mute it before it is sent to any downstream Audio Bus. In this way, the additional instrument lowers the volume of the bass instrument, although the kick drum plays simultaneously.

---