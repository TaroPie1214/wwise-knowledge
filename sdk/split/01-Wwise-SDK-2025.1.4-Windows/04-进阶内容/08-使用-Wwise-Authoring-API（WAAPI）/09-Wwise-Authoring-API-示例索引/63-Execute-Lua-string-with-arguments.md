# Execute Lua string with arguments

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Execute Lua string with arguments

Executes Lua code that accesses custom arguments passed via `wa_args`. All additional arguments in the WAAPI call are accessible as fields in the `wa_args` table within the Lua code.

# Function URI

[ak.wwise.core.executeLuaScript](ak_wwise_core_executeluascript.html)

# Arguments

{

"luaString": "return { sum = wa\_args.a + wa\_args.b, product = wa\_args.a \* wa\_args.b }",

"a": 10,

"b": 20

}

# Result

{

"return": {

"sum": 30,

"product": 200

}

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。