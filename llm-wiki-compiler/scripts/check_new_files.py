import os
import json
import time

# 設定路徑
WATCH_DIRS = [
    # LLM Wiki 核心知識庫 (21_LLM_Wiki_核心知識庫) - 已移至 Documents 根目錄
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/21_LLM_Wiki_核心知識庫/02_Raw_原始資料",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/21_LLM_Wiki_核心知識庫",
    # 工作紀錄與系統
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/20_Work_Logs_工作紀錄",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/19_System_Settings_系統設定",
    # 執行與規劃
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/17_Execution_Logs_執行紀錄",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/16_Planning_工作規劃",
    # 探索與工具
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/15_Exploration_工具探索",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/06_Skill_Mgmt_技能管理",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/02_Skills_技能與工具指南",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/01_Roles_提示詞與角色",
    # 工作與成長
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/14_Work_工作類",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/13_Growth_個人成長與理論",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/12_Tech_KM_技術KM",
    # 技術與運維
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/11_Ops_系統運維與環境",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/03_Arch_技術架構與安全",
    # Dynasafe 與下載
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/10_Work_Dynasafe_Dynasafe專屬",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/09_Downloads_下載管理",
    # 對話與附件
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/08_Transcripts_對話與對接",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/07_Assets_附件與檔案管理",
    # 報告與戰略
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/05_Reports_內部報告與執行紀錄",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/04_Strategy_戰略與案例分析",
    # 市場趨勢
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/00_Trends_市場趨勢",
]
STATE_FILE = os.path.expanduser("~/.qwen/skills/llm-wiki-compiler/state.json")

def get_file_list(dirs):
    files = {}
    # 排除目錄清單
    EXCLUDED_DIRS = {
        '.obsidian', '.git', '.github', 'node_modules', '__pycache__',
        '.venv', 'venv', '.cache', '.trash', 'dist', 'build',
        '21_LLM_Wiki_核心知識庫/01_System_系統層'  # 系統層不編譯
    }
    # 排除檔案類型
    EXCLUDED_EXTENSIONS = {'.DS_Store', '.lock', '.log'}
    
    for d in dirs:
        if not os.path.exists(d): continue
        for root, dirnames, filenames in os.walk(d):
            # 排除特定目錄 (直接修改dirnames阻止os.walk進入)
            dirnames[:] = [
                dirname for dirname in dirnames
                if dirname not in EXCLUDED_DIRS
                and not dirname.startswith('.')
            ]
            
            for f in filenames:
                # 排除隱藏檔案與特定副檔名
                if f.startswith('.'): continue
                ext = os.path.splitext(f)[1]
                if ext in EXCLUDED_EXTENSIONS: continue
                if f.endswith('.DS_Store'): continue
                
                full_path = os.path.join(root, f)
                # 二次檢查路徑中是否包含排除目錄
                if any(excluded in full_path for excluded in EXCLUDED_DIRS):
                    continue
                    
                # 紀錄檔案路徑與最後修改時間
                files[full_path] = os.path.getmtime(full_path)
    return files

def main():
    # 載入舊狀態
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            old_state = json.load(f)
    else:
        old_state = {}

    current_state = get_file_list(WATCH_DIRS)
    
    # 找出新檔案 (包含新增或修改過的)
    new_files = []
    for path, mtime in current_state.items():
        if path not in old_state or mtime > old_state[path]:
            new_files.append(path)

    # 輸出結果
    if new_files:
        print(f"FOUND_NEW_FILES: {json.dumps(new_files, ensure_ascii=False)}")
    else:
        print("NO_NEW_FILES")

    # 更新狀態 (暫不更新，直到確定編譯完成)
    # 這裡的邏輯由 Skill 指令來控制是否寫回狀態

if __name__ == "__main__":
    main()
