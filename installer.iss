
[Setup]
AppName=ECU AI Tuner vNext
AppVersion=1.0
DefaultDirName={pf}\ECU AI Tuner
OutputDir=dist_installer
OutputBaseFilename=ECU_AI_Tuner_Setup
Compression=lzma

[Files]
Source: "dist\ecu_ai_tuner.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ECU AI Tuner"; Filename: "{app}\ecu_ai_tuner.exe"
