# 将命令注册为 Edit in Visual Studio Code

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

将命令注册为 Edit in Visual Studio Code

注册要在新的 Extra 菜单中显示的命令。

# 函数 URI

[ak.wwise.ui.commands.register](ak_wwise_ui_commands_register.html)

# 参数

{

"commands": [

{

"id": "ak.edit\_in\_vscode",

"displayName": "Edit in Visual Studio Code",

"defaultShortcut": "C",

"program": "code",

"startMode": "MultipleSelectionSingleProcessSpaceSeparated",

"args": "${filePath}",

"cwd": "",

"contextMenu": {

"basePath": "Editors",

"enabledFor": "Sound,PropertyContainer,SwitchContainer,RandomSequenceContainer"

},

"mainMenu": {

"basePath": "Extra"

}

}

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。