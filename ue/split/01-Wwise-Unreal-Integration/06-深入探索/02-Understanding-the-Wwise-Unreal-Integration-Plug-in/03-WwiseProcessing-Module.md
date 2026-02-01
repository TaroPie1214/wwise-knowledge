# WwiseProcessing Module

|  |
| --- |
| Wwise Unreal Integration Documentation |

WwiseProcessing Module

# Global Callbacks

The Integration includes a Global Callbacks singleton feature, which games and tools can use to leverage the Sound Engine’s `AkGlobalCallback`. For a description of the callbacks, see [AkGlobalCallbackLocation](https://www.audiokinetic.com/library/edge/?source=SDK&id=_ak_callback_8h_ae7a5e30e1402c7cf90d1b47420911676.html) in the Wwise SDK documentation. Each callback has several functions, each of which has its own uses. None of the functions is ideal in all scenarios.

The following functions are available for each callback:

- **<Location>Async**: The least expensive method, in which the callback is executed as soon as a Task Graph thread is available. You must ensure that the callback follows the best practices for multithreaded code.
- **<Location>Sync**: The fastest, most reactive method, but also the riskiest. It executes the callback in the sound engine threads, which can cause slowdowns and audio glitches. In addition, the limitations of threads created outside of the Unreal thread pools can affect performance. They don’t have the same Unreal thread-local data, stack sizes are different, and priority might be different. Use this option with caution.
- **<Location>Game**: The recommended method for user interface tasks, in which the callback must be executed on the Game Thread.