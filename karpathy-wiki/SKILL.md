---
name: karpathy-wiki
description: "建立並維護一個持久化的 Karpathy Wiki — 基於 Andrej Karpathy 的 LLM Wiki 模式，這是一個具備複利效應的互聯 Markdown 知識庫。數據來源涵蓋原始資料、核心知識庫與工作專區。當用戶添加來源、請求添加至 Wiki、詢問綜合性問題或請求 Wiki 健康檢查時觸發。"
---

# Karpathy Wiki (全域知識維基)

建立並維護一個持久化、具備複利效應的互聯 Markdown 知識庫。基於 Karpathy 的 LLM Wiki 模式：原始資料僅需匯入一次，編譯進 Wiki 後保持更新，而非在每次查詢時重新推導。

## 數據來源 (Raw Sources)
1. **原始資料區**：`/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/21_LLM_Wiki_核心知識庫/02_Raw_原始資料`
2. **核心知識庫**：`/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫`
3. **工作專區**：`/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/12_工作_Dynasafe`

## Wiki 成果路徑 (Wiki Base)
- **根目錄**：`/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/21_LLM_Wiki_核心知識庫`

## 決策樹 (Decision Tree)

```
21_LLM_Wiki_核心知識庫/ 是否存在？
├─ 否 → 用戶說 "init wiki" → 執行 INIT
├─ 是 →
│   ├─ 上述三個數據來源中有新檔案？ → 執行 INGEST
│   ├─ 用戶詢問 Wiki 領域問題？ → 執行 QUERY
│   ├─ 用戶要求 "lint", "health check"？ → 執行 LINT
│   └─ 用戶貼上內容或 URL？ → 存至原始資料區，然後執行 INGEST
```

## Wiki 結構 (Wiki Structure)

```
21_LLM_Wiki_核心知識庫/
├── 01_System_系統層/
│   ├── Index.md        # 內容目錄 — 每個頁面的連結與摘要
│   ├── Log.md          # 所有操作的追加式紀錄
│   └── Schema.md       # Wiki 規範
├── 02_Raw_原始資料/    # 不可變的原始文件（由用戶管理）
├── 03_Wiki_知識層/
│   ├── Synthesis_綜合/ # 高階綜合分析 (原 overview.md)
│   ├── Concepts_概念/  # 概念頁面 (例如: concepts/attention.md)
│   ├── Entities_實體/  # 實體頁面 (例如: entities/gpt-4.md)
│   └── Summaries_摘要/ # 每個匯入來源的摘要
└── 04_Output_產出層/   # 存檔的查詢結果或報告
```

## 操作流程 (Operations)

### INIT
1. 確保上述目錄結構完整。
2. 撰寫或更新 `01_System_系統層/Schema.md` 規範。
3. 初始化 `Index.md` 與 `Log.md`。

### INGEST (匯入)
1. 讀取數據來源中的新文件。
2. 在 `03_Wiki_知識層/Summaries_摘要/` 建立摘要頁面。
3. 建立或更新 `Concepts_概念/` 與 `Entities_實體/`。
4. 更新 `01_System_系統層/Index.md` 與 `Log.md`。

### QUERY (查詢)
1. 讀取 `Index.md` 尋找相關頁面。
2. 結合 Wiki 知識進行綜合回答並標註引用。
3. 價值高的回答存入 `04_Output_產出層/`。

### LINT (檢查)
1. 掃描 Wiki 頁面，檢查矛盾、過時聲明或孤立頁面。
2. 修復或回報問題。

## 頁面規範 (Page Conventions)

每個 Wiki 頁面皆有 YAML frontmatter：
```yaml
---
title: 頁面標題
type: concept | entity | source | query | synthesis
tags: [標籤1, 標籤2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [數據來源路徑/檔名.md]
---
```

## 核心規則
- **LLM 負責維護**，用戶負責提供來源。
- **原始資料不可變**：永遠不修改原始文件。
- **複利效應**：每一次查詢與匯入都應強化既有的知識網絡。
- 維持「人類視角校準器 v2.0」與「PUA 狼性指令集」融合風格。
