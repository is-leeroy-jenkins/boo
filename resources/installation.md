# Boo installation

Boo opens in a dedicated Edge WebView2 window without browser tabs or an address bar. Closing the window stops its local Streamlit server. The existing provider controls and application tabs remain available.

## Requirements

- Windows x64 and Microsoft [Edge WebView2 Runtime](https://developer.microsoft.com/en-us/microsoft-edge/webview2/).
- Python 3.11 or 3.12 for a PyPI installation. The Windows installer includes Python.
- Internet access and your own provider credentials for GPT, Gemini, and Grok services. Local sentence-transformer models may require a download.

## Install from PyPI

After the first publication, run in PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install boo-py
boo
```

`boo` launches the tabless Windows UI. `boo-browser` launches ordinary browser mode and supports other operating systems. The distribution is `boo-py`; the import is `boo`.

## Windows installer

1. Open [Windows installer Actions](https://github.com/is-leeroy-jenkins/boo/actions/workflows/windows-installer.yml) after merging the packaging changes.
2. Run **Build Boo Windows desktop installer** on `main`.
3. Download and extract the **Boo-Windows-Installer** artifact from the successful run.
4. Run `Boo-Setup-0.1.0.exe`, choose the optional desktop shortcut, and finish the wizard.
5. Launch Boo from the Start Menu or desktop shortcut.

The default installation is `%LOCALAPPDATA%\Programs\Boo` and requires no administrator privileges. Builds are unsigned unless signing is configured. The workflow uploads an artifact; it does not publish an installer release automatically.

## Credentials and data

Set `OPENAI_API_KEY`, `GEMINI_API_KEY` (or `GOOGLE_API_KEY`), and `XAI_API_KEY` for the providers you use. Grok management features also require `XAI_MANAGEMENT_KEY`. Google Cloud features require their normal project configuration and application default credentials. Provider keys can also be entered through the existing application controls.

Example persistent user setting:

```powershell
[Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'your-key', 'User')
```

Restart your terminal or sign out and back in before launching through a shortcut so the process receives changed environment settings. API keys are not included in the package.

Writable resources, theme settings, databases, exports, and logs use `%LOCALAPPDATA%\Boo`. The nested `stores\sqlite\datamodels` directory is created for Boo's database. Bundled defaults are copied only when missing, preserving existing user files. Development databases, logs, notebooks, secrets, and GIF demos are excluded. The local server binds to `127.0.0.1` on an available port.

## Build from source

Install Python 3.11 x64, Git, and [Inno Setup 6](https://jrsoftware.org/isinfo.php), then run on Windows:

```powershell
git clone https://github.com/is-leeroy-jenkins/boo.git
cd boo
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements-desktop.txt
python desktop.py
python -m PyInstaller --noconfirm --clean boo.spec
& "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "installer\boo.iss"
```

The installer is written to `dist-installer`. Build on Windows; PyInstaller does not cross-compile Windows executables from Linux.

## Troubleshooting and upgrades

Check `%LOCALAPPDATA%\Boo\desktop.log` for startup errors. Install WebView2 if the window does not open. Verify credentials and internet access if provider requests fail. Back up `%LOCALAPPDATA%\Boo` before upgrading.

Close Boo and run the newer Setup executable to upgrade. Uninstall through Windows Settings → Apps → Boo. User data remains after uninstall and can be removed separately.

A successful Windows build and clean-machine test are required to validate the native installer. Check startup, provider workflows, database persistence, window-close server cleanup, and uninstall.

[PyPI release instructions](pypi-release.md) · [README](../README.md)
