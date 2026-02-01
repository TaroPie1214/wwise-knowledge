# RandomSeed

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkPluginServiceRNG](class_a_k_1_1_i_ak_plugin_service_r_n_g.html)

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [CreateRNG](class_a_k_1_1_i_ak_plugin_service_r_n_g_ae267909ad06df7f0f2c2c1b138e5864e.html#ae267909ad06df7f0f2c2c1b138e5864e) | | [RandomSeed](class_a_k_1_1_i_ak_plugin_service_r_n_g_a1f71793e4249802c70337bbedaa312ed.html#a1f71793e4249802c70337bbedaa312ed) | | [~IAkPluginServiceRNG](class_a_k_1_1_i_ak_plugin_service_r_n_g_ab19a8cefe9bfbbb9d530f13cae6b6d50.html#ab19a8cefe9bfbbb9d530f13cae6b6d50) | | [◆](#a1f71793e4249802c70337bbedaa312ed)RandomSeed() |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | virtual [AkUInt64](_ak_numeral_types_8h_a7b5402d7570cb20a11c8d21f2c2710ec.html#a7b5402d7570cb20a11c8d21f2c2710ec) AK::IAkPluginServiceRNG::RandomSeed | ( |  | ) | const | | pure virtual |  Advances and returns a PRNG seed that a plug-in may use in its own RNG for DSP processing This is the same seed used for the internal sound engine randomization. |