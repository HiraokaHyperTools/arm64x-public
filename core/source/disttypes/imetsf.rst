IME & TSF を配布したい
=================================================

DLL の構成
-------------------------------------------------

例えば ``Windows-classic-samples`` にある ``Text Services Framework Case Sample`` を配布する場合です:

- ``case.dll`` (x86)
- ``case.dll`` (x64)
- ``case.dll`` (Arm64X)

備考:

- ``tsfcase`` のオリジナルは、こちらにあります:

   - `Windows-classic-samples/Samples/Win7Samples/winui/tsf/tsfcase at main · microsoft/Windows-classic-samples <https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/Win7Samples/winui/tsf/tsfcase>`_

- 検証目的で試用したい方向けにバイナリーはこちらで配布しています:

   - `Releases · HiraokaHyperTools/tsfcase <https://github.com/HiraokaHyperTools/tsfcase/releases>`_

- ``tsfcase`` の使い方については、こちらを参照してください。言語バーの表示が必要です:

   - `TSF (Text Services Framework) サンプルを実行 #IME - Qiita <https://qiita.com/kenjiuno/items/0bf31538c02c8932f12f#tsfcase>`_

- Arm64 版よりも Arm64X 版での配布が好ましいです

セットアップの構成
-------------------------------------------------

単一の NSIS セットアップにまとめる案が考えられます:

- ``Setup_tsfcase.exe`` (Windows 7, 8.1, 10, 11 向け)

NSIS セットアップでの判定方法の例
-------------------------------------------------

公式の NSIS で作成したセットアップは x86 アプリとして動作します。

NSIS スクリプトでは、プラットフォームを判別するための条件分岐を記述しつつ、プラットフォーム固有のアクションを追加していきます。

.. code-block:: nsis

   ; ...

   !include 'LogicLib.nsh'
   !include 'x64.nsh'

   ; ...

   InstType "x86" IT_X86
   InstType "x64" IT_X64
   InstType "ARM64" IT_ARM64
   
   ; The stuff to install
   Section "32-bit (x86) 版をインストール" SEC_X86
     SectionInstType ${IT_X86} ${IT_X64} ${IT_ARM64}
     
     ; Set output path to the installation directory.
     SetOutPath $INSTDIR
     
     ; Put file there
     SetOutPath "$WINDIR\System32\IME\Case"
     File "Release\case.dll"
   
     ExecWait 'regsvr32.exe /s "$OUTDIR\case.dll"' $0
     DetailPrint "Result: $0"
   SectionEnd
   
   Section /o "64-bit (x64) 版をインストール" SEC_X64
     SectionInstType ${IT_X64}
     
     ; Set output path to the installation directory.
     SetOutPath $INSTDIR
     
     ; Put file there
     ${DisableX64FSRedirection}
     SetOutPath "$WINDIR\System32\IME\Case"
     File "x64\Release\case.dll"
   
     ExecWait 'regsvr32.exe /s "$OUTDIR\case.dll"' $0
     DetailPrint "Result: $0"
     ${EnableX64FSRedirection}
   
   SectionEnd
   
   Section /o "64-bit (ARM64X) 版をインストール" SEC_ARM64X
     SectionInstType ${IT_ARM64}
     
     ; Set output path to the installation directory.
     SetOutPath $INSTDIR
     
     ; Put file there
     ${DisableX64FSRedirection}
     SetOutPath "$WINDIR\System32\IME\Case"
     File "ARM64EC\Release\case.dll"
   
     ExecWait 'regsvr32.exe /s "$OUTDIR\case.dll"' $0
     DetailPrint "Result: $0"
     ${EnableX64FSRedirection}
   
   SectionEnd
   
   Function .onInit
     ${If} ${IsNativeAMD64}
       SectionSetFlags ${SEC_X64} ${SF_SELECTED}
     ${ElseIf} ${IsNativeARM64}
       SectionSetFlags ${SEC_ARM64X} ${SF_SELECTED}
     ${EndIf}
   FunctionEnd
   
   ; ...

IME テスト用アプリ
-------------------------------------------------

IME の機能性をテストするためのサンプルアプリを用意しました。

- `HiraokaHyperTools/MFCRichEditPad <https://github.com/HiraokaHyperTools/MFCRichEditPad>`__

リッチ エディット コントロール を使用しています。

- `リッチ エディット コントロールについて - Win32 apps | Microsoft Learn <https://learn.microsoft.com/ja-jp/windows/win32/controls/about-rich-edit-controls>`__

リッチ エディット バージョン 4.1 より Text Services Framework (TSF) のサポートが含まれます との記述があり、 TSF との相性確認ができそうです。

CRichEditView の派生クラスをビューとして利用していて、
使用しているウィンドウ クラスは RICHEDIT50W です。

- `CRichEditView クラス | Microsoft Learn <https://learn.microsoft.com/ja-jp/cpp/mfc/reference/cricheditview-class?view=msvc-170>`__

その昔、 ワードパッド という リッチ エディット コントロール の動作を確認できる便利なアプリがありましたが、もうありません。

- `Windows クライアントの非推奨の機能 | Microsoft Learn <https://learn.microsoft.com/ja-jp/windows/whats-new/deprecated-features>`__

.. pull-quote::

  ワードパッドは更新されなくなり、今後の Windows リリースで削除される予定です。 .doc や.rtfなどのリッチ テキスト ドキュメントには Microsoft Word、.txt などのプレーン テキスト ドキュメントには Windows メモ帳を使用することをお勧めします。

  [Update - March 2024]: ワードパッドは、Windows 11 バージョン 24H2 および Windows Server 2025 以降のすべてのエディションの Windows から削除されます。 開発者で、影響を受けるバイナリに関する情報が必要な場合は、「 非推奨の機能のリソース」を参照してください。

MFCRichEditPad は、ワードパッドの互換品ではないため RTF ファイルの読み書きはできません。

そのため、プラットフォームごとの リッチ エディット コントロール の動作確認の用途にのみ利用できます。

``Setup_MFCRichEditPad.exe`` に、各種バイナリーを同梱しています: ``x86``, ``x64``, ``Arm64``, ``Arm64EC``, ``Arm64X``

ワードパッドの互換品であれば WordPad2010 の方が適しているかもしれません。

- `HiraokaHyperTools/WordPad2010 <https://github.com/HiraokaHyperTools/WordPad2010>`__

但し WordPad2010 で使用しているウィンドウ クラスは RichEdit20A です。
