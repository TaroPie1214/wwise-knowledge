# Using Wwise Motion in Unreal

|  |
| --- |
| Wwise Unreal Integration Documentation |

Using Wwise Motion in Unreal

This tutorial demonstrates how to add a vibration effect to a controller through the Motion plug-in.

Before you begin this tutorial:

- Install the Motion plug-in through the Wwise Launcher.
- Learn about Motion integration. Refer to [Integrating Wwise Motion](https://www.audiokinetic.com/en/library/edge/?source=SDK&id=integrating_elements_motion.html) for details.
- Add a Motion Bus to the Wwise Project. See <a href="https://www.audiokinetic.com/library/edge/?source=Help&id=add\_motion\_bus\_project.html" target="\_blank>Adding a Motion Bus to a Wwise Project.

# Adding a Motion Bus to the Wwise Project

First, add a new bus to your Wwise project and associate the Motion plug-in with it.

**To add a Motion bus:**

1. In Wwise Authoring, open the Busses hierarchy and create a new Audio bus under the Default Work Unit and call it "Motion Bus".
2. Select the new bus and change the Audio Device to a Wwise Motion Audio Device. By default, it is called "Wwise\_Motion".
3. In the Containers hierarchy, create a Sound SFX called "MotionSFX" and change its Output Bus to "Motion Bus".
4. Add a Motion Source as its Source.
5. (Optional) Do one or both of the following in the Motion Source Editor:
   - Change the Actuator Configuration of the Motion plug-in to something that matches the targeted controller device.
   - Unlink the Actuator Configuration, depending on the platform. This example targets Windows with a Generic 1-Channel configuration.
6. Play the MotionSFX to verify that the controller vibrates.
7. Create a new Event called “Play\_Motion” that plays the Sound “MotionSFX”.
8. Generate SoundBanks and save the Wwise project.

# Integrating Motion into the Game

To transmit the Motion signal to the gamepad, you need to call AddOutput in Unreal with the corresponding Audio Device. You can do this either with a Blueprint or in C++. You can use various engine events to determine when to call AddOutput:

- Call it on the PlayerController when it is possessed by a pawn (that is, when a real player starts controlling it), but the Gamepad must be connected first.
- React to an event when a gamepad is connected through the OnInputDeviceConnectionChange callback.
- React to platform-specific callbacks when new gamepad controllers are plugged in.

First, however, you must create assets for the Event and the Audio Device.

**To create Motion assets in Unreal:**

1. Open the Wwise Browser, and click **Reconcile**. ![](../../../images/btn_reconcile.png)
2. Regenerate your SoundBanks.

## Using Blueprints

Before you proceed with this section of the tutorial, ensure that a gamepad is connected. The example also targets an XInput controller type (Xbox controller).

**To add vibration through Blueprint:**

1. Open your GameMode Blueprint Class, find the Player Controller Class and click **+** to create a new Blueprint. You can also click on the Toolbar Blueprint button, then in the GameMode click **Edit [GameMode]** > **PlayerController** > **Create, derive from PlayerController**.
2. Open the PlayerController Blueprint and in the Event Graph, right-click to add the OnPossess event. Add the AddOutput function and connect the Exec pin to OnPossess.
3. Drag the “In Settings” pin to create a Make AkOutputSettings node.
4. In the AkOutputSettings box, select “Wwise\_Motion” for the Audio Device ShareSet pin. The Id Device pin refers to the DeviceID, which varies by platform. For Windows, it is an index from 0 to 3 in the order of the connection of the gamepad. Set it to 0 to select the first available gamepad connected.   
   Unreal cannot retrieve the DeviceID as described in the [Game setup table](https://www.audiokinetic.com/en/library/edge/?source=SDK&id=integrating_elements_motion.html#motion_application_setup). For other platforms, you must write C++ code to retrieve the proper ID.  
   You can now post Play\_Motion with a Post Event function to make the gamepad vibrate.

To stop the gamepad from vibrating, you can use the RemoveOutput function using the return value of the AddOutput function as the parameter.

## Using C++

You can use C++ to add vibration effects to controllers. C++ is more flexible than Blueprints. In particular, it is easier to select something other than the first controller for the DeviceID.

As in the Blueprint section, this example targets Windows and uses an XInput controller.

**To add vibration through C++:**

1. In Unreal, click **Tools** > **New C++ Class**. The Add C++ Class dialog opens.
2. Select **Player Controller** as the parent class and click **Next**.
3. Name the controller and click **Create Class**. The new class opens in your development environment.
4. In the `[UnrealProjectName].Build.cs` file, add “WwiseSoundEngine” to the list of PublicDependencyModuleNames. You need this to call Wwise SDK functions.
5. Copy the following code into the `[PlayerControllerClassName].h` file:

   // Copyright Audiokinetic 2022

   #pragma once

   #include "CoreMinimal.h"

   #include "GameFramework/PlayerController.h"

   #include "MyPlayerController.generated.h"

   UCLASS()

   class WWISEDEMOGAME\_API AMyPlayerController : public APlayerController

   {

   GENERATED\_BODY()

   private:

   virtual void AddMotionOutput();

   protected:

   virtual void OnPossess(APawn\* InPawn) override;

   };
6. Copy the following code into the `[PlayerControllerClassName].cpp` file:

   // Copyright Audiokinetic 2022

   #include "MyPlayerController.h"

   #include "Engine/LocalPlayer.h"

   #include "Wwise/API/WwiseSoundEngineAPI.h"

   void AMyPlayerController::AddMotionOutput()

   {

   // Because a PlayerController can be instantiated on Server, we want to add Motion only to the Local Player Controller.

   if (IsLocalController())

   {

   int32 index = GetInputIndex();

   auto\* SoundEngine = IWwiseSoundEngineAPI::Get();

   if (index != INVALID\_CONTROLLERID && LIKELY(SoundEngine))

   {

   AkOutputSettings outputSettings("Wwise\_Motion", index);

   SoundEngine->AddOutput(outputSettings);

   }

   }

   }

   void AMyPlayerController::OnPossess(APawn\* InPawn)

   {

   Super::OnPossess(InPawn);

   AddMotionOutput();

   }

   As in the Blueprint, this code calls AddOutput when the PlayerController possesses a Pawn. The AddMotionOutput function starts by querying whether the current PlayerController is local. Then, the SoundEngine's API is used to call Wwise functions directly. GetInputIndex returns the Gamepad index as defined by Unreal. For an XInput device on Windows, this corresponds to a range of 0 to 3, so it matches Wwise expectations.
7. Compile and start Unreal Editor. In the Toolbar Blueprint menu, go to GameMode > PlayerController > Select PlayerController Class, and select the new C++ class.  
   You can post Play\_Motion with a Post Event function to make the gamepad vibrate.

|  |  |
| --- | --- |
|  | **注記：**  - For DualSense on Windows, as stated in the [Integrating Wwise Motion](https://www.audiokinetic.com/en/library/edge/?source=SDK&id=integrating_elements_motion.html#wwise_motion_libscepad) documentation, you must link to the static library of libScePad for PC Games. In UE5, DualSense is supported through the use of the WinDualShock plug-in, which links to libScePad, and so you must use the ScePad function from this library. - The Wwise Unreal Integration links to Motion Dynamically, so you must use the AKMOTIONSINK\_DYNAMIC\_LINK\_SCEPAD\_FUNCTIONS macro in Unreal. |

# Additional Platform-Specific Information

This section includes extra setup information for different platforms.

On Windows, you can use the following code to differentiate between an XInput controller and DualSense or DualShock:

#if defined(PLATFORM\_WINDOWS) && PLATFORM\_WINDOWS

static FString XInputControllerIdentifier = TEXT("XInputController");

static FString DualShock4InputControllerIdentifier = TEXT("DualShock4");

static FString DualSenseInputControllerIdentifier = TEXT("DualSense");

const FInputDeviceScope\* InputScope = FInputDeviceScope::GetCurrent();

if (InputScope)

{

if (InputScope->HardwareDeviceIdentifier == XInputControllerIdentifier)

{

// XInput controller, fetch 0 to 3.

}

else if ((InputScope->HardwareDeviceIdentifier == DualShock4InputControllerIdentifier) || (InputScope->HardwareDeviceIdentifier == DualSenseInputControllerIdentifier))

{

// DualSense or DualShock controller, fetch with ScePadOpen or ScePadGetHandle.

}

#endif