# 加载 SoundBank

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

加载 SoundBank

在 Wwise 声音引擎中，使用 Event（事件）和 Game Syncs（游戏同步器）控制播放。这些元素引用 SoundBank 中存储的内部声音结构，并最终引用松散的媒体文件。所有这些内容在使用之前必须由声音引擎完成加载。

|  |  |
| --- | --- |
|  | **备注:** PrepareEvent 和 LoadBank 不可共用，因为两者都会将数据加载到内存中。 |

# 显式与隐式媒体加载

您可以显式或隐式加载 SoundBank 。这两种方法（将在下文中详细介绍）提供的选择都暗含优缺点，需要根据特定场景对这些优缺点做出评估。

## 显式 SoundBank 加载

您可以使用声音引擎 API 的 [AK::SoundEngine::LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 方法之一显式加载 SoundBank 。在加载 SoundBank 后，它里面的所有对象就准备就绪了。

在下例中，将显式加载 SoundBank BANK\_01。此 SoundBank 通过 ID 进行标识，ID 在 Wwise\_IDs.h 头文件中定义。有关使用字符串（Unicode 或 ANSI）或 ID 标识 SoundBank 的讨论，请参阅 [标识 SoundBank](soundengine_banks_general.html#soundengine_banks_general_identification) 。其中包含事件 PLAY\_SOUND\_01 及其相关的声音结构和媒体（请参阅 [Wwise 帮助](https://www.audiokinetic.com/library/?source=Help&id=managing_soundbanks)，了解有关使用 Wwise 生成 SoundBank 的详情）。加载后，事件会发送给声音引擎。

#include "Wwise\_IDs.h"

// ...

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) gameObj = 3;

[AK::SoundEngine::RegisterGameObj](namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html#a895ed0f83a0dea8fc284491c0ee0152c)( gameObj );

// 使用 ID 同步加载 SoundBank 。

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) returnedBankID;

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)(

AK::BANKS::BANK\_01, // 要加载的 SoundBank 的标识符。

returnedBankID // 返回的 SoundBank ID。

);

if( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

// SoundBank 加载失败。

// 处理错误……

}

// 加载成功。

// 根据要求使用 SoundBank ……

// 举例而言，如果 SoundBank 中包含事件 PLAY\_SOUND\_01 及其

// 相关声音结构和媒体。

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)(

AK::EVENTS::PLAY\_SOUND\_01, // 事件的唯一 ID

gameObj // 相关游戏对象 ID

);

## 隐式媒体加载

PrepareEvent/PrepareGameSync API 可以隐式加载 SoundBank 中未包含的媒体。为此，您必须首先通过 [LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 显式加载包含 Event 或 Game Sync 定义的 SoundBank 。这些 SoundBank 通常只含 Event 和结构，不含媒体，因此很轻量。请参阅 Wwise 帮助，了解如何定义没有媒体数据的 SoundBank 。当 SoundBank 中不包含被引用的媒体时，文件系统中必须以松散媒体文件的形式提供该媒体。在加载 Event 和 Game Sync [的定义后，必须对它们做“Prepare”操作以便使用（AK::SoundEngine::PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 和 [AK::SoundEngine::PrepareGameSyncs()](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc)）。在对事件或游戏同步器做 Prepare 操作时，声音引擎将从文件系统中隐式提取被引用的媒体文件。可把声音结构包含在不包含事件定义的 SoundBank 中。然后 Event 所在的 SoundBank 中将包含对含有结构数据的 SoundBank 的引用，在 对事件做 Prepare 操作时，被引用 SoundBank 中的结构将与媒体一起隐式加载。包含的所有结构将从链接的 SoundBank 中加载，而非仅从 Event 所引用的 SoundBank 中加载，为此，把 Event 和结构绑定在同一个 SoundBank 中通常更为实用。

在下例中，SoundBank BANK\_02 显式加载，它所引用的媒体隐式加载。它包含事件 PLAY\_SOUND\_02 的定义和相关声音结构。由于它不包含事件相关媒体，因此若不提前 对事件做 Prepare 操作，则该事件的发送将会失败。因此，在成功加载 SoundBank 后，先 对事件做 Prepare 操作，然后再发送。在 对事件做 Prepare 操作时，声音引擎将自动加载成功发送事件所需要的所有媒体。

#include "Wwise\_IDs.h"

// ...

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) gameObj = 3;

[AK::SoundEngine::RegisterGameObj](namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html#a895ed0f83a0dea8fc284491c0ee0152c)( gameObj );

// 使用 ID 同步加载 SoundBank 。

// 此 SoundBank 可能只包含您要使用的事件的定义。

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) returnedBankID;

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)(

AK::BANKS::BANK\_02, // 要加载的 SoundBank 的标识符。

returnedBankID // 返回的 SoundBank ID。

);

if( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

// SoundBank 加载失败。

// 处理错误……

}

// 加载成功。事件 PLAY\_SOUND\_02 的定义及其相关结构已加载。

// 为了发送事件，需要 对事件做 Prepare 操作（在此例中采用同步模式）。

[AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) eventToPrepare = AK::EVENTS::PLAY\_SOUND\_02;

eResult = [PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)(

[Preparation\_Load](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba7bb39cc6dfafe005cddfbf12c0d62ad0), // Preparation type: load.

&eventToPrepare, // 事件 ID 的数组。

1 // 数组中的事件 ID 数量。

);

if ( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

// 事件 Prepare 操作失败。

// 处理错误……

}

// 事件的 Prepare 操作成功：声音引擎收集了成功发送事件

// structures if necessary) that are required to successfully post the event, by loading all

// necessary media under the hood.

// 发送事件。

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)(

AK::EVENTS::PLAY\_SOUND\_02, // 事件的唯一 ID

gameObj // 相关游戏对象 ID

);

获得有关如何使用 [AK::SoundEngine::PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 和 [AK::SoundEngine::PrepareGameSyncs](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc) 的完整示例，请参阅以下章节：

- [预备 Action Event](sdk_bank_training.html#sdk_bank_training_Method_4)
- [预备 Event 和 Game Sync（Switch 和 State）](sdk_bank_training.html#sdk_bank_training_Method_5)

# 同步与异步加载

SoundBank 加载是在单独的声音引擎线程中执行的。主要 API 的所有 [LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)、PrepareEvent() 和 [PrepareGameSyncs()](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc) 功能均可通过同步和异步加载方案获取。

## 同步 SoundBank 加载

同步 [AK::SoundEngine::LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 功能是阻塞功能。这些 API 函数将在加载 SoundBank 完成或发生错误时将返回。

## 异步 SoundBank 加载

异步 [AK::SoundEngine::LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 功能立即返回，并在完成请求的操作后，以 cookie 作为参数来调用回调函数。异步调用时，必须在回调函数中执行错误处理。

cookie 参数是可选参数，为方便操作而提供。如果您不使用它，只需赋予 NULL 值。声音引擎将不使用此指针；它仅通过回调函数返回。

## SoundBank 回调原型

搭配 [LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)、UnloadBank()、PrepareEvent() 和 [PrepareGameSyncs()](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc) 的异步版本使用的回调函数必须遵循此原型：

typedef void( \*[AkBankCallbackFunc](_ak_callback_types_8h_a5f4438e001923453a9f795eb64946be6.html#a5f4438e001923453a9f795eb64946be6) )(

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) in\_bankID,

void \* in\_pInMemoryBankPtr,

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) in\_eLoadResult,

void \* in\_pCookie

);

您负责实现回调函数，因此您必须保证它的有效性。

参数 in\_bankID 在针对 PrepareEvent 和 PrepareGameSync 接收回调时用不到，请直接忽略。

请参阅 AkBankCallbackFunc 了解传递给回调函数的参数的定义。

# 从内存或者通过文件 I/O 加载 SoundBank

如前面 [标识 SoundBank](soundengine_banks_general.html#soundengine_banks_general_identification) 中述，您可以自己从文件中加载 SoundBank ，然后为相应的 [LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 重载提供指针和大小，也可以指定 SoundBank 标识符（ID 或字符串，见上文讨论），让声音引擎通过 Stream Manager 加载 SoundBank 文件。

## 从内存中加载

使用以下某个 [LoadBankMemoryView()](namespace_a_k_1_1_sound_engine_a7e8069027779f518a2049dffbb8ecbcb.html#a7e8069027779f518a2049dffbb8ecbcb) 原型来加载位于内存中最终位置的 SoundBank：

// 同步，原地。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) [LoadBankMemoryView](namespace_a_k_1_1_sound_engine_a7e8069027779f518a2049dffbb8ecbcb.html#a7e8069027779f518a2049dffbb8ecbcb)(

void \* in\_pInMemoryBankPtr, ///< Pointer to the in-memory bank to load

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uInMemoryBankSize, ///< Size of the in-memory bank to load

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) & out\_bankID ///< Returned bank ID

);

// 异步，原地。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) [LoadBankMemoryView](namespace_a_k_1_1_sound_engine_a7e8069027779f518a2049dffbb8ecbcb.html#a7e8069027779f518a2049dffbb8ecbcb)(

void \* in\_pInMemoryBankPtr, ///< Pointer to the in-memory bank to load

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uInMemoryBankSize, ///< Size of the in-memory bank to load

[AkBankCallbackFunc](_ak_callback_types_8h_a5f4438e001923453a9f795eb64946be6.html#a5f4438e001923453a9f795eb64946be6) in\_pfnBankCallback, ///< Callback function

void \* in\_pCookie, ///< Callback cookie

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) & out\_bankID ///< Returned bank ID

);

声音引擎内不复制内存，因此必须确保在卸载 SoundBank 之前，内存一直保持有效。根据具体平台要求，SoundBank 加载涉及的内存指针上可能要用到一些对齐限制。在所有平台上，内存必须与 AK\_BANK\_PLATFORM\_DATA\_ALIGNMENT 字节对齐。某些平台可能有不同的要求，因此您应该检查对应平台的 SDK 文档。

或者，使用以下某个 [LoadBankMemoryCopy()](namespace_a_k_1_1_sound_engine_ac16591355aef3ffaf2f8e9ac7a5b95ad.html#ac16591355aef3ffaf2f8e9ac7a5b95ad) 原型来加载位于内存中临时位置的 SoundBank：

// 同步，非原地。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) [LoadBankMemoryCopy](namespace_a_k_1_1_sound_engine_ac16591355aef3ffaf2f8e9ac7a5b95ad.html#ac16591355aef3ffaf2f8e9ac7a5b95ad)(

void \* in\_pInMemoryBankPtr, ///< Pointer to the in-memory bank to load

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uInMemoryBankSize, ///< Size of the in-memory bank to load

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) & out\_bankID ///< Returned bank ID

);

// 异步，非原地。

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) [LoadBankMemoryCopy](namespace_a_k_1_1_sound_engine_ac16591355aef3ffaf2f8e9ac7a5b95ad.html#ac16591355aef3ffaf2f8e9ac7a5b95ad)(

void \* in\_pInMemoryBankPtr, ///< Pointer to the in-memory bank to load

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uInMemoryBankSize, ///< Size of the in-memory bank to load

[AkBankCallbackFunc](_ak_callback_types_8h_a5f4438e001923453a9f795eb64946be6.html#a5f4438e001923453a9f795eb64946be6) in\_pfnBankCallback, ///< Callback function

void \* in\_pCookie, ///< Callback cookie

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) & out\_bankID ///< Returned bank ID

);

SoundBank 将被复制到声音引擎内新分配的位置，完成加载操作后便可立即释放传递的指针。

[LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 解析随附指针前几个字节中存储的 SoundBank ID，并返回此 ID。保存好 SoundBank ID，以备稍后卸载 SoundBank 。

|  |  |
| --- | --- |
|  | **备注:** 如果您选择自己执行文件 I/O，并向声音引擎馈送指针，则必须使用显式 SoundBank 加载。隐式 SoundBank 加载可能无法预测。按照 PrepareXXXX 命令，您无法确定要加载的 SoundBank 数量以及这些 SoundBank 的内存需求。这就是没有 PrepareEvent 和 PrepareGameSyncs 内存版的原因。 |

## 通过文件 I/O 加载

每当需要读取文件时，声音引擎总是使用 Stream Manager。请参阅 [标识 SoundBank](soundengine_banks_general.html#soundengine_banks_general_identification) 了解有关 SoundBank 标识与 I/O 的讨论。

您可以使用 [AK::SoundEngine::SetBankLoadIOSettings()](namespace_a_k_1_1_sound_engine_ab8f05d2ee628529bb2bde9dab2d56047.html#ab8f05d2ee628529bb2bde9dab2d56047) 功能，在 Stream Manager 方面微调声音引擎 SoundBank 加载程序的行为。有关 I/O 的详情，请参阅 [流播放/流管理器](streamingdevicemanager.html) 一节。

## 内存占用

声音引擎解析 SoundBank 的元数据，并在声音引擎的默认池中创建它的对象。

在涉及 I/O 的显式 [LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 函数中，会从磁盘读取媒体并将其复制到内存中。在 I/O 期间，将按照声音引擎初始化设置中 [AkInitSettings::uBankReadBufferSize](struct_ak_init_settings_ae4c40fd9bab28527705d43b2247bbe21.html#ae4c40fd9bab28527705d43b2247bbe21 "The number of bytes read by the BankReader when new data needs to be loaded from disk during serializ...") 指定的大小分块读取 SoundBank。该数值越大，读取次数就越少，但会增加 SoundBank I/O 期间的内存用量。

# 卸载 SoundBank

有许多 [UnloadBank()](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64) 重载可用于显式卸载 SoundBank ：

- 使用 ID 标识
- 使用字符串标识（Unicode 或 ANSI）
- 同步
- 异步

同样，搭配 Preparation\_Unload 标志使用 [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 函数来减少与这些事件相关的结构和媒体的引用计数。当隐式加载的 SoundBank 中所有对象的引用计数减少到 0 时，它会自动卸载。

另外，要搭配 Preparation\_Unload 标志使用 [PrepareGameSyncs()](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc) 函数来卸载采用了 Prepare 操作的事件所加载的媒体。只有当选择了指定游戏同步器时，这些事件才会播放。请注意，游戏同步器没有引用计数，使用 Preparation\_Unload 标志调用它一次将立即卸载未被引用的媒体。

|  |  |
| --- | --- |
|  | **备注:** 如果在卸载 SoundBank 时其所引用的声音正在播放，并且 SoundBank 中包含声音的声音结构，则声音将停止播放。如果 SoundBank 中只包含媒体，但其它已加载的 SoundBank 中有媒体和声音结构，则声音有可能会停止。这取决于媒体是使用该 SoundBank 中的数据播放还是使用其它 SoundBank 中的数据播放。请参阅 [复制库内容](soundengine_banks_loading.html#soundengine_banks_dup_contents) 。 |

|  |  |
| --- | --- |
|  | **备注:** 如果有事件更改过此声音的参数（例如 SetVolume 事件），则此更改信息将被移除。如果参数已被 RTPC、State 或 Swtich 更改过，则参数将保留在内存中，并将在重新加载 SoundBank 时自动应用。 |

以下代码使用 Unicode 字符串标识符和默认 SoundBank 内存分配方法同步加载和卸载 SoundBank 。它通过 [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 隐式加载和卸载 SoundBank 。

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349) bankID;

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) eResult = [AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)( L"Bank1.bnk", bankID );

if( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

// Failed loading bank.

// 处理错误……

}

// SoundBank 加载成功。

// 对事件做 Prepare 操作。

const char \* pszEvent = "Event1";

eResult = [PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)( [Preparation\_Load](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba7bb39cc6dfafe005cddfbf12c0d62ad0), &pszEvent, 1 );

if( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

// 准备事件失败。

// 处理错误……

}

// 使用事件和 SoundBank 数据……

// 然后解除对事件做的 Prepare 操作。

eResult = [PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)( [Preparation\_Unload](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba37375e4d359e99b67d0a69f4a5714b92), &pszEvent, 1 );

if( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

// 解除事件的 Prepare 操作失败。

// 处理错误……

}

// 卸载 SoundBank 。

// 注：SoundBank 使用 LoadBank() 返回的 SoundBank ID 卸载。此调用

// AK::SoundEngine::UnloadBank( L"Bank1.bnk", NULL );

// 也可行：声音引擎在内部把“Bank1.bnk”字符串转换成 SoundBank ID。

eResult = [AK::SoundEngine::UnloadBank](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)( bankID, NULL );

if( eResult != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e) )

{

// 卸载 SoundBank 失败。

// 处理错误……

}

# 对 SoundBank 做 Prepare 操作

除 [LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 和 [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 函数外，还可对 SoundBank 做 Prepare 操作。您可以使用以下任一方法对 SoundBank 做 Prepare：

- AkBankContent\_All
- AkBankContent\_StructureOnly

这两种方法使用的是相同的 PrepareBank 机制，只是在实现上有少许不同，但最常用的是 AkBankContent\_All。.

## AkBankContent\_All

使用 `AkBankContent_All` 来对 SoundBank 做 Prepare 可以克服 [LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 机制的一些弱点，同时还可以发挥 [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 机制的优势。在使用此方法时， SoundBank 中仍可包含所有内容类型（事件、结构数据和媒体文件），但是此方法不直接加载媒体文件，而是运用类似于 PrepareEvent 的机制把所有媒体加载到内存中。在使用 [PrepareBank()](namespace_a_k_1_1_sound_engine_a7d92b3c386cd60e76be54ca69f051c09.html#a7d92b3c386cd60e76be54ca69f051c09) 加载媒体时，Wwise 首先查看媒体文件在内存中是否已经存在，然后再加载。这可以避免内存中出现媒体文件重复，从而把内存占用保持在最低水平。

AkBankContent\_All 是 [PrepareBank()](namespace_a_k_1_1_sound_engine_a7d92b3c386cd60e76be54ca69f051c09.html#a7d92b3c386cd60e76be54ca69f051c09) 的默认加载机制，它会检查 SoundBank 中需要载入内存池的媒体项。如果特定事件的媒体在 SoundBank 中不存在，则稍后可调用 [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 从松散文件中加载它。

## AkBankContent\_StructureOnly

在搭配 `AkBankContent_StructureOnly` 使用 [PrepareBank()](namespace_a_k_1_1_sound_engine_a7d92b3c386cd60e76be54ca69f051c09.html#a7d92b3c386cd60e76be54ca69f051c09) 时，会从 SoundBank 中加载事件和结构元数据，但会忽略 SoundBank 中包含的媒体。由于 [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 必须把媒体当作磁盘中的松散文件进行访问，并且无法读取包含在 SoundBank 中的文件，因此只有当您打算稍后使用其它加载机制加载 SoundBank 时，`AkBankContent_StructureOnly` 才有用。在使用 [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 分别加载媒体的大多数场景中，媒体不应包含在 SoundBank 中，`AkBankContent_StructureOnly` 标志将产生与 `AkBankContent_All` 相同的结果。

`AkBankContent_StructureOnly` 标志可能有用的一个场合是实现多个加载的配置。游戏可有使用 [PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238) 按需加载松散文件的“工具模式”，以及使用 [LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13) 整体加载同一 SoundBank 的“游戏模式”。

如果需要，可通过 API 同步或异步调用 [PrepareBank()](namespace_a_k_1_1_sound_engine_a7d92b3c386cd60e76be54ca69f051c09.html#a7d92b3c386cd60e76be54ca69f051c09)。然而，建议不要对同一 SoundBank 同时使用 `AkBankContent_All` 和`AkBankContent_StructureOnly` ，因为媒体一旦使用 `AkBankContent_All` 进行加载，卸载时将释放所有内容，包括事件、结构和媒体。

# 清空库

当您想要重置声音引擎的内容时，调用 `AK::SoundEngine::ClearBanks()` 函数非常有用。请注意，在调用 `SoundEngine::Term()` 之前，您不必调用 `ClearBanks()。ClearBanks 在内部调用` `AK::SoundEngine::ClearPreparedEvents`。

在调用此函数后：

- 所有声音停止播放。
- 所有 SoundBank 均会卸载，包括初始化包。
- 所有 State 管理信息均会清空，因为这些信息是初始化包的一部分。

# 清空已做了 Prepare 操作的事件

无论某个事件已经做了多少次 Prepare，调用 [AK::SoundEngine::ClearPreparedEvents()](namespace_a_k_1_1_sound_engine_af9648460be2ed1a0093ff09b42ef36f5.html#af9648460be2ed1a0093ff09b42ef36f5) 函数将取消到目前为止已做了 Prepare 操作的所有事件。在调用 `AK::SoundEngine::ClearBanks()` 时，内部将调用 `AK::SoundEngine::ClearPreparedEvents()` 。

# 复制库内容

各个 SoundBank 只可加载一次。如果您试图第二次显式加载某个库，则将导致 SoundBank 加载错误。

The Wwise sound engine allows you to have the same Events, sound structures, or media in two or more banks, and have them all loaded at the same time.

|  |  |
| --- | --- |
|  | **备注:** 对于不支持媒体重定位的 OpusNX，若某一声音同时用于多个正在播放的 SoundBank，而该 SoundBank 已被卸载，则将停止播放该声音。 播放不会过渡到其它有这份声音并且已加载的 SoundBank 中。 |

在使用 `PrepareEvent` 时，如果多个不同事件需要加载同一媒体内容，则内存中不会出现重复加载该媒体复制品的情况。 多个事件可引用同一媒体对象，只有当引用同一媒体对象的所有事件都被取消了 Prepare 操作时才会卸载此媒体对象。

Using `LoadBank` along with `PrepareEvent` to load the same media content may cause media duplication because banks are loaded as an entity when using `LoadBank`.

参见
:   - [集成详情—— SoundBank](soundengine_banks.html)
    - [一般信息](soundengine_banks_general.html)
    - [SoundBank 集成示例](sdk_bank_training.html)
    - [AK::SoundEngine::LoadBank()](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)
    - [AK::SoundEngine::UnloadBank()](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)
    - [AK::SoundEngine::ClearBanks()](namespace_a_k_1_1_sound_engine_ab934f98a6622976d24e0a096911eb0c8.html#ab934f98a6622976d24e0a096911eb0c8)
    - [AK::SoundEngine::PrepareEvent()](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)
    - [AK::SoundEngine::PrepareGameSyncs()](namespace_a_k_1_1_sound_engine_a76c611710ef7ffdd2d59f34e35b67cdc.html#a76c611710ef7ffdd2d59f34e35b67cdc)
    - [AK::SoundEngine::ClearPreparedEvents()](namespace_a_k_1_1_sound_engine_af9648460be2ed1a0093ff09b42ef36f5.html#af9648460be2ed1a0093ff09b42ef36f5)

[AkBankCallbackFunc](_ak_callback_types_8h_a5f4438e001923453a9f795eb64946be6.html#a5f4438e001923453a9f795eb64946be6)

void(\* AkBankCallbackFunc)(AkUInt32 in\_bankID, const void \*in\_pInMemoryBankPtr, enum AKRESULT in\_eLoadResult, void \*in\_pCookie)

**Definition:** [AkCallbackTypes.h:388](_ak_callback_types_8h_source.html#l00388)

[AK::SoundEngine::PrepareEvent](namespace_a_k_1_1_sound_engine_a2e6ebb779470b43d78984c27f6a0c238.html#a2e6ebb779470b43d78984c27f6a0c238)

AKSOUNDENGINE\_API AKRESULT PrepareEvent(PreparationType in\_PreparationType, const char \*\*in\_ppszString, AkUInt32 in\_uNumEvent)

[AkBankID](_ak_typedefs_8h_a472a3d18cbb0c4f081b3b619e4a2f349.html#a472a3d18cbb0c4f081b3b619e4a2f349)

AkUInt32 AkBankID

Run time bank ID

**Definition:** [AkTypedefs.h:54](_ak_typedefs_8h_source.html#l00054)

[AK::SoundEngine::LoadBankMemoryView](namespace_a_k_1_1_sound_engine_a7e8069027779f518a2049dffbb8ecbcb.html#a7e8069027779f518a2049dffbb8ecbcb)

AKSOUNDENGINE\_API AKRESULT LoadBankMemoryView(const void \*in\_pInMemoryBankPtr, AkUInt32 in\_uInMemoryBankSize, AkBankID &out\_bankID)

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560)

AkUInt64 AkGameObjectID

Game object ID

**Definition:** [AkTypedefs.h:39](_ak_typedefs_8h_source.html#l00039)

[AK::SoundEngine::RegisterGameObj](namespace_a_k_1_1_sound_engine_a895ed0f83a0dea8fc284491c0ee0152c.html#a895ed0f83a0dea8fc284491c0ee0152c)

AKSOUNDENGINE\_API AKRESULT RegisterGameObj(AkGameObjectID in\_gameObjectID)

[AK::SoundEngine::LoadBank](namespace_a_k_1_1_sound_engine_a95f8f6841a618ec3d5e51a30a1614e13.html#a95f8f6841a618ec3d5e51a30a1614e13)

AKSOUNDENGINE\_API AKRESULT LoadBank(const char \*in\_pszString, AkBankID &out\_bankID, AkBankType in\_bankType=AkBankType\_User)

[AK::SoundEngine::Preparation\_Unload](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba37375e4d359e99b67d0a69f4a5714b92)

@ Preparation\_Unload

PrepareEvent() will unload required information to play the specified event.

**Definition:** [AkSoundEngine.h:2706](_ak_sound_engine_8h_source.html#l02706)

[AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc)

AkUInt32 AkUniqueID

Unique 32-bit ID

**Definition:** [AkTypedefs.h:31](_ak_typedefs_8h_source.html#l00031)

[AK::SoundEngine::Preparation\_Load](namespace_a_k_1_1_sound_engine_a21e0dbb1f9aebfc22fdd88634dc1067b.html#a21e0dbb1f9aebfc22fdd88634dc1067ba7bb39cc6dfafe005cddfbf12c0d62ad0)

@ Preparation\_Load

PrepareEvent() will load required information to play the specified event.

**Definition:** [AkSoundEngine.h:2705](_ak_sound_engine_8h_source.html#l02705)

[AK::SoundEngine::UnloadBank](namespace_a_k_1_1_sound_engine_ac91406bc2fe061e4248cb448207b5a64.html#ac91406bc2fe061e4248cb448207b5a64)

AKSOUNDENGINE\_API AKRESULT UnloadBank(const char \*in\_pszString, const void \*in\_pInMemoryBankPtr, AkBankType in\_bankType=AkBankType\_User)

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63)

AKRESULT

**Definition:** [AkEnums.h:32](_ak_enums_8h_source.html#l00031)

[AK::SoundEngine::LoadBankMemoryCopy](namespace_a_k_1_1_sound_engine_ac16591355aef3ffaf2f8e9ac7a5b95ad.html#ac16591355aef3ffaf2f8e9ac7a5b95ad)

AKSOUNDENGINE\_API AKRESULT LoadBankMemoryCopy(const void \*in\_pInMemoryBankPtr, AkUInt32 in\_uInMemoryBankSize, AkBankID &out\_bankID)

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e)

@ AK\_Success

The operation was successful.

**Definition:** [AkEnums.h:34](_ak_enums_8h_source.html#l00034)

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)

AKSOUNDENGINE\_API AkPlayingID PostEvent(AkUniqueID in\_eventID, AkGameObjectID in\_gameObjectID, AkUInt32 in\_uFlags=0, AkCallbackFunc in\_pfnCallback=NULL, void \*in\_pCookie=NULL, AkUInt32 in\_cExternals=0, AkExternalSourceInfo \*in\_pExternalSources=NULL, AkPlayingID in\_PlayingID=AK\_INVALID\_PLAYING\_ID)