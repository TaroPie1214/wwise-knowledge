# Triggering Wwise Events in Animation Sequences

|  |
| --- |
| Wwise Unreal Integration Documentation |

Triggering Wwise Events in Animation Sequences

You can use an Animation Notify to trigger Wwise Events in Animation Sequences.

An AkComponent must be attached to the animated mesh component. If you use the Animation Notify on a mesh component that does not have an attached AkComponent, an AkComponent is created with default values for all `UPROPERTIES`, and it is not possible to modify them. If you want to modify the notify's behaviour, we recommend that you create a copy in your project and modify the copy.

The Blueprint for the Animation Notify is located here: `…/Plugins/Wwise/Content/AnimNotify_AkEvent.uasset`

To add an Animation Notify:

1. In the Unreal Content Browser, open an Animation Sequence asset.
2. Right-click the **Notifies** track in the Animation Sequence Editor and click **Add notify** > **AkEvent** or **AkEventByName**.  
   The animation notification has the following properties:
   - **Event** or **Event Name**: The [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent) to post.
   - **Attach Name**: The name of the socket that emits the [UAkAudioEvent](pg_features_objects_assets.html#features_objects_classes_UAkAudioEvent). If not defined, the animation owner emits the AkAudioEvent.
   - **Follow**: Determines whether the Event follows the mesh or is posted at a specific location.

For more information on the Animation Sequence Editor in Unreal, refer to [Animation Sequence Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequence-editor-in-unreal-engine).