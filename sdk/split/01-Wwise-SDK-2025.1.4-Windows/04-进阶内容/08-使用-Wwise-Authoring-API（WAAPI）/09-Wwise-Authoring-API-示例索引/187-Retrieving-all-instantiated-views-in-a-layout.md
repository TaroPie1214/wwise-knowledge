# Retrieving all instantiated views in a layout

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Retrieving all instantiated views in a layout

Returns a list of all instantiated views in a given layout.

# 函数 URI

[ak.wwise.ui.layout.getViewInstances](ak_wwise_ui_layout_getviewinstances.html)

# 参数

{

"name": "Designer"

}

# 结果

{

"viewInstances": [

{

"viewID": "{E773AA9A-2F00-45F1-BD61-3C13C321BE6C}",

"viewIsDocked": true,

"viewName": "Project Explorer"

},

{

"viewID": "{E773AA9A-2F00-45F1-BD61-3C13C321BE6D}",

"viewIsDocked": true,

"viewName": "Game Object 3D Viewer"

}

]

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。