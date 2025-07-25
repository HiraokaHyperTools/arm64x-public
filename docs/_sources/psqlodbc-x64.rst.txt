psqlodbc_x64.msi
=========================================================

つぎのセットアップをダウンロードして、インストールしようとしています。

https://ftp.postgresql.org/pub/odbc/releases/REL-17_00_0006/psqlodbc_x64.msi

.. image:: imgs/x64/a1.png

.. image:: imgs/x64/a2.png

.. image:: imgs/x64/a3.png

.. image:: imgs/x64/a4.png

エラーが発生しました。 ``Ignore`` で強行

.. image:: imgs/x64/a5.png

エラーが発生しました。 ``Ignore`` で強行

.. image:: imgs/x64/a6.png

エラーが発生しました。 ``Ignore`` で強行

.. image:: imgs/x64/a7.png

エラーが発生しました。 ``Ignore`` で強行

.. image:: imgs/x64/a8.png

.. image:: imgs/x64/a9.png

インストーラーのエラーを 4 回無視してインストールが完了しました。

つぎに ODBC データソースの設定をしていきます。

この Windows 11 の odbcad32 は 2 つです:

- ``ODBC Data Source Administrator (32-bit)`` (x86 版)
- ``ODBC Data Source Administrator (64-bit)`` (Arm64 版)

.. image:: imgs/x64/a64-odbcad32.png

``ODBC Data Sources (64-bit)`` を起動:

.. image:: imgs/x64/a64-odbcad32-64.png

``Add`` で ``PostgreSQL Unicode(x64)`` を選択:

.. image:: imgs/x64/odbcad32-64-add-psqlodbc.png

エラーが発生して追加ができませんでした。

.. code-block:: text

   ---------------------------
   Microsoft ODBC Administrator
   ---------------------------
   The setup routines for the PostgreSQL Unicode(x64) ODBC driver could not be loaded due to system error code 193: .
   ---------------------------
   OK   
   ---------------------------

.. image:: imgs/x64/odbcad32-64-add-psqlodbc-err.png

.. code-block:: text

   ---------------------------
   Driver's ConfigDSN, ConfigDriver, or ConfigTranslator failed
   ---------------------------
   Errors Found:



   The setup routines for the PostgreSQL Unicode(x64) ODBC driver could not be loaded due to system error code 193: .
   ---------------------------
   OK   
   ---------------------------


.. image:: imgs/x64/odbcad32-64-add-psqlodbc-err2.png

追加ができませんでしたので、検証はこれで終了です。

.. image:: imgs/x64/odbcad32-64-add-psqlodbc-end.png
