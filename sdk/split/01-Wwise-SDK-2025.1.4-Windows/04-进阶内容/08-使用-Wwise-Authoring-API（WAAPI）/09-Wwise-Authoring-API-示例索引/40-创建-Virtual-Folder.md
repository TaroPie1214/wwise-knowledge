# 创建 Virtual Folder

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

创建 Virtual Folder

在 Default Work Unit 下创建新的 'Guns' Virtual Folder。若已存在同名的文件夹，则自动命名为唯一名称。

# 函数 URI

[ak.wwise.core.object.create](ak_wwise_core_object_create.html)

# 参数

{

"parent": "\\Containers\\Default Work Unit",

"type": "Folder",

"name": "Foot Steps",

"onNameConflict": "rename"

}

# 结果

{

"id": "{66666666-7777-8888-9999-AAAAAAAAAAAA}",

"name": "Foot Steps"

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。