# Wwise 文档 PageIndex 转换日志

## 概述

将 Wwise 文档从简单树结构转换为带 LLM summary 的 PageIndex 格式，以支持更智能的推理式检索。

## 文档清单

| 文档 | 文件名 | 节点数 | 状态 | 开始时间 | 完成时间 |
|------|--------|--------|------|----------|----------|
| Help (中文) | wwise_help_zh.md | 2,944 | ✅ 完成 | 13:25 | 13:28 |
| SDK (中文) | wwise_sdk_zh.md | 9,387 | ⏳ 待处理 | - | - |
| UE (中文) | wwise_ue_zh.md | 8,257 | ⏳ 待处理 | - | - |

**总计**: 20,620 节点

## 技术方案

### API 配置
- **Endpoint**: `$ANTHROPIC_BASE_URL` (环境变量)
- **Model**: `claude-haiku-4-5-20251001`
- **格式**: Anthropic API 兼容

### 转换流程
1. 读取现有 structure.json（仅含 title, node_id, line_num）
2. 从原始 .md 文件提取每个节点的文本内容
3. 调用 LLM 为每个节点生成 summary
4. 保存带 summary 的新 structure.json

### 输出格式
```json
{
  "doc_name": "wwise_help_zh",
  "doc_description": "Wwise 音频中间件官方帮助文档（中文版）...",
  "structure": [
    {
      "title": "节点标题",
      "node_id": "0001",
      "summary": "LLM 生成的节点摘要...",
      "line_num": 123,
      "nodes": [...]
    }
  ]
}
```

## 进度日志

### 2026-02-01

- [x] 测试 API 连接 ✅ (13:18 UTC)
  - Endpoint: `$ANTHROPIC_BASE_URL/v1/messages`
  - Model: `claude-haiku-4-5-20251001` 工作正常
- [x] 创建转换脚本 ✅ (13:20 UTC)
  - 位置: `scripts/build_pageindex.py` (重写，直接从 MD 构建)
  - 并发: 10 个请求
  - 支持断点续传
- [x] Help 文档转换完成 ✅ (13:28 UTC)
  - 2,944 节点，耗时 2.1 分钟
  - 1,645 个 summary + 753 个 prefix_summary
  - 输出: `indexes/wwise_help_zh_pageindex.json` (5.1 MB)

---

## 备注

- 预计每个节点 1 次 API 调用
- 使用 Haiku 模型降低成本
- 可以分批处理，支持断点续传
