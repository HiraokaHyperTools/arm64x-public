Rust Arm64X 対応状況
================================

生成について
--------------------------------

(2026-04-02 現在)

``rustc 1.94.1 (e408947bf 2026-03-25)`` では、 既知の問題があります。 そのため、 未対応と判断します。

* `ARM64EC static libraries fail when linked into ARM64X DLLs · Issue #145154 · rust-lang/rust <https://github.com/rust-lang/rust/issues/145154>`__

一方で、 こちらのプルリクエスト 148799 を適用した Rust であれば、 正常なバイナリーが生成できることを確認しました。

* `Switch the destructors implementation for thread locals on Windows to use FLS by ohadravid · Pull Request #148799 · rust-lang/rust <https://github.com/rust-lang/rust/pull/148799>`__
