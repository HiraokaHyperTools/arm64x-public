ActiveX コントロールを配布したい
=================================================

DLL の構成
-------------------------------------------------

例えば QR コード生成の ActiveX コントロール を配布する場合です (libqrencode を採用):

- ``QRCStamp.ocx`` (x86)
- ``QRCStamp.ocx`` (x64)
- ``QRCStamp.ocx`` (Arm64X)

備考:

- ActiveX コントロールは 32 ビット版と 64 ビット版のバイナリーを好みの場所へ配置できます。
  ``レジストリ リダイレクター`` の働きによります。
- ActiveX コントロール (x86, x64, ARM64) の試験に有用な ActiveXTestContainer の自作ビルドをこちらで配布しています:
  `Releases · HiraokaHyperTools/ActiveXTestContainer <https://github.com/HiraokaHyperTools/ActiveXTestContainer/releases>`_
- QRCodeActiveXControl の開発レポジトリはこちら:
  `HiraokaHyperTools/QRCodeActiveXControl: QRCode Generator Control for ActiveX <https://github.com/HiraokaHyperTools/QRCodeActiveXControl>`_
- Arm64 版よりも Arm64X 版での配布が好ましいです

セットアップの構成
-------------------------------------------------

単一の NSIS セットアップにまとめる案が考えられます:

- ``Setup_QRCodeActiveXControl_0_0_5.exe`` (Windows 7, 8.1, 10, 11 向け)

NSIS セットアップでの判定方法の例
-------------------------------------------------

公式の NSIS で作成したセットアップは x86 アプリとして動作します。

NSIS スクリプトでは、プラットフォームを判別するための条件分岐を記述しつつ、プラットフォーム固有のアクションを追加していきます。

.. code-block:: nsis

   ; ...

   !define BINDIR "RELEASE"
   !define BINDIR64 "x64\RELEASE"
   !define BINDIRA64X "ARM64EC\RELEASE"

   ; ...

   !include "LogicLib.nsh"
   !include "x64.nsh"

   ; ...

   Section ""
     ; ...

     ; Put file there
     SetOutPath $INSTDIR
     File "${BINDIR}\QRCStamp.ocx"
     ${If} ${IsNativeAMD64}
       SetOutPath $INSTDIR\x64
       File "${BINDIR64}\QRCStamp.ocx"
     ${ElseIf} ${IsNativeARM64}
       SetOutPath $INSTDIR\x64
       File "${BINDIRA64X}\QRCStamp.ocx"
     ${EndIf}

     ; ...
   SectionEnd

   Section "Register QRCStamp.ocx (32 bit)"
     ExecWait 'REGSVR32 /s "$INSTDIR\QRCStamp.ocx"' $0
     DetailPrint "Result: $0"
   SectionEnd
   
   Section "Register QRCStamp.ocx (64 bit)"
     ExecWait 'REGSVR32 /s "$INSTDIR\x64\QRCStamp.ocx"' $0
     DetailPrint "Result: $0"
   SectionEnd
