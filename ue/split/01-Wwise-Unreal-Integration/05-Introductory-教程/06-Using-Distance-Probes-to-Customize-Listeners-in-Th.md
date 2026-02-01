# Using Distance Probes to Customize Listeners in Third-Person Games

|  |
| --- |
| Wwise Unreal Integration Documentation |

Using Distance Probes to Customize Listeners in Third-Person Games

Before you begin this tutorial, refer to [Working with Listeners in Third-Person Perspective Games](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_listeners.html#third_person_perspective) for a general introduction to Distance Probe usage in Wwise.

This tutorial demonstrates how to use a Blueprint to assign a Distance Probe in Wwise. The example uses the Third Person project template, and the ThirdPersonCharacter Actor is used for the Distance Probe. The exact steps might vary depending on your project.

**To use a Blueprint to assign a Distance Probe:**

1. In the Content Browser, go to **Content** > **ThirdPerson** > **Blueprints** and double-click **BP\_ThirdPersonCharacter**. The Blueprint opens.
2. On the Event Graph, right-click an empty area and add a **BeginPlay** Event.
3. Right-click to add a second node, **Set Distance Probe**, and connect it to **Event BeginPlay**.
4. Drag a pin from the **Listener** input parameter of **Set Distance Probe**, and add a **Get Player Camera Manager** node.

   |  |  |
   | --- | --- |
   |  | **注記：** Wwise Unreal 集成会将 Game Object 自动注册为默认听者并绑定到 "PlayerCameraManager" Actor。 |
5. Drag a connection from the **Distance Probe** input parameter, and add a **Get a reference to self** variable. In this context, **Self** refers to the **ThirdPersonCharacter** Actor.

   ![](../../../images/GSTutorialDistanceProbeBlueprint.png)
6. Use Wwise Authoring to connect to the game and confirm that the Distance Probe is set up correctly. 有关详细信息，请参阅[对 Distance Probe 实施性能分析](https://www.audiokinetic.com/library/edge/?source=SDK&id=soundengine_listeners.html#profiling_distance_probe)章节。

# Distance Probes and Ak Reverb Volumes

In the Wwise Unreal Integration, Distance Probes interact with AkReverbVolumes, which are actors that have Late Reverb components (see [AkReverbVolume](pg_features_objects_actors.html#features_akreverbvolume)).

When a game object changes position, it checks for late reverb components, then calls [AK::SoundEngine::SetGameObjectAuxSendValues()](https://www.audiokinetic.com/library/edge/?source=SDK&id=namespace_a_k_1_1_sound_engine_af960fca0239e219b9d08c2659fe9e5d4.html) with the corresponding aux bus. If the Distance Probe is a game object that emits sound, and the game object is in the AkReverbVolume actor, the sound is sent to the aux bus of the AkReverbVolume. If the camera is a game object that emits sound, it sends to that aux bus if it is inside the AkReverbVolume.