#define MyAppName "Boo"
#ifndef MyAppVersion
  #define MyAppVersion "0.1.0"
#endif

[Setup]
AppId={{FD75462D-1F5F-49B7-989C-BCFC3DAFE881}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher=is-leeroy-jenkins
DefaultDirName={localappdata}\Programs\Boo
DefaultGroupName=Boo
OutputDir=..\dist-installer
OutputBaseFilename=Boo-Setup-{#MyAppVersion}
Compression=lzma2
SolidCompression=yes
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=lowest
WizardStyle=modern
UninstallDisplayName=Boo
UninstallDisplayIcon={app}\Boo.exe
CloseApplications=yes

[Files]
Source: "..\dist\Boo\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Icons]
Name: "{group}\Boo"; Filename: "{app}\Boo.exe"
Name: "{autodesktop}\Boo"; Filename: "{app}\Boo.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Boo.exe"; Description: "Launch Boo"; Flags: nowait postinstall skipifsilent
