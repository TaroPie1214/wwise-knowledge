# 快速入门示例集成—— SoundBank

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

快速入门示例集成—— SoundBank

# SoundBank 集成示例

如 [了解 SoundBank](concept_banks.html) 中所述， SoundBank 分为两种类型：初始化包 和 SoundBank。 每个 Wwise 工程都有一个初始化包，它必须在加载其它 SoundBank 之前加载。工程中会有任意数量的 SoundBank，其中部分可能用于多种语言。

以下代码首先在 Low-Level I/O（底层 I/O）模块中设置基本路径和特定语言的子目录。如果您不沿用此模块或干脆不沿用整个 Streaming Manager，则需要根据情况调整此代码。请参阅 [流播放/流管理器](streamingdevicemanager.html) 了解更多信息。

代码于是加载初始化包，在默认情况下，初始化包名为“Init.bnk”。如果您决定重命名此文件，则必须相应地更新代码。

最后，此代码加载“Car.bnk”、“Human.bnk”和“MarkerTest.bnk” SoundBank。在我们的工程示例中，它们包含`Play_Engine` 、`Stop_Engine` 和 `Play_Hello` 等事件。

// SoundBank 文件名称

#define BANKNAME\_INIT L"Init.bnk"

#define BANKNAME\_CAR L"Car.bnk"

#define BANKNAME\_HUMAN L"Human.bnk"

#define BANKNAME\_MARKERTEST L"MarkerTest.bnk"

(...)

//

// 设置 SoundBank 路径

//

g\_lowLevelIO.SetBasePath( [AKTEXT](_platforms_2_windows_2_ak_types_8h_ab37c4500d1c5377b3f54077b8222dde7.html#ab37c4500d1c5377b3f54077b8222dde7)("../../../samples/IntegrationDemo/WwiseProject/GeneratedSoundBanks/Windows/") );

[AK::StreamMgr::SetCurrentLanguage](namespace_a_k_1_1_stream_mgr_ae4820886baae734dd90177a49a2be1eb.html#ae4820886baae734dd90177a49a2be1eb)( [AKTEXT](_platforms_2_windows_2_ak_types_8h_ab37c4500d1c5377b3f54077b8222dde7.html#ab37c4500d1c5377b3f54077b8222dde7)("English(US)") );

//

// （从文件名）同步加载 SoundBank 。

//

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) bankID; // 未使用。这些 SoundBank 可以通过它们的文件名来卸载。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( BANKNAME\_INIT, bankID );

assert( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) );

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( BANKNAME\_CAR, bankID );

assert( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) );

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( BANKNAME\_HUMAN, bankID );

assert( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) );

eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( BANKNAME\_MARKERTEST, bankID );

assert( eResult == [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) );

请参阅 [集成详情—— SoundBank](soundengine_banks.html) 了解声音引擎中有关 SoundBank 的更多信息，并参阅 [文件位置解析](streamingmanager_lowlevel.html#streamingmanager_lowlevel_location) 了解有关本地化的信息。

|  |  |
| --- | --- |
|  | **备注:** 此例程摘自 [示例](samplecode.html) 一节中的“声音引擎集成工程示例”部分。请参阅 [Integration Demo 示例](soundengine_integration_samplecode.html) 了解更多信息。 |

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349)

AkUInt32 AkBankID

Run time bank ID

**Definition:** [AkTypedefs.h:54](_ak_typedefs_8h_source.html#l00054)

[AK::StreamMgr::SetCurrentLanguage](namespace_a_k_1_1_stream_mgr_ae4820886baae734dd90177a49a2be1eb.html#ae4820886baae734dd90177a49a2be1eb)

AKSOUNDENGINE\_API AKRESULT SetCurrentLanguage(const AkOSChar \*in\_pszLanguageName)

[AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)

AKSOUNDENGINE\_API AKRESULT LoadBank(const char \*in\_pszString, AkBankID &out\_bankID, AkBankType in\_bankType=AkBankType\_User)

[AKTEXT](_platforms_2_windows_2_ak_types_8h_ab37c4500d1c5377b3f54077b8222dde7.html#ab37c4500d1c5377b3f54077b8222dde7)

#define AKTEXT(x)

**Definition:** [AkTypes.h:159](_platforms_2_windows_2_ak_types_8h_source.html#l00159)

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63)

AKRESULT

**Definition:** [AkEnums.h:32](_ak_enums_8h_source.html#l00031)

[AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e)

@ AK\_Success

The operation was successful.

**Definition:** [AkEnums.h:34](_ak_enums_8h_source.html#l00034)