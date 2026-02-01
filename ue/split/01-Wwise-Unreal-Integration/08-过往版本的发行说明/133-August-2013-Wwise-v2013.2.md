# August 2013 - Wwise v2013.2

|  |
| --- |
| Wwise Unreal Integration Documentation |

August 2013 - Wwise v2013.2

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the Unreal Engine August 2013 release of the integration (in addition to upgrading to the new Unreal build).

# August 2013 - Wwise v2013.2

- Fixed confusion between Actor, AkComponent, the Wwise game object and their respective lifespans:
  - AkComponent follows attachment semantics of Epic's AudioComponent. AkComponents are re-used when all attachment parameters match.
  - AkGameplayStatics contains global helpers targetting Actors for easy use in blueprints.
- Fixed missing Events and Banks in SoundBank Definition File.
- Fixed game object names in Wwise Profiler.
- Generating SoundBanks now triggers a refresh of loaded banks.
- Set RTPC Value global helper now supports setting a Game Parameter at global scope (no Actor target).