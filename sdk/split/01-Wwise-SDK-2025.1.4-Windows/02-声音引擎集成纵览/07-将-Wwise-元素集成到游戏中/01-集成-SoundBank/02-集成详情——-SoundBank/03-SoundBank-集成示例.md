# SoundBank 集成示例

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

SoundBank 集成示例

以下各节包含各种 SoundBank 管理策略的集成示例。有关这些策略的详细信息，请参阅 Wwise Help 中的 [SoundBank 管理策略](https://www.audiokinetic.com/library/edge/?source=Help&id=strategies_for_managing_soundbanks)。

|  |  |
| --- | --- |
|  | **备注:** PrepareEvent 和 LoadBank 不可共用，因为两者都会将数据加载到内存中。 |

# "All-in-one" SoundBank

在采用此策略时，所有 Event 内容、声音结构数据和媒体文件会全部存储在一个 SoundBank 中。有关该策略的论述及其在 Wwise 设计工具中的实现，请参阅 Wwise Help 中的 ["All-in-one" SoundBank](https://www.audiokinetic.com/library/edge/?source=Help&id=method_1_all_in_one_bank)。

此游戏只有一个 SoundBank，在初始化游戏时加载它就行。当然，必须先初始化声音引擎。

...

// 在此初始化声音引擎。

...

// 加载 "Init" 和 "All-in-one" SoundBank。

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) bankID; // 此示例中未使用。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Init.bnk", bankID );

if( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"MyAllInOneBank.bnk", bankID );

}

...

# 多个完整的 SoundBank

此策略比较适合单人游戏。其中所有可能用到的声音都是由玩家在游戏中的位置决定的。有关该策略的论述及其在 Wwise 设计工具中的实现，请参阅 Wwise Help 中的[多个完整的 SoundBank](https://www.audiokinetic.com/library/edge/?source=Help&id=method_2_multiple_complete_banks)。

在游戏中，要适时加载正确的 SoundBank。例如，游戏可以在开始时加载通用 SoundBank ，然后根据游戏中玩家的实际位置加载其它 SoundBank 。注意，有些游戏需要有足够的内存才能一次加载多个关卡来实现关卡之间的过渡。

除了 `LoadBank()` ，还可使用 AkBankContent\_All 来预备 SoundBank。这样可以避免在内存中重复加载媒体（参见 [对 SoundBank 做 Prepare 操作](soundengine_banks_loading.html#soundengine_banks_preparingbanks) 章节）。

...

// 在此初始化声音引擎。

...

// 加载初始化 Bank 和通用 SoundBank 。

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) bankID; // 此示例中未使用。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Init.bnk", bankID );

if( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"CommonEvents.bnk", bankID );

}

...

// 在代码中多处，取决于实际需要：

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Level\_1.bnk", bankID );

...

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Level\_2.bnk", bankID );

...

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Level\_3.bnk", bankID );

...

eResult = [AK::SoundEngine::UnloadBank](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)( L"Level\_1.bnk", NULL );

...

eResult = [AK::SoundEngine::UnloadBank](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)( L"Level\_2.bnk", NULL );

...

eResult = [AK::SoundEngine::UnloadBank](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)( L"Level\_3.bnk", NULL );

# 细致地管理媒体

对于包含很多素材的复杂游戏，可考虑采用此策略。有关该策略的论述及其在 Wwise 设计工具中的实现，请参阅 Wwise Help 中的[细致地管理媒体](https://www.audiokinetic.com/library/edge/?source=Help&id=method_3_micromanaging_media)。

在游戏开始时加载通用 SoundBank，然后在需要时加载其他 SoundBank。比如，游戏可在开始时加载 "Event" SoundBank 和通用脚步声 SoundBank，然后根据玩家在游戏中的位置加载其他 SoundBank。

// 加载初始化和事件 SoundBank

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) bankID; // 此示例中未使用。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Init.bnk", bankID );

if( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"EventBank.bnk", bankID );

}

if( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Common\_Footstep\_bank.bnk", bankID );

}

...

// 在代码中多处，可能取决于位置：

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Winter\_Footstep\_bank.bnk", bankID );

...

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Desert\_Footstep\_bank.bnk", bankID );

...

eResult = [AK::SoundEngine::UnloadBank](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)( L"Winter\_Footstep\_bank.bnk", NULL );

...

eResult = [AK::SoundEngine::UnloadBank](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)( L"Desert\_Footstep\_bank.bnk", NULL );

# 预备 Action Event

若需要较高的媒体粒度以便降低内存用量，但又不想管理与 Event 相关的结构和媒体，可考虑采用此策略。有关该策略的论述及其在 Wwise 设计工具中的实现，请参阅 Wwise Help 中的[预备 Action Event](https://www.audiokinetic.com/library/edge/?source=Help&id=method_4_preparing_action_events)。

在游戏开始时加载 Event 所在的 SoundBank，然后在游戏中需要时预备 Event。系统会自动加载对应的结构和媒体。

// 初始化声音引擎。

[AkInitSettings](struct_ak_init_settings.html) initSettings;

[AkPlatformInitSettings](struct_ak_platform_init_settings.html) platformInitSettings;

[AK::SoundEngine::GetDefaultInitSettings](namespace_a_k_1_1_sound_engine_a03381fc17e1b0ee16c2ab501c647ab9e.html#a03381fc17e1b0ee16c2ab501c647ab9e)( initSettings );

[AK::SoundEngine::GetDefaultPlatformInitSettings](namespace_a_k_1_1_sound_engine_aecdb9cd8f2d7f461ef1a58f5f5f5725d.html#aecdb9cd8f2d7f461ef1a58f5f5f5725d)( platformInitSettings );

// Set the required settings

...

// 设置 PrepareEvent 相关设置。

initSettings.bEnableGameSyncPreparation = false; // 当前示例中未使用。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::SoundEngine::Init](namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a9a26da64092b97243844df77cbcdbf5f)( initSettings, platformInitSettings );

if( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

// Handle error.

}

// 加载初始化 SoundBank 和事件/结构 SoundBank 。

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) bankID; // 此示例中未使用。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Init.bnk", bankID );

if( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Events.bnk", bankID );

}

...

// And then, at various points in the code:

const char \* pEventsNameArray[1] = { "My\_Event\_Name" };

// Preparing an event:

eResult = [AK::SoundEngine::PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)( [Preparation\_Load](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba7bb39cc6dfafe005cddfbf12c0d62ad0), pEventsNameArray, 1 ); // 1 is the array size

// Unpreparing an event:

eResult = [AK::SoundEngine::PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)( [Preparation\_Unload](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba37375e4d359e99b67d0a69f4a5714b92), pEventsNameArray, 1 ); // 1 is the array size

# 预备 Event 和 Game Sync（Switch 和 State）

此策略跟 [预备 Action Event](sdk_bank_training.html#sdk_bank_training_Method_4) 基本相同，不过在预备 Event 时可更好地控制所加载的媒体。有关该策略的论述及其在 Wwise 设计工具中的实现，请参阅 Wwise Help 中的[预备 Event 和 Game Sync（Switch 和 State）](https://www.audiokinetic.com/library/edge/?source=Help&id=method_5_preparing_events_and_game_syncs_switches_and_states)。

`AK::SoundEngine::PrepareEvent` 和 `AK::SoundEngine::PrepareGameSync` 的调用顺序并不重要。每次状态改变都会通过交叉匹配 Event 和 Game Sync 来更新媒体池。

// 初始化声音引擎。

[AkInitSettings](struct_ak_init_settings.html) initSettings;

[AkPlatformInitSettings](struct_ak_platform_init_settings.html) platformInitSettings;

[AK::SoundEngine::GetDefaultInitSettings](namespace_a_k_1_1_sound_engine_a03381fc17e1b0ee16c2ab501c647ab9e.html#a03381fc17e1b0ee16c2ab501c647ab9e)( initSettings );

[AK::SoundEngine::GetDefaultPlatformInitSettings](namespace_a_k_1_1_sound_engine_aecdb9cd8f2d7f461ef1a58f5f5f5725d.html#aecdb9cd8f2d7f461ef1a58f5f5f5725d)( platformInitSettings );

// Set the required settings.

...

// 设置 PrepareEvent 相关设置。

////////////////////////////////////////////////////////////////

// bEnableGameSyncPreparation 标志设为 true，以激活

// 准备游戏同步器机制。When set to false, the media

// associated with all game syncs is loaded and there is no need

// to call AK::SoundEngine:PrepareGameSyncs.

//

// When set to true, no media that is game sync dependent will be

// loaded unless the game sync is activated by calling AK::SoundEngine:PrepareGameSyncs

////////////////////////////////////////////////////////////////

initSettings.bEnableGameSyncPreparation = true;

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK](namespace_a_k.html).[SoundEngine](namespace_a_k_1_1_sound_engine.html).Init( initSettings, platformInitSettings );

if( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

// 处理错误。

}

// 加载初始化 Bank 和事件/结构 SoundBank 。

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) bankID; // 此示例中未使用。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Init.bnk", bankID );

if( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Events.bnk", bankID );

}

// ... At this point,

// the two events are loaded, but not prepared. 当前没有加载媒体。

const char \* pNameArray[1];

// Prepare the main character footstep event.

pNameArray[0] = "Play\_Maincharacter\_FootSteps";

eResult = [AK::SoundEngine::PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)( [Preparation\_Load](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba7bb39cc6dfafe005cddfbf12c0d62ad0), pNameArray, 1 ); // 1 is the array size

// ... At this point,

// one event has been prepared, but no media has been loaded yet.

// 从现在起，游戏中始终可用 concrete。

pNameArray[0] = "Concrete";

eResult = [AK::SoundEngine::PrepareGameSyncs](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc)( [Preparation\_Load](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba7bb39cc6dfafe005cddfbf12c0d62ad0), in\_eType, "GroundTexture", pNameArray, 1 );

// ... At this point,

// the 3 sounds, Sound\_Concrete\_main\_1, Sound\_Concrete\_main\_2, and Sound\_Concrete\_main\_3 are loaded.

// 现在，假设主人公进入一片雪地。

pNameArray[0] = "Snow";

eResult = [AK::SoundEngine::PrepareGameSyncs](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc)( [Preparation\_Load](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba7bb39cc6dfafe005cddfbf12c0d62ad0), in\_eType, "GroundTexture", pNameArray, 1 );

// ... At this point,

// 3 more sounds just got loaded : Sound\_Snow\_main\_1, Sound\_Snow\_main\_2 and Sound\_Snow\_main\_3

// Then let's say that a Monster suddenly appears.

pNameArray[0] = "Play\_Monster\_Footsteps";

eResult = [AK::SoundEngine::PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)( [Preparation\_Load](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba7bb39cc6dfafe005cddfbf12c0d62ad0), pEventsNameArray, 1 ); // 1 is the array size

// ... At this point,

// 6 more sounds just got loaded ( Sound\_Concrete\_Monster\_1.2.3 and Sound\_Snow\_Monster\_1.2.3 )

// And now our player decides to run away from the monster, and the monster goes after them.

// 怪兽和玩家一直奔跑，来到没有积雪的地方。

pNameArray[0] = "Snow";

eResult = [AK::SoundEngine::PrepareGameSyncs](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc)( [Preparation\_Unload](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba37375e4d359e99b67d0a69f4a5714b92), in\_eType, "GroundTexture", pNameArray, 1 );

// ... 在此时，

// 与积雪相关的 6 个声音（Sound\_Snow\_Monster\_1.2.3 和 Sound\_Snow\_main\_1.2.3）已从内存中卸载。

...

参见
:   - [集成详情—— SoundBank](soundengine_banks.html)
    - [一般信息](soundengine_banks_general.html)
    - [加载 SoundBank](soundengine_banks_loading.html)
    - [AK::SoundEngine::LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)
    - [AK::SoundEngine::UnloadBank()](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)
    - [AK::SoundEngine::ClearBanks()](namespace_a_k_1_1_sound_engine_ab934f98a6622976d24e0a096911eb0c8.html#ab934f98a6622976d24e0a096911eb0c8)
    - [AK::SoundEngine::PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)
    - [AK::SoundEngine::PrepareGameSyncs()](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc)
    - [AK::SoundEngine::ClearPreparedEvents()](namespace_a_k_1_1_sound_engine_af9648460be2ed1a0093ff09b42ef36f5.html#af9648460be2ed1a0093ff09b42ef36f5)

[AK::SoundEngine::PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)

AKSOUNDENGINE\_API AKRESULT PrepareEvent(PreparationType in\_PreparationType, const char \*\*in\_ppszString, AkUInt32 in\_uNumEvent)

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349)

AkUInt32 AkBankID

Run time bank ID

**Definition:** [AkTypedefs.h:54](_ak_typedefs_8h_source.html#l00054)

[AK](namespace_a_k.html)

Definition of data structures for AkAudioObject

**Definition:** [AkWwiseSDKVersion.cs:31](_ak_wwise_s_d_k_version_8cs_source.html#l00030)

[AK::SoundEngine::PrepareGameSyncs](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc)

AKSOUNDENGINE\_API AKRESULT PrepareGameSyncs(PreparationType in\_PreparationType, AkGroupType in\_eGameSyncType, const char \*in\_pszGroupName, const char \*\*in\_ppszGameSyncName, AkUInt32 in\_uNumGameSyncs)

[AK::SoundEngine::Init](namespace_a_k_1_1_sound_engine_a9a26da64092b97243844df77cbcdbf5f.html#a9a26da64092b97243844df77cbcdbf5f)

AKSOUNDENGINE\_API AKRESULT Init(AkInitSettings \*in\_pSettings, AkPlatformInitSettings \*in\_pPlatformSettings)

[AkPlatformInitSettings](struct_ak_platform_init_settings.html)

**Definition:** [AkWinSoundEngine.h:43](_ak_win_sound_engine_8h_source.html#l00042)

[AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)

AKSOUNDENGINE\_API AKRESULT LoadBank(const char \*in\_pszString, AkBankID &out\_bankID, AkBankType in\_bankType=AkBankType\_User)

[AK::SoundEngine::Preparation\_Unload](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba37375e4d359e99b67d0a69f4a5714b92)

@ Preparation\_Unload

PrepareEvent() will unload required information to play the specified event.

**Definition:** [AkSoundEngine.h:2706](_ak_sound_engine_8h_source.html#l02706)

[AK::SoundEngine::GetDefaultInitSettings](namespace_a_k_1_1_sound_engine_a03381fc17e1b0ee16c2ab501c647ab9e.html#a03381fc17e1b0ee16c2ab501c647ab9e)

AKSOUNDENGINE\_API void GetDefaultInitSettings(AkInitSettings &out\_settings)

[AK::SoundEngine::Preparation\_Load](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba7bb39cc6dfafe005cddfbf12c0d62ad0)

@ Preparation\_Load

PrepareEvent() will load required information to play the specified event.

**Definition:** [AkSoundEngine.h:2705](_ak_sound_engine_8h_source.html#l02705)

[AK::SoundEngine::UnloadBank](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)

AKSOUNDENGINE\_API AKRESULT UnloadBank(const char \*in\_pszString, const void \*in\_pInMemoryBankPtr, AkBankType in\_bankType=AkBankType\_User)

[AK::SoundEngine::GetDefaultPlatformInitSettings](namespace_a_k_1_1_sound_engine_aecdb9cd8f2d7f461ef1a58f5f5f5725d.html#aecdb9cd8f2d7f461ef1a58f5f5f5725d)

AKSOUNDENGINE\_API void GetDefaultPlatformInitSettings(AkPlatformInitSettings &out\_platformSettings)

[AK::SoundEngine](namespace_a_k_1_1_sound_engine.html)

**Definition:** [AllPluginsRegistrationHelpers.h:36](_all_plugins_registration_helpers_8h_source.html#l00035)

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63)

AKRESULT

**Definition:** [AkEnums.h:32](_ak_enums_8h_source.html#l00031)

[AkInitSettings](struct_ak_init_settings.html)

**Definition:** [AkSoundEngine.h:193](_ak_sound_engine_8h_source.html#l00192)

[AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e)

@ AK\_Success

The operation was successful.

**Definition:** [AkEnums.h:34](_ak_enums_8h_source.html#l00034)