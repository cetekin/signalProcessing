# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['projeV2.py'],
             pathex=['/home/tekin/Desktop/gitRepos/signalProcessing'],
             binaries=[],
             datas=[],
             hiddenimports=['sklearn.neighbors.typedefs', 'sklearn.ensemble', 'sklearn.neighbors.quad_tree', 'sklearn.tree._utils'],
             hookspath=['/home/tekin/Desktop/gitRepos/signalProcessing/hookFolder'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='projeV2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='projeV2')
