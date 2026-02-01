# AkCmd_SA_SetGameObjectRadius

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

[所有成员列表](struct_ak_cmd___s_a___set_game_object_radius-members.html) |
[Public 属性](#pub-attribs)

AkCmd\_SA\_SetGameObjectRadius结构体 参考

`#include <AkCommandTypes.h>`

|  |  |
| --- | --- |
| Public 属性 | |
| [AkGameObjectID](_ak_typedefs_8h_a352a1eb6955fa208062e40a9ccdd2560.html#a352a1eb6955fa208062e40a9ccdd2560) | [gameObjectID](struct_ak_cmd___s_a___set_game_object_radius_a3586972a9a72c117f55985c95abe036e.html#a3586972a9a72c117f55985c95abe036e) |
|  | Game object ID [更多...](struct_ak_cmd___s_a___set_game_object_radius_a3586972a9a72c117f55985c95abe036e.html#a3586972a9a72c117f55985c95abe036e) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [outerRadius](struct_ak_cmd___s_a___set_game_object_radius_a4f729134062c54bece48589903f58e15.html#a4f729134062c54bece48589903f58e15) |
|  | Outer radius around each sound position, defining 50% spread. Must satisfy `innerRadius` <= `outerRadius`. [更多...](struct_ak_cmd___s_a___set_game_object_radius_a4f729134062c54bece48589903f58e15.html#a4f729134062c54bece48589903f58e15) |
|  | |
| [AkReal32](_ak_numeral_types_8h_afc38459f26e2b23defe588026e886a98.html#afc38459f26e2b23defe588026e886a98) | [innerRadius](struct_ak_cmd___s_a___set_game_object_radius_ad95db9faea47f840ac1e359c068c2d1d.html#ad95db9faea47f840ac1e359c068c2d1d) |
|  | Inner radius around each sound position, defining 100% spread and 0 attenuation distance. Must satisfy `innerRadius` <= `outerRadius`. [更多...](struct_ak_cmd___s_a___set_game_object_radius_ad95db9faea47f840ac1e359c068c2d1d.html#ad95db9faea47f840ac1e359c068c2d1d) |
|  | |

## 详细描述

Define an inner and outer radius around each sound position for a specified game object. If the radii are set to 0, the game object is a point source. Non-zero radii create a Radial Emitter. The radii are used in spread and distance calculations that simulates sound emitting from a spherical volume of space. When applying attenuation curves, the distance between the listener and the inner sphere (defined by the sound position and `innerRadius`) is used. The spread for each sound position is calculated as follows:

- If the listener is outside the outer radius, the spread is defined by the area that the sphere occupies in the listener field of view. Specifically, this angle is calculated as `2.0*asinf( outerRadius / distance )`, where distance is the distance between the listener and the sound position.
- When the listener intersects the outer radius (the listener is exactly `outerRadius` units away from the sound position), the spread is exactly 50%.
- When the listener is between the inner and outer radii, the spread interpolates linearly from 50% to 100% as the listener transitions from the outer radius towards the inner radius.
- If the listener is inside the inner radius, the spread is 100%.

  |  |  |
  | --- | --- |
  |  | **备注:** Transmission and diffraction calculations in Spatial Audio always use the center of the sphere (the position(s) passed into `AkCmd_SetPosition` or `AkCmd_SetMultiplePositions`) for raycasting. To obtain accurate diffraction and transmission calculations for radial sources, where different parts of the volume may take different paths through or around geometry, it is necessary to pass multiple sound positions into `AkCmd_SetMultiplePositions` to allow the engine to 'sample' the area at different points.  This command can fail for the following reasons: |
- AK\_InvalidParameter: `gameObjectID` is invalid or `outerRadius` > `innerRadius`
- AK\_IDNotFound: `gameObjectID` is specified but is not a registered game object.
- AK\_InsufficientMemory: Not enough memory to complete the operation.

参见
:   - [AkCommand\_SA\_SetGameObjectRadius](_ak_command_types_8h_a001b78645b8b0335c0dd2e128cca2cfd.html#a001b78645b8b0335c0dd2e128cca2cfdaaaa4a14c77692f932cca22c7b94a85a1)
    - [AkCmd\_SetPosition](struct_ak_cmd___set_position.html)
    - [AkCmd\_SetMultiplePositions](struct_ak_cmd___set_multiple_positions.html)

在文件 [AkCommandTypes.h](_ak_command_types_8h_source.html) 第 [1781](_ak_command_types_8h_source.html#l01781) 行定义.