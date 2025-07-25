COM コンポーネントを配布したい
=================================================

DLL の構成
-------------------------------------------------

例えば Windows エクスプローラー 向けの サムネイル ハンドラー を配布する場合です:

- ``CmdThumbGen.dll`` (x86)
- ``CmdThumbGen.dll`` (x64)
- ``CmdThumbGen.dll`` (Arm64X)

備考:

- COM コンポーネントは 32 ビット版と 64 ビット版のバイナリーを好みの場所へ配置できます。
  ``レジストリ リダイレクター`` の働きによります。
- CmdThumbGen の開発レポジトリはこちら:
  `kenjiuno/ThumbGensPack: Thumbnail Generator pack for Windows 7 Explorer <https://github.com/kenjiuno/ThumbGensPack>`_
- Arm64 版よりも Arm64X 版での配布が好ましいです

セットアップの構成
-------------------------------------------------

単一の NSIS セットアップにまとめる案が考えられます:

- ``Setup_ThumbGensPack.exe`` (Windows 7, 8.1, 10, 11 向け)

NSIS セットアップでの判定方法の例
-------------------------------------------------

公式の NSIS で作成したセットアップは x86 アプリとして動作します。

NSIS スクリプトでは、プラットフォームを判別するための条件分岐を記述しつつ、プラットフォーム固有のアクションを追加していきます。

.. code-block:: nsis

   ; ...

   !define CmdThumbGen_X86 "CmdThumbGen\Release"
   !define CmdThumbGen_X64 "CmdThumbGen\x64\Release"
   !define CmdThumbGen_ARM64X "CmdThumbGen\ARM64EC\Release"

   ; ...
   
   !include "LogicLib.nsh"
   !include "x64.nsh"

   ; ...

   Section "CmdThumbGen 導入"
     ; Set output path to the installation directory.
     SetOutPath $INSTDIR
   
     File "${CmdThumbGen_X86}\CmdThumbGen.dll"
     File "${CmdThumbGen_X86}\CmdThumbGen.pdb"
   
     ExecWait 'REGSVR32 /s "$OUTDIR\CmdThumbGen.dll"' $0
     DetailPrint "結果: $0"
   SectionEnd

   Section /o "CmdThumbGen(x64) 導入" SEC_CMDTHUMBGEN_X64
     ; Set output path to the installation directory.
     SetOutPath $INSTDIR\x64
   
     File "${CmdThumbGen_X64}\CmdThumbGen.dll"
     File "${CmdThumbGen_X64}\CmdThumbGen.pdb"
   
     ExecWait 'REGSVR32 /s "$OUTDIR\CmdThumbGen.dll"' $0
     DetailPrint "結果: $0"
   SectionEnd
   
   Section /o "CmdThumbGen(Arm64X) 導入" SEC_CMDTHUMBGEN_ARM64X
     ; Set output path to the installation directory.
     SetOutPath $INSTDIR\x64
   
     File "${CmdThumbGen_ARM64X}\CmdThumbGen.dll"
     File "${CmdThumbGen_ARM64X}\CmdThumbGen.pdb"
   
     ExecWait 'REGSVR32 /s "$OUTDIR\CmdThumbGen.dll"' $0
     DetailPrint "結果: $0"
   SectionEnd

   Function .onInit
     ${If} ${IsNativeAMD64}
       SectionSetFlags ${SEC_CMDTHUMBGEN_X64} ${SF_SELECTED}
     ${EndIf}
   
     ${If} ${IsNativeARM64}
       SectionSetFlags ${SEC_CMDTHUMBGEN_ARM64X} ${SF_SELECTED}
     ${EndIf}
   FunctionEnd
