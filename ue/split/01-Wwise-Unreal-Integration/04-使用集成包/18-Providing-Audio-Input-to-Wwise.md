# Providing Audio Input to Wwise

|  |
| --- |
| Wwise Unreal Integration Documentation |

Providing Audio Input to Wwise

The Unreal integration provides audio input to Wwise through the Wwise [Audio Input Source Plug-in](https://www.audiokinetic.com/library/edge/?source=SDK&id=referencematerial__audioinput.html). In order to provide audio input to Wwise, classes must inherit from `AkAudioInputComponent`.

# AkAudioInputComponent

`AkAudioInputComponent` 由 [AkComponent](pg_features_objects_components.html#features_akcomponent) 派生。It is a specialized `AkComponent` that you can use to provide audio input to Wwise. To do so, you must implement two key functions:

/\* 音频回调。此回调将由 Wwise 声音引擎连续调用，并用于为声音引擎提供音频采样。

\*/

virtual bool FillSamplesBuffer(uint32 NumChannels, uint32 NumSamples, float\*\* BufferToFill);

/\* 此回调用于为 Wwise 声音引擎提供所需音频格式。\*/

virtual void GetChannelConfig(AkAudioFormat& AudioFormat);

`AkAudioInputComponent` also has one Blueprint function, **Post Associated Audio Input Event**, which posts the component's AkAudioEvent to Wwise along with the associated AudioSamples callback and AudioFormat callback, using this component as the game object source.

# Customizing Audio Input Behavior

You can write custom classes that derive from `AkAudioInputComponent` in order to implement custom audio input behavior. The following `UAkVoiceInputComponent.h` and `UAkVoiceInputComponent.cpp` examples show a class that takes microphone input and pipes it to the Wwise Sound Engine.

Before you can use these files in a C++ Unreal project, you must perform some initial setup. First, add the AkAudio and the Unreal Voice modules to the `PublicDependencyModuleNames` in the project's `Build.cs` file. 例如：

public class MyModule : ModuleRules

{

public MyModule(ReadOnlyTargetRules Target) : base(Target)

{

PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "AkAudio", "Voice" });

// 其他设置

}

}

Next, add the following lines to the `DefaultEngine.ini` file:

[Voice]

bEnabled=true

After these setup steps are complete, add the desired custom behavior. In the following example, a class takes microphone input and sends it to Wwise.

|  |  |
| --- | --- |
|  | **注記：** The sample code in this section is not intended for use in shipped games. It is only a short example of how to implement custom behavior. |

Here is an example of a customized `AkVoiceInputComponent.h` file:

#pragma once

#include "CoreMinimal.h"

#include "AkAudioInputComponent.h"

#include "Voice.h"

#include "AkVoiceInputComponent.generated.h"

/\*

\*/

UCLASS(ClassGroup = Audiokinetic, BlueprintType, hidecategories = (Transform, Rendering, Mobility, LOD, Component, Activation), meta = (BlueprintSpawnableComponent))

class WWISEDEMOGAME\_API UAkVoiceInputComponent : public UAkAudioInputComponent

{

GENERATED\_BODY()

UAkVoiceInputComponent(const class FObjectInitializer& ObjectInitializer);

virtual void TickComponent(float DeltaTime, enum ELevelTick TickType, FActorComponentTickFunction \*ThisTickFunction) override;

protected:

/\* 此函数会在 Wwise 声音引擎中注销此组件所属的 GameObject 后调用。\*/

virtual void PostUnregisterGameObject() override;

/\* 音频回调。此回调将由 Wwise 声音引擎连续调用，并用于为声音引擎提供音频采样。\*/

virtual bool FillSamplesBuffer(uint32 NumChannels, uint32 NumSamples, float\*\* BufferToFill) override;

/\* 此回调用于为 Wwise 声音引擎提供所需音频格式。\*/

virtual void GetChannelConfig(AkAudioFormat& AudioFormat) override;

/\* Unreal IVoiceCapture，用于获取话筒输入。\*/

TSharedPtr<IVoiceCapture> VoiceCapture;

/\* 此数组会在每次 Voice Capture 传入新的缓冲数据时重置和重写。\*/

TArray<uint8> IncomingRawVoiceData;

/\* 此数组会存管 Voice Capture 之前收集的所有音频数据。

在处理可用话筒数据时写入，在向 Wwise 引擎发送数据时读取并缩减。

建议不要缩减音频回调中的缓冲数据。请勿将此代码行用在发售的游戏中！\*/

TArray<uint8> CollectedRawVoiceData;

/\* 此标记用于阻止将话筒数据写入正被读取的已收集数据缓冲区。\*/

FThreadSafeBool bIsReadingVoiceData = false;

};

Here is an example of a customized `AkVoiceInputComponent.cpp` file:

#include "AkVoiceInputComponent.h"

UAkVoiceInputComponent::UAkVoiceInputComponent(const class FObjectInitializer& ObjectInitializer) :

UAkAudioInputComponent(ObjectInitializer)

{

CollectedRawVoiceData.Reset();

VoiceCapture = FVoiceModule::Get().CreateVoiceCapture();

}

void UAkVoiceInputComponent::TickComponent(float DeltaTime, enum ELevelTick TickType, FActorComponentTickFunction \*ThisTickFunction)

{

Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

if (!VoiceCapture.IsValid())

{

return;

}

uint32 NumAvailableVoiceCaptureBytes = 0;

EVoiceCaptureState::Type CaptureState = VoiceCapture->GetCaptureState(NumAvailableVoiceCaptureBytes);

/\* IVoiceCapture 会在每次 Tick 时更新其 EVoiceCaptureState。

我们可以在两次 Tick 之间通过该状态来辨别是否真的有要收集的新数据。\*/

if (CaptureState == EVoiceCaptureState::Ok && NumAvailableVoiceCaptureBytes > 0)

{

uint32 NumVoiceCaptureBytesReturned = 0;

IncomingRawVoiceData.Reset((int32)NumAvailableVoiceCaptureBytes);

IncomingRawVoiceData.AddDefaulted(NumAvailableVoiceCaptureBytes);

uint64 SampleCounter = 0;

VoiceCapture->GetVoiceData(IncomingRawVoiceData.GetData(), NumAvailableVoiceCaptureBytes, NumVoiceCaptureBytesReturned, SampleCounter);

if (NumVoiceCaptureBytesReturned > 0)

{

/\* 在从收集的数据缓冲区读取数据时加以调节 \*/

while (bIsReadingVoiceData) {}

CollectedRawVoiceData.Append(IncomingRawVoiceData);

}

}

}

bool UAkVoiceInputComponent::FillSamplesBuffer(uint32 NumChannels, uint32 NumSamples, float\*\* BufferToFill)

{

if (!VoiceCapture.IsValid())

{

return false;

}

const uint8 NumBytesPerSample = 2;

const uint32 NumRequiredBytesPerChannel = NumSamples \* NumBytesPerSample;

const uint32 NumRequiredBytes = NumRequiredBytesPerChannel \* NumChannels;

int16 VoiceSample = 0;

uint32 RawChannelIndex = 0;

uint32 RawSampleIndex = 0;

bIsReadingVoiceData = true;

const int32 NumSamplesAvailable = CollectedRawVoiceData.Num() / NumBytesPerSample;

const uint32 BufferSlack = (uint32)FMath::Max(0, (int32)(NumSamples \* NumChannels) - NumSamplesAvailable);

for (uint32 c = 0; c < NumChannels; ++c)

{

RawChannelIndex = c \* NumRequiredBytesPerChannel;

for (uint32 s = 0; s < NumSamples; ++s)

{

if (s >= (NumSamples - BufferSlack) / NumChannels)

{

/\* 若 Wwise 引擎认为从 Voice Capture 收到的数据不足，则使用零来填补缺失采样。\*/

BufferToFill[c][s] = 0.0f;

}

else

{

/\* 将传入的话筒音频数据转换为带符号浮点数。\*/

uint32 RawSampleDataMSBIndex = s \* 2 + 1;

uint32 RawSampleDataLSBIndex = s \* 2;

VoiceSample = (CollectedRawVoiceData[RawSampleDataMSBIndex] << 8) | CollectedRawVoiceData[RawSampleDataLSBIndex];

BufferToFill[c][s] = VoiceSample / (float)INT16\_MAX;

}

}

}

const int32 NumBytesRead = (NumSamples - BufferSlack) \* NumBytesPerSample;

/\* 注意：建议不要缩减音频回调中的缓冲数据。请勿将此代码行用在发售的游戏中！\*/

CollectedRawVoiceData.RemoveAt(0, NumBytesRead);

bIsReadingVoiceData = false;

return true;

}

void UAkVoiceInputComponent::GetChannelConfig(AkAudioFormat& AudioFormat)

{

const int sampleRate = 16000;

AudioFormat.uSampleRate = sampleRate;

AudioFormat.channelConfig.SetStandard(AK\_SPEAKER\_SETUP\_MONO);

if (VoiceCapture.IsValid())

{

/\* 发送空白设备名称以使用默认设备。\*/

if (!VoiceCapture->Init(FString(""), AudioFormat.uSampleRate, AudioFormat.channelConfig.uNumChannels))

{

UE\_LOG(LogTemp, Error, TEXT("Failed to initialize device for voice input!"));

return;

}

VoiceCapture->Start();

}

}

void UAkVoiceInputComponent::PostUnregisterGameObject()

{

Super::PostUnregisterGameObject();

if (VoiceCapture.IsValid())

{

VoiceCapture->Stop();

VoiceCapture->Shutdown();

}

}

After you add the class to an Unreal project, you can create a custom Blueprint class that has an `AkVoiceInputComponent`, and can call the **Post Associated Audio Input Event** Blueprint function (from base class `AkAudioInputComponent`) to start sending microphone data to Wwise. The following image shows part of the Blueprint for a custom Blueprint class, based on `Actor`, that has an `AkVoiceInputComponent` called `AkVoiceInput`.

![](../../../images/audioinput_blueprint.png)