# AkCmd_SA_SetImageSource

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_image_source-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetImageSource结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkImageSourceID](_ak_typedefs_8h_aa8cb517b34d4fc2a5ad99c122136db30.html#aa8cb517b34d4fc2a5ad99c122136db30) | [imageSourceID](struct_ak_cmd___s_a___set_image_source_a5f4d29628d9e4e4ca24707fbe41a4523.html#a5f4d29628d9e4e4ca24707fbe41a4523) |
|  | The ID of the image source being added. [更多...](struct_ak_cmd___s_a___set_image_source_a5f4d29628d9e4e4ca24707fbe41a4523.html#a5f4d29628d9e4e4ca24707fbe41a4523) |
|  | |
| struct [AkImageSourceSettings](struct_ak_image_source_settings.html) | [info](struct_ak_cmd___s_a___set_image_source_aac25aea7b83037b5fb4a136fc6f60e5c.html#aac25aea7b83037b5fb4a136fc6f60e5c) |
|  | Image source information. [更多...](struct_ak_cmd___s_a___set_image_source_aac25aea7b83037b5fb4a136fc6f60e5c.html#aac25aea7b83037b5fb4a136fc6f60e5c) |
|  | |
| [AkUniqueID](_ak_typedefs_8h_a8341fa4d01d2fa852c3cc410401b04dc.html#a8341fa4d01d2fa852c3cc410401b04dc) | [auxBusID](struct_ak_cmd___s_a___set_image_source_a9294eb0f0e2b0d2a14af8028bb6ba78f.html#a9294eb0f0e2b0d2a14af8028bb6ba78f) |
|  | Aux bus that has the AkReflect plug in for early reflection DSP. Pass AK\_INVALID\_AUX\_ID to use the reflections aux bus defined in the authoring tool. [更多...](struct_ak_cmd___s_a___set_image_source_a9294eb0f0e2b0d2a14af8028bb6ba78f.html#a9294eb0f0e2b0d2a14af8028bb6ba78f) |
|  | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___set_image_source_a81ba313969b0caaf908cf97ee6bba4c4.html#a81ba313969b0caaf908cf97ee6bba4c4) |
|  | The ID of the emitter game object to which the image source applies. Pass AK\_INVALID\_GAME\_OBJECT to apply to all game objects that have a reflections aux bus assigned in the authoring tool. [更多...](struct_ak_cmd___s_a___set_image_source_a81ba313969b0caaf908cf97ee6bba4c4.html#a81ba313969b0caaf908cf97ee6bba4c4) |
|  | |

## 详细描述

Add or update an individual image source for processing via the AkReflect plug-in. Use this API for detailed placement of reflection image sources, whose positions have been determined by the client, such as from the results of a ray cast, computation or by manual placement. One possible use case is generating reflections that originate far enough away that they can be modeled as a static point source, for example, off of a distant mountain. The SpatialAudio API manages image sources added via [AkCmd\_SA\_SetImageSource](struct_ak_cmd___s_a___set_image_source.html) and sends them to the AkReflect plug-in that is on the aux bus with ID `auxBusID`. The image source applies all game objects that have a reflections aux send defined in the authoring tool, or only to a specific game object if `gameObjectID` is used.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **备注:** The `AkImageSourceSettings` struct passed in `info` must contain a unique image source ID to be able to identify this image source across frames and when updating and/or removing it later.   Each instance of AkReflect has its own set of data, so you may reuse ID, if desired, as long as `in_gameObjectID` and `in_AuxBusID` are different.   |  |  | | --- | --- | |  | **备注:** It is possible for the AkReflect plugin to process reflections from both `SetImageSource` and the geometric reflections API on the same aux bus and game object, but be aware that image source ID collisions are possible. The image source IDs used by the geometric reflections API are generated from hashed data that uniquely identifies the reflecting surfaces. If a collision occurs, one of the reflections will not be heard. While collision are rare, to ensure that it never occurs use an aux bus for `SetImageSource` that is unique from the aux bus(es) defined in the authoring tool, and from those passed to `SetEarlyReflectionsAuxSend`. |  |  |  | | --- | --- | |  | **备注:** For proper operation with AkReflect and the SpatialAudio API, any aux bus using AkReflect should have 'Listener Relative Routing' checked and the 3D Spatialization set to None in the Wwise authoring tool. See [总线实例](spatial_audio_apigeometry_er.html#spatial_audio_wwiseprojectsetup_businstances) for more details. |   Optionally, you can associate a name to the image source for profiling purposes. Call AK\_CommandBuffer\_AddString after adding the command to attach a name to the image source:   ``` auto cmd = (AkCmd_SA_SetImageSource*)AK_CommandBuffer_Add(buffer, AkCommand_SA_SetImageSource); // Fill command... AK_CommandBuffer_AddString(buffer, "My image source"); ```   This command can fail for the following reasons:   - AK\_IDNotFound: `gameObjectID` was specified but is not registered.   参见  - [AkCommand\_SA\_SetImageSource](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfda96e5c87f8383997d06c0a1f11e5785a6 "See AkCmd_SA_SetImageSource") - [AK\_CommandBuffer\_AddString](_ak_command_buffer_8h_a6b6d59f7fb356dc8f2ed3488e3bf0392.html#a6b6d59f7fb356dc8f2ed3488e3bf0392) - [AkCmd\_SA\_RemoveImageSource](struct_ak_cmd___s_a___remove_image_source.html) - [AkCmd\_SA\_ClearImageSources](struct_ak_cmd___s_a___clear_image_sources.html) - [总线实例](spatial_audio_apigeometry_er.html#spatial_audio_wwiseprojectsetup_businstances) |

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1392](_ak_command_types_8h_source.html#l01392) 行定义.