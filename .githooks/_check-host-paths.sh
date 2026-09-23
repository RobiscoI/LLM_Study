#!/bin/sh
# 공통 본체 — tools/study-config/resolve.ps1 을 호출한다.
# Git Bash 로 파이프될 때 PowerShell 이 콘솔 OEM 코드페이지로 인코딩하면
# 한글이 깨지므로 OutputEncoding 을 UTF-8 로 강제한다.
root=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
script="$root/tools/study-config/resolve.ps1"
[ -f "$script" ] || exit 0

win_script=$(cygpath -w "$script" 2>/dev/null || echo "$script")

powershell.exe -NoProfile -ExecutionPolicy Bypass -Command \
  "[Console]::OutputEncoding=[System.Text.Encoding]::UTF8; & '$win_script'" 2>/dev/null

exit 0
