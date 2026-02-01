# Execute Lua file from path

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Execute Lua file from path

Executes a Lua script from a file path. This is the traditional way to execute Lua scripts and is preferred for longer, more complex scripts. Custom arguments can be passed and accessed via `wa_args` within the script file.

# Function URI

[ak.wwise.core.executeLuaScript](ak_wwise_core_executeluascript.html)

# Arguments

{

"luaScript": "C:\\scripts\\my\_script.lua",

"customArg": "value"

}

# Result

{

"return": {

"status": "Script executed successfully"

}

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。