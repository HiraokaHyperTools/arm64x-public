psqlodbc_arm64.msi (Arm64)
=========================================================

つぎのセットアップをダウンロードして、インストールしようとしています。

https://github.com/psqlodbc-for-win10-arm64/psqlodbc/releases/download/17.00.0004-arm64.alpha1/psqlodbc_arm64.msi

.. image:: imgs/a64/b1.png

.. image:: imgs/a64/b2.png

.. image:: imgs/a64/b3.png

.. image:: imgs/a64/b4.png

.. image:: imgs/a64/b5.png

インストールが完了しました。

つぎに ODBC データソースの設定をしていきます。

この Windows 11 の odbcad32 は 2 つです:

- ``ODBC Data Source Administrator (32-bit)`` (x86 版)
- ``ODBC Data Source Administrator (64-bit)`` (Arm64 版)

.. image:: imgs/a64/a64-odbcad32.png

``ODBC Data Sources (64-bit)`` を起動し ``Add`` で ``PostgreSQL Unicode(arm64)`` を選択して ``Finish`` をクリック:

.. image:: imgs/a64/a64-odbcad32-64.png

``PostgreSQL Unicode ODBC Driver(psqlODBC) Setup`` 画面が起動しました:

.. image:: imgs/a64/odbcad32-64-add-psqlodbc.png

接続情報を入力して ``Test`` をクリック。
``Connection successful`` が表示されました。
正常に動作しているようです。

.. code-block:: text

   ---------------------------
   Connection Test
   ---------------------------
   Connection successful
   ---------------------------
   OK   
   ---------------------------

.. image:: imgs/a64/odbcad32-64-add-psqlodbc-ok.png

``OK`` をクリック、
``Save`` をクリックして、設定を保存します。

Microsoft Access で確認します。

- 起動
- テスト用のデータベースを開き
- ``External Data`` タブを開く
- ``New Data Source`` → ``From Other Sources`` → ``ODBC Database`` を選択
- ``Link to the data source by creating a linked table.`` を選択し ``OK`` をクリック

``Select Data Source`` 画面が表示されます:

.. image:: imgs/a64/access-dsn.png

``PostgreSQL35W`` を選択して ``OK`` をクリックすると、エラーが発生しました。

.. code-block:: text

   Microsoft Access

   ODBC--call failed.

   Specified driver could not be loaded due to system error  193: (PostgreSQL Unicode(arm64), C:\Program Files\psqlODBC\1700\bin\podbc35w.dll), (#160)

.. image:: imgs/a64/access-dsn-add-err.png

想定通りの結果になりました。

Arm64EC (x64) バイナリーである ``MSACCESS.EXE`` は、
Arm64 バイナリーである psqlODBC との互換性がありません。

そのため psqlODBC のロードに失敗しました。
