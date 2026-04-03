Arm64X は fat binary か
===================================

fat binary の定義について
-----------------------------------

Wikipedia によると、次のように記述があります。

.. pull-quote::

   ファットバイナリ（fat binary）とは、
   コンピュータソフトウェアのバイナリ形式の一種で、
   一つのソフトを、
   互換性のない複数のCPUで実行できるように各CPU用のコードを同時に格納した形式をいう。

この記述ですと、該当するかどうかが「微妙」です。

Arm64X バイナリーは ``Qualcomm Snapdragon X`` シリーズなどの Arm CPU 上でしか動作しないコードです。

Arm64X バイナリーには、 つぎの 3 種類のコードが混在します:

* ``arm64`` は Arm64 のコードです。
* ``arm64ec`` も Arm64 のコードです。 但し、 コードの記述内容に制限が付いています。
* ``x64`` も一部存在します。 但し、これは ``.hexpthk`` Hybrid Export Patch Thunk (何の略称であるかは諸説あり) という、 Prism エミュレーター内部で実行することを想定した、 16 バイト程度の JMP 用のコードです。 ビジネスロジックを記述するような性質のものでありません。

Intel の CPU や、
AMD の CPU のような、
``x86_64`` のみの 64-bit コードを解釈するような CPU では、
実行ができません。

そのため
「複数 CPU で実行できる」
は成立しません。

よって ファットバイナリ では無いのかもしれません。

そう呼称したい気持ちは理解できますが…

vcruntime140.dll での割合
-----------------------------------

``vcruntime140.dll`` を例にして、 各アーキテクチャのコードが占める凡その容量を確認してみましょう。
確認には Hybrid Code Address Range Table を使用します。

.. code-block:: text

   dir C:\Windows\System32\vcruntime140.dll
    ドライブ C のボリューム ラベルは OS です
    ボリューム シリアル番号は 0E8D-48C6 です
   
    C:\Windows\System32 のディレクトリ
   
   2025/11/21  22:58           203,336 vcruntime140.dll
                  1 個のファイル             203,336 バイト
                  0 個のディレクトリ  261,685,112,832 バイトの空き領域

.. code-block:: text

   InspectTLSCallback.exe chpe C:\Windows\System32\vcruntime140.dll
                    2 CHPE Version
   
             00031000 Offset of Arm64X arm64x redirection metadata table
                   47  Count of Arm64X arm64x redirection metadata table entries
   
     000000018002AA10 Hybrid code address range table
                    4 Hybrid code address range count
   
     Hybrid Code Address Range Table
   
                 Address Range
           ----------------------
           arm64  0000000180001000 - 000000018001020F (00001000 - 0001020F)
         arm64ec  0000000180011000 - 0000000180021E73 (00011000 - 00021E73)
             x64  0000000180022000 - 000000018002347F (00022000 - 0002347F)
         arm64ec  0000000180024000 - 00000001800240BF (00024000 - 000240BF)
   
     Arm64X Redirection Metadata Table
   
           FFS Start           ARM64EC Address
           ------------------------------------
           0000000180022070 -> 0000000180024050
           0000000180022720 -> 0000000180024070
           0000000180022AC0 -> 0000000180024040

   ...

.. list-table::
    :header-rows: 1

    * - 項目
      - バイト数
      - 割合
    * - ファイルサイズ
      - 203,336
      - 100 %
    * - arm64
      - 61,968
      - 30 %
    * - arm64ec
      - 69,428
      - 34 %
    * - x64
      - 5,248
      - 3 %
    * - その他
      - 66,692
      - 33 %

実質的に、 ``arm64`` と ``arm64ec`` とでは、
両方とも同程度の容量を消費するようです。

バイナリーによってはデータの容量の方が大きいこともあり、
コードのサイズは目立たない場合もあります。
