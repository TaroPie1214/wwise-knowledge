# Optimizing Memory Usage with Reference-Loaded Switch Containers

|  |
| --- |
| Wwise Unreal Integration Documentation |

Optimizing Memory Usage with Reference-Loaded Switch Containers

|  |  |
| --- | --- |
|  | **注記：** Before version 2022.1 of the Wwise Unreal 集成, this feature was called the "Split Switch Container Media". |

By default, when Wwise Event assets are loaded, all resources they might use (SoundBanks and media) are loaded with them. In deep, nested switch container hierarchies, a large number of media resources can be loaded, and the amount of memory required to load these resources increases accordingly. You can use reference-loaded switch containers on a per-event basis to optimize memory usage: when enabled, resources are only loaded if they are referenced, based on Switch or State values.

If the media in your Switch Container is streamed, which is common for large music files, this feature improves performance because the files are only opened for streaming when necessary. Memory usage is also reduced if the media has a prefetch chunk.

This feature is only available for certain Events that use Switch Containers. It provides the most benefits for Events used in several different contexts, and that only use a subset of the container's Switch values in each context.

例如：

- 主角的脚步声 Event 可能包含较深的层级结构，其取决于多个 Switch（如鞋子类型、地面材质和天气状况）。However, most maps only contain a subset of materials or weather conditions. Similarly, the character typically only wears one type of footwear at a time, so loading sounds for all other footwear types are unnecessary.
- Different branches of a dynamic music system based on Switch Containers could depend on Switches or States that are only used in specific maps.

The following image shows a Footstep Event dependency tree:

![](../../../images/switch_container_footstep_hierarchy.png)

If the active level references the Human\_Surface\_Material Switch and only references the Material\_Dirt Switch Value (through a SetSwitch node in the Level Blueprint, for example), only the FS\_Dirt\_[01-04] media files are loaded into memory. When a sublevel that references Material\_Grass is loaded, grass\_[01-04] media files are automatically loaded with the Switch.

|  |  |
| --- | --- |
|  | **警告：** When this option is enabled, Switch or State values are loaded in memory to determine which media to load. Be cautious in the following cases:   - **Setting State or Switch Values with strings**. You must ensure that the corresponding Switch or State value asset is loaded, for example by using the [Load Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/EditorScripting/Asset_1/LoadAsset) Blueprint Node. - **Setting State or Switch Values from C++**. You must ensure that the corresponding Switch or State Value asset is loaded, for example by using Unreal Engine [Asynchronous Asset Loading](https://dev.epicgames.com/documentation/en-us/unreal-engine/asynchronous-asset-loading). - **Using RTPC-Controlled Switch Containers**. This type of container causes inconsistencies when loading media. Avoid using this option if you are using RTPC-Controlled Switch Containers.   In addition, be careful when loading and setting Switches or States in submaps or menus. When those levels are unloaded, the Switch or State Value assets will probably be unloaded as well if they are not referenced in the persistent level, which causes their associated media to be unloaded. 若 Switch Value 或 State Value 仍然设在场景中的 GameObject 上，很可能会产生不符合预期的行为。 |

# Enabling Reference-Loaded Switch Container Media

每个 [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) 都包含 [FWwiseEventInfo](pg_features_objects_assets.html#features_objects_classes_FWwiseEventInfo) 结构，以此识别其所代表的 Wwise Event。The WwiseEventInfo structure also contains the SwitchContainerLoading field, which can enable reference-loaded Switch Container media.

![](../../../images/WwiseEventInfo_LoadOnReference.png)

.

When set to **AlwaysLoad**, the default mode for all Events, all media resources are loaded with the Event. When set to **LoadOnReference**, only the referenced media resources are loaded with the Event.

# 技术细节

When this option is activated and a Wwise Event asset is cooked by the WwiseResourceCooker, its cooked data contains a set of SwitchContainerLeaves. 这些 Leaf 是由一系列不同的 Switch Value 或 State Value 到所要加载的媒体和 SoundBank 的扁平映射。As seen in the previous example, the FS\_Dirt\_[01-04] media are only needed if the Human\_Surface\_Material and Material\_Dirt Switches Values are loaded as well. This is represented by a SwitchContainerLeaf with a "key" formed by the pair of Human\_Surface\_Material and Material\_Dirt switches and a payload of FS\_Dirt\_[01-04] media to load. 在通过 WwiseResourceLoader 加载 Wwise Event 时，会将与之对应的一组 SwitchContainerLeaf 添加到 WwiseResourceLoader 针对各个已知 Switch Value 和 State Value 追踪的 Leaf 列表中。When Switch and State Values are loaded (or unloaded) by the WwiseResourceLoader, it checks its list of known SwitchContainerLeaves associated with that value to see if any media need to be loaded (or unloaded).

|  |  |
| --- | --- |
|  | **注記：** 只有在通过 WwiseResourceLoader 加载 Event、Switch 和 State 素材时，才会对媒体依赖关系进行评估。Setting and unsetting Switches or States in the Sound Engine does not cause media to be loaded or unloaded. |

When a Default Value is set on a Switch Container, the resources that only depend on Default Values are always loaded. The same behavior applies to the Generic Path that can be set in Music Hierarchy Switch Containers. In these cases, resources such as SoundBanks and Media are not put in SwitchContainerLeaves. Instead, they are always loaded with with Events that use those Switch Containers.

This system is easiest to work with when you use Blueprints and Wwise assets to post Events and set Switch and State Values. In this case, the assets are loaded in memory with the level so the WwiseResourceLoader does not miss any information. To optimize memory usage even more, you can also disable the **AutoLoad** property exposed by [UAkAudioType](pg_features_objects_assets.html#features_objects_classes_UAkAudioType), available in all Wwise assets. 在禁用此选项时，必须调用各个素材的 **LoadData** 和 **UnloadData**（可在 Blueprint 中找到）方法以便 WwiseResourceLoader 予以加载和卸载。

最后，在尝试利用字符串在声音引擎中发送 Event 或设置 Switch 和 State 时，游戏设计师需要确保 WwiseResourceLoader 已经加载必要的资源。This likely requires the relevant Event, Switch Value, and State Value assets to be manually loaded (or referenced in maps or Blueprints). However, it is possible to build Switch or State Value CookedData programmatically, and then load and unload them in the WwiseResourceLoader instead of assets.