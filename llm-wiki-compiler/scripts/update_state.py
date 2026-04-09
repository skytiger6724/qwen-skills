#!/usr/bin/env python3
"""更新 state.json - 與 check_new_files.py 使用完全相同的路徑和排除規則"""
import os
import json
import time

# 與 check_new_files.py 完全一致的設定
WATCH_DIRS = [
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/21_LLM_Wiki_核心知識庫/02_Raw_原始資料",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/21_LLM_Wiki_核心知識庫",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/20_Work_Logs_工作紀錄",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/19_System_Settings_系統設定",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/17_Execution_Logs_執行紀錄",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/16_Planning_工作規劃",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/15_Exploration_工具探索",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/06_Skill_Mgmt_技能管理",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/02_Skills_技能與工具指南",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/01_Roles_提示詞與角色",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/14_Work_工作類",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/13_Growth_個人成長與理論",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/12_Tech_KM_技術KM",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/11_Ops_系統運維與環境",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/03_Arch_技術架構與安全",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/10_Work_Dynasafe_Dynasafe專屬",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/09_Downloads_下載管理",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/08_Transcripts_對話與對接",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/07_Assets_附件與檔案管理",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/05_Reports_內部報告與執行紀錄",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/04_Strategy_戰略與案例分析",
    "/Users/dwaynejohnson/Library/CloudStorage/OneDrive-個人/Documents/00_KM_核心知識庫/00_Trends_市場趨勢",
]

EXCLUDED_DIRS = {
    '.obsidian', '.git', '.github', 'node_modules', '__pycache__',
    '.venv', 'venv', '.cache', '.trash', 'dist', 'build',
}

EXCLUDED_EXTENSIONS = {'.DS_Store', '.lock', '.log'}

STATE_FILE = os.path.expanduser("~/.qwen/skills/llm-wiki-compiler/state.json")

def get_file_list(dirs):
    files = {}
    for d in dirs:
        if not os.path.exists(d):
            continue
        for root, dirnames, filenames in os.walk(d):
            dirnames[:] = [
                dn for dn in dirnames
                if dn not in EXCLUDED_DIRS and not dn.startswith('.')
            ]
            for f in filenames:
                if f.startswith('.') or f.endswith('.DS_Store'):
                    continue
                ext = os.path.splitext(f)[1]
                if ext in EXCLUDED_EXTENSIONS:
                    continue
                full_path = os.path.join(root, f)
                files[full_path] = os.path.getmtime(full_path)
    return files

def main():
    current_state = get_file_list(WATCH_DIRS)
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(current_state, f, indent=2, ensure_ascii=False)
    print(f"STATE_UPDATED: {len(current_state)} files indexed")

if __name__ == "__main__":
    main()
