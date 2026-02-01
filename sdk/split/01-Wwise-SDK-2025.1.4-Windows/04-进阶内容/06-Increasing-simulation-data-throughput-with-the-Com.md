# Increasing simulation data throughput with the Command Buffer API

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Increasing simulation data throughput with the Command Buffer API

Some games frequently have to send a high volume of data to the sound engine. For example, games with lots of game objects and game syncs send hundreds of values to the sound engine at regular intervals. Although you can manage this data transfer with the C++ API, a more efficient way to do so is to use the fully asynchronous, C-compatible Command Buffer API.

The Command Buffer API has two primary advantages over the C++ API:

- 它可以在大规模数据传输当中最大限度地降低 CPU 用量并减少内存分配。
- 它与 C11 编译器完全兼容。所以，它的函数可直接与其他支持外部函数接口 (FFI) 的编程语言（如 Rust）绑定。

# Understanding the Command Buffer API

The Command Buffer API works like other command buffer-based APIs, such as [Vulkan](https://docs.vulkan.org/spec/latest/chapters/cmdbuffers.html) and [DirectStorage](https://learn.microsoft.com/en-us/gaming/gdk/_content/gc/system/overviews/directstorage/directstorage-overview). The command buffer is a region of memory that contains a sequential list of instructions for the sound engine. For example, a single command buffer can contain several unrelated commands such as:

- Registering game objects
- Posting events
- Updating RTPC values

After you construct the buffer and submit it to the sound engine, the buffer is added to the sound engine's internal processing queue. The commands in the buffer are then processed asynchronously on the next audio rendering frame, in the order in which they are listed in the buffer.

Commands can fail during processing. When a command fails, the sound engine proceeds to the next command in the buffer.

Clients can be called back when all commands in a buffer are processed. When this callback occurs, the client can inspect the result code of each command in the buffer and release or re-use the memory area.

# Constructing command buffers

To construct a command buffer, the size of the buffer must first be determined. The size of the buffer depends on the quantity and type of commands it contains. You can use the `AK_CommandBuffer_MinSize()` and `AK_CommandBuffer_CmdSize()` functions to calculate the buffer size.

After the buffer size is calculated, the client can allocate the buffer using `AK_CommandBuffer_Create()`. This function allocates the buffer and initializes it as an empty but valid command buffer.

For example, the following code demonstrates how to create a valid command buffer able to accomodate 20 `RegisterGameObject` commands and 20 `SetRTPC` commands:

size\_t buffer\_size = [AK\_CommandBuffer\_MinSize](_ak_command_buffer_8h_a82240c411d92107bed90b0d368590845.html#a82240c411d92107bed90b0d368590845)() + (20 \* [AK\_CommandBuffer\_CmdSize](_ak_command_buffer_8h_a36a84f23dce2a8a1c5184c5461b9726d.html#a36a84f23dce2a8a1c5184c5461b9726d)([AkCommand\_RegisterGameObject](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdafa6120328cdb73a0745a5777863dc0d4))) + (20 \* [AK\_CommandBuffer\_CmdSize](_ak_command_buffer_8h_a36a84f23dce2a8a1c5184c5461b9726d.html#a36a84f23dce2a8a1c5184c5461b9726d)([AkCommand\_SetRTPC](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda95aa5709b8fff06b947d3eda020b1189)));

void \* buffer = [AK\_CommandBuffer\_Create](_ak_command_buffer_8h_a995f9aaba5db0a2afd5ea4c490c2a28c.html#a995f9aaba5db0a2afd5ea4c490c2a28c)(buffer\_size);

assert(buffer != NULL);

|  |  |
| --- | --- |
|  | **备注:** Alternatively, clients can choose to manage the command buffer memory using their own engine's allocation hooks. To do so, replace the call to `AK_CommandBuffer_Create()` with a manual memory allocation of the same size, using an alignment of 4 bytes. Then, use `AK_CommandBuffer_Init()` to initialize the content of the buffer as an empty but valid command buffer.  Note that such buffers should be released using the usual method provided by the game engine. See [Cleaning up](goingfurther_commandbufferapi.html#goingfurther_commandbufferapi_cleanup) for more details. |

To add commands to the buffer, use `AK_CommandBuffer_Add()`. For example, the following code demonstrates how to fill the buffer with 20 `RegisterGameObject` commands and 20 `SetRTPC` commands:

for (int i=0; i < 20; i++)

{

[AkCmd\_RegisterGameObject](struct_ak_cmd___register_game_object.html) \* pCmd = ([AkCmd\_RegisterGameObject](struct_ak_cmd___register_game_object.html)\*)[AK\_CommandBuffer\_Add](_ak_command_buffer_8h_af47a12700e1cd382114958c3d9c31211.html#af47a12700e1cd382114958c3d9c31211)(buffer, [AkCommand\_RegisterGameObject](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdafa6120328cdb73a0745a5777863dc0d4), 0);

assert(pCmd != nullptr); // If null is returned, it means the buffer is full and cannot accomodate another command.

pCmd->[gameObjectID](struct_ak_cmd___register_game_object_a26cf8b895f9d1edfd3151b5455dc54e5.html#a26cf8b895f9d1edfd3151b5455dc54e5) = 100 + i;

}

for (int i=0; i < 20; i++)

{

[AkCmd\_SetRTPC](struct_ak_cmd___set_r_t_p_c.html) \* pCmd = ([AkCmd\_SetRTPC](struct_ak_cmd___set_r_t_p_c.html)\*)[AK\_CommandBuffer\_Add](_ak_command_buffer_8h_af47a12700e1cd382114958c3d9c31211.html#af47a12700e1cd382114958c3d9c31211)(buffer, [AkCommand\_SetRTPC](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda95aa5709b8fff06b947d3eda020b1189), 0);

assert(pCmd != nullptr);

pCmd->[rtpcID](struct_ak_cmd___set_r_t_p_c_a71e3883d6dfdbf8479dbe4601e4858c3.html#a71e3883d6dfdbf8479dbe4601e4858c3) = MY\_RTPC\_ID;

pCmd->[rtpcValue](struct_ak_cmd___set_r_t_p_c_a1675d3bcf513f2adb6a75f79f74dec15.html#a1675d3bcf513f2adb6a75f79f74dec15) = 5.5;

pCmd->[gameObjectID](struct_ak_cmd___set_r_t_p_c_ac60a5a93956f8c25d8df7b93f53f21ee.html#ac60a5a93956f8c25d8df7b93f53f21ee) = 100 + i; // Because commands in a buffer are executed sequentially, this ID will have been registered by the time this command is processed.

}

Each command has a code (dictated by the enum `AkCommand`) and a fixed-size payload structure. Not all commands have the same payload size. The example above shows that the `AkCommand_RegisterGameObject` command has a payload described by the `AkCmd_RegisterGameObject` structure, while `AkCommand_SetRTPC` has the payload described by the `AkCmd_SetRTPC` structure. See the documentation for `AkCommand` to learn which payload structures are associated with command codes.

## Extra payload data

Some commands require additional payload data of variable size. For example, the `AkCommand_SetListeners` command must be followed by an array of listener IDs. The number of listeners can vary based on the needs of the game.

To add a variable-sized payload to a command, first add the command with `AK_CommandBuffer_Add`, then add the variable-sized payload with the appropriate function based on the payload's type:

- For strings, use `AK_CommandBuffer_AddString`. This function associates a name with a game object, which is useful during profiling.
- For arrays of simple data types, use `AK_CommandBuffer_AddArray`. This function is used for commands with a "number of items" field, such as `AkCmd_SetListeners` and `AkCmd_SetMultiplePositions`.
- For external sources, use `AK_CommandBuffer_AddExternalSources`. This function is used exclusively for `AkCommand_PostEvent`.
- For Spatial Audio geometry data, use `AK_CommandBuffer_AddGeometry`. This function is used exclusively for `AkCommand_SA_SetGeometry`.

For example, the following code adds a `AkCommand_SetListeners` command with three listener IDs:

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) listenerIDs[3] = { 200, 300, 400 };

[AkCmd\_SetListeners](struct_ak_cmd___set_listeners.html)\* pCmd = ([AkCmd\_SetListeners](struct_ak_cmd___set_listeners.html)\*)[AK\_CommandBuffer\_Add](_ak_command_buffer_8h_af47a12700e1cd382114958c3d9c31211.html#af47a12700e1cd382114958c3d9c31211)(buffer, [AkCommand\_SetListeners](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda28d2e0777e20fd3e1041437522db6431));

pCmd->[gameObjectID](struct_ak_cmd___set_listeners_aa7fa22efa253000ec63e28b01b86f962.html#aa7fa22efa253000ec63e28b01b86f962) = 100;

pCmd->[numListenerIDs](struct_ak_cmd___set_listeners_a24f52ff397bfea59fbbbc0fb179d9ee4.html#a24f52ff397bfea59fbbbc0fb179d9ee4) = 3;

[AK\_CommandBuffer\_AddArray](_ak_command_buffer_8h_a7512f07e3e8f24cf4ed15bebf3a6392e.html#a7512f07e3e8f24cf4ed15bebf3a6392e)(buffer, sizeof([AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560)), pCmd->[numListenerIDs](struct_ak_cmd___set_listeners_a24f52ff397bfea59fbbbc0fb179d9ee4.html#a24f52ff397bfea59fbbbc0fb179d9ee4), listenerIDs);

If you do not add extra payload data to a command that requires it, the command fails with an `AK_InvalidParameter` result. To learn whether a particular command requires extra payload data, refer to the documentation of the command.

# Executing commands and inspecting results

To execute the commands, you must call `AK_CommandBuffer_Submit()` to submit the buffer to the sound engine. This function places the buffer in the sound engine's pending message queue. Its commands are processed asynchronously on the next audio rendering frame, in the order in which they were added to the buffer.

|  |  |
| --- | --- |
|  | **警告:** Avoid releasing or writing to the buffer until all commands in the buffer are processed. |

When a command is processed, the result of the command is written in the command buffer itself. Clients must designate a callback function before submitting the buffer in order to inspect command results. When this callback is called by the sound engine, clients can iterate through the commands to check result codes.

You can also use the callback to determine when the buffer can be re-used to submit additional commands, or when it can be released.

The following example shows how to register the command buffer callback, submit the buffer, and check results when processing is complete:

// This simple example uses a global lock to protect the buffer on the client side.

// You can replace this with your preferred constructs

[CAkLock](class_c_ak_lock.html) g\_bufferLock;

void OnCommandBufferDone(void\* in\_pCookie);

void SubmitCommandBuffer(void\* buffer)

{

g\_bufferLock.[Lock](class_c_ak_lock_aa0315513e073c9688c9c216db29083a4.html#aa0315513e073c9688c9c216db29083a4)();

[AkCommandBufferHeader](struct_ak_command_buffer_header.html)\* pHeader = static\_cast<[AkCommandBufferHeader](struct_ak_command_buffer_header.html)\*>(buffer);

pHeader->[completionCallback](struct_ak_command_buffer_header_ab7f0b276825a8aa0cb2be9a4d4ce7bcf.html#ab7f0b276825a8aa0cb2be9a4d4ce7bcf) = OnCommandBufferDone;

pHeader->[completionCallbackCookie](struct_ak_command_buffer_header_a11c54c5d7e0f2ce379990e65b3fb0682.html#a11c54c5d7e0f2ce379990e65b3fb0682) = buffer; // This is a user-defined value passed to the callback.

[AK\_CommandBuffer\_Submit](_ak_command_buffer_8h_ac1446f3c255c5f106fd0da55a340d4e4.html#ac1446f3c255c5f106fd0da55a340d4e4)(buffer);

}

void OnCommandBufferDone(void\* in\_pCookie)

{

[AkCommandBufferIterator](struct_ak_command_buffer_iterator.html) it;

[AK\_CommandBuffer\_Begin](_ak_command_buffer_8h_ab02aeefa1db98786d3133a41cc3027ae.html#ab02aeefa1db98786d3133a41cc3027ae)(in\_pCookie, &it);

while ([AK\_CommandBuffer\_Next](_ak_command_buffer_8h_a66fa021ab3bd03957b61bd74ce88ef08.html#a66fa021ab3bd03957b61bd74ce88ef08)(&it))

{

if (it.[header](struct_ak_command_buffer_iterator_a33db0cc07340b6a43e5159be2dd516d5.html#a33db0cc07340b6a43e5159be2dd516d5)->[result](struct_ak_command_header_a349ed38e4a74cff355cced1a35987d61.html#a349ed38e4a74cff355cced1a35987d61) != [AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e))

{

[AKPLATFORM::OutputDebugMsgV](namespace_a_k_p_l_a_t_f_o_r_m_ac11ab17883b9df951f2523abd90b7128.html#ac11ab17883b9df951f2523abd90b7128)("Command with code %d failed: Result = %d\n", it.[header](struct_ak_command_buffer_iterator_a33db0cc07340b6a43e5159be2dd516d5.html#a33db0cc07340b6a43e5159be2dd516d5)->[code](struct_ak_command_header_a1a3b088b97d89b4131018ddae654d5d0.html#a1a3b088b97d89b4131018ddae654d5d0), it.[header](struct_ak_command_buffer_iterator_a33db0cc07340b6a43e5159be2dd516d5.html#a33db0cc07340b6a43e5159be2dd516d5)->[result](struct_ak_command_header_a349ed38e4a74cff355cced1a35987d61.html#a349ed38e4a74cff355cced1a35987d61));

}

}

g\_bufferLock.[Unlock](class_c_ak_lock_abebc1b39d6ecbb2c3c1be866d0135669.html#abebc1b39d6ecbb2c3c1be866d0135669)(); // Buffer can be re-used now!

}

# Cleaning up

As demonstrated above, it is customary to re-use the same buffer for multiple command submissions to avoid churn on the memory manager. However, as with all other memory resources, command buffers must eventually be released. To release a command buffer, call `AK_CommandBuffer_Destroy()`.

|  |  |
| --- | --- |
|  | **警告:** Do not use `AK_CommandBuffer_Destroy()` to free a manually-allocated command buffer!Use your engine's memory allocation hooks instead. Only buffers created by `AK_CommandBuffer_Create()` should be released using `AK_CommandBuffer_Destroy()`. |

# Events and Playing IDs

When you use the Command Buffer API to post Events, the user generates Playing IDs before the Events are posted. In contrast, the C++ `AK::SoundEngine::PostEvent` API returns a valid Playing ID after the Event is posted.

To post an event with Command Buffer, first generate a Playing ID with `AK_SoundEngine_GeneratePlayingID()`. Next, use this ID when you construct the `AkCmd_PostEvent` command. Finally, submit the buffer that contains the commands.

The PostEvent command consumes its Playing ID when processed. Therefore, it is not possible to share the same Playing ID for multiple PostEvents. A new Playing ID must be generated for each PostEvent command. PostEvent commands that refer to Playing IDs that were previously consumed will fail to process.

Here is an example of a command buffer that posts two distinct Events:

void\* buffer = [AK\_CommandBuffer\_Create](_ak_command_buffer_8h_a995f9aaba5db0a2afd5ea4c490c2a28c.html#a995f9aaba5db0a2afd5ea4c490c2a28c)([AK\_CommandBuffer\_MinSize](_ak_command_buffer_8h_a82240c411d92107bed90b0d368590845.html#a82240c411d92107bed90b0d368590845)() + [AK\_CommandBuffer\_CmdSize](_ak_command_buffer_8h_a36a84f23dce2a8a1c5184c5461b9726d.html#a36a84f23dce2a8a1c5184c5461b9726d)([AkCommand\_PostEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf20e9790432e3db005cd602adcf4d962)) \* 2);

assert(buffer != nullptr);

[AkCmd\_PostEvent](struct_ak_cmd___post_event.html)\* postEvent1 = ([AkCmd\_PostEvent](struct_ak_cmd___post_event.html)\*)[AK\_CommandBuffer\_Add](_ak_command_buffer_8h_af47a12700e1cd382114958c3d9c31211.html#af47a12700e1cd382114958c3d9c31211)(buffer, [AkCommand\_PostEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf20e9790432e3db005cd602adcf4d962), 0);

postEvent1->[eventID](struct_ak_cmd___post_event_ac2f257b0dc6268b25c6dcb57075ff5a2.html#ac2f257b0dc6268b25c6dcb57075ff5a2) = [AK\_SoundEngine\_GetIDFromString](_ak_command_buffer_8h_a1a2169a039c3495d9595dedc08eca2f1.html#a1a2169a039c3495d9595dedc08eca2f1)("my\_event");

postEvent1->[playingID](struct_ak_cmd___post_event_afd6138b4a6f412766540cedc8357482d.html#afd6138b4a6f412766540cedc8357482d) = [AK\_SoundEngine\_GeneratePlayingID](_ak_command_buffer_8h_a4d75a81be7be245c1e49cea34e32bfc3.html#a4d75a81be7be245c1e49cea34e32bfc3)();

postEvent1->[gameObjectID](struct_ak_cmd___post_event_a2a1a6012ddf0620e9778d4ed52905e7e.html#a2a1a6012ddf0620e9778d4ed52905e7e) = 100;

[AkCmd\_PostEvent](struct_ak_cmd___post_event.html)\* postEvent2 = ([AkCmd\_PostEvent](struct_ak_cmd___post_event.html)\*)[AK\_CommandBuffer\_Add](_ak_command_buffer_8h_af47a12700e1cd382114958c3d9c31211.html#af47a12700e1cd382114958c3d9c31211)(buffer, [AkCommand\_PostEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf20e9790432e3db005cd602adcf4d962), 0);

postEvent2->[eventID](struct_ak_cmd___post_event_ac2f257b0dc6268b25c6dcb57075ff5a2.html#ac2f257b0dc6268b25c6dcb57075ff5a2) = [AK\_SoundEngine\_GetIDFromString](_ak_command_buffer_8h_a1a2169a039c3495d9595dedc08eca2f1.html#a1a2169a039c3495d9595dedc08eca2f1)("another\_event");

postEvent2->[playingID](struct_ak_cmd___post_event_afd6138b4a6f412766540cedc8357482d.html#afd6138b4a6f412766540cedc8357482d) = [AK\_SoundEngine\_GeneratePlayingID](_ak_command_buffer_8h_a4d75a81be7be245c1e49cea34e32bfc3.html#a4d75a81be7be245c1e49cea34e32bfc3)();

postEvent2->[gameObjectID](struct_ak_cmd___post_event_a2a1a6012ddf0620e9778d4ed52905e7e.html#a2a1a6012ddf0620e9778d4ed52905e7e) = 100;

[AK\_CommandBuffer\_Submit](_ak_command_buffer_8h_ac1446f3c255c5f106fd0da55a340d4e4.html#ac1446f3c255c5f106fd0da55a340d4e4)(buffer);

# Command buffer memory layout

Clients do not have to use the `AK_CommandBuffer_Init()` and `AK_CommandBuffer_Add()` functions to construct a command buffer. The content of the buffer can be constructed manually. Its memory layout is defined by the various structures defined in `AK/command_types.h`.

The following diagram shows the sequential layout of a valid command buffer in memory.

```
+-----------------------------------------------------+
| CBH | CH1 | CP1 | CH2 | CP2 | ... | CHN | CPN | EOB |
+-----------------------------------------------------+

CBH = Command Buffer Header (AkCommandBufferHeader)
CHN = Nth Command Header (AkCommandHeader)
CPN = Nth Command Payload. Its size is dictated by the command header's "size" member.
EOB = End-of-buffer marker. AkCommandHeader structure with the command code AkCommand_EndOfBuffer (0) and payload size 0.
```

Note the following about the preceding diagram:

- You could divide the "Command Payload" into a fixed-size payload (the command's payload struct) and a variable-size payload. In this case, the command header's "size" member must equal the sum of the fixed-size and variable-size payloads.
- External sources and geometry data have a complex serialization scheme that might change between Wwise versions. We recommend that you always use `AK_CommandBuffer_AddExternalSources` and `AK_CommandBuffer_AddGeometry` to serialize these structures to a command buffer.
- The memory address of each segment that forms the buffer must be aligned on 4 bytes. You must pad variable-size payloads to ensure alignment.

|  |  |
| --- | --- |
|  | **警告:** Submitting or iterating over a malformed command buffer can lead to undefined behavior or crashes. |

[AkCommand\_RegisterGameObject](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdafa6120328cdb73a0745a5777863dc0d4)

@ AkCommand\_RegisterGameObject

See AkCmd\_RegisterGameObject

**Definition:** [AkCommandTypes.h:38](_ak_command_types_8h_source.html#l00038)

[AKPLATFORM::OutputDebugMsgV](namespace_a_k_p_l_a_t_f_o_r_m_ac11ab17883b9df951f2523abd90b7128.html#ac11ab17883b9df951f2523abd90b7128)

void OutputDebugMsgV(const wchar\_t \*in\_pszFmt,...)

**Definition:** [AkPlatformFuncs.h:316](_win32_2_ak_platform_funcs_8h_source.html#l00316)

[AK\_CommandBuffer\_Add](_ak_command_buffer_8h_af47a12700e1cd382114958c3d9c31211.html#af47a12700e1cd382114958c3d9c31211)

AKSOUNDENGINE\_API void \* AK\_CommandBuffer\_Add(void \*in\_buffer, enum AkCommand in\_cmd\_id)

[AkCmd\_SetRTPC::gameObjectID](struct_ak_cmd___set_r_t_p_c_ac60a5a93956f8c25d8df7b93f53f21ee.html#ac60a5a93956f8c25d8df7b93f53f21ee)

AkGameObjectID gameObjectID

(optional) Game Object ID; specify AK\_INVALID\_GAME\_OBJECT for global scope or if using playingID

**Definition:** [AkCommandTypes.h:240](_ak_command_types_8h_source.html#l00240)

[AK\_CommandBuffer\_Create](_ak_command_buffer_8h_a995f9aaba5db0a2afd5ea4c490c2a28c.html#a995f9aaba5db0a2afd5ea4c490c2a28c)

AKSOUNDENGINE\_API struct AkCommandBufferHeader \* AK\_CommandBuffer\_Create(size\_t in\_size)

[AK\_CommandBuffer\_CmdSize](_ak_command_buffer_8h_a36a84f23dce2a8a1c5184c5461b9726d.html#a36a84f23dce2a8a1c5184c5461b9726d)

AKSOUNDENGINE\_API size\_t AK\_CommandBuffer\_CmdSize(enum AkCommand in\_cmd\_id)

[AkCommand\_PostEvent](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaf20e9790432e3db005cd602adcf4d962)

@ AkCommand\_PostEvent

See AkCmd\_PostEvent

**Definition:** [AkCommandTypes.h:37](_ak_command_types_8h_source.html#l00037)

[AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560)

AkUInt64 AkGameObjectID

Game object ID

**Definition:** [AkTypedefs.h:39](_ak_typedefs_8h_source.html#l00039)

[AkCommand\_SetRTPC](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda95aa5709b8fff06b947d3eda020b1189)

@ AkCommand\_SetRTPC

See AkCmd\_SetRTPC

**Definition:** [AkCommandTypes.h:41](_ak_command_types_8h_source.html#l00041)

[AkCmd\_SetRTPC::rtpcValue](struct_ak_cmd___set_r_t_p_c_a1675d3bcf513f2adb6a75f79f74dec15.html#a1675d3bcf513f2adb6a75f79f74dec15)

AkRtpcValue rtpcValue

Value to set

**Definition:** [AkCommandTypes.h:239](_ak_command_types_8h_source.html#l00239)

[AkCommandBufferHeader::completionCallbackCookie](struct_ak_command_buffer_header_a11c54c5d7e0f2ce379990e65b3fb0682.html#a11c54c5d7e0f2ce379990e65b3fb0682)

void \* completionCallbackCookie

User cookie for done\_callback

**Definition:** [AkCommandTypes.h:1967](_ak_command_types_8h_source.html#l01967)

[AkCmd\_PostEvent](struct_ak_cmd___post_event.html)

**Definition:** [AkCommandTypes.h:161](_ak_command_types_8h_source.html#l00160)

[AkCommandHeader::result](struct_ak_command_header_a349ed38e4a74cff355cced1a35987d61.html#a349ed38e4a74cff355cced1a35987d61)

AkUInt16 result

**Definition:** [AkCommandTypes.h:1976](_ak_command_types_8h_source.html#l01976)

[AkCommandBufferHeader::completionCallback](struct_ak_command_buffer_header_ab7f0b276825a8aa0cb2be9a4d4ce7bcf.html#ab7f0b276825a8aa0cb2be9a4d4ce7bcf)

AkCommandCallbackFunc completionCallback

At that point in time, the client can free the command buffer memory, or re-use it for something else...

**Definition:** [AkCommandTypes.h:1965](_ak_command_types_8h_source.html#l01965)

[AkCommand\_SetListeners](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda28d2e0777e20fd3e1041437522db6431)

@ AkCommand\_SetListeners

See AkCmd\_SetListeners

**Definition:** [AkCommandTypes.h:44](_ak_command_types_8h_source.html#l00044)

[AK\_CommandBuffer\_Submit](_ak_command_buffer_8h_ac1446f3c255c5f106fd0da55a340d4e4.html#ac1446f3c255c5f106fd0da55a340d4e4)

AKSOUNDENGINE\_API void AK\_CommandBuffer\_Submit(void \*in\_buffer)

[AK\_SoundEngine\_GetIDFromString](_ak_command_buffer_8h_a1a2169a039c3495d9595dedc08eca2f1.html#a1a2169a039c3495d9595dedc08eca2f1)

AKSOUNDENGINE\_API AkUInt32 AK\_SoundEngine\_GetIDFromString(const char \*in\_pszString)

[CAkLock](class_c_ak_lock.html)

**Definition:** [AkLock.h:37](_win32_2_ak_lock_8h_source.html#l00036)

[AkCommandBufferIterator::header](struct_ak_command_buffer_iterator_a33db0cc07340b6a43e5159be2dd516d5.html#a33db0cc07340b6a43e5159be2dd516d5)

struct AkCommandHeader \* header

Pointer to header of command. Use this to check the code of the command and the result code after pro...

**Definition:** [AkCommandTypes.h:1989](_ak_command_types_8h_source.html#l01989)

[CAkLock::Unlock](class_c_ak_lock_abebc1b39d6ecbb2c3c1be866d0135669.html#abebc1b39d6ecbb2c3c1be866d0135669)

AKRESULT Unlock(void)

Unlock

**Definition:** [AkLock.h:59](_win32_2_ak_lock_8h_source.html#l00059)

[AK\_CommandBuffer\_AddArray](_ak_command_buffer_8h_a7512f07e3e8f24cf4ed15bebf3a6392e.html#a7512f07e3e8f24cf4ed15bebf3a6392e)

AKSOUNDENGINE\_API void \* AK\_CommandBuffer\_AddArray(void \*in\_buffer, size\_t item\_size, AkUInt16 num\_items, const void \*items)

[AK\_CommandBuffer\_Next](_ak_command_buffer_8h_a66fa021ab3bd03957b61bd74ce88ef08.html#a66fa021ab3bd03957b61bd74ce88ef08)

AKSOUNDENGINE\_API int AK\_CommandBuffer\_Next(struct AkCommandBufferIterator \*inout\_iterator)

[AkCommandBufferIterator](struct_ak_command_buffer_iterator.html)

**Definition:** [AkCommandTypes.h:1988](_ak_command_types_8h_source.html#l01987)

[AkCmd\_SetRTPC::rtpcID](struct_ak_cmd___set_r_t_p_c_a71e3883d6dfdbf8479dbe4601e4858c3.html#a71e3883d6dfdbf8479dbe4601e4858c3)

AkRtpcID rtpcID

Game parameter ID

**Definition:** [AkCommandTypes.h:238](_ak_command_types_8h_source.html#l00238)

[AkCmd\_SetListeners](struct_ak_cmd___set_listeners.html)

**Definition:** [AkCommandTypes.h:344](_ak_command_types_8h_source.html#l00343)

[AkCmd\_SetListeners::gameObjectID](struct_ak_cmd___set_listeners_aa7fa22efa253000ec63e28b01b86f962.html#aa7fa22efa253000ec63e28b01b86f962)

AkGameObjectID gameObjectID

Game Object ID

**Definition:** [AkCommandTypes.h:345](_ak_command_types_8h_source.html#l00345)

[AK\_CommandBuffer\_MinSize](_ak_command_buffer_8h_a82240c411d92107bed90b0d368590845.html#a82240c411d92107bed90b0d368590845)

AKSOUNDENGINE\_API size\_t AK\_CommandBuffer\_MinSize(void)

[AK\_CommandBuffer\_Begin](_ak_command_buffer_8h_ab02aeefa1db98786d3133a41cc3027ae.html#ab02aeefa1db98786d3133a41cc3027ae)

AKSOUNDENGINE\_API void AK\_CommandBuffer\_Begin(void \*in\_buffer, struct AkCommandBufferIterator \*out\_iterator)

[AkCmd\_RegisterGameObject](struct_ak_cmd___register_game_object.html)

**Definition:** [AkCommandTypes.h:188](_ak_command_types_8h_source.html#l00187)

[AkCmd\_PostEvent::gameObjectID](struct_ak_cmd___post_event_a2a1a6012ddf0620e9778d4ed52905e7e.html#a2a1a6012ddf0620e9778d4ed52905e7e)

AkGameObjectID gameObjectID

Associated game object ID

**Definition:** [AkCommandTypes.h:164](_ak_command_types_8h_source.html#l00164)

[CAkLock::Lock](class_c_ak_lock_aa0315513e073c9688c9c216db29083a4.html#aa0315513e073c9688c9c216db29083a4)

AKRESULT Lock(void)

Lock

**Definition:** [AkLock.h:52](_win32_2_ak_lock_8h_source.html#l00052)

[AkCommandBufferHeader](struct_ak_command_buffer_header.html)

Describes the data written at the beginning of any initialized command buffer.

**Definition:** [AkCommandTypes.h:1962](_ak_command_types_8h_source.html#l01961)

[AkCmd\_PostEvent::eventID](struct_ak_cmd___post_event_ac2f257b0dc6268b25c6dcb57075ff5a2.html#ac2f257b0dc6268b25c6dcb57075ff5a2)

AkUniqueID eventID

Unique ID of the event

**Definition:** [AkCommandTypes.h:163](_ak_command_types_8h_source.html#l00163)

[AkCommandHeader::code](struct_ak_command_header_a1a3b088b97d89b4131018ddae654d5d0.html#a1a3b088b97d89b4131018ddae654d5d0)

AkUInt16 code

Unique ID of the command, as listed in AkCommand enum

**Definition:** [AkCommandTypes.h:1973](_ak_command_types_8h_source.html#l01973)

[AkCmd\_RegisterGameObject::gameObjectID](struct_ak_cmd___register_game_object_a26cf8b895f9d1edfd3151b5455dc54e5.html#a26cf8b895f9d1edfd3151b5455dc54e5)

AkGameObjectID gameObjectID

ID of the game object to be registered. Valid range is [0 to 0xFFFFFFFFFFFFFFDF].

**Definition:** [AkCommandTypes.h:189](_ak_command_types_8h_source.html#l00189)

[AK\_Success](_ak_enums_8h_a64f7d1f79613cc4dcc49a4efba6caa63.html#a64f7d1f79613cc4dcc49a4efba6caa63ad7c47fea3da641e7422573c6a13dc35e)

@ AK\_Success

The operation was successful.

**Definition:** [AkEnums.h:34](_ak_enums_8h_source.html#l00034)

[AkCmd\_SetRTPC](struct_ak_cmd___set_r_t_p_c.html)

**Definition:** [AkCommandTypes.h:237](_ak_command_types_8h_source.html#l00236)

[AK\_SoundEngine\_GeneratePlayingID](_ak_command_buffer_8h_a4d75a81be7be245c1e49cea34e32bfc3.html#a4d75a81be7be245c1e49cea34e32bfc3)

AKSOUNDENGINE\_API AkPlayingID AK\_SoundEngine\_GeneratePlayingID(void)

Generates a new playing ID. This is guaranteed to return a different value every time this is called.

[AkCmd\_SetListeners::numListenerIDs](struct_ak_cmd___set_listeners_a24f52ff397bfea59fbbbc0fb179d9ee4.html#a24f52ff397bfea59fbbbc0fb179d9ee4)

AkUInt32 numListenerIDs

Number of listeners

**Definition:** [AkCommandTypes.h:347](_ak_command_types_8h_source.html#l00347)

[AkCmd\_PostEvent::playingID](struct_ak_cmd___post_event_afd6138b4a6f412766540cedc8357482d.html#afd6138b4a6f412766540cedc8357482d)

AkPlayingID playingID

Unique ID that will be associated with this playback. Use AK\_SoundEngine\_GeneratePlayingID() to gener...

**Definition:** [AkCommandTypes.h:162](_ak_command_types_8h_source.html#l00162)