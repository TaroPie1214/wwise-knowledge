# Migrating to the UE4.11/4.12 Wwise 2016.1.1 integration

|  |
| --- |
| Wwise Unreal Integration Documentation |

Migrating to the UE4.11/4.12 Wwise 2016.1.1 integration

As part of the fix for WG-30404, the `AttenuationScalingFactor` `UPROPERTY` of `AkComponent` has been made read-only in Blueprints. To set its value, you now need to call the `SetAttenuationScalingFactor` method on `AkComponent`.