# GetDeviceProfile

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AK](namespace_a_k.html)
- [IAkStreamMgrProfile](class_a_k_1_1_i_ak_stream_mgr_profile.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [GetDeviceProfile](class_a_k_1_1_i_ak_stream_mgr_profile_ac8280a0212698611fcc5f4b173c21832.html#ac8280a0212698611fcc5f4b173c21832) | | [GetNumDevices](class_a_k_1_1_i_ak_stream_mgr_profile_a7260fd56a4eac4e8cf299ed92ed658e5.html#a7260fd56a4eac4e8cf299ed92ed658e5) | | [StartMonitoring](class_a_k_1_1_i_ak_stream_mgr_profile_a66cae38e39771bef15100d112feab413.html#a66cae38e39771bef15100d112feab413) | | [StopMonitoring](class_a_k_1_1_i_ak_stream_mgr_profile_a32895a4a3fae7449e2c73d7bc7ffc3a6.html#a32895a4a3fae7449e2c73d7bc7ffc3a6) | | [~IAkStreamMgrProfile](class_a_k_1_1_i_ak_stream_mgr_profile_a94a400d58854ab89784956eb99ebb86b.html#a94a400d58854ab89784956eb99ebb86b) | | [◆](#ac8280a0212698611fcc5f4b173c21832)GetDeviceProfile() |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | virtual [IAkDeviceProfile](class_a_k_1_1_i_ak_device_profile.html)\* AK::IAkStreamMgrProfile::GetDeviceProfile | ( | [AkUInt32](_ak_numeral_types_8h_a39c6c5d577901802ca77775760b704ce.html#a39c6c5d577901802ca77775760b704ce) | *in\_uDeviceIndex* | ) |  | | pure virtual |  Get a device profile for a specified device index.  备注  [GetDeviceProfile()](class_a_k_1_1_i_ak_stream_mgr_profile_ac8280a0212698611fcc5f4b173c21832.html#ac8280a0212698611fcc5f4b173c21832) refers to devices by index, which must honor the call to [AK::IAkStreamMgrProfile::GetNumDevices()](class_a_k_1_1_i_ak_stream_mgr_profile_a7260fd56a4eac4e8cf299ed92ed658e5.html#a7260fd56a4eac4e8cf299ed92ed658e5).  The device index is not the same as the device ID (AkDeviceID).  参见  - [流播放/流管理器](streamingdevicemanager.html)  参数  |  |  | | --- | --- | | in\_uDeviceIndex | Device index: [0,numDevices[ | |