# Understanding the Wwise Unreal Integration Plug-ins

|  |
| --- |
| Wwise Unreal Integration Documentation |

Understanding the Wwise Unreal Integration Plug-ins

The Wwise Unreal Integration is divided into multiple plug-ins, each with its own subset of modules.

You can add a `Wwise<Name>ModuleName` configuration to the Audio section of the Engine settings file, which overrides the default behavior of most modules. See [覆盖 Wwise Unreal 集成](using_cpp.html#overriding_integration_cpp) for more information.

You can use the following modules to customize the Wwise Unreal Integration for your workflow.

# Wwise Plug-in

The Wwise Plug-in contains the traditional Wwise Unreal Integration, a managed integration that provides users with a suggested workflow.

![](../../../images/ModulesDependencyTree-Wwise.png)

- AkAudio 模块  
  该根模块适用于大部分面向用户的 Integration 功能。
- [Wwise Module](module_wwise.html)   
  A simple module that links to all of the other optional modules.
- Concurrency Module   
  Low-level constructs allowing operations to be properly threaded.
- [WwiseFileHandler 模块](module_filehandler.html)   
  Provides the Wwise sound engine with the media, SoundBanks, and external sources it needs, and handles requests from the Wwise Location Resolver and I/O Hook.
- ObstructionOcclusion Module   
  Provides the Obstruction and Occlusion algorithms. See [Occlusion](using_features_occlusion.html) for details.
- [WwiseProcessing Module](module_processing.html)   
  Provides asynchronous processing of runtime objects. This is currently limited to Global Callbacks.
- [WwiseResourceLoader 模块](module_resourceloader.html)   
  At a high level, handles all Wwise object types and interfaces with the [WwiseFileHandler 模块](module_filehandler.html) to load and unload the files associated with these Wwise objects.
- Utils Modules (EngineUtils, ObjectUtils, Utils)   
  Provides basic utilities and helpers for features such as cross-engine version support and test suites.

**未烘焙的工程和编辑器模块：**

- AudiokineticTools Module   
  Contains Editor-specific AkAudio module features.
- [WwiseProjectDatabase 模块](module_projectdatabase.html)   
  该模块提供基于内存的数据库视图来显示 Wwise 工程所生成 SoundBank 的当前状态。
- Reconcile Module   
  Provides tools to reconcile Unreal project assets with Wwise project assets.
- [WwiseResourceCooker 模块](module_resourcecooker.html)   
  Converts Wwise Object Info structures to Cooked structures for the WwiseResourceLoader and copies a requested object’s files from the GeneratedSoundBanks directory to the Staging directory of the packaging process.

**可选模块：**

- AudioLink Modules   
  Allows a project to pipe the audio part of each Unreal component into a Wwise project's input component. See [Combining Unreal and Wwise Audio with AudioLink](using_audio_link.html) for more information.
- [WwiseSimpleExternalSourceManager 模块](using_features_simpleexternalsourcemanager.html)   
  A minimal External Source Manager implementation used for internal testing as well as in certain projects, such as the Wwise Demo Game.

# WwiseNiagara Plug-in

The WwiseNiagara plug-in contains a unique module, WwiseNiagara. When enabled alongside Unreal's Niagara plug-in, it allows a simple usage of Wwise audio components inside a Niagara particle emitter. See [使用 Wwise Unreal Niagara Integration](using_features_niagara.html) for more information.

![](../../../images/ModulesDependencyTree-WwiseNiagara.png)

# WwiseSoundEngine Plug-in

The WwiseSoundEngine plug-in is lowest-level part of the Wwise SoundEngine, and is used by the Wwise plug-in. It contains the bridge to the Wwise libraries, and has no automated features. It can be useful for projects that require custom Unreal integrations.

The plug-in adds several Unreal Build Tool (UBT) features: the ThirdParty folder is parsed, and bridges to older compatible versions are automatically provided. Plug-in directories and platform support are also determined.

![](../../../images/ModulesDependencyTree-WwiseSoundEngine.png)

- Authoring Module   
  On platforms and configurations that support WAAPI (Wwise Authoring API), this enables connections to Wwise Authoring through a network socket. No Unreal-aware client is provided. This is an Editor-specific module. See [Wwise Authoring API (WAAPI)](using_features_waapi.html) for more information.
- LowLevelUtils Module   
  Low-level utilities and helpers that provide features such as version determination and Unreal statistic reporting.
- [WwiseSoundEngine 模块](module_soundengine.html)   
  At the lowest level, provides the bridge between the Wwise SoundEngine libraries and the Unreal project. The current WwiseSoundEngine version of the plug-in provides the current version of the API, with backward compatibility when possible.

**可选模块：**

- WwiseSoundEngine Versioned Modules   
  Provides the bridges to previous versions of the Wwise SoundEngine, allowing for backward compatibility. See [静态声音引擎桥接](module_soundengine.html#soundengine_bridging) for more information.
- WwiseSoundEngine\_Null Module   
  Provides a bridge to a "null" SoundEngine, where the SoundEngine is ignored. This is used for some Unreal build configurations, such as program and server configurations. See [Null SoundEngine](module_soundengine.html#soundengine_null) for more information.