# Wwise Authoring Query Language (WAQL) 参考

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Wwise Authoring Query Language (WAQL) 参考

# 概述

Wwise Authoring Query Language (WAQL) 方便查询 Wwise 工程及其对象。如需进一步了解 WAQL 中的各种概念，请参阅 [使用 Wwise Authoring Query Language (WAQL)](waql_introduction.html) 章节。 查询具有以下几种形式：

|  |  |
| --- | --- |
| 概览 | 说明 |
| $ **SOURCE**  $ **SOURCE** **TRANSFORM**  $ **SOURCE** **TRANSFORM**, **TRANSFORM**, ...  $ **TRANSFORM** | **SOURCE** 为对象生成器，其会输出对象序列。有关不同查询源的详细信息，请参阅下表。    **TRANSFORM** 为序列转换。其会接收输入序列，并输出另一序列。    **注意：**若未指定源，则将工程中定义的所有对象隐式设为查询源。 |

# 参考

## Sources

Specify the starting point of the query.

| SOURCE | Query Source | IntegrationDemo 工程中所要执行的 WAQL 查询 |
| --- | --- | --- |
| from object **OBJECT\_SPECIFIER**  from object **OBJECT\_SPECIFIER**, **OBJECT\_SPECIFIER**, ...  **OBJECT\_SPECIFIER**  **OBJECT\_SPECIFIER**, **OBJECT\_SPECIFIER** | 从指定的对象生成对象序列。    **OBJECT\_SPECIFIER** 具有以下几种形式：   - **路径**：对象的绝对路径，以反斜杠为开头，含顶层物理文件夹，前后加双引号。 - **GUID**：128 位 GUID，两边带大括号，前后加双引号。 - **唯一限定名称**：对象名称，前缀对象类型，前后加双引号。仅适用于在整个项目中强制使用唯一名称的对象类型：Event、Bus、Effect、GameParameter 等。 - **唯一限定 ID**：对象 ID（32 位短 ID），前缀对象类型，前后加双引号。仅适用于在整个项目中强制使用唯一名称的对象类型：Event、Bus、Effect、GameParameter 等。 | $ from object "\Containers\Default Work Unit\Hello"  $ from object "\Busses\Default Work Unit\Main Audio Bus"  $ from object "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}"  $ from object "Event:Play\_Hello"  $ from object "Event:2952797154"  $ from object "Event:Play\_Hello", "Bus:Main Audio Bus"  $ "Event:Play\_Hello", "Bus:Main Audio Bus"  $ "\Containers" |
| from type **OBJECT\_TYPE**  from type **OBJECT\_TYPE**, **OBJECT\_TYPE**, ... | 从指定的类型生成对象序列。可指定一种或多种对象类型。    **OBJECT\_TYPE** 为 Wwise 对象类型。有关对象类型的完整列表，请参阅 [Wwise 对象参考](wobjects_index.html) 章节。该类型不区分大小写。 | $ from type Event  $ from type sound  $ from type Sound  $ from type randomSequenceContainer, switchContainer, blendContainer  $ from type bus |
| from query **QUERY\_SPECIFIER** | 从 Query Editor 中所定义 Wwise Query 的执行结果生成对象序列。    **QUERY\_SPECIFIER** 具有以下几种形式：   - **路径**：对象的绝对路径，以反斜杠为开头，含顶层物理文件夹，前后加双引号。 - **GUID**：128 位 GUID，两边带大括号，前后加双引号。   **注意**：此生成器要求内存分配大小等于所生成序列的大小。 | $ from query "\Queries\Factory Queries\Audio Source\Audio Source - Format = Vorbis"  $ from query "{4D1B2AA5-19D8-44D3-AAE5-94024469CE7C}" |
| from search **TEXT** | 从整个工程的文本搜索结果生成对象序列。    **TEXT** 为前后加双引号的文本字符串。将搜索文本中指定的每个单词与工程对象内的单词匹配。    **注意**：结果与 Wwise 工具栏搜索相同。 | $ from search "gun"  $ from search "foot walk" |
| from project | 生成包含工程中所有对象的对象序列。 | $ from project |

## Transforms

Change a sequence of objects into another one.

| TRANSFORM | 可联用的转换 | 示例 |
| --- | --- | --- |
| where **BOOLEAN\_EXPRESSION** | 对输入序列的对象进行筛选，并滤掉那些与指定表达式不匹配的对象。    **BOOLEAN\_EXPRESSION** 为可返回 true 或 false 的表达式。针对输入队列的每个对象执行该表达式，并滤掉那些表达式返回结果为 false 的对象。    有关详细信息，请参阅表达式部分。 | $ from type Sound where @Volume < 0  $ from type Sound where -1 = @Volume  $ from type Sound where @OutputBus="Bus:Main Audio Bus"  $ from type Sound where @UserAuxSend0="AuxBus:Hangar\_Env"  $ from type Event select children where @Target.path : "hello"  $ from type RandomSequenceContainer where childrenCount > 2 and childrenCount <= 4  $ from type Sound where notes : "All"  $ from type Sound where notes : "\*audiokinetic\*"  $ from type Sound where @UserAuxSend0 != null |
| skip **COUNT** | 跳过输入序列中指定数量的对象，然后返回其余对象。    **COUNT** 为所要跳过的元素数量。 | $ from type Sound skip 10 |
| take **COUNT** | 从输入序列的开头连续返回指定数量的对象。    **COUNT** 为所要返回的元素数量。 | $ from type Sound take 10 |
| select **OBJECT\_EXPRESSION** | 将输入序列的各个对象转换为新的形式。    **OBJECT\_EXPRESSION** 为可返回零到多个对象的表达式。针对输入队列的每个对象执行该表达式，并将表达式的结果转换为新的序列。    有关详细信息，请参阅表达式部分。 | $ from object "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}" select parent  $ from object "Bus:Main Audio Bus" select children  $ from object "\Containers\Default Work Unit" select descendants, this where @Volume < 0  $ from object "\Containers\Default Work Unit\Hello" select @OutputBus  $ from object "{CBCD492C-982D-4EE4-AE75-0019CA6577EF}" select parent.@Attenuation |
| orderby **VALUE\_EXPRESSION**    orderby **VALUE\_EXPRESSION** reverse | 按升序顺序排列并返回输入序列的对象。若要按降序顺序排列，请在表达式之后添加 **reverse**。    **VALUE\_EXPRESSION** 为用于结合排序算法对对象进行比较的表达式。该表达式必须返回可比较值，如字符串、数字值或布尔值。    **注意**：orderby 要求内存分配大小等于输入序列的大小。 | $ from type Sound orderby name  $ from type Sound orderby name reverse  $ from type Bus orderby @BusVolume  $ from type Action orderby @Target.name |
| distinct | 仅返回输入序列的独特对象。重复的对象条目将被合并为一个条目，确保序列中的每个对象都是唯一的。    **注意**：distinct 会改变序列的顺序。为此，最好将 orderby 语句放在 distinct 语句之后。    **注意**：distinct 要求内存分配大小等于输入序列的大小。 | $ from object "\Containers" select descendants select @OutputBus distinct |

## Expressions

Select other objects, or values associated with the objects, in the sequence.

| 对象表达式 | 可返回零到多个对象的表达式 | 示例 |
| --- | --- | --- |
| **OBJECT\_EXPRESSION**    **OBJECT\_EXPRESSION**.**OBJECT\_EXPRESSION...** | 可使用零到多个对象表达式来返回 Wwise 对象。使用点号分隔各个表达式。 | $ from object "Event:Play\_Hello" select parent.parent |
| **REFERENCE\_NAME**  @**REFERENCE\_NAME**  @@**REFERENCE\_NAME** | 返回被当前对象引用的对象以获取特定引用名称。    若使用 @，则使用对象上直接定义的引用。    若不用 @，则使用 Override 设置查找引用值。该值为播放时所用的实际值。若存在同名的访问器，则优先使用该值；在这种情况下，须在引用名称之前使用 @@。    **REFERENCE\_NAME** 为当前对象的引用名称。有关对象类型及相关引用的完整列表，请参阅 [Wwise 对象参考](wobjects_index.html) 章节。该名称不区分大小写。 | $ from type Sound select OutputBus  $ from type Sound select effects  $ from type Sound select @@Effects  $ from type Sound where outputBus="Bus:Main Audio Bus" |
| children | 返回对象的直接子对象 (children)。 | $ from object "\Containers\Default Work Unit" select children |
| descendants | 返回单个序列中所含对象的全部下级对象 (descendant)。这些下级对象包括所有以递归方式获取的子对象。    **注意**：不包含当前对象。若要包含当前对象，请使用 select descendants, this。 | $ from object "\Containers\Default Work Unit" select descendants  $ from object "\Containers\Default Work Unit" select descendants, this |
| this | 返回当前对象。 | $ from object "\Busses\Default Work Unit\Main Audio Bus" select this, descendants |
| parent | 返回对象的直接父对象 (parent)。若对象没有父对象，则不返回任何对象。 | $ from type Sound select parent  $ from type Sound where parent.name : "\*engine" |
| ancestors | 返回单个序列中所含对象的全部上级对象 (ancestor)。这些上级对象包括所有以递归方式获取的父对象。    **注意**：不包含当前对象。若要包含当前对象，请使用 select ancestors, this。 | $ from object "Event:Play\_Hello" select ancestors  $ from object "Event:Play\_Hello" select ancestors, this |
| referencesTo | 返回所有引用当前对象的对象。 | $ from type Effect select referencesTo  $ "Event:Play\_Hello" select referencesTo |
| owner | 返回对象的所有者。仅其他对象之内定义的 Custom 对象设有所有者。    Shareset 对象没有所有者。它们有父对象 (**parent**) 和引用它们的对象 (**referencesTo**)。    比如，Custom 效果器的所有者为以其作为插入效果器的对象。 | $ from type Effect select owner  $ from type Effect where owner.name :"\*env" |
| randomizer("<strong>PROPERTY\_NAME</strong>") | Returns the randomizer object associated with the specified property. Use the following properties on the randomizer object: min, max, enabled.    **PROPERTY\_NAME** 为当前对象的属性名称。Refer to [Wwise 对象参考](wobjects_index.html) for the complete list of object types and their properties. 该名称不区分大小写。 | $ from type sound where randomizer("pitch") != null   $ from type sound where randomizer("highpass").min < 0  $ from type sound where randomizer("lowpass").max > 0  $ from type sound where randomizer("volume").enabled = true |
| state("<strong>STATE\_NAME</strong>") | Returns the custom state object associated with the specified state.    **STATE\_NAME** refers to the qualified name, path or GUID of a state for the current object. See [Wwise 对象参考](wobjects_index.html) for the complete list of object types and their properties. 该名称不区分大小写。 | $ from type sound where state("State:myState") != null   $ from type sound where state("{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}") != null |
| workunit | 返回用于保存当前对象的 Work Unit 对象。 | $ from type Effect select workunit |
| musicTransitionRoot | (DEPRECATED) Returns the Music Transition root object associated with the current object. This is deprecated. The TransitionRoot reference should be used instead.    **注意**：该表达式仅适用于 MusicSegment、MusicTrack、MusicPlaylistContainer 和 MusicSwitchContainer 类型的对象。 | $ from project select musicTransitionRoot |
| musicTransitionObject | Returns the object associated with the current music transition object.    **Note**: This only works with objects of type MusicTransition. | $ from type musictransition select musicTransitionObject |
| musicPlaylistRoot | (DEPRECATED) Returns the Music Playlist root object associated with the current object. This is deprecated. The PlaylistRoot reference should be used instead.    **注意**：该表达式仅适用于 MusicPlaylistContainer 类型的对象。 | $ from project select musicPlaylistRoot |
| maxDurationSource | Returns a JSON object containing the id of the Audio Source object that has the maximum playback duration (in seconds) for all descendants of the current object. The JSON object also includes the maximum duration value itself.    **Note**: This only works with Containers objects and Events. | $ from object "\Containers" select maxDurationSource |
| maxDurationSourceObject | 返回当前对象的所有下级对象中播放时长（秒）最长的 Audio Source 对象。    **Note**: This only works with Containers objects and Events. | $ from object "\Containers" select maxDurationSource |
| maxRadiusAttenuation | Returns a JSON object containing the id of the attenuation object that has the maximum radius distance in all descendants of the current objects. The JSON object also contains the maximum radius distance value itself.    **Note**: This only works with Containers objects and Events. | $ from type Sound select maxRadiusAttenuation |
| maxRadiusAttenuationObject | 返回当前对象的所有下级对象中半径距离最长的衰减对象。    **Note**: This only works with Containers objects and Events. | $ from type Sound select maxRadiusAttenuation |
| audioSourceLanguage | 返回用于当前 Audio Source 的语言对象。    **注意**：该表达式仅适用于 Audio Source 对象。 | $ from type AudioFileSource select audioSourceLanguage |
| switchContainerChildContext | 返回与当前 Switch Container 对象关联的 Switch Container 上下文对象。Switch Container 上下文对象存有有关 Switch Container 关联的设置。    **注意**：该表达式仅适用于 SwitchContainer 类型的对象。 | $ from project select switchContainerChildContext |
| switchGroupGameParameter | Returns the Game Parameter object associated with the current Switch Group object. The object is returned even if the "UseGameParameter" property of the Switch Group is false.    **Note**: This only works with objects of type SwitchGroup. | $ from type switchgroup select switchGroupGameParameter |
| panner | Returns the Speaker Panner object.    **Note**: This only works with objects that support Positioning. | $ where panner.panX > 5 |
| stateGroups | Returns the state groups that are used for the states of the associated object. These are the state groups added in the States tab. The return is a list of objects.    **Note**: This can only be used in a return expression. |  |
| customStates | Returns the list of the current object's custom states that have a defined value.    **Note**: This only works with objects that support states. | $ from type Sound select customStates |
| originalState | Returns the original state associated with the custom state object.    **Note**: This only works with custom state objects. | $ from type CustomState select originalState    $ from type bus select customStates select originalState    $ where customstates.any()  return: ["type", "id", "name", "customstates.{volume, pitch, lowpass, highpass, originalState.name as state, originalState.parent.name as stateGroup} as customStates"] |
| extractEvents | Returns the Event objects referenced by this object.    **注意**：该表达式仅适用于 SoundBank 类型的对象。 | $ from type soundbank where extractEvents.any(name="MyEvent") |
| extractStructures | Returns the object structures referenced by this object.    **注意**：该表达式仅适用于 SoundBank 类型的对象。 | $ from type soundbank where extractStructures.any(type="sound") |
| extractMedia | Returns the paths of the media files referenced by this object.    **注意**：该表达式仅适用于 SoundBank 类型的对象。This can only be used in a return expression. |
| soundbanksReferencingEvent | Returns the SoundBank objects referencing the current Event object.    **Note**: This only works with objects of type Event. | $ from type event where soundbanksReferencingEvent.count() = 1 |
| 数值表达式 | 可返回数字值、字符串或布尔值的表达式 | 示例 |
| **OBJECT\_EXPRESSION**.**VALUE\_EXPRESSION**    **OBJECT\_EXPRESSION.OBJECT\_EXPRESSION. VALUE\_EXPRESSION** | 可使用零到多个对象表达式，并后跟数值表达式，来返回联用对象的值。使用点号分隔各个表达式。 | $ where OutputBus.id = "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}" |
| **PROPERTY\_NAME**  @**PROPERTY****\_NAME**  @@**PROPERTY****\_NAME** | 返回特定对象的属性值。    Without the @, the override settings are used to find the property value. 该值为播放时所用的实际值（即有效值）。If there is an accessor of the same name, it will take precedence; in those rare cases, @@ must be used before the property name.    若使用 @，则使用对象上直接定义的属性（即便没有覆盖）。    @@ 等同于不用 @。    **PROPERTY\_NAME** 为当前对象的属性名称。Refer to [Wwise 对象参考](wobjects_index.html) for the complete list of object types and their properties. 该名称不区分大小写。 | $ from type Sound where volume < 0  $ from type Sound where @UserAuxSendVolume0 < 0  $ from type Sound where IsLoopingEnabled = true  $ from type sound where isloopingenabled = true |
| id | 以 "{0CB93450-E995-40E5-98A5-239F15B1F1D4}" 形式返回 128 位 GUID。    该 GUID 为工程中对象的唯一标识符。 | $ where id = "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}" |
| shortId | 返回对象的 32 位短 ID 数字值。该 ID 将用在声音引擎中。    **注意**：唯一短 ID 对应的值域取决于对象类型。对于某些对象类型（如 Bus、Events、Effect 和 Game Sync），只有同一类型的所有对象使用唯一的 ID。对于其他对象类型（如 Sound 和 Container），则在整个工程中使用唯一的 ID。 | $ where shortId = 1588715066 |
| name | 以字符串形式返回对象的名称。 | $ from type Event where name : "\*hello\*"  $ where name = "Play\_Hello" |
| notes | 以字符串形式返回对象的注释（也叫备注）。 | $ where notes : "audiokinetic" |
| type | 以字符串形式返回对象的类型。    有关对象类型的完整列表，请参阅 [Wwise 对象参考](wobjects_index.html) 章节。 | $ where type = "Sound" |
| nodeType | Returns the type of the node as a string.    Refer to [Wwise Nodes Reference](wobjectnodetypes.html) for the complete list of node types. | $ where nodeType = "Sound SFX" |
| classId | 返回对象的 classID。classID 是一个代表对象类型和效果器/源/转码插件类型的数字值。    有关 classID 的完整列表，请参阅 [Wwise 对象参考](wobjects_index.html) 章节。 | $ where classId = 8847363 |
| category | 返回对象的类别。    可将工程根文件夹下的顶层文件夹名称用作类别。 | $ where category = "Containers"  $ where category = "Busses"  $ where category = "Events" |
| filePath | 返回与 Work Unit 或工程关联的文件路径。该路径为 wwu 或 wproj 文件的绝对路径。 | $ where type = "WorkUnit" and filePath : "\*wwu" |
| path | 返回 Wwise 工程内的工程路径。该路径包含类别（即顶层文件夹名称）。 | $ where path : "microphone" |
| activeSource | 返回与声音对象关联的活跃音频源。 | $ from type Sound select activeSource |
| isPlayable | 若对象可在 Transport 中或 Event 内播放，则返回 true。否则，返回 false。 | $ where isPlayable  $ where isPlayable = false  $ where !isPlayable |
| childrenCount | 返回当前对象的子对象数量。 | $ where childrenCount > 10  $ where type = "RandomSequenceContainer" and childrenCount > 5 |
| pluginName | 返回插件供应商提供的插件名称。    插件名称适用于效果器插件、源插件、音频设备和元数据对象。    注意，插件名称不同于对象名称。 | $ where pluginName = "" |
| convertedFilePath | 返回与当前对象关联的转码后文件的绝对路径。    **注意**：该表达式仅适用于 Sound 和 AudioSource 类型的对象。 | $ from type Sound where convertedFilePath : "hello" |
| originalFilePath | 返回与当前对象关联的原始文件的绝对路径。    **Note**: This only works with objects of type Sound, AudioSource, Music Clip and Music Clip MIDI. | $ from type Sound where originalFilePath : "hello" |
| originalRelativeFilePath | Returns the path of the original file associated with the current object, relative to the project's Originals folder.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Music Clip MIDI. | $ from type Sound where originalFilePath : "hello" |
| originalTotalChannelCount | Returns the total number of channels of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalTotalChannelCount > 3 |
| originalNormalChannelCount | Returns the total number of channels in the default plane of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalNormalChannelCount > 3 |
| originalHeightChannelCount | Returns the total number of channels in the height plane of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalHeightChannelCount > 0 |
| originalLFEChannelCount | Returns the total number of low-frequency channels of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalLFEChannelCount > 0 |
| originalNonLFEChannelCount | Returns the total number of channels exclusive of the low-frequency channels of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalNonLFEChannelCount > 0 |
| originalAnonymousChannelCount | Returns the total number of anonymous channels of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalAnonymousChannelCount > 0 |
| originalAmbisonicsChannelCount | Returns the total number of ambisonics channels of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalAmbisonicsChannelCount > 0 |
| originalChannelConfig | Returns the channel configuration string of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalChannelConfig = "7.1.4" |
| originalChannelMask | Returns the channel configuration mask of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalChannelMask = 185919 |
| originalSampleRate | Returns the sample rate of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalSampleRate = 48000 |
| originalBitDepth | Returns the bit depth of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalBitDepth = 16 |
| originalFileSize | Returns the size in bytes of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalFileSize != 0 |
| originalDataSize | Returns the size in bytes of the original file's data associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalDataSize != 0 |
| originalSampleCount | Returns the number of samples in the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalSampleCount != 0 |
| originalDuration | Returns the duration in seconds of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media.    This can differ from the duration field because originalDuration does not include trims. | $ from type Sound where originalDuration > 1 |
| originalCodec | Returns the codec of the original file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where originalCodec = "PCM" |
| convertedTotalChannelCount | Returns the total number of channels of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedTotalChannelCount > 3 |
| convertedNormalChannelCount | Returns the total number of channels in the default plane of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedNormalChannelCount > 3 |
| convertedHeightChannelCount | Returns the total number of channels in the height plane of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedHeightChannelCount > 0 |
| convertedLFEChannelCount | Returns the total number of low-frequency channels of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedLFEChannelCount > 0 |
| convertedNonLFEChannelCount | Returns the total number of channels exclusive of the low-frequency channels of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedNonLFEChannelCount > 0 |
| convertedAnonymousChannelCount | Returns the total number of anonymous channels of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedAnonymousChannelCount > 0 |
| convertedAmbisonicsChannelCount | Returns the total number of ambisonics channels of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedAmbisonicsChannelCount > 0 |
| convertedChannelConfig | Returns the channel configuration string of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedChannelConfig = "7.1.4" |
| convertedChannelMask | Returns the channel configuration mask of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedChannelMask = 185919 |
| convertedSampleRate | Returns the sample rate of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedSampleRate = 48000 |
| convertedSampleRateSetting | Returns the sample rate, expressed as a string, of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedSampleRateSetting = "As Input" |
| convertedBitDepth | Returns the bit depth of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedSampleRate = 16 |
| convertedFileSize | Returns the size in bytes of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedFileSize != 0 |
| convertedDataSize | Returns the size in bytes of the converted file's data associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedDataSize != 0 |
| convertedSampleCount | Returns the number of samples in the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedSampleCount != 0 |
| convertedDuration | Returns the duration in seconds of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media.    This can differ from the duration field because convertedDuration does not include trims. | $ from type Sound where convertedDuration > 1 |
| convertedTrimmedDuration | Returns the duration in seconds of the trimmed converted audio source associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media.    This can differ from the convertedDuration field because convertedDuration does not include trims. | $ from type Sound where convertedTrimmedDuration > 1 |
| convertedCodec | Returns the codec of the converted file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media. | $ from type Sound where convertedCodec = "Vorbis" |
| conversionFormat | Returns the codec of the file associated with the current object.    **Note**: This only works with objects of type Sound, AudioSource, Music Clip, and Plug-in Media.    This differs from convertedCodec because the file does not have to be converted. | $ from type Sound where conversionFormat = "Vorbis" |
| soundbankBnkFilePath | 返回与当前对象关联的 BNK 文件的绝对路径。    **注意**：该表达式仅适用于 SoundBank 类型的对象。 | $ where soundbankBnkFilePath : "car" |
| mediaId | Unique value given to file. Used by the sound engine to identify the file.    **Note**: This only works with objects of type AudioSource, MidiFileSource and PluginMediaSource. | $ where mediaId > 0 |
| conversionHash | The hash of everything in the project that affects a file's conversion (Conversion ShareSet, file modifications in the Source Editor, and so on).    **Note**: This only works with objects of type AudioSource, MidiFileSource and PluginMediaSource. | $ where conversionHash > 0 |
| contentHash | The hash of the conversionHash and the hash of the original file's contents.    **Note**: This only works with objects of type AudioSource, MidiFileSource and PluginMediaSource. | $ where contentHash != "" |
| workunitIsDefault | 若 Work Unit 对象为该类别的 Default Work Unit，则返回 true。    **注意**：该表达式仅适用于 WorkUnit 类型的对象。 | $ where workunitIsDefault |
| workunitType | 返回当前 Work Unit 对象的类型。其可为以下数值：   - "folder": for Physical folder objects, such as "\Containers". - "rootFile"：用于所含的 Work Unit 对象。 - "nestedFile"   **注意**：该表达式仅适用于 WorkUnit 类型的对象。 | $ where workunitType = "folder"  $ where workunitType = "rootFile" and !workunitIsDefault |
| workunitIsDirty | 若 Work Unit 有未保存的更改，则返回 true。    **注意**：该表达式仅适用于 WorkUnit 类型的对象。 | $ where workunitIsDirty |
| workunitIsLoaded | Returns true if a Work Unit is currently loaded in the Project. False if it has been unloaded.    **注意**：该表达式仅适用于 WorkUnit 类型的对象。 | $ where workunitIsLoaded |
| isExplicitMute | 若对象被显式设为了 Mute 状态，则返回 true。 | $ where isExplicitMute |
| isExplicitSolo | 若对象被显式设为了 Solo 状态，则返回 true。 | $ where isExplicitSolo |
| isImplicitMute | 若对象被隐式设为了 Mute 状态，则返回 true。 | $ where isImplicitMute |
| isImplicitSolo | 若对象被隐式设为了 Solo 状态，则返回 true。 | $ where isImplicitSolo |
| isIncluded | Returns true if the object is included. If one or more of the object's ancestors is excluded, the object is excluded as well. | $ where isIncluded |
| isLanguageIncluded | Returns true if the audio source object's parent includes the audio source's language. The parent must be a Sound. | $ where (parent.type="sound" and isLanguageIncluded) |
| isLinked("<strong>PROPERTY\_NAME</strong>") | Returns true if the specified property of the current object is linked.    **PROPERTY\_NAME** refers to the name of a property, reference or object list for the current object. Refer to [Wwise 对象参考](wobjects_index.html) for the complete list of object types and their properties. 该名称不区分大小写。 | $ where isLinked("pitch") |
| isOverridable("<strong>PROPERTY\_NAME</strong>") | Returns true if the specified property of the current object has an override property.    **PROPERTY\_NAME** refers to the name of a property, reference or object list for the current object. Refer to [Wwise 对象参考](wobjects_index.html) for the complete list of object types and their properties. 该名称不区分大小写。 | $ where isOverridable("SpeakerPanning") |
| isSourceOfOverride("<strong>PROPERTY\_NAME</strong>") | Returns true if the object is the source of override for the specified property.    **PROPERTY\_NAME** refers to the name of a property, reference or object list for the current object. Refer to [Wwise 对象参考](wobjects_index.html) for the complete list of object types and their properties. 该名称不区分大小写。 | $ where isSourceOfOverride("SpeakerPanning") |
| supportsStates | Returns true if the object supports the use of States on any of its properties.    See [Wwise 对象参考](wobjects_index.html) for the complete list of object types and their properties. | $ where supportsStates |
| supportsRandomizer | Returns true if the object supports the use of a Randomizer on any of its properties.    See [Wwise 对象参考](wobjects_index.html) for the complete list of object types and their properties. | $ where supportsRandomizer |
| hasProperty("<strong>PROPERTY\_NAME</strong>") | Returns true if the object has the specified property.    **PROPERTY\_NAME** refers to the name of a property, reference or object list for the current object. Refer to [Wwise 对象参考](wobjects_index.html) for the complete list of object types and their properties. 该名称不区分大小写。 | $ where hasProperty("InitialDelay") |
| stateProperties | Returns the properties that are used for the states of the associated object. This represents the visible columns in the States tab. The return is a list of strings.    **Note**: This can only be used in a return expression. |  |
| validity | Returns a JSON object representing the status of validity. There are 3 fields in the object: isValid (boolean), details (string), severity (string). The details and severity fields are only available when isValid is false. This can be used with Effect Slots, Events and Actions. | $ where validity.isValid |
| maxDurationSource.id | 返回时长最长的 Audio Source 对象的 ID (GUID)。 | $ where maxDurationSource.id = "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}" |
| maxDurationSource.trimmedDuration | 返回修剪的最长音频源的时长（秒）。 | $ where maxDurationSource.trimmedDuration >= 2 |
| duration.min | Returns the minimum possible time (in seconds) playback can take.    **注意**：此项适用于可包含 Audio Source 对象的所有对象（以源的形式直接实现，或通过下级对象间接实现）。 | $ where duration.min = 3 |
| duration.max | Returns the maximum possible time (in seconds) playback can take.    **注意**：此项适用于可包含 Audio Source 对象的所有对象（以源的形式直接实现，或通过下级对象间接实现）。 | $ where duration.max = 5 |
| duration.type | 返回时长的类型（可为 Infinite、Mixed、OneShot 或 Unknown）。 | $ where duration.type = "oneShot" |
| loudness.integrated | Returns the integrated loudness measurement in LUFS for the entire associated audio file. | $ from type sound where loudness.integrated > -14 |
| loudness.momentaryMax | Returns the momentary max measurement in LUFS for the associated audio file. The value represents the highest loudness value obtained with a very short (100ms) window evaluation. | $ from type sound where loudness.momentaryMax > -14 |
| audioSourceTrimValues.trimBegin | 返回修剪的音频源的时间范围的起点。 | $ where audioSourceTrimValues.trimBegin = 2 |
| audioSourceTrimValues.trimEnd | 返回修剪的音频源的时间范围的终点。 | $ where audioSourceTrimValues.trimEnd = 5 |
| maxRadiusAttenuation.id | 返回半径最长的 Attenuation 对象的 ID (GUID)。    **Note**: This only works with Containers objects and Events. | $ where maxRadiusAttenuation.id = "{1514A4D8-1DA6-412A-A17E-75CA0C2149F3}" |
| maxRadiusAttenuation.radius | 返回半径最长的 Attenuation 对象的半径。    **Note**: This only works with Containers objects and Events. | $ where maxRadiusAttenuation.radius > 100 |
| curveToUse | For the current Attenuation object this returns a string representing the curve to use for a given curve type.    See [ak.wwise.core.object.setAttenuationCurve](ak_wwise_core_object_setattenuationcurve.html) for the list of curve types and uses.    **Note**: This only works with objects of type Attenuation. | $ from type Attenuation where curveToUse("VolumeWetGameUsage") = "UseVolumeDry" |
| hasEmptySwitchStateAssignment | For the current object this returns true if there are empty objects or paths assigned to any Switches or States it uses.    **Note**: This only works with objects of type SwitchContainer, MusicSwitchTrack, MusicSwitchContainer and DialogueEvent. | $ where hasEmptySwitchStateAssignment |

## List Functions

Perform conditional logic or select specific elements on all items of the list at once. You can use list functions on object lists and other lists provided by WAQL, such as children, descendants, ancestors, and referencesTo.

Refer to [Wwise 对象参考](wobjects_index.html) to learn more about the object lists available in the different object types.

| List Functions | 说明 | 示例 |
| --- | --- | --- |
| count | Returns the number of items in the list that match the specified condition, otherwise returns false. The condition statement is optional. | $ where children.count() > 3  $ where effects.count(effect.pluginname:"eq") > 0 |
| any | Returns true if any items match the condition, otherwise returns false. Returns false if empty. The condition statement is optional. | $ where rtpc.any()  $ where children.any(type = "Sound") |
| all | Returns true if all items in the list match the specified condition, otherwise returns false. Returns false if empty. The condition statement is mandatory. | $ where children.all(type = "Sound") |
| first | Returns the first item thats matches the specified condition. The condition statement is optional. | $ where effects.first(effect.pluginname :"EQ") != null  $ where children.first().type = "Sound" |
| last | Returns the last item that matches the specified condition. The condition statement is optional. | $ where effects.last(effect.pluginname :"EQ") != null  $ where children.last().type = "Sound" |
| take | Takes the specified number of items, and returns them in a new list. | $ select children.take(2) |
| skip | Skips the specified number of items, and returns the rest in a new list. | $ select effects.skip(1) |
| at | Returns the item at the specified index in the list. | $ select effects.at(0) |
| where | Returns the items that match the specified condition in a new list. | $ select effects.where(effect.pluginname :"EQ") |

## Boolean Operators

Evaluate a boolean expression and return true or false.

| 条件运算符和逻辑运算符 | 说明 | 示例 |
| --- | --- | --- |
| = | 对两个值进行比较；可为字符串、数字值或布尔值。 | $ where name = "Hello"  $ from type sound where volume = -1   $ from type sound where inclusion = true |
| != | 对两个值进行比较；可为字符串、数字值或布尔值。 | $ where name != "Hello"  $ from type sound where volume != -1   $ from type sound where inclusion != true |
| <  <=  >  >= | 对两个数字值进行比较。 | $ from type sound where volume < 0  $ from type sound where volume > -3 and volume < 0 |
| : | 对两个字符串值进行比较，单词部分匹配即返回 true（以指定文本为开头）。    同时，还可使用通配符来与单词的结尾进行匹配。 | $ where name : "Hello"  $ where name : "Hel"  $ where name : "\*ello" |
| = /**REGEX**/ | 若指定的正则表达式与当前字符串匹配，则返回 true。    使用 ECMAScript 正则表达式。 | $ where name = /Hello/  $ where name = /llo$/  $ where name = /[a-z][0-9]/ |
| ! | Negates an expression. | $ where !(name = "Hello")  $ from type sound where !(volume < -3) |
| 以及 | 将两个表达式联用并取同时符合两个条件的值。 | $ from type sound where name = "Hello" and volume = 0  $ from type sound where volume > -3 and volume < 0 |
| 或者 | 将两个表达式联用并取符合其中任一条件的值。 | $ where name = "Hello" or name = "Hi"  $ from type sound where volume = -3 or volume = 0 |
| () | 指定多个表达式的逻辑运算顺序。 | $ from type sound where (volume = -3 or volume = 0) and (name = "Hello" or name = "Hi") |

## Advanced Operators

Perform complex data manipulations.

| 概览 | 说明 | 示例 |
| --- | --- | --- |
| **OBJECT\_EXPRESSION**.{**EXPRESSION1**,**EXPRESSION2**,...} | **Composition operator.** Returns a new JSON object composed of the enumerated expressions. The enumerated expressions become keys on the resulting objects, with corresponding values. You can use this operator to control which elements to obtain on Wwise objects.    Note: This operator can only be used in return expressions. | $ from type sound  return: ["path", "OutputBus.{name, shortid}"]    $ from type audiofilesource where markers.any()  return: ["path", "Markers.{time, label}"]    $ from type event  return: ["name", "children.target.{path, type}"]    $ from type customstate  return: ["volume", "originalstate.{name, parent.name}"] |
| **OBJECT\_EXPRESSION**.[**EXPRESSION1**,**EXPRESSION2**,...] | **Concatenation operator.** Returns a new list, which is the concatenation of the enumerated lists or objects. | $ from type randomsequencecontainer  return: ["[this, ancestors].name"] |
| **EXPRESSION** as **NAME** | **Alias keyword.** Renames the specified expression to another name, which becomes the key in the results. You can use this keyword to rename complex assessors.    Note: This keyword can only be used in return expressions. | $ from type sound  return : ["outputbus.name as bus", "duration.max as duration"]    $ from type event  return : ["name as event", "children.target.[this, descendants].where(type=\"Sound").originalRelativeFilePath as originals"] |