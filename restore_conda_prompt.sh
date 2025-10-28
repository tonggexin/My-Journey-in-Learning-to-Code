#!/bin/bash

# 这个脚本用于恢复conda环境提示符的默认设置
# 请在WSL终端中运行

echo "正在恢复conda环境提示符的默认设置..."

# 方法1：移除env_prompt配置项
conda config --remove-key env_prompt 2>/dev/null || echo "注意: env_prompt配置项可能不存在"

# 方法2：直接编辑.condarc文件（如果存在）
if [ -f "$HOME/.condarc" ]; then
    echo "已找到.condarc文件，正在编辑..."
    grep -v "env_prompt" "$HOME/.condarc" > "$HOME/.condarc.tmp"
    mv "$HOME/.condarc.tmp" "$HOME/.condarc"
fi

echo "恢复完成！请重新打开终端或运行 'source ~/.bashrc' 来应用更改。"
echo "如果需要为特定环境自定义提示符，可以使用环境变量CONDA_PROMPT_MODIFIER。"