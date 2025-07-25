psqlodbc_arm64.msi (Arm64X)
=========================================================

つぎのセットアップをダウンロードして、インストールしようとしています。

https://github.com/psqlodbc-for-win10-arm64/psqlodbc/releases/download/17.00.0004-arm64x.alpha3/psqlodbc_arm64_msi_signed.msi

.. image:: imgs/a64x/c1.png

.. image:: imgs/a64x/c2.png

.. image:: imgs/a64x/c3.png

.. image:: imgs/a64x/c4.png

.. image:: imgs/a64x/c5.png

インストールが完了しました。

つぎに ODBC データソースの設定をしていきます。

この Windows 11 の odbcad32 は 2 つです:

- ``ODBC Data Source Administrator (32-bit)`` (x86 版)
- ``ODBC Data Source Administrator (64-bit)`` (Arm64 版)

.. image:: imgs/a64x/a64-odbcad32.png

``ODBC Data Sources (64-bit)`` を起動し ``Add`` で ``PostgreSQL Unicode(x64)`` を選択して ``Finish`` をクリック:

.. image:: imgs/a64x/a64-odbcad32-64.png

``PostgreSQL Unicode ODBC Driver(psqlODBC) Setup`` 画面が起動しました:

.. image:: imgs/a64x/odbcad32-64-add-psqlodbc.png

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

.. image:: imgs/a64x/odbcad32-64-add-psqlodbc-ok.png

``OK`` をクリック、
``Save`` をクリックして、設定を保存します。

Microsoft Access で確認します。

- 起動
- テスト用のデータベースを開き
- ``External Data`` タブを開く
- ``New Data Source`` → ``From Other Sources`` → ``ODBC Database`` を選択
- ``Link to the data source by creating a linked table.`` を選択し ``OK`` をクリック

``Select Data Source`` 画面が表示されます:

.. image:: imgs/a64x/access-dsn.png

``PostgreSQL35W`` を選択して ``OK`` をクリックすると、
``Link Tables`` 画面が表示されました。

.. image:: imgs/a64x/link-tables.png

事前に設定しておいた ``public.key_value_pair`` テーブルを選択して ``OK`` をクリック:

``public_key_value_pair`` リンクテーブルが作成されました。これを開きました:

.. image:: imgs/a64x/kvp.png

ここまでの流れで Arm64 環境における Microsoft Access と psqlODBC との動作確認ができました。

Arm64X バイナリーである psqlODBC は、

- ``ODBC Data Source Administrator (64-bit)`` (Arm64) で動作しました。
- ``Microsoft Access`` (Arm64EC (x64)) で動作しました。

Arm 版 Windows 11 環境向けに Arm64X バイナリーのビルドと配布が必要になる理由を確認できました。
