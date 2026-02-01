# Localizing Audio Assets

|  |
| --- |
| Wwise Unreal Integration Documentation |

Localizing Audio Assets

You can use Wwise Unreal 集成 features to map Unreal Cultures to Wwise languages and ensure that your corresponding Unreal and Wwise projects support the same set of languages for asset localization. After the mapping is complete, you can change languages with certain Blueprint nodes or through the C++ AkAudioDevice API.

# Mapping Unreal Cultures to Wwise Languages

For Unreal Cultures, you can use any [ISO-639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) and, optionally, an [ISO 3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) (fr-CA, en-GB, and so on). For the Wwise Language, you can use any of the languages in your Wwise project. For more information on localization in Wwise, refer to [Localizing Your Project](https://www.audiokinetic.com/library/edge/?source=Help&id=localizing_project).

**To map an Unreal Culture to a Wwise language:**

1. From the Unreal menu bar, click **Edit** > **Project Settings**.
2. In the Wwise section, click **Integration Settings**. The Localization section includes the mapping of Unreal Cultures to Wwise languages:  

   ![](../../../images/UnrealToWwiseCultureMap.png)
3. Click **Add Element** (+). A new row is added to the list.
4. In the text box on the left, type a valid Unreal Culture and in the text box on the right, type a corresponding Wwise language.

|  |  |
| --- | --- |
|  | **注記：** The Wwise language must match the specified language in the Wwise project exactly (capitalization, spacing, and any special characters such as parentheses). |

# Changing Languages with Blueprints

After you map the Unreal Cultures to the Wwise languages, you can use Blueprint nodes to change audio languages and cultures in Unreal. Two Blueprint nodes are available:

- **Set Current Audio Culture**   

  ![](../../../images/blueprint_SetCurrentAudioCulture.png)
- **Set Current Audio Culture Async**   

  ![](../../../images/blueprint_SetCurrentAudioCultureAsync.png)

# Changing Languages with the API

You can change the audio language or culture directly from code in the C++ AkAudioDevice API `FAkAudioDevice::Get()->SetCurrentAudioCulture()`. You can pass either a Wwise language or an Unreal Culture to the C++ function or Blueprint node.

When `SetCurrentAudioCulture()` is called:

1. The string passed to the function determines the Wwise language to set.
2. The Integration calls `FWwiseResourceLoader::SetLanguage` with the `EWwiseReloadLanguage::Immediate` parameter.
3. Integration 使用新的语言调用 `IWwiseStreamMgrAPI::SetCurrentLanguage`。

The asynchronous variant immediately calls `IWwiseStreamMgrAPI::SetCurrentLanguage`, and `FWwiseResourceLoader::SetLanguage` (which does the heavy lifting of reloading Wwise resources) is called in an asynchronous task. 在完成 `FWwiseResourceLoader::SetLanguage` 后，会触发 **Completed** Blueprint Event。

Advanced users might want to use different values of `EWwiseReloadLanguage`. If this is the case, we recommend that you avoid using the supplied Blueprints and the AkAudioDevice API and to call the `FWwiseResourceLoader::SetLanguage` and `IWwiseStreamMgrAPI::SetCurrentLanguage` functions directly.

The three possible states of `EWwiseReloadLanguage` are:

- **EWwiseReloadLanguage::Immediate**
  - 将加载 Event 资源时所用的 FWwiseResourceLoader 中的 CurrentLanguage 变量设为新的语言。
  - The resources of all Soundbanks, ShareSets, Aux Busses, and Events that were loaded in the previous language are reloaded.
- **EWwiseReloadLanguage::Safe**
  - Does the same things as **Immediate**, but also calls `IWwiseSoundEngineAPI::StopAll()` to stop all playing sounds before resources are reloaded.
- **EWwiseReloadLanguage::Manual**
  - Only the CurrentLanguage variable in the FWwiseResourceLoader is changed to the new language.
  - The user is responsible for unloading and reloading the Wwise resources that require the language change.

|  |  |
| --- | --- |
|  | **注記：** Due to limitations in the Wwise Sound Engine, we recommend that you change languages when no localized sounds are playing. If an event is playing, the Sound Engine does not unload the bank that contains it. A loaded bank cannot be replaced by a new bank with the same name, even if it is in a different language. The bank must be unloaded first. |

# Packaging Localized Assets

在烘焙本地化的 Wwise 素材时，会随素材一起打包各个语言的资源（.bnk 和 .wem 文件）。Refer to [烘焙和打包](using_knownissues.html#knownissues_packaging) on the [已知问题](using_knownissues.html) page.