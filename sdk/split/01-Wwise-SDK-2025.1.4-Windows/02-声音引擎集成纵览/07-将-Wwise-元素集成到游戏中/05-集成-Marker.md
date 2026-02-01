# 集成 Marker

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

集成 Marker

# 简介

Marker（标记）是插入 WAV 文件并用在波形中标示位置的标识符。通常可以在 WAV 编辑器应用程序（例如 SoundForge®、Adobe® Audition® 或 CueTool）中创建这些标记。

当播放到特定位置时，应用程序可使用这些标记来获得通知。例如，您可以使用此信息将视觉内容的绘制与正在播放的音频同步，或者了解随机容器正在播放哪个文件，以便在游戏中显示正确的字幕。

|  |  |
| --- | --- |
|  | **备注:** 使用 Wwise 标记通知（Marker Notification）功能通常是集成对口型或字幕解决方案最高效的方式。 |

# 使用 .wav 文件格式

块（chunk）是用于存储提示点（cue point）或有关提示点的数据的数据存储单元。提示点是 .wav 格式文件中标示的兴趣点。

## 提示块

提示块（cue chunk）格式用于存储标记位置，标记位置用于提示 .wav 文件中的兴趣点。

偏移量 字节 说明 值

0x00 4 块 ID "cue " (0x63756520)

0x04 4 块数据大小 取决于提示点数量

0x08 4 提示点数量 列中提示点的数量

0x0c 提示点从此开始

#define CueID 'cue ' /\* 提示块的块 ID\*/

typedef struct {

ID chunkID;

long chunkSize;

long dwCuePoints;

CuePoint points[];

} CueChunk;

typedef struct {

long dwIdentifier;

long dwPosition;

ID fccChunk;

long dwChunkStart;

long dwBlockStart;

long dwSampleOffset;

} CuePoint;

## 列表块

列表块（list chunk）是包 .wav 文件内部的容器，其中包含子块。相关数据列表块（associated data list chunk，adtl）格式用于存储标签、注释以及与提示点的关联文本。

偏移量 字节 说明 值

0x00 4 块 ID "list" (0x6C696E74)

0x04 4 块数据大小 取决于包含的子块

0x08 4 类型 ID "adtl" (0x6164746C)

0x0c 子块从此开始

## 标签子块

标签子块（label sub-chunk）格式用于存储提示点的关联字符串。它应该位于关联数据列表块内。

偏移量 字节 说明 值

0x00 4 块 ID "labl" (0x6C61626C)

0x04 4 块数据大小 取决于文本大小

0x08 4 提示点 ID 参阅提示块 dwIdentifier

0x0c 标签（大小可变的文本）

# 使用源插件

源插件也可生成标记通知。

在源插件内，可使用 `AK::IAkPluginServiceMarkers::CreateMarkerNotificationService()` 创建 `AK::IAkPluginServiceMarkers::IAkMarkerNotificationService` 实例。然后，可使用 `AK::IAkPluginServiceMarkers::IAkMarkerNotificationService::SubmitMarkerNotifications()` 将标记通知发给使用 `AkAudioMarker` 结构的游戏。

struct [AkAudioMarker](struct_ak_audio_marker.html)

{

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) [dwIdentifier](struct_ak_audio_marker_adef1428c7f4476db4dbeee707eec8984.html#adef1428c7f4476db4dbeee707eec8984); ///< 标识符。

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) [dwPosition](struct_ak_audio_marker_a614e69d4179a70b5d096b1812b3bd876.html#a614e69d4179a70b5d096b1812b3bd876); ///< 音频数据中的位置（采样帧）。

const char\* [strLabel](struct_ak_audio_marker_aee87f10b0ad8d8bb5d226221479720a6.html#aee87f10b0ad8d8bb5d226221479720a6); ///< 从文件获取的标记的标签。

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) [dwLabelSize](struct_ak_audio_marker_aa1c572e31ad099fb92d0bae6cf1e15f7.html#aa1c572e31ad099fb92d0bae6cf1e15f7); ///< 从文件读取的标签 + 结尾空字符的长度。

};

## Marker Generator 源插件示例

下面举例展示了用于生成标记通知的源插件。

class MyMarkerGeneratorSourcePlugin : public IAkSourcePlugin

{

private:

IAkSourcePluginContext\* m\_pSourcePluginContext{};

IAkPluginServiceMarkers::IAkMarkerNotificationService\* m\_pMarkerNotificationService{};

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) m\_uElapsedSamples{};

static constexpr [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) g\_uPayloadSize{ 64 };

char m\_Payload[g\_uPayloadSize]{};

// ...

public:

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) [Init](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8)(

IAkPluginMemAlloc \* in\_pAllocator, ///< 插件所要使用的内存分配器的接口

IAkSourcePluginContext \* in\_pSourcePluginContext, ///< 源插件的上下文的接口

IAkPluginParam \* in\_pParams, ///< 插件参数的接口

[AkAudioFormat](struct_ak_audio_format.html) & io\_rFormat ///< 插件所生成的输出数据的音频格式（默认为单声道原生格式）

) override

{

m\_pSourcePluginContext = in\_pSourcePluginContext;

m\_pMarkerNotificationService = [AK\_GET\_PLUGIN\_SERVICE\_MARKERS](_i_ak_plugin_8h_aca83a0bac8086bebd99fd3b1290926b5.html#aca83a0bac8086bebd99fd3b1290926b5)(m\_pSourcePluginContext)->CreateMarkerNotificationService(m\_pSourcePluginContext);

return [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e);

}

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63) [Term](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f)(

IAkPluginMemAlloc \* in\_pAllocator ///< 插件所要使用的内存分配器的接口

) override

{

[AK\_GET\_PLUGIN\_SERVICE\_MARKERS](_i_ak_plugin_8h_aca83a0bac8086bebd99fd3b1290926b5.html#aca83a0bac8086bebd99fd3b1290926b5)(m\_pSourcePluginContext)->TerminateMarkerNotificationService(m\_pMarkerNotificationService);

return [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e);

}

void Execute(

[AkAudioBuffer](class_ak_audio_buffer.html) \* io\_pBuffer ///< 输入/输出缓冲区数据结构（原地处理）

) override

{

static constexpr [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) uNumMarkers{ 1 };

[AkAudioMarker](struct_ak_audio_marker.html) markers[uNumMarkers];

markers[0].[dwIdentifier](struct_ak_audio_marker_adef1428c7f4476db4dbeee707eec8984.html#adef1428c7f4476db4dbeee707eec8984) = 'mrkr';

markers[0].[dwPosition](struct_ak_audio_marker_a614e69d4179a70b5d096b1812b3bd876.html#a614e69d4179a70b5d096b1812b3bd876) = m\_uElapsedSamples;

markers[0].[strLabel](struct_ak_audio_marker_aee87f10b0ad8d8bb5d226221479720a6.html#aee87f10b0ad8d8bb5d226221479720a6) = m\_Payload;

markers[0].[dwLabelSize](struct_ak_audio_marker_aa1c572e31ad099fb92d0bae6cf1e15f7.html#aa1c572e31ad099fb92d0bae6cf1e15f7) = g\_uPayloadSize;

const [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) offsetsInBuffer[uNumMarkers]{ 0 };

m\_pMarkerNotificationService->SubmitMarkerNotifications(markers, offsetsInBuffer, uNumMarkers);

// 向前移动标记的位置

m\_uElapsedSamples += io\_pBuffer->[MaxFrames](class_ak_audio_buffer_a537445dce6e3ed09dd2c337fd73c6b41.html#a537445dce6e3ed09dd2c337fd73c6b41)();

}

// ...

};

# 如何使用标记通知

以下是有关如何设置应用程序，以使它能够接收标记通知的说明：

- 在发送播放事件时，应将 `AK_Marker` 标识添加到 `in_uiFlags` 。如果您还想收到End of Event（事件结束）通知，则应使用 `AK_EndOfEvent` | `AK_Marker` ，因为这些标志采取按位异或运算。

[AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3) [AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)(

[AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) in\_eventID, // Unique ID of the event

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) in\_gameObjectID, // Associated game object ID

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) in\_uFlags = 0, // Bitmask: see AkCallbackType

[AkCallbackFunc](_ak_callback_types_8h_af644072775b1cdd813e2d32792a22005.html#af644072775b1cdd813e2d32792a22005) in\_pfnCallback = NULL, // Callback function

void \* in\_pCookie = NULL // Callback cookie that will be sent to the callback function

// along with additional information

);

- 您的回调函数必须采用以下格式：

static void MarkersCallback(

[AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732) in\_eType, // Type of callback reason, in this case AK\_Marker on

// reception of a marker event.

[AkCallbackInfo](struct_ak_callback_info.html)\* in\_pCallbackInfo // 指向回调信息结构的指针，在本例中为

// AkMarkerCallbackInfo\*。

）

- 当您调用回调函数时，您首先需要检查传入的是哪种通知。例如，如果您只想处理`AK_Marker` 通知，则在收到任何其他事件类型时应返回。
- 根据通知的类型，您可以将`in_pCallbackInfo` 类型转换（typecast）为相应的信息结构类型。对于 AK\_Marker 通知，相应的信息结构类型为 AkMarkerCallbackInfo。

// 对应于 AK\_Marker 的回调信息结构。

struct [AkMarkerCallbackInfo](struct_ak_marker_callback_info.html) : public [AkEventCallbackInfo](struct_ak_event_callback_info.html)

{

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) [uIdentifier](struct_ak_marker_callback_info_aa7748e167a3ef098db4d9bb88be3489c.html#aa7748e167a3ef098db4d9bb88be3489c); // 提示点标识符

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) [uPosition](struct_ak_marker_callback_info_a3cee8ac29ebb9b0bb14d27317da99535.html#a3cee8ac29ebb9b0bb14d27317da99535); // 提示点中的位置（单位：采样帧）

const char\* [strLabel](struct_ak_marker_callback_info_a170f3dc5b73d97dcedfc3f94d258ace2.html#a170f3dc5b73d97dcedfc3f94d258ace2); // 标记的标签（以空字符为结尾）

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) [uLabelSize](struct_ak_marker_callback_info_a6fd9819cd571fafcf79fd0667722c4dd.html#a6fd9819cd571fafcf79fd0667722c4dd); // 标签字符串的大小（含结尾空字符）

};

- 如果之后您打算引用标签，则一定要复制`strLabel` 字符串成员的内容，因为在回调返回后，指针可能会被作废。

参见
:   [快速入门示例集成——事件](quickstart_sample_integration_events.html)

# 通知延迟

目前当缓冲区向下传递到硬件时发送通知。这意味着，发送通知与遇到标记之间存在一定延时。这样在真正播放与标记关联的声音之前，应用程序有足够的时间来收集并处理标记中的信息。

注意这个延时取决于平台。

# 回调线程

Marker 回调和 End of Event 回调从声音引擎的主线程完成。这意味着您的应用程序应从通知中收集它所需的全部信息，并立即返回。如果需要进行任何处理，则应当从通知中复制相关信息后，使用单独的线程来执行。

如果应用程序占用线程太久，声音引擎可能掉入 underrun（欠载运行）状态，导致输出停止播放。

注解
:   在回调函数返回后，声音引擎将释放被引用的数据，因此应复制来自回调函数的标签字符串。

# Wwise 捕获日志和标记

Wwise Profiler 可以显示来自声音引擎的标记通知。为此，必须确保启用 Profiler Settings 对话框中的 Markers Notification Data 选项。当播放到达标记处并已请求通知时，Capture Log 中将在新的一行中显示相关信息。注意，如果需要可以过滤掉这些通知，方法是取消选择 Capture Log Filter 对话框中的 Markers Notification Data 复选框。

参见
:   [集成详情——事件](soundengine_events.html)

[AkAudioMarker](struct_ak_audio_marker.html)

Defines the parameters of a marker.

**Definition:** [AkAudioMarker.h:16](_ak_audio_marker_8h_source.html#l00015)

[AkCallbackFunc](_ak_callback_types_8h_af644072775b1cdd813e2d32792a22005.html#af644072775b1cdd813e2d32792a22005)

AkEventCallbackFunc AkCallbackFunc

**Definition:** [AkCallbackTypes.h:350](_ak_callback_types_8h_source.html#l00350)

[AkMarkerCallbackInfo::strLabel](struct_ak_marker_callback_info_a170f3dc5b73d97dcedfc3f94d258ace2.html#a170f3dc5b73d97dcedfc3f94d258ace2)

const char \* strLabel

Label of the marker (null-terminated)

**Definition:** [AkCallbackTypes.h:183](_ak_callback_types_8h_source.html#l00183)

[AkEventCallbackInfo](struct_ak_event_callback_info.html)

**Definition:** [AkCallbackTypes.h:159](_ak_callback_types_8h_source.html#l00158)

[AkAudioMarker::dwIdentifier](struct_ak_audio_marker_adef1428c7f4476db4dbeee707eec8984.html#adef1428c7f4476db4dbeee707eec8984)

AkUInt32 dwIdentifier

Identifier.

**Definition:** [AkAudioMarker.h:17](_ak_audio_marker_8h_source.html#l00017)

[AkMarkerCallbackInfo](struct_ak_marker_callback_info.html)

**Definition:** [AkCallbackTypes.h:180](_ak_callback_types_8h_source.html#l00179)

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560)

AkUInt64 AkGameObjectID

Game object ID

**Definition:** [AkTypedefs.h:39](_ak_typedefs_8h_source.html#l00039)

[AkCallbackInfo](struct_ak_callback_info.html)

**Definition:** [AkCallbackTypes.h:273](_ak_callback_types_8h_source.html#l00272)

[AkAudioMarker::dwLabelSize](struct_ak_audio_marker_aa1c572e31ad099fb92d0bae6cf1e15f7.html#aa1c572e31ad099fb92d0bae6cf1e15f7)

AkUInt32 dwLabelSize

Length of label read the from the file + terminating null character.

**Definition:** [AkAudioMarker.h:20](_ak_audio_marker_8h_source.html#l00020)

[AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc)

AkUInt32 AkUniqueID

Unique 32-bit ID

**Definition:** [AkTypedefs.h:31](_ak_typedefs_8h_source.html#l00031)

[AK::Comm::Init](namespace_a_k_1_1_comm_a596691b552b507c26b4df958ee1c6de8.html#a596691b552b507c26b4df958ee1c6de8)

AKSOUNDENGINE\_API AKRESULT Init(const AkCommSettings &in\_settings)

[AK::Comm::Term](namespace_a_k_1_1_comm_a94e307d2974b89cc4fbc8ab0fef20d2f.html#a94e307d2974b89cc4fbc8ab0fef20d2f)

AKSOUNDENGINE\_API void Term()

[AkMarkerCallbackInfo::uIdentifier](struct_ak_marker_callback_info_aa7748e167a3ef098db4d9bb88be3489c.html#aa7748e167a3ef098db4d9bb88be3489c)

AkUInt32 uIdentifier

Cue point identifier

**Definition:** [AkCallbackTypes.h:181](_ak_callback_types_8h_source.html#l00181)

[AkMarkerCallbackInfo::uLabelSize](struct_ak_marker_callback_info_a6fd9819cd571fafcf79fd0667722c4dd.html#a6fd9819cd571fafcf79fd0667722c4dd)

AkUInt32 uLabelSize

Size of the label string (including the terminating null character)

**Definition:** [AkCallbackTypes.h:184](_ak_callback_types_8h_source.html#l00184)

[AkMarkerCallbackInfo::uPosition](struct_ak_marker_callback_info_a3cee8ac29ebb9b0bb14d27317da99535.html#a3cee8ac29ebb9b0bb14d27317da99535)

AkUInt32 uPosition

Position in the cue point (unit: sample frames)

**Definition:** [AkCallbackTypes.h:182](_ak_callback_types_8h_source.html#l00182)

[AKRESULT](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63)

AKRESULT

**Definition:** [AkEnums.h:32](_ak_enums_8h_source.html#l00031)

[AkAudioMarker::strLabel](struct_ak_audio_marker_aee87f10b0ad8d8bb5d226221479720a6.html#aee87f10b0ad8d8bb5d226221479720a6)

const char \* strLabel

Label of the marker taken from the file.

**Definition:** [AkAudioMarker.h:19](_ak_audio_marker_8h_source.html#l00019)

[AkCallbackType](_ak_callback_types_8h_a948c083ff18dc4c8dfe1d32cb0eb6732.html#a948c083ff18dc4c8dfe1d32cb0eb6732)

AkCallbackType

Type of callback. Used as a bitfield in methods AK::SoundEngine::PostEvent() and AK::SoundEngine::Dyn...

**Definition:** [AkCallbackTypes.h:61](_ak_callback_types_8h_source.html#l00060)

[AK\_GET\_PLUGIN\_SERVICE\_MARKERS](_i_ak_plugin_8h_aca83a0bac8086bebd99fd3b1290926b5.html#aca83a0bac8086bebd99fd3b1290926b5)

#define AK\_GET\_PLUGIN\_SERVICE\_MARKERS(plugin\_ctx)

**Definition:** [IAkPlugin.h:1988](_i_ak_plugin_8h_source.html#l01988)

[AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce)

uint32\_t AkUInt32

Unsigned 32-bit integer

**Definition:** [AkNumeralTypes.h:35](_ak_numeral_types_8h_source.html#l00035)

[AkAudioBuffer](class_ak_audio_buffer.html)

**Definition:** [AkCommonDefs.h:310](_ak_common_defs_8h_source.html#l00309)

[AkAudioMarker::dwPosition](struct_ak_audio_marker_a614e69d4179a70b5d096b1812b3bd876.html#a614e69d4179a70b5d096b1812b3bd876)

AkUInt32 dwPosition

Position in the audio data in sample frames.

**Definition:** [AkAudioMarker.h:18](_ak_audio_marker_8h_source.html#l00018)

[AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e)

@ AK\_Success

The operation was successful.

**Definition:** [AkEnums.h:34](_ak_enums_8h_source.html#l00034)

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)

AKSOUNDENGINE\_API AkPlayingID PostEvent(AkUniqueID in\_eventID, AkGameObjectID in\_gameObjectID, AkUInt32 in\_uFlags=0, AkCallbackFunc in\_pfnCallback=NULL, void \*in\_pCookie=NULL, AkUInt32 in\_cExternals=0, AkExternalSourceInfo \*in\_pExternalSources=NULL, AkPlayingID in\_PlayingID=AK\_INVALID\_PLAYING\_ID)

[AkAudioFormat](struct_ak_audio_format.html)

Defines the parameters of an audio buffer format.

**Definition:** [AkCommonDefs.h:61](_ak_common_defs_8h_source.html#l00060)

[AkPlayingID](_ak_typedefs_8h_a9270609771369ea575443fe080bbe9c3.html#a9270609771369ea575443fe080bbe9c3)

AkUInt32 AkPlayingID

A unique identifier generated whenever a PostEvent is called (or when a Dynamic Sequence is created)....

**Definition:** [AkTypedefs.h:34](_ak_typedefs_8h_source.html#l00034)

[AkAudioBuffer::MaxFrames](class_ak_audio_buffer_a537445dce6e3ed09dd2c337fd73c6b41.html#a537445dce6e3ed09dd2c337fd73c6b41)

AkForceInline AkUInt16 MaxFrames() const

**Definition:** [AkCommonDefs.h:489](_ak_common_defs_8h_source.html#l00489)