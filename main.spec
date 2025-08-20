# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/axe.png', 'assets'), ('assets/bg.png', 'assets'), ('assets/bgg.png', 'assets'), ('assets/branch.png', 'assets'), ('assets/branch_flipped.png', 'assets'), ('assets/cloud.png', 'assets'), ('assets/dead.png', 'assets'), ('assets/dead_flipped.png', 'assets'), ('assets/github.png', 'assets'), ('assets/gmail.png', 'assets'), ('assets/info.png', 'assets'), ('assets/info_panel.png', 'assets'), ('assets/info_panel2.png', 'assets'), ('assets/landing_bg.png', 'assets'), ('assets/leaderboard.png', 'assets'), ('assets/leftji.png', 'assets'), ('assets/loading.png', 'assets'), ('assets/log.png', 'assets'), ('assets/man.gif', 'assets'), ('assets/man_down_left.png', 'assets'), ('assets/man_down_right.png', 'assets'), ('assets/man_up_left.png', 'assets'), ('assets/man_up_right.png', 'assets'), ('assets/menu.png', 'assets'), ('assets/mute.png', 'assets'), ('assets/mute2.png', 'assets'), ('assets/slack.png', 'assets'), ('assets/smiling_man.png', 'assets'), ('assets/squished.png', 'assets'), ('assets/squished_4.png', 'assets'), ('assets/tick.png', 'assets'), ('assets/timberly.png', 'assets'), ('assets/time_over.png', 'assets'), ('assets/tree.png', 'assets'), ('assets/volume.png', 'assets'), ('assets/watching_man.png', 'assets'), ('assets/wave.png', 'assets'), ('assets/wood.png', 'assets'), ('audio/chop.wav', 'audio'), ('audio/dead.wav', 'audio'), ('audio/magic_forest.wav', 'audio'), ('audio/time_up.wav', 'audio'), ('fonts/BebasNeue-Regular.ttf', 'fonts'), ('fonts/VarelaRound-Regular.ttf', 'fonts'), ('assets/logo.png', 'assets'), ('assets/logo.ico', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Timberly',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\logo.ico'],
)
