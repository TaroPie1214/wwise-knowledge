# Using the Integration in the Unreal Editor

|  |
| --- |
| Wwise Unreal Integration Documentation |

Using the Integration in the Unreal Editor

The Wwise Unreal 集成 adds various options to the Unreal Editor. You can use the additional options to perform important tasks, which are described in the following sections:

- [Managing Wwise and Unreal Assets](features_editor_auto_sync.html). When you update Assets in Wwise Authoring, corresponding Unreal Assets are automatically updated. If a WAAPI connection is enabled, any deletions or name changes through the Wwise Browser in Unreal are also applied to the Wwise project.
- [Managing Assets with the Wwise Browser](features_editor_wwise_browser.html). The Wwise Browser is a viewer that you can use to drag Wwise objects into Unreal, preview sounds, rename objects, and delete objects. Changes you make in Unreal also apply to the Wwise project.
- [Reconciling Wwise UAssets](features_editor_reconcile.html). Use the Wwise Browser or a Commandlet to update the UAssets of your project with your changes in the Wwise project.
- [Working with Reverb](features_editor_reverb_estimation.html). Use the `AkLateReverbComponent` to assign aux busses and drive global reverb RTPCs.
- [Visualizing Radii](features_editor_radius.html). When you update `AkAmbientSound` assets in Wwise Authoring, you can see the radii change in Unreal.
- [Using the Editor Listener](features_editor_listener.html). Use the Editor Listener to preview positioned audio and 3D-spatialized sounds.
- [Testing with Multiple Play In Editor and Wwise Instances](features_editor_multiplayer.html). Run multiple Play In Editor sessions with separate Wwise instances.