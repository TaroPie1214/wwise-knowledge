# Geometry

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Geometry

The Geometry API allows the game to send a triangle mesh to Wwise Spatial Audio, for these purposes:

- 利用 Reflect 模拟早期反射（参见 [使用 Geometry API 模拟早期反射](spatial_audio_apigeometry_er.html) 章节）。
- 模拟声音从发声体传播到听者所在位置的过程中产生的边缘衍射（参见 [使用 Geometry API 模拟衍射和透射](spatial_audio_apigeometry_diffract.html) 章节）。
- Defining the shape of a room.
  - Computing which room each Game Object is in: [Room Containment](spatial_audio_apigeometry_rc.html).
  - Measuring an accurate distance to the shape of the room: [Geometric Room Distance on Direct Paths](spatial_audio_roomsportals_distance.html)

参见
:   - [描述几何构造](spatial_audio_apigeometry_geometry.html)
    - [射线追踪引擎几何构造指南](raytracing_geometry_guide.html)
    - [第三人称视角和 Spatial Audio](spatial_audio_third_person.html)