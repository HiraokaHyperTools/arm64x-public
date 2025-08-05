.. _dsd-tech-sh-u09c:

DSD TECH SH-U09C USB
========================================================

Windows 標準では未対応、
ドライバーの追加インストールにより動作します。

.. pull-quote::

    DSD TECH SH-U09C USB - TTLシリアルアダプター + FTDI FT232RLチップ Windows 10 8 7 Mac OS X対応

- `Amazon.co.jp: DSD TECH SH-U09C USB - TTLシリアルアダプター + FTDI FT232RLチップ Windows 10 8 7 Mac OS X対応 : パソコン・周辺機器 <https://www.amazon.co.jp/dp/B07BBPX8B8>`_

FTDI のサイトよりドライバーを入手し、手動でのインストール作業が必要です:

- `VCP Drivers - FTDI <https://ftdichip.com/drivers/vcp-drivers/>`_

``Windows (Desktop)*`` の ``2.12.36.20A***`` をクリックして ``CDM-v2.12.36.20-for-ARM64-WHQL-Certified.zip`` をダウンロードします。

zip を展開した後、デバイスマネージャーを開き、解決されていないデバイスについて、ドライバーの手動インストールを実行します。

``USB Serial Converter`` と ``USB Serial Port (COMx)`` のそれぞれについて、ドライバーの手動インストールによる解決が必要でした。
