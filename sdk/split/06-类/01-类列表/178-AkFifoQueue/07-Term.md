# Term

|  |
| --- |
| Wwise SDK 2025.1.4 - Windows |

- [AkFifoQueue](struct_ak_fifo_queue.html)

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | | [AkFifoQueue](struct_ak_fifo_queue_a10df635c81ffe4f8f141b3780407da4e.html#a10df635c81ffe4f8f141b3780407da4e) | | [Dequeue](struct_ak_fifo_queue_a088fbbb4403b4a6c5f7b97b62d511c79.html#a088fbbb4403b4a6c5f7b97b62d511c79) | | [Empty](struct_ak_fifo_queue_ae21a45080f08643b7cdbe76d28e916cf.html#ae21a45080f08643b7cdbe76d28e916cf) | | [Enqueue](struct_ak_fifo_queue_a9534ca2568a6a3170a5c762617eca803.html#a9534ca2568a6a3170a5c762617eca803) | | [Init](struct_ak_fifo_queue_a0063b8407d823b9ffc497007cae92d49.html#a0063b8407d823b9ffc497007cae92d49) | | [Term](struct_ak_fifo_queue_a64ef6b5d61b2009e9c41a0928763b5af.html#a64ef6b5d61b2009e9c41a0928763b5af) | | [~AkFifoQueue](struct_ak_fifo_queue_a3fe4ed6d383be37b071ace71f83a67ff.html#a3fe4ed6d383be37b071ace71f83a67ff) | | [◆](#a64ef6b5d61b2009e9c41a0928763b5af)Term() template<typename T , T TDEFAULT, class TAlloc = ArrayPoolDefault>   |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | | |  |  |  |  |  | | --- | --- | --- | --- | --- | | void [AkFifoQueue](struct_ak_fifo_queue.html)< T, TDEFAULT, TAlloc >::Term | ( |  | ) |  | | inline |  Free memory reserved for the queue and reset internal state The queue MUST be empty when this is called!  在文件 [AkFifoQueue.h](_ak_fifo_queue_8h_source.html) 第 [85](_ak_fifo_queue_8h_source.html#l00085) 行定义.  引用了 [AKASSERT](_ak_assert_8h_source.html#l00069) , 以及 [AK::MemoryMgr::Free()](namespace_a_k_1_1_memory_mgr_a6ee20149a37b11b31589c6f23f46db65.html#a6ee20149a37b11b31589c6f23f46db65).  被这些函数引用 [AkFifoQueue< T, TDEFAULT, TAlloc >::~AkFifoQueue()](_ak_fifo_queue_8h_source.html#l00049). |