# 通过指定 Inclusion 来在磁盘上生成新的 SoundBank

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

通过指定 Inclusion 来在磁盘上生成新的 SoundBank

导入并生成新的 SoundBank，然后将其写入到磁盘上的 SoundBank 生成文件夹。

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

],

"rebuild": true

}

],

"platforms": [

"Windows",

"Linux"

],

"clearAudioFileCache": true,

"writeToDisk": true

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。