20.1.0 での TLS callback 検証
======================================

.. code-block:: text

   C:\Proj\arm64x-upon-llvm>clang-cl --target=aarch64-pc-windows-msvc tls_callback.c -c -o tls_callback.arm64.o
   
   C:\Proj\arm64x-upon-llvm>clang-cl --target=arm64ec-pc-windows-msvc tls_callback.c -c -o tls_callback.arm64ec.o
   
   C:\Proj\arm64x-upon-llvm>
   C:\Proj\arm64x-upon-llvm>lld-link /machine:arm64   /subsystem:windows /dll tls_callback.arm64.o                        /out:tls_callback.arm64.dll
   
   C:\Proj\arm64x-upon-llvm>lld-link /machine:arm64ec /subsystem:windows /dll tls_callback.arm64ec.o                      /out:tls_callback.arm64ec.dll
   lld-link: warning: ignoring unknown argument: -arm64xsameaddress:MyTlsCallback
   lld-link: error: -arm64xsameaddress:MyTlsCallback is not allowed in .drectve (tls_callback.arm64ec.o)
   
   C:\Proj\arm64x-upon-llvm>lld-link /machine:arm64x  /subsystem:windows /dll tls_callback.arm64.o tls_callback.arm64ec.o /out:tls_callback.arm64x.dll
   lld-link: warning: ignoring unknown argument: -arm64xsameaddress:MyTlsCallback
   lld-link: error: -arm64xsameaddress:MyTlsCallback is not allowed in .drectve (tls_callback.arm64ec.o)
   
   C:\Proj\arm64x-upon-llvm>
   C:\Proj\arm64x-upon-llvm>loader.arm64.exe tls_callback.arm64.dll
   Attempting to load DLL: tls_callback.arm64.dll
   TLS Callback fired (ARM64)
   DLL loaded successfully: tls_callback.arm64.dll
   
   C:\Proj\arm64x-upon-llvm>loader.arm64ec.exe tls_callback.arm64ec.dll
   Attempting to load DLL: tls_callback.arm64ec.dll
   Failed to load DLL: tls_callback.arm64ec.dll
   
   C:\Proj\arm64x-upon-llvm>loader.arm64.exe tls_callback.arm64x.dll
   Attempting to load DLL: tls_callback.arm64x.dll
   Failed to load DLL: tls_callback.arm64x.dll
   
   C:\Proj\arm64x-upon-llvm>loader.arm64ec.exe tls_callback.arm64x.dll
   Attempting to load DLL: tls_callback.arm64x.dll
   Failed to load DLL: tls_callback.arm64x.dll

Arm64EC バイナリーのリンクでエラーが発生しました:

* ``lld-link: warning: ignoring unknown argument: -arm64xsameaddress:MyTlsCallback``
* ``lld-link: error: -arm64xsameaddress:MyTlsCallback is not allowed in .drectve (tls_callback.arm64ec.o)``
