ODBC ドライバーを配布したい
=================================================

DLL の構成
-------------------------------------------------

例えば PostgreSQL の ODBC ドライバーを配布する場合です:

- ``psqlodbc30a.dll`` (x86)
- ``psqlodbc35w.dll`` (x86)
- ``psqlodbc30a.dll`` (x64)
- ``psqlodbc35w.dll`` (x64)
- ``psqlodbc30a.dll`` (Arm64X)
- ``psqlodbc35w.dll`` (Arm64X)

備考:

- ``psqlodbc30a.dll`` は ``PostgreSQL ANSI`` ドライバー
- ``psqlodbc35w.dll`` は ``PostgreSQL Unicode`` ドライバー
- 依存コンポーネントの DLL も用意する必要があります

   - C ランタイム: ``vcruntime140.dll``
   - PostgreSQL: ``libpq.dll``
   - OpenSSL: ``libcrypto-3-x64.dll``, ``libssl-3-x64.dll``

- Arm64 版よりも Arm64X 版での配布が好ましいです

セットアップの構成
-------------------------------------------------

セットアップは 3 通り用意する案が考えられます:

- ``psqlodbc_x86.msi`` (Windows 7, 8.1, 10, 11 向け)
- ``psqlodbc_x64.msi`` (Windows 7, 8.1, 10, 11 向け)
- ``psqlodbc_arm64.msi`` (Arm 版 Windows 10, 11 向け)
