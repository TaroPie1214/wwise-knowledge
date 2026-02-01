# GetProjectLicenseID

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [ak\_wwise\_plugin\_host\_v2](structak__wwise__plugin__host__v2.html)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [ak\_wwise\_plugin\_host\_v2](structak__wwise__plugin__host__v2_a34cf26edd95c4bc664f5c4f920aa336e.html#a34cf26edd95c4bc664f5c4f920aa336e) | | [GetProjectLicenseID](structak__wwise__plugin__host__v2_a763d62bc4cbc232ded6451df60c5fae2.html#a763d62bc4cbc232ded6451df60c5fae2) | | [Instance](structak__wwise__plugin__host__v2_aaed6fdc821c2577ff7d95ba861d747b4.html#aaed6fdc821c2577ff7d95ba861d747b4) | | [◆](#a763d62bc4cbc232ded6451df60c5fae2)GetProjectLicenseID |  | | --- | | [AK::Wwise::Plugin::LicenseID](struct_a_k_1_1_wwise_1_1_plugin_1_1_license_i_d.html)(\* ak\_wwise\_plugin\_host\_v2::GetProjectLicenseID) (const struct [ak\_wwise\_plugin\_host\_v2](structak__wwise__plugin__host__v2.html) \*in\_this) |  Obtain the project license ID  This ID is composed of 8 characters and is used to identify a project with Audiokinetic. You may use this ID as a key to identify a given project when implementing a custom licensing scheme.  参数  |  |  |  | | --- | --- | --- | | [in] | in\_this | Current instance of this interface. |  返回  An instance of LicenseID filled with the project license ID, or zeroed-out if the project has no license.  在文件 [Host.h](_host_8h_source.html) 第 [76](_host_8h_source.html#l00076) 行定义.  被这些函数引用 [AK.Wwise::Plugin::V2::Host::GetProjectLicenseID()](_host_8h_source.html#l00110). |