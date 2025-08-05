Deprecated features への危機感
=================================================

`Windows クライアントの非推奨の機能 | Microsoft Learn <https://learn.microsoft.com/ja-jp/windows/whats-new/deprecated-features>`_ というページがあります。

ここには、恐らく、商業的な理由で継続が困難となった機能・技術が墓石のように列挙される、そういった場所であると考えています。

Microsoft の Mixed Reality
-------------------------------------------------

このリストに ``Windows Mixed Reality`` が墓標入りした時には驚いたものです。

.. pull-quote::

   Windows Mixed Reality

   Windows Mixed Realityは非推奨となり、バージョン 24H2 Windows 11で削除されます。 この非推奨には、Mixed Reality ポータル アプリ、SteamVR 用のWindows Mixed Reality、および Steam VR Beta が含まれます。 既存のWindows Mixed Realityデバイスは、ユーザーが現在リリースされているバージョンのWindows 11バージョン 23H2 のままである場合、2026 年 11 月まで Steam と連携し続けます。 2026 年 11 月以降、Windows Mixed Realityはセキュリティ更新プログラム、セキュリティ以外の更新プログラム、バグ修正プログラム、テクニカル サポート、またはオンライン技術コンテンツの更新プログラムを受け取らなくなります。	

   2023 年 12 月

私は ``Acer AH101`` という Windows Mixed Reality ヘッドセットを購入して、実際に使用していた事があります。
そのため、多少の感情移入はあります。
しかし、購入したはいいものの、ほとんど活用はしていませんでした。

Microsoft HoloLens
-------------------------------------------------

実は Microsoft HoloLens も EOL (End of life) で終了する雰囲気です。

`マイクロソフト、「HoloLens 2」の生産を終了へ--後継機の予定は不明 - ZDNET Japan <https://japan.zdnet.com/article/35224470/>`_

.. pull-quote::

   HoloLens 2は、2027年12月31日まで機能維持のためにセキュリティ更新などのサポートを受け続けることができる。

先達てアレックス・キップマンが Microsoft を退職していますし (実はクビらしい)

そのため、主だった Mixed Reality 事業はこれで幕引きになるのではないでしょうか。

EOL (End of life) の理屈
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

この EOL はどういう理屈かといいますと:

- 製品には予め 5 年間などの EOL (寿命) が設定された上で販売される
- EOL までの期間は、セキュリティ更新やバグ修正が提供される
- EOL 以降はサポートが提供されなくなる
- そのため EOL が到達するまでに、次世代製品の投入をするなどしている

Microsoft HoloLens ファミリーについては ``次世代製品の投入`` がなかったために EOL を待つのみになりました。

理由はいくつか考えられます:

- 商業的な理由: 事業としての採算が取れないため、会社が EOL の判断をした場合
- 優秀なリーダーがいなくなった
- 全体のパイ (消費者ニーズ) が縮小した

Windows RT
-------------------------------------------------

初代 Surface は Windows RT という Windows 8 の Arm 版を搭載していました。

- `「Windows RT」の行方--「Windows 10」との関係は？ - ZDNET Japan <https://japan.zdnet.com/article/35059344/>`_

.. pull-quote::

   「Windows RT」は、携帯電話で多く用いられているARMチップを搭載したデバイス上で稼働するMicrosoftのOSであり、大きくデザインが変わった「Windows 8」とともに2012年後半に市場に投入された。Windows RTは登場後、苦戦を強いられ、ユーザーを引きつけることができなかった。その理由には、「Outlook」のような従来のWindowsプログラムが同OS上で動作しなかったせいもある。またMicrosoftは、より優れた製品を作り上げるためにWindows RTデバイスの開発プロセスを厳しく統制し、協業するチップメーカーの数を絞り込んだ。しかしそれによって、Windows RTを搭載した製品は同社の「Surface」以外にほとんど登場しないという結果になった。

私は手を出しませんでしたが、この頃は Windows XP / Windows 7 が全盛の時期でした。

次世代 OS である Windows 8 への移行については色々な懸念が噴出していた時期でもあります。

Windows 95 から続いてきた伝統的な「スタートメニューが消滅する」というビッグニュースがあり、この 1 件だけでも様々なユーザー層が大混乱を引き起こしたものです。

そんな懸念の嵐の中でひっそりと流されるように消滅していったのが Windows RT でした。

こちらは 2023/01/10 に EOL を迎えました。

- `Windows RT - Microsoft Lifecycle | Microsoft Learn <https://learn.microsoft.com/ja-jp/lifecycle/products/windows-rt>`_


.. list-table::

   * - リスト
     - 開始日
     - メインストリームの終了日
     - 延長された終了日
   * - Windows RT
     - 2012年10月30日
     - 2018年1月9日
     - 2023年1月10日

Microsoft Windows 10 Mobile
-------------------------------------------------

Microsoft のモバイル機器の事業については、
iPhone の登場までに限りますが、
色々なタイプのデバイスやソフトウェアが近未来を描きたいかの如く大量に発表され、
また一定の評価を得ていたように思います。 

ご存知のように iPhone / iPad の登場により、近未来感の模索という長い旅路はここで終結してしまいました。

そう、モバイルデバイスはそのビジネスモデルとともに商業化に成功し、生活必需品 (贅沢品) としての地位を確立したからです。

この分野では首位を維持し続けるために、
強力なリーダーシップと、業界を牽引するための実力や実績が必要になります。
Microsoft はそういったビジョンを実現できるような人材を欠いていたのかもしれません。

- `Windows 10 Mobile のサポート終了 - Microsoft Lifecycle | Microsoft Learn <https://learn.microsoft.com/ja-jp/lifecycle/announcements/windows-10-mobile-end-of-support>`_

.. pull-quote::

   Windows 10 Mobile Version 1709 (2017 年 10 月リリース) は Windows 10 Mobile の最終リリースであり、Microsoft によるサポートは 2019 年 12 月 10 日で終了します。 このサポート終了日は、Windows 10 Mobile および Windows 10 Mobile Enterprise を含む、すべての Windows 10 Mobile 製品に適用されます。


Deprecated features 入りする傾向
-------------------------------------------------

Deprecated features 入りする傾向の 1 つに「利用者数が少ないもの」があると思います。

そして、一度でもここに名前が刻まれてしまうと、もう手のつけようがなくなります。

Arm...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ここに Arm 版 Windows が入ることのないように願うばかりです。

それを防ぐための方法はあるのでしょうか…

関与
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

私は Arm 版 Windows を延命したいと考えているので、多少なりとも貢献をしたいのです。

Arm 版 Windows の普及にあたっては、技術的に解決が可能な障壁も多くあります。

それらを個別具体的に 1 つずつ丁寧に問題の解析をして、解決に結びつけていく事に意味があると考えます。
「問題解決」を続けていく限り、逆に助けてくれる人も増えていくに違いありません。

その延命策の一環として、こういった情報発信をしている側面があります。
