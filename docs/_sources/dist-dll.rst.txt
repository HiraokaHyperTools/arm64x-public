DLL を配布する場合
=================================================

DLL の配布を主目的とするケースです。

方針、例:

- DLL は 5 種類: x86, x64, Arm64, Arm64EC, Arm64X
- x86 版は常にインストールする
- どのバイナリーが利用可能かによってセットアップの方針が異なってくる
- 理想は x86 + x64 + Arm64X の組み合わせ

x86 + x64
-------------------------------------------------

psqlODBC の Windows 向けバイナリーでは 2 点方式になっています:

- ``psqlodbc_x64.msi``
- ``psqlodbc_x86.msi``

x86 + x64 + Arm64
-------------------------------------------------

Shining Light Productions 社のご好意によって提供されている OpenSSL の Windows 向けバイナリーでは 3 点方式になっています:

- ``Win64OpenSSL-3_5_1.exe`` (x64)
- ``Win32OpenSSL-3_5_1.exe`` (x86)
- ``Win64ARMOpenSSL-3_5_1.exe`` (Arm64)

※ Arm64EC 版および Arm64X 版は存在しません。必要な場合は、自分でビルドしましょう。

x86 + x64 + Arm64X
-------------------------------------------------

Microsoft の `サポートされている最新の Visual C++ 再頒布可能パッケージのダウンロード | Microsoft Learn <https://learn.microsoft.com/ja-jp/cpp/windows/latest-supported-vc-redist?view=msvc-170>`_ では 3 点方式になっています:

- ``vc_redist.arm64.exe`` バイナリーは Arm64X
- ``vc_redist.x86.exe``
- ``vc_redist.x64.exe``

※ Arm64X 版が提供されています。 Arm 版 Windows 11 では、x64 アプリおよび Arm64 アプリの両方から利用ができます。

Microsoft の `ODBC Driver for SQL Server のダウンロード - ODBC Driver for SQL Server | Microsoft Learn <https://learn.microsoft.com/ja-jp/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16>`_ では 3 点方式になっています:

- ``msodbcsql.msi`` (x64)
- ``msodbcsql.msi`` (x86)
- ``msodbcsql.msi`` (ARM64) バイナリーは Arm64X

※ Arm64X 版が提供されています。 Arm 版 Windows 11 では、x64 アプリおよび Arm64 アプリの両方から利用ができます。
