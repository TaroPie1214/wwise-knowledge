# 针对多个平台和输出路径对 External Source 进行转码

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

针对多个平台和输出路径对 External Source 进行转码

按照给定的各个 wsources 文件在可选和默认输出路径针对多个平台对 External Source 进行转码。

# 函数 URI

[ak.wwise.core.soundbank.convertExternalSources](ak_wwise_core_soundbank_convertexternalsources.html)

# 参数

{

"sources": [

{

"input": "C:\\My-Wsources\\sources1.wsources",

"platform": "Windows"

},

{

"input": "C:\\My-Wsources\\sources2.wsources",

"platform": "{6E0CB257-C6C8-4C5C-8366-2740DFC441EC}",

"output": "C:\\ExternalSources-Alternate\\Windows"

},

{

"input": "C:\\My-Wsources\\sources1.wsources",

"platform": "Linux",

"output": "C:\\ExternalSources-Alternate\\Linux"

}

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。