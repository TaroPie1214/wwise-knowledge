# 集成 External Source

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

集成 External Source

External Source 是在 Wwise 里您可以放到声音对象中的一种特殊类型的源（Source）。它表明在运行时将采用真实声音数据。这对于管理大量对白非常有用。如果没有它，则需要为每行对白准备一个声音对象和一个事件，并需要将声音对象和事件打包到 SoundBank 中，并进行适当的分包管理。如果已经在使用别的系统（例如由人工智能驱动的语音生成器）管理对白，则 External Source 也同样非常有用。

在 Wwise 中创建 External Source 的方式与创建其他源插件一样，都是通过**Add Source**按钮，如果需要，可让它成为复杂结构的一部分。在游戏端，使用 External Source 播放事件与播放其他声音一样都是通过 [AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e) 和 [AK::SoundEngine::DynamicSequence::Playlist::Enqueue](class_a_k_1_1_sound_engine_1_1_dynamic_sequence_1_1_playlist_a9155f633c7fdda4283d318d89c2cd4bb.html#a9155f633c7fdda4283d318d89c2cd4bb) 来实现的。The actual audio data source information must be provided when an Event with an external source is posted. The decision of which data to play is left entirely to the programmer. 这同时意味着源文件的文件管理是在 Wwise 声音引擎外部来完成的。虽然这需要更多的工作量，但同时也提高了灵活性。

The audio data can be provided either as the path to a file to stream or as a memory pointer. Two formats are supported: Wwise's native WEM format and WAV files. We recommend using the WEM format because it is optimized for Wwise and the target platforms. In some occasions, WAV files can be more convenient, but they have some limitations:

- They must be PCM encoded.
- They can only be streamed from a file, in-memory data is not supported.
- Wwise will do its best to map the audio channels correctly, but it may not always give the expected results.

# External Source 的转码

If you opt to used the recommended WEM proprietary format; you will need to convert your input files in order to pass them to the sound engine at runtime. 对此，可通过 Wwise 设计工具中的 External Sources List 文件来实现。这个 XML 文件包含转码所需的全部文件以及所要使用的转码设置。要指定 wsources 文件，请访问 External Sources 选项卡中的 Project Settings。以下是此文件的示例：

<?xml version="1.0" encoding="UTF-8"?>

<ExternalSourcesList SchemaVersion="1" Root="d:\TestProject\ExternalSources">

<[Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af) Path="kaaboom.wav" Conversion="VeryCompressed" />

<[Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af) Path="SomeOtherFolderInTheProject\working.wav" Conversion="PCM"/>

<[Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af) Path="d:\FolderOutsideTheProject\out.wav" Conversion="PCM" Destination="out.wav"/>

<[Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af) Path="..\RelativeOutsideTheProject\relative.wav" Conversion="PCM" Destination="relative.wav"/>

<[Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af) Path="MyHdrSound.wav" Conversion="PCM" AnalysisTypes="6"/>

</ExternalSourcesList>

Root 属性指定源条目的根路径。如果省略此属性，则工程目录将被视为根路径。Root 路径可以是完整路径，也可以是相对于工程目录的相对路径。

Source 条目指定要转码的一个文件：

- Path 始终代表相对于 Root 的路径。
- Conversion 属性是用于转码文件的 Conversion Setting ShareSet（转码设置共享集）的名称。如果未指定，它则将使用工程的 Default Conversion Setting（默认转码设置）。
- Destination 属性是可选的，可让您指定不同的目标文件名和路径。此路径是 Project Settings 或命令行中指定的输出路径的相对路径。您也可以使用此属性对文件重命名。注意，您不能只使用文件路径：您还需要指定文件名。另外，无论 Destination 属性的扩展名是什么，转码文件的扩展名始终是“.wem”。如果未指定 Destination 属性，则输出路径中总是会复制 Root 目录下的文件夹层级结构。如果您使用 Root 目录外的文件，则必须指定 Destination 属性。
- AnalysisTypes（分析类型）用于确定转码文件的文件头中应包含的分析元数据类型。声音引擎可使用的分析类型目前有两种：Loudness（响度）和 HDR。 – 响度用于响度归一化，如果某目标声音结构勾选了“Enable Loudness Normalization”复选框，则您应该为其 External Source 添加 Loudness 分析类型。要包含 Loudness 分析类型，则要设置 AnalysisTypes 为 2。 – HDR 主要由声音的包络构成。如果您打算为勾选了“Enable Envelope”复选框的目标结构使用HDR系统，则应在其内源中包含 HDR 分析类型。要包含 HDR 分析类型，则要设置 AnalysisTypes 为 4。 – 设置 AnalysisTypes 为 6（即 2 + 4）会同时包含这两种类型。

External Source 的转码是在生成 SoundBank 时与所有其他文件转码一起自动完成的。注意，已经转好码的文件不会再白白重新转码。

|  |  |
| --- | --- |
|  | **注意:** 为了避免重新转码，Wwise 会将一些数据保存到输出目录下的 Wwise.dat 文件中。此文件对于游戏来说不是必要的，因此不应包含在最终发布的文件中。如果此文件已被删除，在所有波形文件将重新转码。 |

输入目录的目录结构将相对于根目录复制到输出目录下。在上述示例中，输出目录包含“ExternalSources”文件夹和"Lower Tests\Originals\SFX"文件夹。注意，路径中包含的“..”将被去除，而从该路径中第一个真正的文件夹开始。

# 命令行转码

通过命令行工具，还可只转码工程的 External Source。例如，此命令将为 Xbox One 转码 External Source，不会产生 SoundBank。

"%WWISEROOT%\Authoring\x64\Release\bin\WwiseConsole.exe" convert-external-source "C:\Project name.wproj" --platform XBoxOne

有关命令行工具（(WwiseConsole）的详情，请参阅 [使用命令行](bankscommandline.html) 。

# 流播放与内存播放

To provide the audio data to the sound engine, you can either specify a file name or a data pointer (WEM format only) in the [AkExternalSourceInfo](struct_ak_external_source_info.html) structure. 这样会完全覆盖 Wwise 工程中声音对象上的 Streaming 复选框。当使用数据指针时，您将负责内存管理，并确保在整个播放期间数据一直保持在内存中。

当指定文件名时，文件将被打开，并像正常的流播放文件一样从磁盘中流式播放。文件在磁盘中的位置必须在 Low-Level I/O（底层 I/O） 子系统中通过实现 File Location Resolver（文件位置解析器）来解析。请参阅 [Low-Level I/O](streamingmanager_lowlevel.html) 了解有关 Low-Level I/O 子系统的详情。

默认的文件位置解析器服务位于 CAkFileLocationBase 中，并作为 SDK 中的示例提供给用户（请参阅 [默认底层 I/O 实现](samplecode.html#samplecode_integration_defaultlowlevelio) ）。该实现不支持子文件夹；它假定各个 External Source 流播放文件与“标准”的流播放文件放在同一位置。

Wwise Stream Manager 会将标记传给 [AK::StreamMgr::IAkLowLevelIOHook::BatchOpen()](class_a_k_1_1_stream_mgr_1_1_i_ak_low_level_i_o_hook_a0abfde848b599b5e5b8e8ed63dc8b555.html#a0abfde848b599b5e5b8e8ed63dc8b555) 以便用户正确解析文件位置 ([AkFileSystemFlags](struct_ak_file_system_flags.html "File system flags for file descriptors mapping."))。在此抽象层次上，通过使用“公司 ID”（AkFileSystemFlags::uCompanyID），您可以将 External Source 与标准流播放文件区分开来。对于 SoundBank 和标准流播放文件，Wwise 传递的是 AKCOMPANYID\_AUDIOKINETIC，而对于 External Source，传递的则是 AKCOMPANYID\_AUDIOKINETIC\_EXTERNAL。因此您可以使用此值来搜索磁盘别的位置上的 External Source。

|  |  |
| --- | --- |
|  | **备注:** [AkFileSystemFlags::bIsLanguageSpecific](struct_ak_file_system_flags_a6fc45a77ef8411269da43d3d63b669db.html#a6fc45a77ef8411269da43d3d63b669db "True when the file location depends on language") is always set to false with external sources, even if the external source was included in a "Voice" sound structure. 事实上，我们建议您在独立于语言的 Sound SFX 对象中使用 External Source 而不要在 Sound Voice 中使用。当在 [AkExternalSourceInfo](struct_ak_external_source_info.html) 中指定文件名或 ID 时，必须从一开始就处理本地化。 |

# 示例：通过 External Source 机制播放单个声音

工程必须包括：

- 名为 MySound 的声音，并且配备一个名字也为“MyExternal”的 External Source（通过“Add Source”按钮添加）
- 播放事件“Play\_MySound”
- 包含了该事件的 SoundBank
- Project Settings 中的 External Sources List 文件（见上例）
- The External Sources List file must define the source "One.wav" (implicitly converted into "One.wem").

[AkExternalSourceInfo](struct_ak_external_source_info.html) source;

source.[iExternalSrcCookie](struct_ak_external_source_info_a198a69d12cc42071f764a6f793060c77.html#a198a69d12cc42071f764a6f793060c77) = [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)("MyExternal"); // cookie 是 External Source 对象名称的哈希索引。

source.[szFile](struct_ak_external_source_info_af29151c09e6b12f9b4f5b4c9a9389ba1.html#af29151c09e6b12f9b4f5b4c9a9389ba1) = [AKTEXT](_platforms_2_windows_2_ak_types_8h_ab37c4500d1c5377b3f54077b8222dde7.html#ab37c4500d1c5377b3f54077b8222dde7)("One.wem"); //The file we're going to play.

source.[idCodec](struct_ak_external_source_info_aa414d16c9d27dee981e13ce4ba8da2d5.html#aa414d16c9d27dee981e13ce4ba8da2d5) = [AKCODECID\_PCM](_ak_constants_8h_a9d668f1ec7a3a4f5bada195815866870.html#a9d668f1ec7a3a4f5bada195815866870); //The file is in PCM.

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)( "Play\_MySound", 2, 0, NULL, 0, 1, &source );

source.[szFile](struct_ak_external_source_info_af29151c09e6b12f9b4f5b4c9a9389ba1.html#af29151c09e6b12f9b4f5b4c9a9389ba1) = [AKTEXT](_platforms_2_windows_2_ak_types_8h_ab37c4500d1c5377b3f54077b8222dde7.html#ab37c4500d1c5377b3f54077b8222dde7)("Two.wav"); //Let's play a different file with the same event/source, in WAV format

source.[idCodec](struct_ak_external_source_info_aa414d16c9d27dee981e13ce4ba8da2d5.html#aa414d16c9d27dee981e13ce4ba8da2d5) = [AKCODECID\_PCM\_WAV](_ak_constants_8h_a2550b7306afb24dac74d1753b00e7f00.html#a2550b7306afb24dac74d1753b00e7f00); //The file is in PCM, WAV format.

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)( "Play\_MySound", 2, 0, NULL, 0, 1, &source );

|  |  |
| --- | --- |
|  | **备注:** When using WEM files, the extension of the file has to be ".wem". 在 External Sources List 文件中，您可以重命名目标文件，但不可更改其扩展名。一旦转码，文件的扩展名始终为“.wem”。如果您将转码好的文件打包成 File Package（文件包），则还需要在代码中用其扩展名“.wem”引用它：File Packager（文件打包器）通过哈希算法来为完整名称（包括扩展名）来生成查询 ID。 |

# 示例：使用多个 External Source 播放事件

您可以通过一个单一事件替换许多波形文件。例如，您可以设置装有 3 个 External Source 的序列容器。如果事件可触发播放多个 External Source，则这些 External Source 在整个工程中不得重名（因此各自能有独一无二的 cookie），以便在填充 [AkExternalSourceInfo](struct_ak_external_source_info.html) 结构时能够区分它们。

工程必须包括：

- 名为 MyExternalSequence 的序列容器，装有 3 个声音，每个声音有一个 External Source（通过“Add Source”按钮添加）
- 源名称应为 1、2 和 3，以便我们能够分别替换它们。
- 播放事件“Play\_MyExternalSequence”
- 包含了该事件的 SoundBank
- 工程设置中的 External Source 列表（见上例）
- External Source 列表必须定义源“One.wav”、“Four.wav”和“Five.wav”（分别在“One.wem”、“Four.wem”和“Five.wem”中隐式转码）。

[AkExternalSourceInfo](struct_ak_external_source_info.html) sources[3];

sources[0].[iExternalSrcCookie](struct_ak_external_source_info_a198a69d12cc42071f764a6f793060c77.html#a198a69d12cc42071f764a6f793060c77) = [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)("Extern\_1st\_number");

sources[0].[szFile](struct_ak_external_source_info_af29151c09e6b12f9b4f5b4c9a9389ba1.html#af29151c09e6b12f9b4f5b4c9a9389ba1) = [AKTEXT](_platforms_2_windows_2_ak_types_8h_ab37c4500d1c5377b3f54077b8222dde7.html#ab37c4500d1c5377b3f54077b8222dde7)("Five.wem");

sources[0].[idCodec](struct_ak_external_source_info_aa414d16c9d27dee981e13ce4ba8da2d5.html#aa414d16c9d27dee981e13ce4ba8da2d5) = [AKCODECID\_PCM](_ak_constants_8h_a9d668f1ec7a3a4f5bada195815866870.html#a9d668f1ec7a3a4f5bada195815866870);

sources[1].[iExternalSrcCookie](struct_ak_external_source_info_a198a69d12cc42071f764a6f793060c77.html#a198a69d12cc42071f764a6f793060c77) = [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)("Extern\_2nd\_number");

sources[1].[szFile](struct_ak_external_source_info_af29151c09e6b12f9b4f5b4c9a9389ba1.html#af29151c09e6b12f9b4f5b4c9a9389ba1) = [AKTEXT](_platforms_2_windows_2_ak_types_8h_ab37c4500d1c5377b3f54077b8222dde7.html#ab37c4500d1c5377b3f54077b8222dde7)("One.wem");

sources[1].[idCodec](struct_ak_external_source_info_aa414d16c9d27dee981e13ce4ba8da2d5.html#aa414d16c9d27dee981e13ce4ba8da2d5) = [AKCODECID\_PCM](_ak_constants_8h_a9d668f1ec7a3a4f5bada195815866870.html#a9d668f1ec7a3a4f5bada195815866870);

sources[2].[iExternalSrcCookie](struct_ak_external_source_info_a198a69d12cc42071f764a6f793060c77.html#a198a69d12cc42071f764a6f793060c77) = [AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)("Extern\_3rd\_number");

sources[2].[szFile](struct_ak_external_source_info_af29151c09e6b12f9b4f5b4c9a9389ba1.html#af29151c09e6b12f9b4f5b4c9a9389ba1) = [AKTEXT](_platforms_2_windows_2_ak_types_8h_ab37c4500d1c5377b3f54077b8222dde7.html#ab37c4500d1c5377b3f54077b8222dde7)("Four.wem");

sources[2].[idCodec](struct_ak_external_source_info_aa414d16c9d27dee981e13ce4ba8da2d5.html#aa414d16c9d27dee981e13ce4ba8da2d5) = [AKCODECID\_VORBIS](_ak_constants_8h_ae231b80b0548ed6445a06698b8281f18.html#ae231b80b0548ed6445a06698b8281f18); //The codec can be different for each source, if needed

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)( "Play\_MyExternalSequence", 2, 0, NULL, 0, 3, sources );

# Wwise Unreal 集成Examples

For more information about how to use external sources in projects integrated with Unreal, see Wwise Unreal 集成documentation:

- [使用 External Source](https://www.audiokinetic.com/library/edge/?source=UE4&id=using_features_ext_src.html) (Wwise Unreal Integration)

[AkExternalSourceInfo::idCodec](struct_ak_external_source_info_aa414d16c9d27dee981e13ce4ba8da2d5.html#aa414d16c9d27dee981e13ce4ba8da2d5)

AkCodecID idCodec

Codec ID for the file. One of the audio formats defined in AkTypes.h (AKCODECID\_XXX)

**Definition:** [AkSoundEngineTypes.h:189](_ak_sound_engine_types_8h_source.html#l00189)

[AkExternalSourceInfo::szFile](struct_ak_external_source_info_af29151c09e6b12f9b4f5b4c9a9389ba1.html#af29151c09e6b12f9b4f5b4c9a9389ba1)

const char \* szFile

UTF-8 File path for the source. If not NULL, the source will be streaming from disk....

**Definition:** [AkSoundEngineTypes.h:190](_ak_sound_engine_types_8h_source.html#l00190)

[AKCODECID\_PCM](_ak_constants_8h_a9d668f1ec7a3a4f5bada195815866870.html#a9d668f1ec7a3a4f5bada195815866870)

#define AKCODECID\_PCM

PCM encoding

**Definition:** [AkConstants.h:116](_ak_constants_8h_source.html#l00116)

[AkExternalSourceInfo::iExternalSrcCookie](struct_ak_external_source_info_a198a69d12cc42071f764a6f793060c77.html#a198a69d12cc42071f764a6f793060c77)

AkUInt32 iExternalSrcCookie

Cookie identifying the source, given by hashing the name of the source given in the project....

**Definition:** [AkSoundEngineTypes.h:188](_ak_sound_engine_types_8h_source.html#l00188)

[AkExternalSourceInfo](struct_ak_external_source_info.html)

**Definition:** [AkSoundEngineTypes.h:128](_ak_sound_engine_types_8h_source.html#l00127)

[AKCODECID\_VORBIS](_ak_constants_8h_ae231b80b0548ed6445a06698b8281f18.html#ae231b80b0548ed6445a06698b8281f18)

#define AKCODECID\_VORBIS

Vorbis encoding

**Definition:** [AkConstants.h:119](_ak_constants_8h_source.html#l00119)

[AKTEXT](_platforms_2_windows_2_ak_types_8h_ab37c4500d1c5377b3f54077b8222dde7.html#ab37c4500d1c5377b3f54077b8222dde7)

#define AKTEXT(x)

**Definition:** [AkTypes.h:159](_platforms_2_windows_2_ak_types_8h_source.html#l00159)

[AKCODECID\_PCM\_WAV](_ak_constants_8h_a2550b7306afb24dac74d1753b00e7f00.html#a2550b7306afb24dac74d1753b00e7f00)

#define AKCODECID\_PCM\_WAV

Standard PCM WAV file parser

**Definition:** [AkConstants.h:121](_ak_constants_8h_source.html#l00121)

[AK.Wwise::Plugin::Source](namespace_a_k_1_1_wwise_1_1_plugin_a6397b4db19f43bd157d4851720f838af.html#a6397b4db19f43bd157d4851720f838af)

V1::Source Source

Latest version of the C++ Source interface.

**Definition:** [Source.h:173](_source_8h_source.html#l00173)

[AK::SoundEngine::GetIDFromString](namespace_a_k_1_1_sound_engine_a1aae6ebdec25946fb2897ce0e025366d.html#a1aae6ebdec25946fb2897ce0e025366d)

AKSOUNDENGINE\_API AkUInt32 GetIDFromString(const char \*in\_pszString)

[AK::SoundEngine::PostEvent](namespace_a_k_1_1_sound_engine_a41e9ef8d42951871fe4a8ae58a29a68e.html#a41e9ef8d42951871fe4a8ae58a29a68e)

AKSOUNDENGINE\_API AkPlayingID PostEvent(AkUniqueID in\_eventID, AkGameObjectID in\_gameObjectID, AkUInt32 in\_uFlags=0, AkCallbackFunc in\_pfnCallback=NULL, void \*in\_pCookie=NULL, AkUInt32 in\_cExternals=0, AkExternalSourceInfo \*in\_pExternalSources=NULL, AkPlayingID in\_PlayingID=AK\_INVALID\_PLAYING\_ID)