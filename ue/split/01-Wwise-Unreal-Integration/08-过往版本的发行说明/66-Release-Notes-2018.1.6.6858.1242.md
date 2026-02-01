# Release Notes 2018.1.6.6858.1242

|  |
| --- |
| Wwise Unreal Integration Documentation |

Release Notes 2018.1.6.6858.1242

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed between the 2018.1.5.6835.1218 and the 2018.1.6.6858.1242 release of the integration (in addition to upgrading to the new Unreal build).

|  |  |
| --- | --- |
|  | **注記：** 此 Integration 版本不支持实验性的 Unreal Engine 4 功能。 |

# Unreal Engine 4.19/4.20/4.21 - Wwise 2018.1.6.6858.1242

- **WG-40782** Changed Blueprint's `AkCallbackInfo` to be pooled and created on demand.
- **WG-41003** Removed "*Structure member is not initialized properly*" warnings.
- **WG-41101** Reduced compile time by stopping use of monolithic headers.
- **WG-41204** Fixed: An Unreal window hangs when running in headless mode and the Wwise Project path is empty.
- **WG-41245** Fixed: In Wwise Demo Game, WAAPI subscriptions to boolean calls do not return a call failed message.
- **WG-41259** Removed Wwise Motion from the Integration Demo.
- **WG-41339** Fixed: Sequencer Event clips continuously retrigger when clip length exceeds Event duration.