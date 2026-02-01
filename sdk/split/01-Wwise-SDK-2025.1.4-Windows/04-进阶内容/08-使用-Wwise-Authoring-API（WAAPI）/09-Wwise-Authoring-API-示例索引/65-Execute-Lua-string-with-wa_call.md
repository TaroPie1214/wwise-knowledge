# Execute Lua string with wa_call

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Execute Lua string with wa\_call

Executes Lua code that calls WAAPI functions using `wa_call`. This demonstrates how to interact with the Wwise API from within the Lua code, such as adding a log message.

# Function URI

[ak.wwise.core.executeLuaScript](ak_wwise_core_executeluascript.html)

# Arguments

{

"luaString": "wa\_call('ak.wwise.core.log.addItem', { message = wa\_args.message, severity = 'Message' }, {})\nreturn 'success'",

"message": "Hello from Lua string"

}

# Result

{

"return": "success"

}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。