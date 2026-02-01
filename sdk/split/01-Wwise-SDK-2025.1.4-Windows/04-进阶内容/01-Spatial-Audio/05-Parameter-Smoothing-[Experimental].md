# Parameter Smoothing [Experimental]

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Parameter Smoothing [Experimental]

|  |  |
| --- | --- |
|  | **备注:** Parameter smoothing is an experimental feature. Refer to [Spatial Audio Experimental Features](spatial_audio_experimental.html) |

# Acoustics Parameters

The Acoustics Engine simulates sound propagation within a virtual environment. It does this by generating and calculating discrete sound paths, which are then passed on to the Sound Engine for audio rendering. You can use the Voice Inspector to examine individual sound paths, which are characterized by the following parameters:

- Position
- Orientation
- Distance（距离）
- Occlusion（声笼）
- Obstruction（声障）
- Diffraction
- Transmission Loss
- Spread
- Aperture
- Volume

|  |  |
| --- | --- |
|  | **备注:** The Volume parameter is called Smoothing in the Voice Inspector. |

These parameters are dynamic and can change rapidly in response to various inputs. For instance, the movement of Game Objects or the discovery of new environmental data by the Acoustics Engine can alter these values. Parameter smoothing uses an exponential moving average filter to limit the rate of change of these parameters over time.

|  |  |
| --- | --- |
|  | **备注:** Parameter smoothing only applies to diffraction, transmission, and direct paths. Reflection paths are not processed by parameter smoothing. |

# Exponential Moving Average (EMA) and Smoothing Constant

Parameter smoothing uses an exponential moving average (EMA), where recent parameter values have a greater influence on the output than older values. A smoothing constant ([AkSpatialAudioInitSettings::fSmoothingConstantMs](struct_ak_spatial_audio_init_settings_a406bea3f65e5fef84954eb2603b8ecd0.html#a406bea3f65e5fef84954eb2603b8ecd0)) determines the degree of weighting decrease for previous observations.

This method ensures that sudden changes in parameters do not cause abrupt shifts in the audio output, which could be jarring to the listener. Instead, parameter changes are gradually introduced, preserving the natural evolution of the sound environment and maintaining a consistent audio experience.

The smoothing constant plays a crucial role in determining how quickly the EMA reacts to parameter changes. A larger value means that the EMA is more responsive to new data, while a smaller value produces a smoother, slower-moving average. You can adjust the value of the smoothing constant based on the desired responsiveness of the audio parameters to changes within the virtual environment.

# Reducing CPU Usage with Parameter Smoothing

You can use parameter smoothing to save CPU usage by selecting conservative values for various other initialization settings. You can reduce the number of rays cast ([AkSpatialAudioInitSettings::uNumberOfPrimaryRays](struct_ak_spatial_audio_init_settings_ae11fb70d949998617a050b5b312ed767.html#ae11fb70d949998617a050b5b312ed767 "The number of primary rays used in the ray tracing engine. A larger number of rays will increase the ...")) and also limit the number of diffraction paths ([AkSpatialAudioInitSettings::uMaxDiffractionPaths](struct_ak_spatial_audio_init_settings_a94f819cee9905b9745f9d628aedf7cf2.html#a94f819cee9905b9745f9d628aedf7cf2)) with only a minimal reduction in audio quality. When using parameter smoothing, we recommend that you experiment with various parameter adjustments to further optimize CPU usage: increase the movement threshold ([AkSpatialAudioInitSettings::fMovementThreshold](struct_ak_spatial_audio_init_settings_a15f96c2d6a69f821c8ae6d677e6d29f4.html#a15f96c2d6a69f821c8ae6d677e6d29f4 "Amount that an emitter or listener has to move to trigger a validation of reflections/diffraction....")), the load balancing spread ([AkSpatialAudioInitSettings::uLoadBalancingSpread](struct_ak_spatial_audio_init_settings_adb7560b0a616975d9f95fb932380002e.html#adb7560b0a616975d9f95fb932380002e "Spread the computation of paths on uLoadBalancingSpread frames [1..[. When uLoadBalancingSpread is se...")), and the maximum diffraction order ([AkSpatialAudioInitSettings::uMaxDiffractionOrder](struct_ak_spatial_audio_init_settings_a0e01d0d34659de40a8d84d93e05dfeab.html#a0e01d0d34659de40a8d84d93e05dfeab)).

## Number of Rays Cast Per Frame

The Acoustics Engine casts from the listener’s position to gather information about the environment. The accuracy of the simulation is proportional to the number of rays cast: when more rays are cast, more environmental data is gathered, leading to a more accurate simulation. However, casting additional rays requires more CPU resources. Therefore, it is desirable to find a balance by casting the minimum number of rays necessary to maintain an accurate simulation.

Insufficient ray casting can cause the acoustics engine to miss critical environmental features such as obstacles, reflective surfaces, or edges, especially in highly complex environments. This can lead to an incomplete perceptual understanding of the environment. At a later point in time, if new information is discovered, corrected paths will be computed and there will be discontinuities in the audio output.

## Diffraction Settings

To mitigate CPU usage, you can reduce the number of diffraction paths per emitter, which is another factor that can contribute to audio discontinuities. Low values for [AkSpatialAudioInitSettings::uMaxDiffractionPaths](struct_ak_spatial_audio_init_settings_a94f819cee9905b9745f9d628aedf7cf2.html#a94f819cee9905b9745f9d628aedf7cf2) typically cause paths to pop in and out, because a shorter path around one side of an obstacle replaces a longer path.

You can also reduce the maximum diffraction order, which determines the maximum number of edges that a single path can contain. Low values for [AkSpatialAudioInitSettings::uMaxDiffractionOrder](struct_ak_spatial_audio_init_settings_a0e01d0d34659de40a8d84d93e05dfeab.html#a0e01d0d34659de40a8d84d93e05dfeab) can cause diffraction value discontinuities when the maximum number of edges is exceeded.

Using parameter smoothing to eliminate discontinuities from conservative diffraction settings makes these kinds of artifacts much less audible and provides a more continuous audio experience.