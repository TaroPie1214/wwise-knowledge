# Unit Testing Your Plug-in

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

Unit Testing Your Plug-in

# Developing Unit Tests for Your Plug-in

If you included the unit test infrastructure when you created your plug-in project, you can develop your own tests. Your plug-in project includes templates for two tests: one for the sound engine plug-in implementation and another for the parameters it uses.

The code is located in the `SoundEnginePluginTest` directory and has the following structure:

```
SoundEnginePluginTest
├───main.cpp
├───MyNewFXFXParamsTest.cpp
└───MyNewFXFXTest.cpp
```

The test project uses the Catch2 open-source unit testing framework. For more information about Catch2, such as how to define test cases, see [Catch2](https://github.com/catchorg/Catch2).

The unit tests are automatically built alongside your plug-in when you use the `wp.py build` command.

# Running Your Unit Tests

To run the unit tests, use the `test` command with the `wp.py` script:

python "%WWISEROOT%/Scripts/Build/Plugins/wp.py" test -c Release -x x64 Windows\_vc160

参见
:   - [将插件打包以便用在 Audiokinetic Launcher 中](effectplugin_tools_packaging.html)