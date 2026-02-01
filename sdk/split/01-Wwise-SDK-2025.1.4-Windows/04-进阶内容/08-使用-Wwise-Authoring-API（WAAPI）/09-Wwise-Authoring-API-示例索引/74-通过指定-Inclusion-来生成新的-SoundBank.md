# 通过指定 Inclusion 来生成新的 SoundBank

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

通过指定 Inclusion 来生成新的 SoundBank

通过示例调用来导入并生成新的 SoundBank，但不会将 SoundBank 保存到工程中。See [ak.wwise.core.soundbank.generated](ak_wwise_core_soundbank_generated.html) to learn how to retrieve the SoundBank data.

# 函数 URI

[ak.wwise.core.soundbank.generate](ak_wwise_core_soundbank_generate.html)

# 参数

{

"soundbanks": [

{

"name": "SampleBank",

"events": [

"Event:Play\_Footsteps",

"Event:Play\_Music"

],

"auxBusses": [

"AuxBus:Cavern"

],

"inclusions": [

"event",

"structure",

"media"

]

}

],

"platforms": [

"Windows",

"Linux"

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。