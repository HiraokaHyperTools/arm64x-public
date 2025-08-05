SoftEther VPN Client Ver 4.44, Build 9807, rtm
===========================================================

セットアップは問題なく完了しました。

しかし、仮想 VPN アダプターのインストールができず、接続ができませんでした。

`SoftEther ダウンロード センター <https://www.softether-download.com/ja.aspx?product=softether>`_ では CPU の選択で ``Intel (x86 and x64)`` しかないため、
Arm CPU は未対応の判断です。

.. code-block:: text

   SoftEther VPN Client

.. code-block:: text

   Intel (x86 and x64)

.. code-block:: text

   SoftEther VPN Client (Ver 4.44, Build 9807, rtm)
   softether-vpnclient-v4.44-9807-rtm-2025.04.16-windows-x86_x64-intel.exe (53.64 MB)
   [Non-SSL (HTTP) Download Link] Try this if the above link fails because your HTTP client doesn't support TLS 1.2.
   リリース日: 2025-04-16  <最新ビルド>
   バージョン更新履歴 (ChangeLog)
   言語: English, Japanese, Simplified Chinese
   OS: Windows, CPU: Intel (x86 and x64)
   (Windows 98 / 98 SE / ME / NT 4.0 SP6a / 2000 SP4 / XP SP2, SP3 / Vista SP1, SP2 / 7 SP1 / 8 / 8.1 / 10 / 11 / Server 2003 SP2 / Server 2008 SP1, SP2 / Hyper-V Server 2008 / Server 2008 R2 SP1 / Hyper-V Server 2008 R2 / Server 2012 / Hyper-V Server 2012 / Server 2012 R2 / Hyper-V Server 2012 R2 / Server 2016 / Server 2019 / Server 2022)

但し、SoftEther VPN Client 以外のプロトコルを利用することで SoftEther VPN Server との接続ができる方法もあります:

- L2TP/IPsec
- OpenVPN
- SSTP

※ 事前設定が必要です。

L2TP/IPsec 参考:

- `SoftEther VPN Server での L2TP/IPsec 設定ガイド - SoftEther VPN プロジェクト <https://ja.softether.org/4-docs/2-howto/L2TP_IPsec_Setup_Guide>`_

OpenVPN 参考:

- `1. 極めて強力な VPN 接続性 - SoftEther VPN プロジェクト <https://ja.softether.org/1-features/1._%E6%A5%B5%E3%82%81%E3%81%A6%E5%BC%B7%E5%8A%9B%E3%81%AA_VPN_%E6%8E%A5%E7%B6%9A%E6%80%A7#OpenVPN_.E3.83.97.E3.83.AD.E3.83.88.E3.82.B3.E3.83.AB.E3.81.AE.E3.82.B5.E3.83.9D.E3.83.BC.E3.83.88:~:text=%E8%A8%AD%E5%AE%9A%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82-,OpenVPN%20%E3%83%97%E3%83%AD%E3%83%88%E3%82%B3%E3%83%AB%E3%81%AE%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88,-SoftEther%20VPN%20Server>`_
- ``OpenVPN プロトコルのサポート`` セクションを確認してください

SSTP 参考:

- `1. 極めて強力な VPN 接続性 - SoftEther VPN プロジェクト <https://ja.softether.org/1-features/1._%E6%A5%B5%E3%82%81%E3%81%A6%E5%BC%B7%E5%8A%9B%E3%81%AA_VPN_%E6%8E%A5%E7%B6%9A%E6%80%A7#:~:text=%E5%88%A9%E7%94%A8%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82-,Microsoft%20SSTP%20VPN%20%E3%83%97%E3%83%AD%E3%83%88%E3%82%B3%E3%83%AB%E3%81%AE%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88,-SoftEther%20VPN%20Server>`_
- ``Microsoft SSTP VPN プロトコルのサポート`` セクションを確認してください

これらの場合でも SoftEther VPN Client は使用しませんので、セットアップは不要です。
