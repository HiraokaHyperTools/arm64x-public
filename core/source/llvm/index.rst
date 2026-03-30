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

Arm64X EXE の生成
------------------------------

main.c

.. code-block:: c

   #include <stdio.h>
   
   int main()
   {
   #if defined(_M_ARM64EC)
       printf("Hello, World! (Arm64EC)\n");
   #elif defined(_M_ARM64)
       printf("Hello, World! (Arm64)\n");
   #else
       printf("Hello, World!\n");
   #endif
       return 0;
   }

ビルド コマンド

.. code-block:: text

   clang-cl --target=arm64ec-pc-windows-msvc main.c -c -o main.arm64ec.o
   clang-cl --target=aarch64-pc-windows-msvc main.c -c -o main.arm64.o

   lld-link /machine:arm64   /subsystem:console main.arm64.o                /out:main.arm64.exe
   lld-link /machine:arm64ec /subsystem:console main.arm64ec.o              /out:main.arm64ec.exe
   lld-link /machine:arm64x  /subsystem:console main.arm64.o main.arm64ec.o /out:main.arm64x.exe

実行してみましょう。

``main.arm64.exe`` は Arm64 バイナリーです。 ``/machine arm64`` では実行できて、 ``/machine AMD64`` では実行できないはずです。

.. code-block:: text

   C:\Proj\arm64x-upon-llvm> start /wait /b /machine arm64 main.arm64.exe
   Hello, World! (Arm64)
   
   C:\Proj\arm64x-upon-llvm> start /wait /b /machine AMD64 main.arm64.exe
   このバージョンの C:\Proj\arm64x-upon-llvm\main.arm64.exe は、実行中の Windows のバージョンと互換性がありません。コンピューターのシステム情報を確認してから、ソフトウェアの発行元に問い合わせてください。

``main.arm64ec.exe`` は Arm64EC バイナリーです。 ``/machine AMD64`` では実行できて、 ``/machine arm64`` では実行できないはずです。

.. code-block:: text

   C:\Proj\arm64x-upon-llvm> start /wait /b /machine arm64 main.arm64ec.exe
   このバージョンの C:\Proj\arm64x-upon-llvm\main.arm64ec.exe は、実行中の Windows のバージョンと互換性がありません。コンピューターのシステム情報を確認してから、ソフトウェアの発行元に問い合わせてください。
   
   C:\Proj\arm64x-upon-llvm> start /wait /b /machine AMD64 main.arm64ec.exe
   Hello, World! (Arm64EC)

``main.arm64x.exe`` は Arm64X バイナリーです。 ``/machine arm64`` でも ``/machine AMD64`` でも、いずれでも実行できるはずです。

.. code-block:: text

   C:\Proj\arm64x-upon-llvm> start /wait /b /machine arm64 main.arm64x.exe
   Hello, World! (Arm64)
   
   C:\Proj\arm64x-upon-llvm> start /wait /b /machine AMD64 main.arm64x.exe
   Hello, World! (Arm64EC)

TLS callback を実装する Arm64X DLL の生成
--------------------------------------------------

tls_callback.c

.. code-block:: c

   #include <windows.h>
   
   BOOL APIENTRY DllMain(
       HMODULE hModule,
       DWORD ul_reason_for_call,
       LPVOID lpReserved)
   {
       switch (ul_reason_for_call)
       {
       case DLL_PROCESS_ATTACH:
       case DLL_THREAD_ATTACH:
       case DLL_THREAD_DETACH:
       case DLL_PROCESS_DETACH:
           break;
       }
       return TRUE;
   }
   
   // https://isc.sans.edu/diary/32580
   
   // Declare TLS callback section
   #pragma section(".CRT$XLB", read)
   
   void PrintSomewhere(LPCSTR msg)
   {
       OutputDebugStringA(msg);
   
       HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
       if (hStdOut != INVALID_HANDLE_VALUE)
       {
           WriteConsoleA(hStdOut, msg, lstrlenA(msg), NULL, NULL);
       }
   }
   
   // TLS callback function
   void WINAPI MyTlsCallback(PVOID hModule, DWORD dwReason, PVOID pReserved)
   {
       if (dwReason == DLL_PROCESS_ATTACH)
       {
   #if defined(_M_ARM64EC)
           PrintSomewhere("TLS Callback fired (ARM64EC)\n");
   #elif defined(_M_ARM64)
           PrintSomewhere("TLS Callback fired (ARM64)\n");
   #else
           PrintSomewhere("TLS Callback fired\n");
   #endif
       }
   }
   
   // https://github.com/ojdkbuild/tools_toolchain_vs2019bt_16113/blob/master/VC/Tools/MSVC/14.29.30133/crt/src/vcruntime/tlsdyn.cpp
   
   #ifdef _M_ARM64EC
   #pragma comment(linker, "-arm64xsameaddress:MyTlsCallback")
   #endif
   
   // Force linker to include TLS directory symbol
   #ifdef _WIN64
   #pragma comment(linker, "/INCLUDE:_tls_used")
   #pragma comment(linker, "/INCLUDE:tls_callback_func")
   #else
   #pragma comment(linker, "/INCLUDE:__tls_used")
   #pragma comment(linker, "/INCLUDE:_tls_callback_func")
   #endif
   
   // Place pointer in TLS callback section (extern "C" prevents mangling)
   __declspec(allocate(".CRT$XLB"))
   PIMAGE_TLS_CALLBACK tls_callback_func = MyTlsCallback;

ビルド コマンド

.. code-block:: text

   clang-cl --target=aarch64-pc-windows-msvc tls_callback.c -c -o tls_callback.arm64.o
   clang-cl --target=arm64ec-pc-windows-msvc tls_callback.c -c -o tls_callback.arm64ec.o
   
   lld-link /dll /machine:arm64   /subsystem:windows /out:tls_callback.arm64.dll   tls_callback.arm64.o
   lld-link /dll /machine:arm64ec /subsystem:windows /out:tls_callback.arm64ec.dll tls_callback.arm64ec.o
   lld-link /dll /machine:arm64x  /subsystem:windows /out:tls_callback.arm64x.dll  tls_callback.arm64.o tls_callback.arm64ec.o

loader.c

.. code-block:: c

   #include <windows.h>
   #include <stdio.h>
   
   int main(int argc, char *argv[])
   {
       if (argc < 2)
       {
           printf("Usage: %s <DLL path>\n", argv[0]);
           return 1;
       }
       else
       {
           printf("Attempting to load DLL: %s\n", argv[1]);
           HMODULE hDLL = LoadLibraryA(argv[1]);
           if (hDLL == NULL)
           {
               printf("Failed to load DLL: %s\n", argv[1]);
               return 1;
           }
           else
           {
               printf("DLL loaded successfully: %s\n", argv[1]);
               FreeLibrary(hDLL);
               return 0;
           }
       }
   }

ビルド コマンド

.. code-block:: text

   clang-cl --target=aarch64-pc-windows-msvc loader.c -o loader.arm64.exe
   clang-cl --target=arm64ec-pc-windows-msvc loader.c -o loader.arm64ec.exe

実行してみましょう。

.. code-block:: text

   C:\Proj\arm64x-upon-llvm> loader.arm64.exe
   Usage: loader.arm64.exe <DLL path>
   
   C:\Proj\arm64x-upon-llvm> loader.arm64.exe tls_callback.arm64.dll
   Attempting to load DLL: tls_callback.arm64.dll
   TLS Callback fired (ARM64)
   DLL loaded successfully: tls_callback.arm64.dll
   
   C:\Proj\arm64x-upon-llvm> loader.arm64ec.exe tls_callback.arm64ec.dll
   Attempting to load DLL: tls_callback.arm64ec.dll
   TLS Callback fired (ARM64EC)
   DLL loaded successfully: tls_callback.arm64ec.dll
   
   C:\Proj\arm64x-upon-llvm> loader.arm64.exe tls_callback.arm64x.dll
   Attempting to load DLL: tls_callback.arm64x.dll
   TLS Callback fired (ARM64)
   DLL loaded successfully: tls_callback.arm64x.dll
   
   C:\Proj\arm64x-upon-llvm> loader.arm64ec.exe tls_callback.arm64x.dll
   Attempting to load DLL: tls_callback.arm64x.dll
   TLS Callback fired (ARM64EC)
   DLL loaded successfully: tls_callback.arm64x.dll

参考までに Windows の DLL で TLS callback を利用するものに
``C:\Windows\System32\mshtml.dll``
があります。

Arm64X 純粋フォワーダー DLL の生成
-------------------------------------

空のファイル ``empty.c`` を用意します。

生成にあたっては、モジュールは実際に存在する必要はありません。
架空のモジュールと、
架空の関数名を指定して生成します。

redir.x64.def

.. code-block:: text

   NAME redir
   EXPORTS
    dummy=x64_redir.dummy

redir.arm64.def

.. code-block:: text

   NAME redir
   EXPORTS
    dummy=arm64_redir.dummy

ビルド コマンド

.. code-block:: text

   clang-cl --target=arm64ec-pc-windows-msvc empty.c -c -o empty.arm64ec.o
   clang-cl --target=aarch64-pc-windows-msvc empty.c -c -o empty.arm64.o
   
   lld-link /dll /machine:arm64x /subsystem:windows /def:redir.x64.def /defArm64Native:redir.arm64.def empty.arm64.o empty.arm64ec.o /out:redir.arm64x.dll

エクスポートを確認しましょう。

.. code-block:: text

   C:\Proj\arm64x-upon-llvm> ReadPEExportTable print-def redir.arm64x.dll
   LIBRARY redir.arm64x
   EXPORTS
    dummy=arm64_redir.dummy
   
   C:\Proj\arm64x-upon-llvm> ReadPEExportTable print-def redir.arm64x.dll --apply-dvrt
   LIBRARY redir.arm64x
   EXPORTS
    dummy=x64_redir.dummy

DVRT を適用することで、 Arm64EC 側のエクスポートテーブルを確認できます。

DVRT を適用しない場合は、 Arm64 側のエクスポートテーブルを確認できます。

ReadPEExportTable は、こちらです。

https://github.com/psqlodbc-for-win10-arm64/Toolings/tree/master/ReadPEExportTable

あるいは Web 版をご利用ください。

https://psqlodbc-for-win10-arm64.github.io/IsArm64XWeb/exportdef
