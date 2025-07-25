EXE を配布する場合
=================================================

アプリケーションの配布を主目的とするケースです。

方針、例:

- EXE は 4 種類: x86, x64, Arm64, Arm64EC
- 64 ビット版については Arm64 or x64 のどちらを優先とするかによってセットアップの書き方が異なってくる

理想 (x86 + x64 + Arm64 + Arm64EC)
-------------------------------------------------

理想は x86 + x64 + Arm64 + Arm64EC の組み合わせですが、運用コストが高くなります:

- ``AppSetup_x86.exe`` (Windows 7, 8.1, 10, 11 向け)
- ``AppSetup_x64.exe`` (Windows 7, 8.1, 10, 11 向け)
- ``AppSetup_Arm64.exe`` (Arm 版 Windows 10, 11 向け)
- ``AppSetup_Arm64EC.exe`` (Arm 版 Windows 11 向け)

x64 のみ
-------------------------------------------------

EDB 社による Windows 向け PostgreSQL のダウンロードでは x64 版のみが提供されています:

- ``postgresql-17.5-3-windows-x64.exe``

x86 + x64 + Arm64
-------------------------------------------------

Shining Light Productions 社のご好意によって提供されている OpenSSL の Windows 向けバイナリーでは 3 点方式になっています:

- ``Win64OpenSSL-3_5_1.exe`` (x64)
- ``Win32OpenSSL-3_5_1.exe`` (x86)
- ``Win64ARMOpenSSL-3_5_1.exe`` (Arm64)

Notepad++ では、つぎのように 3 点方式になっています:

- ``npp.8.8.2.Installer.x64.exe``
- ``npp.8.8.2.Installer.exe`` (32-bit x86)
- ``npp.8.8.2.Installer.arm64.exe``
