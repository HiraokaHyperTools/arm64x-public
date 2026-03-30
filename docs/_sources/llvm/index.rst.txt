LLVM Arm64X 対応状況
==================================

生成について
----------------------------------

(2026-03-31 現在)

``24 March 2026: LLVM 22.1.2`` にて、
Arm64X バイナリーの生成に対応している事を確認しました。

確認できたバリエーション:

* 通常の Arm64X EXE ならびに Arm64X DLL の生成
* ``.CRT$XLB`` セクションおよび ``#pragma comment (linker, "-arm64xsameaddress:__dyn_tls_init")`` の指定により TLS callback を実装する Arm64X DLL の生成
* Arm64X 純粋フォワーダー DLL の生成
