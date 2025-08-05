スターテック USB-RS232C シリアル変換ケーブル
========================================================

未対応です。

.. pull-quote::

    スターテック StarTech.com USB - RS232Cシリアル変換ケーブル/USB 2.0/91cm/USB Type-Aオス・DB9オス/Windows & macOS/USB - D-Sub 9ピン変換アダプター 1P3FP-USB-SERIAL ブラック

- `Amazon.co.jp: スターテック StarTech.com USB - RS232Cシリアル変換ケーブル/USB 2.0/91cm/USB Type-Aオス・DB9オス/Windows & macOS/USB - D-Sub 9ピン変換アダプター 1P3FP-USB-SERIAL ブラック : パソコン・周辺機器 <https://www.amazon.co.jp/dp/B09WPXRGNP?th=1>`_

つぎのドライバーのダウンロードサイトより ``[prolific_pl2303] windows usb serial adapter.zip`` (Version: 4.3.0.0) を試しました:

- `USB - RS232C シリアル変換ケーブル／USB 2.0接続／91cm／1ポート D-Sub 9 ピン／Type-A オス - DB9 オス／各種OS対応／シリアルコンバーター アダプター／バー <https://www.startech.com/ja-jp/cards-adapters/1p3fp-usb-serial?srsltid=AfmBOoqhe_9Wib0mPTQNUj9dYFcYCMsGrZ-DMRtwMc_-he84NsjkmD-e>`_

``[prolific_pl2303] windows usb serial adapter\[prolific_pl2303] windows usb serial adapter\Win 11\PL23XX-M_LogoDriver_Setup_4300_20240704.exe`` のセットアップは完了しましたが、
デバイスは ``USB-Serial Controller D`` (``USB\VID_067B&PID_2303``) のままでした。
つまり、ドライバーは ARM64 に対応していない模様です。
