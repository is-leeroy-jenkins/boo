# -*- mode: python ; coding: utf-8 -*-
"""Package Boo and its dynamically loaded application dependencies."""
from pathlib import Path
from PyInstaller.utils.hooks import collect_all, copy_metadata

root = Path( SPECPATH )
datas = [(str( root / 'app.py' ), '.'),
         (str( root / '.streamlit' / 'config.toml' ), '.streamlit')]
datas += [(str( asset ), str( asset.parent.relative_to( root ) ))
          for asset in (root / 'resources').rglob( '*' )
          if asset.suffix.lower( ) in ('.png', '.ico')]
# Runtime databases are created in user storage; development data and secrets are excluded.
hiddenimports = ['config', 'boogr', 'gemini', 'gpt', 'grok', 'models']
binaries = []
for package in ('streamlit', 'webview',
                'plotly', 'sqlite_vec', 'sentence_transformers', 'transformers',
                'torch', 'tiktoken', 'boogr',
                'google.genai', 'google.cloud.storage', 'openai', 'xai_sdk', 'streamlit_extras', 'streamlit_pdf'):
    package_datas, package_bins, package_hidden = collect_all( package )
    datas += package_datas
    binaries += package_bins
    hiddenimports += package_hidden
for distribution in ('streamlit', 'sentence-transformers', 'transformers'):
    datas += copy_metadata( distribution, recursive=True )

a = Analysis( [str( root / 'desktop.py' )], pathex=[str( root )],
    binaries=binaries, datas=datas, hiddenimports=hiddenimports,
    hookspath=[], runtime_hooks=[], excludes=[], noarchive=False )
pyz = PYZ( a.pure )
exe = EXE( pyz, a.scripts, [], exclude_binaries=True, name='Boo',
    console=False, disable_windowed_traceback=False )
coll = COLLECT( exe, a.binaries, a.datas, strip=False, upx=False, name='Boo' )
