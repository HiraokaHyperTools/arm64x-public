EXE と DLL との関係 (プロセスの相互運用性)
=================================================

論
-------------------------------------------------

32 ビット / 64 ビット という用語が目立っています。
これはどういうことなのでしょうか。

`64 ビット バージョンの Windows での 32 ビット プログラムの互換性に関する考慮事項の概要 - Windows Server | Microsoft Learn <https://learn.microsoft.com/ja-jp/troubleshoot/windows-server/performance/compatibility-limitations-32-bit-programs-64-bit-system>`_

.. pull-quote::

   64 ビット バージョンの Windows では、Microsoft Windows-32-on-Windows-64 (WOW64) サブシステムを使用して、変更なしで 32 ビット プログラムを実行します。 64 ビット バージョンの Windows では、16 ビット バイナリまたは 32 ビット ドライバーはサポートされていません。 16 ビット バイナリまたは 32 ビット ドライバーに依存するプログラムは、プログラムの製造元がプログラムの更新プログラムを提供しない限り、64 ビット バージョンの Windows では実行できません。

`64 ビットの考慮事項 - Win32 apps | Microsoft Learn <https://learn.microsoft.com/ja-jp/windows/win32/tsf/64-bit-platform-considerations>`_

.. pull-quote::

   64 ビット Windows の可用性が高まる中、ユーザーは、さまざまな言語の国際キーボードや東アジア言語の入力メソッド エディター (IME) などの入力メソッドが、32 ビットと 64 ビットの両方のアプリケーションで適切に動作することを期待しています。 Microsoft Windows 用の入力メソッド コンポーネントまたはテキスト サービスを開発する場合は、製品のターゲット プラットフォームとして 64 ビット Windows を検討することが重要です。

   通常、IME とテキスト サービス (Text Services Framework に基づく) はダイナミック リンク ライブラリ (DLL) として実装されるため、DLL は 32 ビット環境または 64 ビット環境で使用するために特別に構築されていることに注意してください。32 ビット環境で使用するために構築された DLL は、64 ビット アプリケーションでは使用できません。その逆も同様です。

まとめ
-------------------------------------------------

ビット数や、プラットフォームが異なるものは混同できません

- 32 ビット (x86) の EXE / DLL は、これらの組み合わせでのみ動作します
- 64 ビット (x64) の EXE / DLL は、これらの組み合わせでのみ動作します
- 64 ビット (Arm64) の EXE / DLL は、これらの組み合わせでのみ動作します

.. image:: imgs/exe-dll1.png

Arm 版 Windows 11
-------------------------------------------------

Arm 版 Windows 11 では 3 種類 (x64, Arm64, Arm64EC) の 64 ビットアプリをサポートしています。この場合は、どのようになりますか。

- ``x64`` アプリを起動した場合は ``x64`` or ``Arm64EC`` バイナリー (EXE, DLL) のみロードできます
- ``Arm64EC`` アプリを起動した場合は ``x64`` or ``Arm64EC`` バイナリー (EXE, DLL) のみロードできます
- ``Arm64`` アプリを起動した場合は ``Arm64`` バイナリー (EXE, DLL) のみロードできます

.. image:: imgs/exe-dll2.png

Arm64EC は、 x64 のサブセット (一部分) であると考えることができます。

.. image:: imgs/exe-dll3.png

Arm64EC バイナリーは 2026-02-14 現在、 Windows では Windows 11 on Arm (あるいはその後継 OS) のみでしか動作しないバイナリーです。 それ以外の OS では動作しない点に注意が必要です。

`ARM 上の ARM64EC for Windows 11 アプリ | Microsoft Learn <https://learn.microsoft.com/ja-jp/windows/arm/arm64ec>`__

.. pull-quote::

   Arm64EC は、Windows 11 の Arm デバイスで実行されているアプリ用の新しいアプリケーション バイナリ インターフェイス (ABI) です。 Windows 11 SDK を使用する必要がある Windows 11 機能であり、Arm 上の Windows 10 では使用できません。

留意点として Arm64 & Arm64EC 両方の特徴を併せ持った ``Arm64X`` バイナリー (EXE, DLL) が存在します。

.. image:: imgs/exe-dll4.png
