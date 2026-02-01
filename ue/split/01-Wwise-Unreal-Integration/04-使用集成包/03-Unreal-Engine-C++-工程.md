# Unreal Engine C++ 工程

|  |
| --- |
| Wwise Unreal Integration Documentation |

Unreal Engine C++ 工程

# 链接模块

The Wwise Unreal Integration is separated into multiple modules and multiple plug-ins. 为了在 C++ 工程内使用 Wwise 的功能，必须在工程的构建文件 (`.Build.cs`) 内链接这些模块。您可以通过从构建文件中移除模块来将其禁用。

在以下示例中，工程包含以下 public 模块：Core、CoreUOBject、Engine、InputCore、AkAudio 和 WwiseSoundEngine。其中，`AkAudio` 和 `WwiseSoundEngine` 为 Wwise 模块。

public class MyModule : ModuleRules

{

public MyModule(ReadOnlyTargetRules Target) : base(Target)

{

PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "AkAudio", "WwiseSoundEngine" });

// 其他设置

}

}

在本例中，可使用 `WwiseSoundEngine` 和 `AkAudio` 模块的功能。模块可包含在 `PublicDependencyModulesNames` 或 `PrivateDependencyModulesNames` 中。For more information about modules, see [Unreal Engine Modules](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-modules).

For more information about Wwise plug-ins and modules, see [Understanding the Wwise Unreal Integration Plug-ins](goingfurther_plugins.html).

# 覆盖 Wwise Unreal 集成

Integration 中的模块（除了 `WwiseSoundEngine`、`AudiokineticTools` 和 `AkAudio`）可通过继承来进行扩展。这些模块的大部分功能都可由开发者根据工程自身需要进行覆盖并修改相应行为。若要覆盖模块，请创建一个新的模块并确保其继承所要覆盖的模块。然后，覆盖所需函数。为了使用新建的模块，请确保将其包含在游戏的 `Build.cs` 中，并添加到 `DefaultEngine.ini`（如下所示）：

[Audio]

WwiseFileHandlerModuleName=WwiseSimpleExternalSource

The [WwiseSimpleExternalSource module](using_features_simpleexternalsourcemanager.html) is an example of overriding a module. 确切来说，它覆盖了 `WwiseFileHandler` 模块以便通过 Data Table 来处理外部源。

# 利用 C++ 创建 AkComponent

在利用 C++ 创建新的 `AkComponent` 时，必须将其关联到父组件。有了 `AkComponent`，API 才能正常运行。以下章节举例展示了如何添加 `AkComponent`。

# 在 Unreal 工程中使用 Wwise API

现在可以通过 Wwise Unreal 集成来使用 Wwise API。您可以通过 `WwiseSoundEngine` 或 `AkAudio` 模块调用大部分函数。

## WwiseSoundEngine Plug-in

The `WwiseSoundEngine` plug-in and module provides low-level access to most SoundEngine API operations. 借助 `WwiseSoundEngine` 模块，可直接、安全地访问 API 函数（如以下示例所示）：

#include "AkAudioEvent.h"

#include "AkComponent.h"

#include "Wwise/API/WwiseSoundEngineAPI.h"

void PostEventSoundEngine(UAkAudioEvent\* Event, AActor\* GameObject)

{

if (auto\* SoundEngine = IWwiseSoundEngineAPI::Get())

{

if(Event && GameObject)

{

TArray<UAkComponent\*> Array;

GameObject->GetComponents<UAkComponent>(Array);

//The Actor doesn't have an AkComponent attached. 若要通过此 Actor 来发出声音，就需要此组件。

if (Array.Num() == 0)

{

//PostEvent doesn't load the event. The Event needs to be loaded beforehand.

if (!Event->IsLoaded())

{

Event->LoadData();

}

auto\* AkAudioComponent = NewObject<UAkComponent>(GameObject);

AkAudioComponent->SetupAttachment(GameObject->GetDefaultAttachComponent());

Array.Add(AkAudioComponent);

AkAudioComponent->RegisterComponent();

}

SoundEngine->PostEvent(Event->GetWwiseShortID(), Array[0]->GetAkGameObjectID());

}

}

}

此代码会在给定 Actor 上发送 Event。您必须在 Actor 上添加 `UAkComponent` 以通过 Wwise 予以注册。同时还要加载 Event，因为 `WwiseSoundEngine` 模块中不会自动加载 Event。

|  |  |
| --- | --- |
|  | **注記：** You must use the WwiseSoundEngine module's `IWwiseSoundEngineAPI` interface for all `AK::SoundEngine` calls. See [WwiseSoundEngine 模块](module_soundengine.html) for more information. |

## AkAudio 模块

`AkAudio` 根模块适用于大部分面向用户的 Integration 功能。它可以完成 `WwiseSoundEngine` 模块可使用 Unreal 组件执行的大部分操作。它包含用于 Integration 所用素材类型和组件的类。作为直接调用 SoundEngine 的替代方法，AkAudioDevice 提供了很多辅助函数来封装常用的 WwiseSoundEngine API。这些辅助函数还会检查是否已加载使用 API 所需的资源并提供更多日志信息。

就像前面的例子一样，以下代码也会在给定 Actor 上发送 Event。同时，还会绑定 `AkComponent` 并加载 Event：

#include "AkAudio.h"

void PostEvent(UAkAudioEvent\* Event, AActor\* GameObject)

{

if (FAkAudioDevice::Get())

{

FAkAudioDevice::Get()->PostAkAudioEventOnActor(Event, GameObject);

}

}

您可以在 `WwiseDemoGame/WwiseCodeExample` 下的 WwiseDemoGame 中找到更多代码示例，并在 `WwiseDemoCodeExampleMap` 中做各种尝试。

# Packaging Requirements

When you package your Unreal project, the assets are "tree-shaken." In other words, Unreal assets that represent Wwise objects are automatically included if they are referenced either by another packaged asset or by a packaged map. If they are, any associated SoundBanks and media files are copied into the built package. Any Wwise Unreal assets that do not satisfy one of these conditions are not included.

This packaging approach is efficient, but in certain cases some Wwise Unreal assets might be improperly excluded, which can cause errors. The following scenarios can cause this type of problem:

- The project uses Wwise Unreal assets that are not directly referenced by packaged maps.
- The project uses Events that are posted by string or from code.

If one of these scenarios applies to your project, you must therefore ensure that either the asset is directly referenced by a map, or ensure that the required assets are manually loaded. To manually add assets, add the containing directory to the project's **Additional Asset Directories to Cook** in the Project Settings. See the [Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/project-section-of-the-unreal-engine-project-settings) section of the Unreal Project Settings documentation for more information.