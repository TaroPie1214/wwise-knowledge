# 集成详情——GetSourcePlayPosition

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

集成详情——GetSourcePlayPosition

# 简介

[在特定情况下，游戏引擎需要有关声音当前播放位置的信息。例如，支持同步渲染视频和音频内容的游戏必须查询声音的播放位置才能正确地渲染游戏画面。如果必须逐帧查询（例如对口型和对白同步），那么播放位置查询比标记（marker）要更适合。播放位置查询的另一大优势是无需编辑源文件。AK::SoundEngine::GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) 返回事件的第一次声音播放所使用的时间。

|  |  |
| --- | --- |
|  | **备注:** 标记适用于表明"声音文件"中发生的事件，而非"声音播放"时的小步渐进。 |

然后您可以通过传递在调用 [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) 中所获得的 AkPlayingID 来调用 [AK::SoundEngine::GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) 方法，从而获取正在播放的源的当前播放位置。

# 示例

下段代码用于说明 [AK::SoundEngine::GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) 方法的用法：

(...)

static [AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) g\_markersPlayingID = 0;

(...)

(...)

g\_markersPlayingID = [AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)( AK::EVENTS::PLAY\_MARKERS\_TEST, GAME\_OBJECT\_ID\_MARKERS );

(...)

[AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24) uPosition = 0;

// 在游戏循环中某个位置（周期性发生）：

[AK::SoundEngine::GetSourcePlayPosition](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283)( g\_markersPlayingID, &uPosition );

// 现在通过使用 uPosition 进行对嘴形

# 限制

- 当事件包含多个播放动作时，GetSourcePlayPosition() 返回在时间 0 时发生的第一个播放动作的目标所播放的第一个源的位置。 当此源停止时，其返回的播放位置将为未定义。
- 连续（随机或序列）容器返回当前正在播放的声音的位置。当有许多声音时，其返回的播放位置将为未定义。 在交叉淡变或精确到采样点的过渡中，只有当上一个源完成播放时下一个源才会返回它的位置。
- 当结合外插法使用时，循环播放源可能会在循环发生时短暂超出循环结束点。
- 当优先级低于特定阈值时，某些虚声部会被终止。发生这种情况时，您可能会从 [AK::SoundEngine::GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) 收到错误码。在调用 [AK::SoundEngine::GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283) 时应总是检查返回值。
- 动态更改音高可能导致在过渡期间播放位置出现短暂轻微偏移。

参见
:   - [集成详情——事件](soundengine_events.html)
    - [AK::SoundEngine::PostEvent()](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)
    - [AK::SoundEngine::GetSourcePlayPosition()](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283)

[AkTimeMs](_ak_typedefs_8h_a8a4d0aa5dba6f9922d6b7b3e48958b24.html#a8a4d0aa5dba6f9922d6b7b3e48958b24)

AkInt32 AkTimeMs

Time in ms

**Definition:** [AkTypedefs.h:35](_ak_typedefs_8h_source.html#l00035)

[AK::SoundEngine::GetSourcePlayPosition](namespace_a_k_1_1_sound_engine_ae0b469d9fb8a099b40f52f004882d283.html#ae0b469d9fb8a099b40f52f004882d283)

AKSOUNDENGINE\_API AKRESULT GetSourcePlayPosition(AkPlayingID in\_PlayingID, AkTimeMs \*out\_puPosition, bool in\_bExtrapolate=true)

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)

AKSOUNDENGINE\_API AkPlayingID PostEvent(AkUniqueID in\_eventID, AkGameObjectID in\_gameObjectID, AkUInt32 in\_uFlags=0, AkCallbackFunc in\_pfnCallback=NULL, void \*in\_pCookie=NULL, AkUInt32 in\_cExternals=0, AkExternalSourceInfo \*in\_pExternalSources=NULL, AkPlayingID in\_PlayingID=AK\_INVALID\_PLAYING\_ID)

[AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3)

AkUInt32 AkPlayingID

A unique identifier generated whenever a PostEvent is called (or when a Dynamic Sequence is created)....

**Definition:** [AkTypedefs.h:34](_ak_typedefs_8h_source.html#l00034)