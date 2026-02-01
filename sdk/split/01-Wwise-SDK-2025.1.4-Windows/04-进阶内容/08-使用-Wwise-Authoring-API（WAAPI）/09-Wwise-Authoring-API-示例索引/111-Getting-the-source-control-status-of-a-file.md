# Getting the source control status of a file

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Getting the source control status of a file

Returns the source control status and owner of the file.

# 函数 URI

[ak.wwise.core.sourceControl.getStatus](ak_wwise_core_sourcecontrol_getstatus.html)

# 参数

{

"files": [

"//projet-file//Originals/SFX/existingFile.wav"

]

}

# 结果

{

"result": [

{

"owner": "user",

"status": "add"

}

],

"log": []

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。