22.1.0 での TLS callback 検証
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
   TLS Callback fired (ARM64EC)
   DLL loaded successfully: tls_callback.arm64x.dll

検証結果は良好です。 確認の結果、問題は見つかりませんでした。

Arm64X での TLS callback 実装については MSFT link.exe と同様の実装方針を選択したようです。

TLS callback のポイント先にトランポリンを設置しています。
Arm64EC 利用時には (DVRT の適用によって) トランポリンのジャンプ先が変更されています。

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
       00000001800211B8      ARM64
       0000000000000000
   
       VirtualAddress   | 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
       -----------------|------------------------------------------------
       00000001800211B8 | 10 FF FF 90 10 D2 02 91 00 02 1F D6 E6 9F BA AD
       00000001800211C8 | E8 27 01 AD EA 2F 02 AD EC 37 03 AD EE 3F 04 AD
       00000001800211D8 | FD 7B 0A A9 FD 83 02 91 20 01 3F D6 E8 03 00 AA
       00000001800211E8 | 69 00 00 90 20 19 47 F9 FD 7B 4A A9 EE 3F 44 AD
   
       AArch64 disassembly by AsmArm64
       ---
       00000001800211B8: 90FFFF10  adrp x16, #-131072
       00000001800211BC: 9102D210  add x16, x16, #180
       00000001800211C0: D61F0200  br x16
       00000001800211C4: ADBA9FE6  stp q6, q7, [sp, #-176]!
       00000001800211C8: AD0127E8  stp q8, q9, [sp, #32]
       00000001800211CC: AD022FEA  stp q10, q11, [sp, #64]
       00000001800211D0: AD0337EC  stp q12, q13, [sp, #96]
       00000001800211D4: AD043FEE  stp q14, q15, [sp, #128]
       00000001800211D8: A90A7BFD  stp x29, x30, [sp, #160]
       00000001800211DC: 910283FD  add x29, sp, #160
       00000001800211E0: D63F0120  blr x9
       00000001800211E4: AA0003E8  mov x8, x0
       00000001800211E8: 90000069  adrp x9, #49152
       00000001800211EC: F9471920  ldr x0, [x9, #3632]
       00000001800211F0: A94A7BFD  ldp x29, x30, [sp, #160]
       00000001800211F4: AD443FEE  ldp q14, q15, [sp, #128]
   
       Navigate to the destination at 00000001800010B4
   
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
       00000001800211B8      RtlIsEcCode = true (ARM64EC)
       0000000000000000
   
       VirtualAddress   | 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
       -----------------|------------------------------------------------
       00000001800211B8 | 90 FF FF 90 10 02 03 91 00 02 1F D6 E6 9F BA AD
       00000001800211C8 | E8 27 01 AD EA 2F 02 AD EC 37 03 AD EE 3F 04 AD
       00000001800211D8 | FD 7B 0A A9 FD 83 02 91 20 01 3F D6 E8 03 00 AA
       00000001800211E8 | 69 00 00 90 20 19 47 F9 FD 7B 4A A9 EE 3F 44 AD
   
       AArch64 disassembly by AsmArm64
       ---
       00000001800211B8: 90FFFF90  adrp x16, #-65536
       00000001800211BC: 91030210  add x16, x16, #192
       00000001800211C0: D61F0200  br x16
       00000001800211C4: ADBA9FE6  stp q6, q7, [sp, #-176]!
       00000001800211C8: AD0127E8  stp q8, q9, [sp, #32]
       00000001800211CC: AD022FEA  stp q10, q11, [sp, #64]
       00000001800211D0: AD0337EC  stp q12, q13, [sp, #96]
       00000001800211D4: AD043FEE  stp q14, q15, [sp, #128]
       00000001800211D8: A90A7BFD  stp x29, x30, [sp, #160]
       00000001800211DC: 910283FD  add x29, sp, #160
       00000001800211E0: D63F0120  blr x9
       00000001800211E4: AA0003E8  mov x8, x0
       00000001800211E8: 90000069  adrp x9, #49152
       00000001800211EC: F9471920  ldr x0, [x9, #3632]
       00000001800211F0: A94A7BFD  ldp x29, x30, [sp, #160]
       00000001800211F4: AD443FEE  ldp q14, q15, [sp, #128]
   
       Navigate to the destination at 00000001800110C0
   
         VirtualAddress   | 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
         -----------------|------------------------------------------------
         00000001800110C0 | FF C3 00 D1 FE 13 00 F9 E2 0F 00 F9 E1 17 00 B9
         00000001800110D0 | E0 07 00 F9 E8 17 40 B9 08 05 00 71 C1 00 00 54
         00000001800110E0 | 01 00 00 14 C0 00 00 F0 00 80 02 91 D4 FF FF 97
         00000001800110F0 | 01 00 00 14 FE 13 40 F9 FF C3 00 91 C0 03 5F D6
   
         AArch64 disassembly by AsmArm64
         ---
         00000001800110C0: D100C3FF  sub sp, sp, #48
         00000001800110C4: F90013FE  str x30, [sp, #32]
         00000001800110C8: F9000FE2  str x2, [sp, #24]
         00000001800110CC: B90017E1  str w1, [sp, #20]
         00000001800110D0: F90007E0  str x0, [sp, #8]
         00000001800110D4: B94017E8  ldr w8, [sp, #20]
         00000001800110D8: 71000508  subs w8, w8, #1
         00000001800110DC: 540000C1  b.ne #24
         00000001800110E0: 14000001  #0:
         00000001800110E4: F00000C0  adrp x0, #110592
         00000001800110E8: 91028000  add x0, x0, #160
         00000001800110EC: 97FFFFD4  bl #-176
         00000001800110F0: 14000001  #0:
         00000001800110F4: F94013FE  ldr x30, [sp, #32]
         00000001800110F8: 9100C3FF  add sp, sp, #48
         00000001800110FC: D65F03C0  ret
   
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
         arm64ec  0000000180011000 - 00000001800218A3 (00011000 - 000218A3)
             x64  0000000180022000 - 000000018002300F (00022000 - 0002300F)
   
     Arm64X Redirection Metadata Table
   
           FFS Start           ARM64EC Address
           ------------------------------------
           0000000180023000 -> 0000000180011F68
