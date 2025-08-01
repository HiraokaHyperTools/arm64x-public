過去に体験した互換性の問題
=================================================

「互換性」を犠牲にしてきた歴史は、今回に始まったことではありません。
今までにも何度か技術的なパラダイムシフトがありました。その度に、古いものはソフト・ハードを問わず、商業的な理由 (主に採算が取れないなど) で切り捨てられてきました。

例:

- MS-DOS から Windows への移行
- Windows 9x から Windows NT への移行
- 32 ビットから 64 ビットへの移行 (Windows Vista, 7, 8, 10, 11)

これはプロダクトデザインの問題でありますので、
別にこの方針に異を唱える気はありません。

但し、その方向性が消費者の求める方向性と異にするのであれば、
話は違って参ります。

例えば、そのプラットフォームに持続可能性はあるのか、です。

MS-DOS から Windows への移行 について
---------------------------------------------------------------------

よくなった点

- RAM 容量 (640 KB) の壁がなくなりました

   - アプリが画像などの大きなデータを容易に扱えるようになりました。
     MS-DOS までは、文字情報の入出力や印刷が主体でした

- Windows がハードウェアを一元管理するようになりました

   - MS-DOS アプリの時代は、アプリごと、ゲームごとに、ハードウェアとドライバーとの対応有無がありました
   - Windows では、ディスプレイ・プリンター・サウンドカードなど周辺機器については OS が一元管理します

- 共通基盤 (Windows API) と SDK が提供されるようになりました

   - MS-DOS アプリでは MS-DOS コール、 BIOS コール、 低レベル I/O コールなど様々な手段を利用して、 直接ハードウェアとの対話をする必要性がありました
   - Windows アプリは Windows API を通して、間接的にハードウェアと対話します。 これにより、 Windows アプリが直接ハードウェアとの対話をする事は許可されなくなりました

- 国産機 (NEC PC-98 シリーズ) と海外機 (IBM PC-AT 互換機) の壁がなくなりました

   - 言語は違えど、海外版のアプリも日本語版 Windows で動作しました

よくなかった点

- MS-DOS アプリからの移行について、暗中模索していく必要がありました

   - 移行のスピード感について
   
      - 移行はかなりゆるやかに進んでいきましたので、 大きな問題にはなりませんでした
      - この頃はネットがありません。 一方で、 Nitfy Serve や PC-VAN など、電話回線を経由して文字情報をやり取りするパソコン通信がありました
      - 主な情報源は、月単位で発行される、パソコン系の技術雑誌 (物理) でした
      - CD-ROM が 1 枚以上、添付される雑誌も結構あり、 メーカーからの更新プログラムが配布されることもありました

   - 日本語入力について
   
      - (記憶にはありませんが) Windows 3.1 には MS-IME が搭載されていたようです
      - のちに ATOK など様々な日本語入力システムが Windows 向けにリリースされています

Windows 9x から Windows NT への移行 について
---------------------------------------------------------------------

よくなった点

- Windows NT は堅牢であり拡張性もあり、様々な消費者ニーズに応えられるようになりました

   - アプリが不具合により強制終了しても OS は安定動作を続けることができました
   - Unicode に標準対応しました。 これにより多言語対応が促進されました
   - ファイルシステムがモジュール式になりました (Windows IFS): FAT, HPFS, NTFS, CDFS (ISO 9660), UDFS (UDF), Dokan, exFAT, ReFS など Microsoft 内外で多数のモジュールが開発されました
   - サブシステムが導入されました。 1 つの OS で複数のプラットフォームに対応できるようになりました。例: WOW, WoW64, WOW64, WSL
   - Windows サービスが導入されました
   - 近代的な 32 ビット OS の仲間入りをしたことで Linux など他の OS 向けに開発された多数のアプリが Windows へ移植されました

- NTFS の利用により 4GB を超えるファイルの取り扱いができるようになりました。

- 業務利用するうえで信頼性の高い先進機能を多数搭載していました

   - NTFS ファイルシステム
   - ネットワーク機能
   - マルチユーザー環境

よくなかった点

- メモリ管理に欠陥のあるアプリ・ゲームが起動できませんでした (当時の PaintShop Pro など)
- Windows 9x のプリンタードライバーが全く使用できませんでした
- ジョイパッドなど一部のコントローラーのドライバーが提供されておらず使用できませんでした
- 一部の SCSI デバイスのドライバーが提供されておらず使用できませんでした (例: 画像スキャナー)
- ウィルス対策ソフトなど、Windows カーネルに干渉するタイプのソフトが未対応であり使用できませんでした

32 ビットから 64 ビット (AMD64, not IA64) への移行について
---------------------------------------------------------------------

よくなった点

- 4GB の壁、の突破

   - メモリーが安価になり 4GB 以上のメモリーを搭載するパソコンも珍しくなくなりました
   - しかし 32 ビットアプリのメモリ空間は 4GB のままでした
   - Windows OS も同様の制約を受けます。 4GB 以上のメモリーを搭載しても認識されないという問題がありました (PAE による緩和策あり)
   - これを解決するべく 64 ビット Windows が登場しました
   - Windows をコア業務として利用しているユーザー層 (CAD での作図、動画編集など) にとっては歓迎されました

- 既存のハードウェアの流用ができました

   - 32 ビット OS と 64 ビット OS との別に関わらず、
     CPU が 64 ビット環境に対応していれば、インストールができました

よくなかった点

- 一部のアプリで一部の機能が正常に動作しませんでした
- プリンタードライバーがメーカーの対応待ちで使用できませんでした
- 同様に、一部の周辺機器のドライバー (USB ドングル等) が 64 ビット OS に対応しておらず使用できませんでした
- ウィルス対策ソフトなど、Windows カーネルに干渉するタイプのソフトが未対応であり使用できませんでした
