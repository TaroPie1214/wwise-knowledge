# Execute Lua string with conditional logic

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Execute Lua string with conditional logic

Executes Lua code with control flow logic. The `luaString` can contain multiple lines and use standard Lua control structures like if/else, loops, and functions.

# Function URI

[ak.wwise.core.executeLuaScript](ak_wwise_core_executeluascript.html)

# Arguments

{

"luaString": "if wa\_args.value > 10 then\n return 'greater'\nelse\n return 'less or equal'\nend",

"value": 15

}

# Result

{

"return": "greater"

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。