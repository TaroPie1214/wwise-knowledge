# Generating a short sine tone WAV file

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Generating a short sine tone WAV file

Generates a 1 second mono WAV file that contains a sine waveform, with a very short attack and release.

# 函数 URI

[ak.wwise.debug.generateToneWAV](ak_wwise_debug_generatetonewav.html)

# 参数

{

"path": "C:\\WAV\\beep.wav",

"channelConfig": "1.0",

"waveform": "sine",

"frequency": 800,

"attackTime": 0.01,

"sustainTime": 0.98,

"releaseTime": 0.01,

"sustainLevel": 0

}

# 选项

{}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。