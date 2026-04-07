21.1.0 での TLS callback 検証
======================================

.. code-block:: text

   C:\Proj\arm64x-upon-llvm>clang-cl --target=aarch64-pc-windows-msvc tls_callback.c -c -o tls_callback.arm64.o
   
   C:\Proj\arm64x-upon-llvm>clang-cl --target=arm64ec-pc-windows-msvc tls_callback.c -c -o tls_callback.arm64ec.o
   
   C:\Proj\arm64x-upon-llvm>
   C:\Proj\arm64x-upon-llvm>lld-link /machine:arm64   /subsystem:windows /dll tls_callback.arm64.o                        /out:tls_callback.arm64.dll
   
   C:\Proj\arm64x-upon-llvm>lld-link /machine:arm64ec /subsystem:windows /dll tls_callback.arm64ec.o                      /out:tls_callback.arm64ec.dll
   
   C:\Proj\arm64x-upon-llvm>lld-link /machine:arm64x  /subsystem:windows /dll tls_callback.arm64.o tls_callback.arm64ec.o /out:tls_callback.arm64x.dll
   
   C:\Proj\arm64x-upon-llvm>
   C:\Proj\arm64x-upon-llvm>loader.arm64.exe tls_callback.arm64.dll
   Attempting to load DLL: tls_callback.arm64.dll
   TLS Callback fired (ARM64)
   DLL loaded successfully: tls_callback.arm64.dll
   
   C:\Proj\arm64x-upon-llvm>loader.arm64ec.exe tls_callback.arm64ec.dll
   Attempting to load DLL: tls_callback.arm64ec.dll
   TLS Callback fired (ARM64EC)
   DLL loaded successfully: tls_callback.arm64ec.dll
   
   C:\Proj\arm64x-upon-llvm>loader.arm64.exe tls_callback.arm64x.dll
   Attempting to load DLL: tls_callback.arm64x.dll
   TLS Callback fired (ARM64)
   DLL loaded successfully: tls_callback.arm64x.dll
   
   C:\Proj\arm64x-upon-llvm>loader.arm64ec.exe tls_callback.arm64x.dll
   Attempting to load DLL: tls_callback.arm64x.dll
   DLL loaded successfully: tls_callback.arm64x.dll

Arm64X DLL の Arm64EC 側が、 正常にロードできないようです。

観察の結果、 複数の課題が見られました:

* TLS callback のアドレスが、 Hybrid Code Address Range Table の arm64ec の範囲内をポイントしていません。 そのため Arm64EC 側では、 TLS callback が x64 コードの扱いになっています。
* Arm64 と Arm64EC とで、 TLS callback の分岐手段が存在していません。

.. code-block:: text

   C:\Proj\arm64x-upon-llvm> C:\Proj\psqlodbc-for-win10-arm64\Toolings\InspectTLSCallback\bin\Debug\net8.0\InspectTLSCallback.exe inspect tls_callback.arm64x.dll
   # Before apply Dvrt
   
                 AA64 machine
                    2 CHPE Version
   
     0000000180039001 Start of raw data
     0000000180039003 End of raw data
     0000000180033524 Address of index
     000000018002DF28 Address of callbacks
                    0 Size of zero fill
             00000000 Characteristics
   
       TLS Callbacks
   
       Address
       ----------------
       00000001800010B4      ARM64
       0000000000000000
   
       VirtualAddress   | 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
       -----------------|------------------------------------------------
       00000001800010B4 | FF C3 00 D1 FE 13 00 F9 E2 0F 00 F9 E1 17 00 B9
       00000001800010C4 | E0 07 00 F9 E8 17 40 B9 08 05 00 71 C1 00 00 54
       00000001800010D4 | 01 00 00 14 40 01 00 F0 00 00 03 91 D5 FF FF 97
       00000001800010E4 | 01 00 00 14 FE 13 40 F9 FF C3 00 91 C0 03 5F D6
   
       AArch64 disassembly by AsmArm64
       ---
       00000001800010B4: D100C3FF  sub sp, sp, #48
       00000001800010B8: F90013FE  str x30, [sp, #32]
       00000001800010BC: F9000FE2  str x2, [sp, #24]
       00000001800010C0: B90017E1  str w1, [sp, #20]
       00000001800010C4: F90007E0  str x0, [sp, #8]
       00000001800010C8: B94017E8  ldr w8, [sp, #20]
       00000001800010CC: 71000508  subs w8, w8, #1
       00000001800010D0: 540000C1  b.ne #24
       00000001800010D4: 14000001  #0:
       00000001800010D8: F0000140  adrp x0, #176128
       00000001800010DC: 91030000  add x0, x0, #192
       00000001800010E0: 97FFFFD5  bl #-172
       00000001800010E4: 14000001  #0:
       00000001800010E8: F94013FE  ldr x30, [sp, #32]
       00000001800010EC: 9100C3FF  add sp, sp, #48
       00000001800010F0: D65F03C0  ret
   
   # After apply Dvrt
   
                 8664 machine
                    2 CHPE Version
                      This is an Arm64EC! (chpeVersion == 2 && header.Machine == 0x8664)
   
     0000000180039001 Start of raw data
     0000000180039003 End of raw data
     0000000180033524 Address of index
     000000018002DF28 Address of callbacks
                    0 Size of zero fill
             00000000 Characteristics
   
       TLS Callbacks
   
       Address
       ----------------
       00000001800010B4      RtlIsEcCode = false (x64)
       0000000000000000
   
       VirtualAddress   | 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
       -----------------|------------------------------------------------
       00000001800010B4 | FF C3 00 D1 FE 13 00 F9 E2 0F 00 F9 E1 17 00 B9
       00000001800010C4 | E0 07 00 F9 E8 17 40 B9 08 05 00 71 C1 00 00 54
       00000001800010D4 | 01 00 00 14 40 01 00 F0 00 00 03 91 D5 FF FF 97
       00000001800010E4 | 01 00 00 14 FE 13 40 F9 FF C3 00 91 C0 03 5F D6
   
       x64 disassembly by Iced
       ---
       00000001800010B4: FF C3              inc ebx
       00000001800010B6: 00 D1              add cl,dl
       00000001800010B8: FE 13              (bad)
       00000001800010BA: 00 F9              add cl,bh
       00000001800010BC: E2 0F              loop 00000001800010CDh
       00000001800010BE: 00 F9              add cl,bh
       00000001800010C0: E1 17              loope 00000001800010D9h
       00000001800010C2: 00 B9 E0 07 00 F9  add [rcx-6FFF820h],bh
       00000001800010C8: E8 17 40 B9 08     call 0000000188B950E4h
       00000001800010CD: 05 00 71 C1 00     add eax,0C17100h
       00000001800010D2: 00 54 01 00        add [rcx+rax],dl
       00000001800010D6: 00 14 40           add [rax+rax*2],dl
       00000001800010D9: 01 00              add [rax],eax
       00000001800010DB: F0 00 00           lock add [rax],al
       00000001800010DE: 03 91 D5 FF FF 97  add edx,[rcx-6800002Bh]
       00000001800010E4: 01 00              add [rax],eax
       00000001800010E6: 00 14 FE           add [rsi+rdi*8],dl
       00000001800010E9: 13 40 F9           adc eax,[rax-7]
       00000001800010EC: FF C3              inc ebx
       00000001800010EE: 00 91 C0 03 5F D6  add [rcx-29A0FC40h],dl
   
.. code-block:: text

   C:\Proj\arm64x-upon-llvm> C:\Proj\psqlodbc-for-win10-arm64\Toolings\InspectTLSCallback\bin\Debug\net8.0\InspectTLSCallback.exe chpe tls_callback.arm64x.dll
                    2 CHPE Version
   
             00037000 Offset of Arm64X arm64x redirection metadata table
                    1  Count of Arm64X arm64x redirection metadata table entries
   
     000000018002DDFE Hybrid code address range table
                    3 Hybrid code address range count
   
     Hybrid Code Address Range Table
   
                 Address Range
           ----------------------
           arm64  0000000180001000 - 00000001800103B3 (00001000 - 000103B3)
         arm64ec  0000000180011004 - 0000000180021893 (00011004 - 00021893)
             x64  0000000180022000 - 000000018002300F (00022000 - 0002300F)
   
     Arm64X Redirection Metadata Table
   
           FFS Start           ARM64EC Address
           ------------------------------------
           0000000180023000 -> 0000000180011F68
