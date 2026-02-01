# 设置游戏对象的 Auxiliary Bus

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

设置游戏对象的 Auxiliary Bus

设置 "listener" 对应 "emitter" 的 Auxiliary Bus，分别为其指定总线名称和数值。

# 函数 URI

[ak.soundengine.setGameObjectAuxSendValues](ak_soundengine_setgameobjectauxsendvalues.html)

# 参数

{

"gameObject": 1122334,

"auxSendValues": [

{

"listener": 5566123,

"auxBus": "AuxBus1",

"controlValue": 0.6

},

{

"listener": 226486,

"auxBus": "AuxBus2",

"controlValue": 0.4

}

]

}

# 结果

{}

有关 Wwise Authoring API 的详细信息，请参阅 [使用 Wwise Authoring API（WAAPI）](waapi.html) 章节。