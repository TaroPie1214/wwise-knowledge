# 将命令注册为 Edit in Wavosaur

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

将命令注册为 Edit in Wavosaur

注册只在上下文菜单中显示的命令。

# 函数 URI

[ak.wwise.ui.commands.register](ak_wwise_ui_commands_register.html)

# 参数

{

"commands": [

{

"id": "ak.open\_in\_wavosaur",

"displayName": "Edit in Wavosaur",

"defaultShortcut": "W",

"program": "c:\\Wavosaur.1.1.0.0-x64(en)\\Wavosaur.exe",

"args": "${originalWavFilePath}",

"cwd": "",

"contextMenu": {}

}

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。