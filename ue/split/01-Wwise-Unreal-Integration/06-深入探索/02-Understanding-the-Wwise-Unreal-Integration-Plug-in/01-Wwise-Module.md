# Wwise Module

|  |
| --- |
| Wwise Unreal Integration Documentation |

Wwise Module

The Wwise module is a simple module that contains links to all of the other permanent modules. It is therefore easy to add a reference to the Wwise module in the project's Build.cs file, instead of references to each of the other modules.

The Wwise module also contains the compiled code of the optional modules and handles their initialization as well. For example, the AudioLink Runtime module is actually compiled and embedded within the Wwise module. Because of this module structure, the Wwise plug-in and its optional modules can be properly embedded as an Engine plug-in.

# WwiseHelper Build Object

To add module dependencies, we recommend that you set them up individually in the project's module if possible. It is possible to add direct access to one of Wwise plug-in's related modules, but doing so adds complexity and potential difficulty during upgrades, for example.

Instead of adding dependencies individually, we recommend that the project's module call:

`WwiseHelper.AddDependencies(this, Target);`

This call adds all dependencies from the other modules.

## WwiseHelper as an Engine Plug-In

It is not possible to include the WwiseHelper when it is part of the Engine plug-in. However, because it is a standalone file, you can copy it to the final project along with the other Build.cs files and use its contents. It is your responsibility to update its contents whenever a new version of the Wwise plug-in is released.