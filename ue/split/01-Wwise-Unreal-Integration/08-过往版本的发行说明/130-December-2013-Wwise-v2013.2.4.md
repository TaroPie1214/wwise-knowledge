# December 2013 - Wwise v2013.2.4

|  |
| --- |
| Wwise Unreal Integration Documentation |

December 2013 - Wwise v2013.2.4

此 Integration 的各个版本分别与特定的 Unreal Engine 4 版本对应。Here is what has changed in the Unreal Engine December 2013 release of the integration (in addition to upgrading to the new Unreal build).

# December 2013 - Wwise v2013.2.4

- Unreal Wwise integration now officially supports PS4 and Xbox One platforms!
- Added platform selection to bank generation dialog box.
- Added bank generation dialog box to build menu.
- `LinkedProject` configuration parameter has been moved from `Engine/Config/BaseEditor.ini` to `<Your Game>/Config/DefaultGame.ini`.
- Added simple occlusion support.
- Fixed a crash when getting the UAkComponent from another component which has no owner.
- **UI-130** Fixed: Fixed performance issues with the UAkComponent::UpdateAkReverbVolumeList method.
- **UI-130** Fixed: Added a flag to the UAkComponent specifying if it is influenced by reverb volumes.
- **UI-132** Fixed: Prevent UAkComponents from ticking on server configurations.
- **UI-135** Fixed: Expose RTPC interpolation time.