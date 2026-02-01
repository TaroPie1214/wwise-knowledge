# 生成多个现有 SoundBank 而不将其写入到磁盘中

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

生成多个现有 SoundBank 而不将其写入到磁盘中

生成多个已存在于工程中的 SoundBank，并通过 WAAPI 对 SoundBank 数据进行流传输。See [ak.wwise.core.soundbank.generated](ak_wwise_core_soundbank_generated.html) to learn how to retrieve the SoundBank data.

# 函数 URI

[ak.wwise.core.soundbank.generate](ak_wwise_core_soundbank_generate.html)

# 参数

{

"soundbanks": [

{

"name": "SampleBank"

},

{

"name": "AnotherBank"

}

],

"platforms": [

"Windows",

"Linux"

],

"languages": [

"English(US)"

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。