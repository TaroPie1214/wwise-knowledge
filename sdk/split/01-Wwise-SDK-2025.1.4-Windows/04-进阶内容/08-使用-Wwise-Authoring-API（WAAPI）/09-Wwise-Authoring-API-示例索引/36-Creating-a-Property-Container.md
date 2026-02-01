# Creating a Property Container

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Creating a Property Container

在 Default Work Unit 下创建新的 'Guns' Virtual Folder。若已存在同名的文件夹，则自动命名为唯一名称。

# Function URI

[ak.wwise.core.object.create](ak_wwise_core_object_create.html)

# Arguments

{

"parent": "{a9129d80-07e0-11e7-93ae-92361f002671}",

"type": "PropertyContainer",

"name": "My Property Container"

}

# Result

{

"id": "{66666666-7777-8888-9999-AAAAAAAAAAAA}",

"name": "My Property Container"

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。