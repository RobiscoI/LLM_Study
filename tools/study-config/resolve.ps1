<#
.SYNOPSIS
  study-config.json 의 PC 의존 경로를 현재 PC 기준으로 해석한다.

.DESCRIPTION
  이 저장소는 여러 PC 에서 공유된다 (RJH / RMS_Digital / USER).
  Python 설치 경로와 대용량 자료 경로가 서로 다르므로,
  study-config.json 의 절대경로를 그대로 쓰면 반드시 실패한다.

  에이전트/스크립트는 이 스크립트를 먼저 실행해서 해석된 값을 써야 한다.
  (DF 저장소의 tools/df-config/resolve.ps1 과 같은 역할이다.)

.PARAMETER Json
  사람이 읽는 요약 대신 해석 결과를 JSON 으로 출력한다 (스크립트 연동용).

.PARAMETER Strict
  문제가 있으면 exit 1.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File tools/study-config/resolve.ps1
  powershell -ExecutionPolicy Bypass -File tools/study-config/resolve.ps1 -Json
#>
[CmdletBinding()]
param(
    [switch]$Json,
    [switch]$Strict
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$cfgPath  = Join-Path $PSScriptRoot 'study-config.json'

if (-not (Test-Path $cfgPath)) {
    Write-Error "config not found: $cfgPath"
    exit 2
}

$cfg = Get-Content -Raw -Encoding UTF8 $cfgPath | ConvertFrom-Json

$problems = New-Object System.Collections.ArrayList
function Add-Problem([string]$msg) { [void]$problems.Add($msg) }

# ---------------------------------------------------------------- host 판정
$hostNames = @($cfg.hosts.PSObject.Properties.Name | Where-Object { $_ -notlike '_*' })
$hostId    = $null

# 1순위: USERNAME
if ($hostNames -contains $env:USERNAME) {
    $hostId = $env:USERNAME
}

# 2순위: repo_root 가 현재 저장소 경로와 일치하는 항목
if (-not $hostId) {
    $norm = $repoRoot.Replace('\', '/').TrimEnd('/')
    foreach ($h in $hostNames) {
        $hr = ([string]$cfg.hosts.$h.repo_root).Replace('\', '/').TrimEnd('/')
        if ($hr -and ($hr -ieq $norm)) { $hostId = $h; break }
    }
}

if (-not $hostId) {
    Add-Problem "등록되지 않은 PC 입니다 (USERNAME=$env:USERNAME). study-config.json 의 hosts 에 항목을 추가하세요. 경로를 추측해서 쓰지 마세요."
    $h = $null
} else {
    $h = $cfg.hosts.$hostId
}

# ---------------------------------------------------------------- Python
$pythonExe = $null
if ($h -and $h.python_exe -and (Test-Path $h.python_exe)) {
    $pythonExe = $h.python_exe
    $pythonSrc = 'study-config.json'
} else {
    $cmd = Get-Command python -ErrorAction SilentlyContinue
    if ($cmd) {
        $pythonExe = $cmd.Source
        $pythonSrc = 'PATH'
    } else {
        Add-Problem 'python 을 찾을 수 없습니다. PATH 에 넣거나 hosts.<PC>.python_exe 를 채우세요.'
        $pythonSrc = '(없음)'
    }
}

# venv 는 있으면 우선한다
$venvRel = if ($h -and $h.venv) { $h.venv } else { '.venv' }
$venvDir = Join-Path $repoRoot $venvRel
$venvPy  = Join-Path $venvDir 'Scripts\python.exe'
$venvOk  = Test-Path $venvPy
if ($venvOk) { $pythonExe = $venvPy; $pythonSrc = "venv ($venvRel)" }

# ---------------------------------------------------------------- .env
$envRel  = if ($h -and $h.env_file) { $h.env_file } else { '.env' }
$envPath = Join-Path $repoRoot $envRel
$envOk   = Test-Path $envPath
if (-not $envOk) {
    Add-Problem ".env 가 없습니다 ($envRel). .env.example 를 복사해 API 키를 채우세요. (.env 는 gitignore 대상이라 상대 PC 에서 넘어오지 않습니다.)"
}

# .env 에 들어 있는 키 이름만 확인한다 (값은 읽지도 출력하지도 않는다)
$envKeys = @()
if ($envOk) {
    $envKeys = @(Get-Content -Encoding UTF8 $envPath |
                 Where-Object { $_ -match '^\s*[A-Za-z_][A-Za-z0-9_]*\s*=' } |
                 ForEach-Object { ($_ -split '=', 2)[0].Trim() })
}
$missing = @()
foreach ($k in $cfg.env.required) {
    if ($envKeys -notcontains $k) { $missing += $k }
}
if ($envOk -and $missing.Count -gt 0) {
    Add-Problem ("필수 환경변수가 .env 에 없습니다: " + ($missing -join ', '))
}

# ---------------------------------------------------------------- data_root
$dataRoot = $null
if ($h -and $h.data_root) {
    $dataRoot = $h.data_root
} else {
    $dataRoot = (Join-Path $repoRoot 'data')
}
$dataOk = Test-Path $dataRoot

# ---------------------------------------------------------------- 출력
$result = [ordered]@{
    host        = $hostId
    label       = if ($h) { $h.label } else { $null }
    repo_root   = $repoRoot
    python_exe  = $pythonExe
    python_src  = $pythonSrc
    venv_dir    = $venvDir
    venv_ok     = $venvOk
    env_file    = $envPath
    env_ok      = $envOk
    env_keys    = $envKeys
    env_missing = $missing
    data_root   = $dataRoot
    data_ok     = $dataOk
    problems    = @($problems)
}

if ($Json) {
    $result | ConvertTo-Json -Depth 6
} else {
    Write-Host ''
    Write-Host '  LLM_Study  호스트 설정' -ForegroundColor Cyan
    Write-Host '  ----------------------------------------------------------'
    Write-Host ("  PC        : {0}  {1}" -f $hostId, $(if ($h) { "($($h.label))" } else { '' }))
    Write-Host ("  repo      : {0}" -f $repoRoot)
    Write-Host ("  Python    : {0}   [{1}]" -f $pythonExe, $pythonSrc)
    Write-Host ("  venv      : {0}" -f $(if ($venvOk) { $venvDir } else { "(없음) $venvDir" }))
    Write-Host ("  .env      : {0}" -f $(if ($envOk) { "있음 — 키 $($envKeys.Count)개" } else { '없음' }))
    Write-Host ("  data_root : {0}   {1}" -f $dataRoot, $(if ($dataOk) { '' } else { '(없음)' }))

    if ($problems.Count -gt 0) {
        Write-Host ''
        Write-Host '  확인 필요' -ForegroundColor Yellow
        foreach ($p in $problems) { Write-Host ("   - {0}" -f $p) -ForegroundColor Yellow }
    } else {
        Write-Host ''
        Write-Host '  문제 없음' -ForegroundColor Green
    }
    Write-Host ''
}

if ($Strict -and $problems.Count -gt 0) { exit 1 }
