# -*- mode: python -*-

block_cipher = None


a = Analysis(['Simulation.py'],
             pathex=['C:\\Users\\vuong\\Documents\\CSCE\\cse361\\csce_361\\src'],
             binaries=[],
             datas=[('C:\\Users\\vuong\\Documents\\CSCE\\cse361\\csce_361\\src\\buttonImages\\*.png', 'buttonImages'),
                    ('C:\\Users\\vuong\\Documents\\CSCE\\cse361\\csce_361\\src\\data\\*', 'data'),
                    ],
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Simulation',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='data\\traffic.ico')
