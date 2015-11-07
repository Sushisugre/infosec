
# pop eax
# 0x000244af(null) => pop %eax ; ret
00024490 <__ctype_get_mb_cur_max>:
   24490:   e8 04 ea 0f 00          call   122e99 <__frame_state_for+0x379>
   24495:   81 c1 6b 2b 19 00       add    $0x192b6b,%ecx
   2449b:   65 8b 15 00 00 00 00    mov    %gs:0x0,%edx
   244a2:   8b 81 d0 fe ff ff       mov    -0x130(%ecx),%eax
   244a8:   8b 04 02                mov    (%edx,%eax,1),%eax
   244ab:   8b 00                   mov    (%eax),%eax
   244ad:   8b 40 58                mov    0x58(%eax),%eax
   244b0:   c3                      ret    
   244b1:   66 90                   xchg   %ax,%ax
   244b3:   66 90                   xchg   %ax,%ax
   244b5:   66 90                   xchg   %ax,%ax
   244b7:   66 90                   xchg   %ax,%ax
   244b9:   66 90                   xchg   %ax,%ax
   244bb:   66 90                   xchg   %ax,%ax
   244bd:   66 90                   xchg   %ax,%ax
   244bf:   90                      nop

# inc eax , inc eax
# 0x0003d5bb(null): inc %eax ; inc %eax ; ret

   0003d570 <setcontext>:
   3d570:   8b 44 24 04             mov    0x4(%esp),%eax
   3d574:   53                      push   %ebx
   3d575:   31 d2                   xor    %edx,%edx
   3d577:   8d 48 6c                lea    0x6c(%eax),%ecx
   3d57a:   bb 02 00 00 00          mov    $0x2,%ebx
   3d57f:   b8 7e 00 00 00          mov    $0x7e,%eax
   3d584:   65 ff 15 10 00 00 00    call   *%gs:0x10
   3d58b:   5b                      pop    %ebx
   3d58c:   3d 01 f0 ff ff          cmp    $0xfffff001,%eax
   3d591:   73 2b                   jae    3d5be <setcontext+0x4e>
   3d593:   8b 44 24 04             mov    0x4(%esp),%eax
   3d597:   8b 48 60                mov    0x60(%eax),%ecx
   3d59a:   d9 21                   fldenv (%ecx)
   3d59c:   8b 48 18                mov    0x18(%eax),%ecx
   3d59f:   8e e1                   mov    %ecx,%fs
   3d5a1:   8b 48 4c                mov    0x4c(%eax),%ecx
   3d5a4:   8b 60 30                mov    0x30(%eax),%esp
   3d5a7:   51                      push   %ecx
   3d5a8:   8b 78 24                mov    0x24(%eax),%edi
   3d5ab:   8b 70 28                mov    0x28(%eax),%esi
   3d5ae:   8b 68 2c                mov    0x2c(%eax),%ebp
   3d5b1:   8b 58 34                mov    0x34(%eax),%ebx
   3d5b4:   8b 50 38                mov    0x38(%eax),%edx
   3d5b7:   8b 48 3c                mov    0x3c(%eax),%ecx
   3d5ba:   8b 40 40                mov    0x40(%eax),%eax
   3d5bd:   c3                      ret    
   3d5be:   e8 d6 58 0e 00          call   122e99 

# mov ecx, eax;
# 0x001440c3(null): mov %ecx,%eax ; ret
<__nss_passwd_lookup+0x1c280>
  1440c3:   89 c8                   mov    %ecx,%eax
  1440c5:   c3                      ret  

# inc ecx;
0x001702fc(null): inc %ecx ; ret

# inc edx
# 0x001285f7(null): inc %edx ; ret
00128020 <__nss_passwd_lookup>:
  128020:   83 ec 18                sub    $0x18,%esp
  128023:   51                      push   %ecx
  128024:   31 c9                   xor    %ecx,%ecx
  128026:   e8 c5 2e fe ff          call   10aef0 <__nss_passwd_lookup2>
  12802b:   83 c4 18                add    $0x18,%esp
  12802e:   c3                      ret    
  12802f:   90                      nop
  128030:   83 ec 18                sub    $0x18,%esp
  128033:   51                      push   %ecx
  128034:   31 c9                   xor    %ecx,%ecx
  128036:   e8 45 2f fe ff          call   10af80 <__nss_passwd_lookup2+0x90>
  12803b:   83 c4 18                add    $0x18,%esp
  12803e:   c3                      ret    
  12803f:   90                      nop
  128040:   83 ec 18                sub    $0x18,%esp
  128043:   51                      push   %ecx
  128044:   31 c9                   xor    %ecx,%ecx
  128046:   e8 b5 2f fe ff          call   10b000 <__nss_passwd_lookup2+0x110>
  12804b:   83 c4 18                add    $0x18,%esp
  12804e:   c3                      ret    
  12804f:   90                      nop
  128050:   83 ec 18                sub    $0x18,%esp
  128053:   51                      push   %ecx
  128054:   31 c9                   xor    %ecx,%ecx
  128056:   e8 25 30 fe ff          call   10b080 <__nss_passwd_lookup2+0x190>
  12805b:   83 c4 18                add    $0x18,%esp
  12805e:   c3                      ret    
  12805f:   90                      nop
  128060:   83 ec 18                sub    $0x18,%esp
  128063:   51                      push   %ecx
  128064:   31 c9                   xor    %ecx,%ecx
  128066:   e8 a5 30 fe ff          call   10b110 <__nss_passwd_lookup2+0x220>
  12806b:   83 c4 18                add    $0x18,%esp
  12806e:   c3                      ret    
  12806f:   90                      nop
  128070:   83 ec 18                sub    $0x18,%esp
  128073:   51                      push   %ecx
  128074:   31 c9                   xor    %ecx,%ecx
  128076:   e8 15 31 fe ff          call   10b190 <__nss_passwd_lookup2+0x2a0>
  12807b:   83 c4 18                add    $0x18,%esp
  12807e:   c3                      ret    
  12807f:   90                      nop
  128080:   83 ec 18                sub    $0x18,%esp
  128083:   51                      push   %ecx
  128084:   31 c9                   xor    %ecx,%ecx
  128086:   e8 95 31 fe ff          call   10b220 <__nss_passwd_lookup2+0x330>
  12808b:   83 c4 18                add    $0x18,%esp
  12808e:   c3                      ret    
  12808f:   90                      nop
  128090:   83 ec 18                sub    $0x18,%esp
  128093:   51                      push   %ecx
  128094:   31 c9                   xor    %ecx,%ecx
  128096:   e8 05 32 fe ff          call   10b2a0 <__nss_passwd_lookup2+0x3b0>
  12809b:   83 c4 18                add    $0x18,%esp
  12809e:   c3                      ret    
  12809f:   90                      nop
  1280a0:   53                      push   %ebx
  1280a1:   8b 4c 24 0c             mov    0xc(%esp),%ecx
  1280a5:   31 c0                   xor    %eax,%eax
  1280a7:   8b 54 24 08             mov    0x8(%esp),%edx
  1280ab:   83 f9 20                cmp    $0x20,%ecx
  1280ae:   0f 83 9c 00 00 00       jae    128150 <__nss_passwd_lookup+0x130>
  1280b4:   e8 dc ad ff ff          call   122e95 <__frame_state_for+0x375>
  1280b9:   81 c3 d7 03 04 00       add    $0x403d7,%ebx
  1280bf:   03 1c 8b                add    (%ebx,%ecx,4),%ebx
  1280c2:   01 ca                   add    %ecx,%edx
  1280c4:   ff e3                   jmp    *%ebx
  1280c6:   8d 76 00                lea    0x0(%esi),%esi
  1280c9:   8d bc 27 00 00 00 00    lea    0x0(%edi,%eiz,1),%edi
  1280d0:   89 42 e4                mov    %eax,-0x1c(%edx)
  1280d3:   89 42 e8                mov    %eax,-0x18(%edx)
  1280d6:   89 42 ec                mov    %eax,-0x14(%edx)
  1280d9:   89 42 f0                mov    %eax,-0x10(%edx)
  1280dc:   89 42 f4                mov    %eax,-0xc(%edx)
  1280df:   89 42 f8                mov    %eax,-0x8(%edx)
  1280e2:   89 42 fc                mov    %eax,-0x4(%edx)
  1280e5:   5b                      pop    %ebx
  1280e6:   c3                      ret    
  1280e7:   89 f6                   mov    %esi,%esi
  1280e9:   8d bc 27 00 00 00 00    lea    0x0(%edi,%eiz,1),%edi
  1280f0:   89 42 e3                mov    %eax,-0x1d(%edx)
  1280f3:   89 42 e7                mov    %eax,-0x19(%edx)
  1280f6:   89 42 eb                mov    %eax,-0x15(%edx)
  1280f9:   89 42 ef                mov    %eax,-0x11(%edx)
  1280fc:   89 42 f3                mov    %eax,-0xd(%edx)
  1280ff:   89 42 f7                mov    %eax,-0x9(%edx)
  128102:   89 42 fb                mov    %eax,-0x5(%edx)
  128105:   88 42 ff                mov    %al,-0x1(%edx)
  128108:   5b                      pop    %ebx
  128109:   c3                      ret    
  12810a:   8d b6 00 00 00 00       lea    0x0(%esi),%esi
  128110:   89 42 e2                mov    %eax,-0x1e(%edx)
  128113:   89 42 e6                mov    %eax,-0x1a(%edx)
  128116:   89 42 ea                mov    %eax,-0x16(%edx)
  128119:   89 42 ee                mov    %eax,-0x12(%edx)
  12811c:   89 42 f2                mov    %eax,-0xe(%edx)
  12811f:   89 42 f6                mov    %eax,-0xa(%edx)
  128122:   89 42 fa                mov    %eax,-0x6(%edx)
  128125:   66 89 42 fe             mov    %ax,-0x2(%edx)
  128129:   5b                      pop    %ebx
  12812a:   c3                      ret    
  12812b:   90                      nop
  12812c:   8d 74 26 00             lea    0x0(%esi,%eiz,1),%esi
  128130:   89 42 e1                mov    %eax,-0x1f(%edx)
  128133:   89 42 e5                mov    %eax,-0x1b(%edx)
  128136:   89 42 e9                mov    %eax,-0x17(%edx)
  128139:   89 42 ed                mov    %eax,-0x13(%edx)
  12813c:   89 42 f1                mov    %eax,-0xf(%edx)
  12813f:   89 42 f5                mov    %eax,-0xb(%edx)
  128142:   89 42 f9                mov    %eax,-0x7(%edx)
  128145:   66 89 42 fd             mov    %ax,-0x3(%edx)
  128149:   88 42 ff                mov    %al,-0x1(%edx)
  12814c:   5b                      pop    %ebx
  12814d:   c3                      ret    
  12814e:   66 90                   xchg   %ax,%ax
  128150:   66 0f ef c0             pxor   %xmm0,%xmm0
  128154:   f7 c2 0f 00 00 00       test   $0xf,%edx
  12815a:   74 14                   je     128170 <__nss_passwd_lookup+0x150>
  12815c:   f3 0f 7f 02             movdqu %xmm0,(%edx)
  128160:   89 d0                   mov    %edx,%eax
  128162:   83 e2 f0                and    $0xfffffff0,%edx
  128165:   83 c2 10                add    $0x10,%edx
  128168:   29 d0                   sub    %edx,%eax
  12816a:   01 c1                   add    %eax,%ecx
  12816c:   66 0f 7e c0             movd   %xmm0,%eax
  128170:   81 f9 80 00 00 00       cmp    $0x80,%ecx
  128176:   73 18                   jae    128190 <__nss_passwd_lookup+0x170>
  128178:   e8 18 ad ff ff          call   122e95 <__frame_state_for+0x375>
  12817d:   81 c3 93 03 04 00       add    $0x40393,%ebx
  128183:   03 1c 8b                add    (%ebx,%ecx,4),%ebx
  128186:   01 ca                   add    %ecx,%edx
  128188:   ff e3                   jmp    *%ebx
  12818a:   8d b6 00 00 00 00       lea    0x0(%esi),%esi
  128190:   e8 00 ad ff ff          call   122e95 <__frame_state_for+0x375>
  128195:   81 c3 6b ee 08 00       add    $0x8ee6b,%ebx
  12819b:   8b 9b 80 01 00 00       mov    0x180(%ebx),%ebx
  1281a1:   39 d9                   cmp    %ebx,%ecx
  1281a3:   0f 83 fb 00 00 00       jae    1282a4 <__nss_passwd_lookup+0x284>
  1281a9:   e8 e7 ac ff ff          call   122e95 <__frame_state_for+0x375>
  1281ae:   81 c3 52 ee 08 00       add    $0x8ee52,%ebx
  1281b4:   3b 8b 90 01 00 00       cmp    0x190(%ebx),%ecx
  1281ba:   0f 83 90 00 00 00       jae    128250 <__nss_passwd_lookup+0x230>
  1281c0:   81 e9 80 00 00 00       sub    $0x80,%ecx
  1281c6:   81 e9 80 00 00 00       sub    $0x80,%ecx
  1281cc:   66 0f 7f 02             movdqa %xmm0,(%edx)
  1281d0:   66 0f 7f 42 10          movdqa %xmm0,0x10(%edx)
  1281d5:   66 0f 7f 42 20          movdqa %xmm0,0x20(%edx)
  1281da:   66 0f 7f 42 30          movdqa %xmm0,0x30(%edx)
  1281df:   66 0f 7f 42 40          movdqa %xmm0,0x40(%edx)
  1281e4:   66 0f 7f 42 50          movdqa %xmm0,0x50(%edx)
  1281e9:   66 0f 7f 42 60          movdqa %xmm0,0x60(%edx)
  1281ee:   66 0f 7f 42 70          movdqa %xmm0,0x70(%edx)
  1281f3:   8d 92 80 00 00 00       lea    0x80(%edx),%edx
  1281f9:   72 35                   jb     128230 <__nss_passwd_lookup+0x210>
  1281fb:   81 e9 80 00 00 00       sub    $0x80,%ecx
  128201:   66 0f 7f 02             movdqa %xmm0,(%edx)
  128205:   66 0f 7f 42 10          movdqa %xmm0,0x10(%edx)
  12820a:   66 0f 7f 42 20          movdqa %xmm0,0x20(%edx)
  12820f:   66 0f 7f 42 30          movdqa %xmm0,0x30(%edx)
  128214:   66 0f 7f 42 40          movdqa %xmm0,0x40(%edx)
  128219:   66 0f 7f 42 50          movdqa %xmm0,0x50(%edx)
  12821e:   66 0f 7f 42 60          movdqa %xmm0,0x60(%edx)
  128223:   66 0f 7f 42 70          movdqa %xmm0,0x70(%edx)
  128228:   8d 92 80 00 00 00       lea    0x80(%edx),%edx
  12822e:   73 96                   jae    1281c6 <__nss_passwd_lookup+0x1a6>
  128230:   81 c1 80 00 00 00       add    $0x80,%ecx
  128236:   e8 5a ac ff ff          call   122e95 <__frame_state_for+0x375>
  12823b:   81 c3 d5 02 04 00       add    $0x402d5,%ebx
  128241:   03 1c 8b                add    (%ebx,%ecx,4),%ebx
  128244:   01 ca                   add    %ecx,%edx
  128246:   ff e3                   jmp    *%ebx
  128248:   90                      nop
  128249:   8d b4 26 00 00 00 00    lea    0x0(%esi,%eiz,1),%esi
  128250:   0f 18 8a 80 03 00 00    prefetcht0 0x380(%edx)
  128257:   0f 18 8a c0 03 00 00    prefetcht0 0x3c0(%edx)
  12825e:   81 e9 80 00 00 00       sub    $0x80,%ecx
  128264:   66 0f 7f 02             movdqa %xmm0,(%edx)
  128268:   0f 29 42 10             movaps %xmm0,0x10(%edx)
  12826c:   0f 29 42 20             movaps %xmm0,0x20(%edx)
  128270:   0f 29 42 30             movaps %xmm0,0x30(%edx)
  128274:   0f 29 42 40             movaps %xmm0,0x40(%edx)
  128278:   0f 29 42 50             movaps %xmm0,0x50(%edx)
  12827c:   0f 29 42 60             movaps %xmm0,0x60(%edx)
  128280:   0f 29 42 70             movaps %xmm0,0x70(%edx)
  128284:   81 c2 80 00 00 00       add    $0x80,%edx
  12828a:   81 f9 80 00 00 00       cmp    $0x80,%ecx
  128290:   73 be                   jae    128250 <__nss_passwd_lookup+0x230>
  128292:   e8 fe ab ff ff          call   122e95 <__frame_state_for+0x375>
  128297:   81 c3 79 02 04 00       add    $0x40279,%ebx
  12829d:   03 1c 8b                add    (%ebx,%ecx,4),%ebx
  1282a0:   01 ca                   add    %ecx,%edx
  1282a2:   ff e3                   jmp    *%ebx
  1282a4:   29 d9                   sub    %ebx,%ecx
  1282a6:   8d 76 00                lea    0x0(%esi),%esi
  1282a9:   8d bc 27 00 00 00 00    lea    0x0(%edi,%eiz,1),%edi
  1282b0:   0f 18 8a c0 03 00 00    prefetcht0 0x3c0(%edx)
  1282b7:   0f 18 8a 80 03 00 00    prefetcht0 0x380(%edx)
  1282be:   81 eb 80 00 00 00       sub    $0x80,%ebx
  1282c4:   66 0f 7f 02             movdqa %xmm0,(%edx)
  1282c8:   66 0f 7f 42 10          movdqa %xmm0,0x10(%edx)
  1282cd:   66 0f 7f 42 20          movdqa %xmm0,0x20(%edx)
  1282d2:   66 0f 7f 42 30          movdqa %xmm0,0x30(%edx)
  1282d7:   66 0f 7f 42 40          movdqa %xmm0,0x40(%edx)
  1282dc:   66 0f 7f 42 50          movdqa %xmm0,0x50(%edx)
  1282e1:   66 0f 7f 42 60          movdqa %xmm0,0x60(%edx)
  1282e6:   66 0f 7f 42 70          movdqa %xmm0,0x70(%edx)
  1282eb:   81 c2 80 00 00 00       add    $0x80,%edx
  1282f1:   81 fb 80 00 00 00       cmp    $0x80,%ebx
  1282f7:   73 b7                   jae    1282b0 <__nss_passwd_lookup+0x290>
  1282f9:   81 f9 80 00 00 00       cmp    $0x80,%ecx
  1282ff:   72 4d                   jb     12834e <__nss_passwd_lookup+0x32e>
  128301:   eb 0d                   jmp    128310 <__nss_passwd_lookup+0x2f0>
  128303:   90                      nop
  128304:   90                      nop
  128305:   90                      nop
  128306:   90                      nop
  128307:   90                      nop
  128308:   90                      nop
  128309:   90                      nop
  12830a:   90                      nop
  12830b:   90                      nop
  12830c:   90                      nop
  12830d:   90                      nop
  12830e:   90                      nop
  12830f:   90                      nop
  128310:   81 e9 80 00 00 00       sub    $0x80,%ecx
  128316:   66 0f e7 02             movntdq %xmm0,(%edx)
  12831a:   66 0f e7 42 10          movntdq %xmm0,0x10(%edx)
  12831f:   66 0f e7 42 20          movntdq %xmm0,0x20(%edx)
  128324:   66 0f e7 42 30          movntdq %xmm0,0x30(%edx)
  128329:   66 0f e7 42 40          movntdq %xmm0,0x40(%edx)
  12832e:   66 0f e7 42 50          movntdq %xmm0,0x50(%edx)
  128333:   66 0f e7 42 60          movntdq %xmm0,0x60(%edx)
  128338:   66 0f e7 42 70          movntdq %xmm0,0x70(%edx)
  12833d:   81 c2 80 00 00 00       add    $0x80,%edx
  128343:   81 f9 80 00 00 00       cmp    $0x80,%ecx
  128349:   73 c5                   jae    128310 <__nss_passwd_lookup+0x2f0>
  12834b:   0f ae f8                sfence 
  12834e:   e8 42 ab ff ff          call   122e95 <__frame_state_for+0x375>
  128353:   81 c3 bd 01 04 00       add    $0x401bd,%ebx
  128359:   03 1c 8b                add    (%ebx,%ecx,4),%ebx
  12835c:   01 ca                   add    %ecx,%edx
  12835e:   ff e3                   jmp    *%ebx
  128360:   66 0f 7f 42 90          movdqa %xmm0,-0x70(%edx)
  128365:   66 0f 7f 42 a0          movdqa %xmm0,-0x60(%edx)
  12836a:   66 0f 7f 42 b0          movdqa %xmm0,-0x50(%edx)
  12836f:   66 0f 7f 42 c0          movdqa %xmm0,-0x40(%edx)
  128374:   66 0f 7f 42 d0          movdqa %xmm0,-0x30(%edx)
  128379:   66 0f 7f 42 e0          movdqa %xmm0,-0x20(%edx)
  12837e:   66 0f 7f 42 f0          movdqa %xmm0,-0x10(%edx)
  128383:   5b                      pop    %ebx
  128384:   c3                      ret    
  128385:   8d 74 26 00             lea    0x0(%esi,%eiz,1),%esi
  128389:   8d bc 27 00 00 00 00    lea    0x0(%edi,%eiz,1),%edi
  128390:   66 0f 7f 42 8f          movdqa %xmm0,-0x71(%edx)
  128395:   66 0f 7f 42 9f          movdqa %xmm0,-0x61(%edx)
  12839a:   66 0f 7f 42 af          movdqa %xmm0,-0x51(%edx)
  12839f:   66 0f 7f 42 bf          movdqa %xmm0,-0x41(%edx)
  1283a4:   66 0f 7f 42 cf          movdqa %xmm0,-0x31(%edx)
  1283a9:   66 0f 7f 42 df          movdqa %xmm0,-0x21(%edx)
  1283ae:   66 0f 7f 42 ef          movdqa %xmm0,-0x11(%edx)
  1283b3:   88 42 ff                mov    %al,-0x1(%edx)
  1283b6:   5b                      pop    %ebx
  1283b7:   c3                      ret    
  1283b8:   90                      nop
  1283b9:   8d b4 26 00 00 00 00    lea    0x0(%esi,%eiz,1),%esi
  1283c0:   66 0f 7f 42 8e          movdqa %xmm0,-0x72(%edx)
  1283c5:   66 0f 7f 42 9e          movdqa %xmm0,-0x62(%edx)
  1283ca:   66 0f 7f 42 ae          movdqa %xmm0,-0x52(%edx)
  1283cf:   66 0f 7f 42 be          movdqa %xmm0,-0x42(%edx)
  1283d4:   66 0f 7f 42 ce          movdqa %xmm0,-0x32(%edx)
  1283d9:   66 0f 7f 42 de          movdqa %xmm0,-0x22(%edx)
  1283de:   66 0f 7f 42 ee          movdqa %xmm0,-0x12(%edx)
  1283e3:   66 89 42 fe             mov    %ax,-0x2(%edx)
  1283e7:   5b                      pop    %ebx
  1283e8:   c3                      ret    
  1283e9:   8d b4 26 00 00 00 00    lea    0x0(%esi,%eiz,1),%esi
  1283f0:   66 0f 7f 42 8d          movdqa %xmm0,-0x73(%edx)
  1283f5:   66 0f 7f 42 9d          movdqa %xmm0,-0x63(%edx)
  1283fa:   66 0f 7f 42 ad          movdqa %xmm0,-0x53(%edx)
  1283ff:   66 0f 7f 42 bd          movdqa %xmm0,-0x43(%edx)
  128404:   66 0f 7f 42 cd          movdqa %xmm0,-0x33(%edx)
  128409:   66 0f 7f 42 dd          movdqa %xmm0,-0x23(%edx)
  12840e:   66 0f 7f 42 ed          movdqa %xmm0,-0x13(%edx)
  128413:   66 89 42 fd             mov    %ax,-0x3(%edx)
  128417:   88 42 ff                mov    %al,-0x1(%edx)
  12841a:   5b                      pop    %ebx
  12841b:   c3                      ret    
  12841c:   8d 74 26 00             lea    0x0(%esi,%eiz,1),%esi
  128420:   66 0f 7f 42 8c          movdqa %xmm0,-0x74(%edx)
  128425:   66 0f 7f 42 9c          movdqa %xmm0,-0x64(%edx)
  12842a:   66 0f 7f 42 ac          movdqa %xmm0,-0x54(%edx)
  12842f:   66 0f 7f 42 bc          movdqa %xmm0,-0x44(%edx)
  128434:   66 0f 7f 42 cc          movdqa %xmm0,-0x34(%edx)
  128439:   66 0f 7f 42 dc          movdqa %xmm0,-0x24(%edx)
  12843e:   66 0f 7f 42 ec          movdqa %xmm0,-0x14(%edx)
  128443:   89 42 fc                mov    %eax,-0x4(%edx)
  128446:   5b                      pop    %ebx
  128447:   c3                      ret    
  128448:   90                      nop
  128449:   8d b4 26 00 00 00 00    lea    0x0(%esi,%eiz,1),%esi
  128450:   66 0f 7f 42 8b          movdqa %xmm0,-0x75(%edx)
  128455:   66 0f 7f 42 9b          movdqa %xmm0,-0x65(%edx)
  12845a:   66 0f 7f 42 ab          movdqa %xmm0,-0x55(%edx)
  12845f:   66 0f 7f 42 bb          movdqa %xmm0,-0x45(%edx)
  128464:   66 0f 7f 42 cb          movdqa %xmm0,-0x35(%edx)
  128469:   66 0f 7f 42 db          movdqa %xmm0,-0x25(%edx)
  12846e:   66 0f 7f 42 eb          movdqa %xmm0,-0x15(%edx)
  128473:   89 42 fb                mov    %eax,-0x5(%edx)
  128476:   88 42 ff                mov    %al,-0x1(%edx)
  128479:   5b                      pop    %ebx
  12847a:   c3                      ret    
  12847b:   90                      nop
  12847c:   8d 74 26 00             lea    0x0(%esi,%eiz,1),%esi
  128480:   66 0f 7f 42 8a          movdqa %xmm0,-0x76(%edx)
  128485:   66 0f 7f 42 9a          movdqa %xmm0,-0x66(%edx)
  12848a:   66 0f 7f 42 aa          movdqa %xmm0,-0x56(%edx)
  12848f:   66 0f 7f 42 ba          movdqa %xmm0,-0x46(%edx)
  128494:   66 0f 7f 42 ca          movdqa %xmm0,-0x36(%edx)
  128499:   66 0f 7f 42 da          movdqa %xmm0,-0x26(%edx)
  12849e:   66 0f 7f 42 ea          movdqa %xmm0,-0x16(%edx)
  1284a3:   89 42 fa                mov    %eax,-0x6(%edx)
  1284a6:   66 89 42 fe             mov    %ax,-0x2(%edx)
  1284aa:   5b                      pop    %ebx
  1284ab:   c3                      ret    
  1284ac:   8d 74 26 00             lea    0x0(%esi,%eiz,1),%esi
  1284b0:   66 0f 7f 42 89          movdqa %xmm0,-0x77(%edx)
  1284b5:   66 0f 7f 42 99          movdqa %xmm0,-0x67(%edx)
  1284ba:   66 0f 7f 42 a9          movdqa %xmm0,-0x57(%edx)
  1284bf:   66 0f 7f 42 b9          movdqa %xmm0,-0x47(%edx)
  1284c4:   66 0f 7f 42 c9          movdqa %xmm0,-0x37(%edx)
  1284c9:   66 0f 7f 42 d9          movdqa %xmm0,-0x27(%edx)
  1284ce:   66 0f 7f 42 e9          movdqa %xmm0,-0x17(%edx)
  1284d3:   89 42 f9                mov    %eax,-0x7(%edx)
  1284d6:   66 89 42 fd             mov    %ax,-0x3(%edx)
  1284da:   88 42 ff                mov    %al,-0x1(%edx)
  1284dd:   5b                      pop    %ebx
  1284de:   c3                      ret    
  1284df:   90                      nop
  1284e0:   66 0f 7f 42 88          movdqa %xmm0,-0x78(%edx)
  1284e5:   66 0f 7f 42 98          movdqa %xmm0,-0x68(%edx)
  1284ea:   66 0f 7f 42 a8          movdqa %xmm0,-0x58(%edx)
  1284ef:   66 0f 7f 42 b8          movdqa %xmm0,-0x48(%edx)
  1284f4:   66 0f 7f 42 c8          movdqa %xmm0,-0x38(%edx)
  1284f9:   66 0f 7f 42 d8          movdqa %xmm0,-0x28(%edx)
  1284fe:   66 0f 7f 42 e8          movdqa %xmm0,-0x18(%edx)
  128503:   66 0f d6 42 f8          movq   %xmm0,-0x8(%edx)
  128508:   5b                      pop    %ebx
  128509:   c3                      ret    
  12850a:   8d b6 00 00 00 00       lea    0x0(%esi),%esi
  128510:   66 0f 7f 42 87          movdqa %xmm0,-0x79(%edx)
  128515:   66 0f 7f 42 97          movdqa %xmm0,-0x69(%edx)
  12851a:   66 0f 7f 42 a7          movdqa %xmm0,-0x59(%edx)
  12851f:   66 0f 7f 42 b7          movdqa %xmm0,-0x49(%edx)
  128524:   66 0f 7f 42 c7          movdqa %xmm0,-0x39(%edx)
  128529:   66 0f 7f 42 d7          movdqa %xmm0,-0x29(%edx)
  12852e:   66 0f 7f 42 e7          movdqa %xmm0,-0x19(%edx)
  128533:   66 0f d6 42 f7          movq   %xmm0,-0x9(%edx)
  128538:   88 42 ff                mov    %al,-0x1(%edx)
  12853b:   5b                      pop    %ebx
  12853c:   c3                      ret    
  12853d:   8d 76 00                lea    0x0(%esi),%esi
  128540:   66 0f 7f 42 86          movdqa %xmm0,-0x7a(%edx)
  128545:   66 0f 7f 42 96          movdqa %xmm0,-0x6a(%edx)
  12854a:   66 0f 7f 42 a6          movdqa %xmm0,-0x5a(%edx)
  12854f:   66 0f 7f 42 b6          movdqa %xmm0,-0x4a(%edx)
  128554:   66 0f 7f 42 c6          movdqa %xmm0,-0x3a(%edx)
  128559:   66 0f 7f 42 d6          movdqa %xmm0,-0x2a(%edx)
  12855e:   66 0f 7f 42 e6          movdqa %xmm0,-0x1a(%edx)
  128563:   66 0f d6 42 f6          movq   %xmm0,-0xa(%edx)
  128568:   66 89 42 fe             mov    %ax,-0x2(%edx)
  12856c:   5b                      pop    %ebx
  12856d:   c3                      ret    
  12856e:   66 90                   xchg   %ax,%ax
  128570:   66 0f 7f 42 85          movdqa %xmm0,-0x7b(%edx)
  128575:   66 0f 7f 42 95          movdqa %xmm0,-0x6b(%edx)
  12857a:   66 0f 7f 42 a5          movdqa %xmm0,-0x5b(%edx)
  12857f:   66 0f 7f 42 b5          movdqa %xmm0,-0x4b(%edx)
  128584:   66 0f 7f 42 c5          movdqa %xmm0,-0x3b(%edx)
  128589:   66 0f 7f 42 d5          movdqa %xmm0,-0x2b(%edx)
  12858e:   66 0f 7f 42 e5          movdqa %xmm0,-0x1b(%edx)
  128593:   66 0f d6 42 f5          movq   %xmm0,-0xb(%edx)
  128598:   66 89 42 fd             mov    %ax,-0x3(%edx)
  12859c:   88 42 ff                mov    %al,-0x1(%edx)
  12859f:   5b                      pop    %ebx
  1285a0:   c3                      ret    
  1285a1:   eb 0d                   jmp    1285b0 <__nss_passwd_lookup+0x590>
  1285a3:   90                      nop
  1285a4:   90                      nop
  1285a5:   90                      nop
  1285a6:   90                      nop
  1285a7:   90                      nop
  1285a8:   90                      nop
  1285a9:   90                      nop
  1285aa:   90                      nop
  1285ab:   90                      nop
  1285ac:   90                      nop
  1285ad:   90                      nop
  1285ae:   90                      nop
  1285af:   90                      nop
  1285b0:   66 0f 7f 42 84          movdqa %xmm0,-0x7c(%edx)
  1285b5:   66 0f 7f 42 94          movdqa %xmm0,-0x6c(%edx)
  1285ba:   66 0f 7f 42 a4          movdqa %xmm0,-0x5c(%edx)
  1285bf:   66 0f 7f 42 b4          movdqa %xmm0,-0x4c(%edx)
  1285c4:   66 0f 7f 42 c4          movdqa %xmm0,-0x3c(%edx)
  1285c9:   66 0f 7f 42 d4          movdqa %xmm0,-0x2c(%edx)
  1285ce:   66 0f 7f 42 e4          movdqa %xmm0,-0x1c(%edx)
  1285d3:   66 0f d6 42 f4          movq   %xmm0,-0xc(%edx)
  1285d8:   89 42 fc                mov    %eax,-0x4(%edx)
  1285db:   5b                      pop    %ebx
  1285dc:   c3                      ret    
  1285dd:   8d 76 00                lea    0x0(%esi),%esi
  1285e0:   66 0f 7f 42 83          movdqa %xmm0,-0x7d(%edx)
  1285e5:   66 0f 7f 42 93          movdqa %xmm0,-0x6d(%edx)
  1285ea:   66 0f 7f 42 a3          movdqa %xmm0,-0x5d(%edx)
  1285ef:   66 0f 7f 42 b3          movdqa %xmm0,-0x4d(%edx)
  1285f4:   66 0f 7f 42 c3          movdqa %xmm0,-


# pop edx
# 0x000f7041(null): pop %edx ; pop %ecx ; pop %ebx ; ret

000f6fb0 <pthread_setcanceltype>:
   f6fb0:   53                      push   %ebx
   f6fb1:   e8 df be 02 00          call   122e95 <__frame_state_for+0x375>
   f6fb6:   81 c3 4a 00 0c 00       add    $0xc004a,%ebx
   f6fbc:   83 ec 08                sub    $0x8,%esp
   f6fbf:   8b 83 18 3d 00 00       mov    0x3d18(%ebx),%eax
   f6fc5:   85 c0                   test   %eax,%eax
   f6fc7:   74 20                   je     f6fe9 <pthread_setcanceltype+0x39>
   f6fc9:   83 ec 08                sub    $0x8,%esp
   f6fcc:   8b 83 d4 3c 00 00       mov    0x3cd4(%ebx),%eax
   f6fd2:   ff 74 24 1c             pushl  0x1c(%esp)
   f6fd6:   ff 74 24 1c             pushl  0x1c(%esp)
   f6fda:   c1 c8 09                ror    $0x9,%eax
   f6fdd:   65 33 05 18 00 00 00    xor    %gs:0x18,%eax
   f6fe4:   ff d0                   call   *%eax
   f6fe6:   83 c4 10                add    $0x10,%esp
   f6fe9:   83 c4 08                add    $0x8,%esp
   f6fec:   5b                      pop    %ebx
   f6fed:   c3                      ret    
   f6fee:   66 90                   xchg   %ax,%ax
   f6ff0:   52                      push   %edx
   f6ff1:   53                      push   %ebx
   f6ff2:   56                      push   %esi
   f6ff3:   ba 02 00 00 00          mov    $0x2,%edx
   f6ff8:   89 cb                   mov    %ecx,%ebx
   f6ffa:   31 f6                   xor    %esi,%esi
   f6ffc:   b9 80 00 00 00          mov    $0x80,%ecx
   f7001:   39 d0                   cmp    %edx,%eax
   f7003:   75 0d                   jne    f7012 <pthread_setcanceltype+0x62>
   f7005:   90                      nop
   f7006:   b8 f0 00 00 00          mov    $0xf0,%eax
   f700b:   65 ff 15 10 00 00 00    call   *%gs:0x10
   f7012:   89 d0                   mov    %edx,%eax
   f7014:   87 03                   xchg   %eax,(%ebx)
   f7016:   85 c0                   test   %eax,%eax
   f7018:   75 eb                   jne    f7005 <pthread_setcanceltype+0x55>
   f701a:   5e                      pop    %esi
   f701b:   5b                      pop    %ebx
   f701c:   5a                      pop    %edx
   f701d:   c3                      ret    
   f701e:   66 90                   xchg   %ax,%ax
   f7020:   53                      push   %ebx
   f7021:   51                      push   %ecx
   f7022:   52                      push   %edx
   f7023:   89 c3                   mov    %eax,%ebx
   f7025:   c7 00 00 00 00 00       movl   $0x0,(%eax)
   f702b:   b9 81 00 00 00          mov    $0x81,%ecx
   f7030:   ba 01 00 00 00          mov    $0x1,%edx
   f7035:   b8 f0 00 00 00          mov    $0xf0,%eax
   f703a:   65 ff 15 10 00 00 00    call   *%gs:0x10
   f7041:   5a                      pop    %edx
   f7042:   59                      pop    %ecx
   f7043:   5b                      pop    %ebx
   f7044:   c3                      ret  

# 
0x00122ea0(null): mov (%esp),%edx ; ret

0x00078dc7(null): inc %eax ; pop %edi ; pop %esi ; ret
00078be0 <memchr>:
   78be0: 53                    push   %ebx
   78be1: e8 af a2 0a 00        call   122e95 <__frame_state_for+0x375>
   78be6: 81 c3 1a e4 13 00     add    $0x13e41a,%ebx
   78bec: 83 bb 40 3a 00 00 00  cmpl   $0x0,0x3a40(%ebx)
   78bf3: 75 05                 jne    78bfa <memchr+0x1a>
   78bf5: e8 36 fe f9 ff        call   18a30 <gnu_get_libc_version+0x1c0>
   78bfa: f7 83 54 3a 00 00 00  testl  $0x4000000,0x3a54(%ebx)
   78c01: 00 00 04 
   78c04: 74 14                 je     78c1a <memchr+0x3a>
   78c06: f7 83 80 3a 00 00 04  testl  $0x4,0x3a80(%ebx)
   78c0d: 00 00 00 
   78c10: 74 10                 je     78c22 <memchr+0x42>
   78c12: 8d 83 90 c9 f8 ff     lea    -0x73670(%ebx),%eax
   78c18: 5b                    pop    %ebx
   78c19: c3                    ret    
   78c1a: 8d 83 30 1c ec ff     lea    -0x13e3d0(%ebx),%eax
   78c20: 5b                    pop    %ebx
   78c21: c3                    ret    
   78c22: 8d 83 f0 b6 ed ff     lea    -0x124910(%ebx),%eax
   78c28: 5b                    pop    %ebx
   78c29: c3                    ret    
   78c2a: 8d b6 00 00 00 00     lea    0x0(%esi),%esi
   78c30: 56                    push   %esi
   78c31: 57                    push   %edi
   78c32: 8b 44 24 0c           mov    0xc(%esp),%eax
   78c36: 8b 54 24 10           mov    0x10(%esp),%edx
   78c3a: 8b 74 24 14           mov    0x14(%esp),%esi
   78c3e: 83 fe 04              cmp    $0x4,%esi
   78c41: 0f 82 48 01 00 00     jb     78d8f <memchr+0x1af>
   78c47: 88 d6                 mov    %dl,%dh
   78c49: 89 d1                 mov    %edx,%ecx
   78c4b: c1 e2 10              shl    $0x10,%edx
   78c4e: 66 89 ca              mov    %cx,%dx
   78c51: a8 03                 test   $0x3,%al
   78c53: 0f 84 cd 00 00 00     je     78d26 <memchr+0x146>
   78c59: 38 10                 cmp    %dl,(%eax)
   78c5b: 0f 84 67 01 00 00     je     78dc8 <memchr+0x1e8>
   78c61: 40                    inc    %eax
   78c62: 4e                    dec    %esi
   78c63: 0f 84 3f 01 00 00     je     78da8 <memchr+0x1c8>
   78c69: a8 03                 test   $0x3,%al
   78c6b: 0f 84 b5 00 00 00     je     78d26 <memchr+0x146>
   78c71: 38 10                 cmp    %dl,(%eax)
   78c73: 0f 84 4f 01 00 00     je     78dc8 <memchr+0x1e8>
   78c79: 40                    inc    %eax
   78c7a: 4e                    dec    %esi
   78c7b: 0f 84 27 01 00 00     je     78da8 <memchr+0x1c8>
   78c81: a8 03                 test   $0x3,%al
   78c83: 0f 84 9d 00 00 00     je     78d26 <memchr+0x146>
   78c89: 38 10                 cmp    %dl,(%eax)
   78c8b: 0f 84 37 01 00 00     je     78dc8 <memchr+0x1e8>
   78c91: 40                    inc    %eax
   78c92: 4e                    dec    %esi
   78c93: e9 8e 00 00 00        jmp    78d26 <memchr+0x146>
   78c98: 90                    nop
   78c99: 8d b4 26 00 00 00 00  lea    0x0(%esi,%eiz,1),%esi
   78ca0: 8b 08                 mov    (%eax),%ecx
   78ca2: bf ff fe fe fe        mov    $0xfefefeff,%edi
   78ca7: 31 d1                 xor    %edx,%ecx
   78ca9: 01 cf                 add    %ecx,%edi
   78cab: 0f 83 04 01 00 00     jae    78db5 <memchr+0x1d5>
   78cb1: 31 cf                 xor    %ecx,%edi
   78cb3: 81 cf ff fe fe fe     or     $0xfefefeff,%edi
   78cb9: 47                    inc    %edi
   78cba: 0f 85 f5 00 00 00     jne    78db5 <memchr+0x1d5>
   78cc0: 8b 48 04              mov    0x4(%eax),%ecx
   78cc3: bf ff fe fe fe        mov    $0xfefefeff,%edi
   78cc8: 31 d1                 xor    %edx,%ecx
   78cca: 01 cf                 add    %ecx,%edi
   78ccc: 0f 83 e0 00 00 00     jae    78db2 <memchr+0x1d2>
   78cd2: 31 cf                 xor    %ecx,%edi
   78cd4: 81 cf ff fe fe fe     or     $0xfefefeff,%edi
   78cda: 47                    inc    %edi
   78cdb: 0f 85 d1 00 00 00     jne    78db2 <memchr+0x1d2>
   78ce1: 8b 48 08              mov    0x8(%eax),%ecx
   78ce4: bf ff fe fe fe        mov    $0xfefefeff,%edi
   78ce9: 31 d1                 xor    %edx,%ecx
   78ceb: 01 cf                 add    %ecx,%edi
   78ced: 0f 83 bc 00 00 00     jae    78daf <memchr+0x1cf>
   78cf3: 31 cf                 xor    %ecx,%edi
   78cf5: 81 cf ff fe fe fe     or     $0xfefefeff,%edi
   78cfb: 47                    inc    %edi
   78cfc: 0f 85 ad 00 00 00     jne    78daf <memchr+0x1cf>
   78d02: 8b 48 0c              mov    0xc(%eax),%ecx
   78d05: bf ff fe fe fe        mov    $0xfefefeff,%edi
   78d0a: 31 d1                 xor    %edx,%ecx
   78d0c: 01 cf                 add    %ecx,%edi
   78d0e: 0f 83 98 00 00 00     jae    78dac <memchr+0x1cc>
   78d14: 31 cf                 xor    %ecx,%edi
   78d16: 81 cf ff fe fe fe     or     $0xfefefeff,%edi
   78d1c: 47                    inc    %edi
   78d1d: 0f 85 89 00 00 00     jne    78dac <memchr+0x1cc>
   78d23: 83 c0 10              add    $0x10,%eax
   78d26: 83 ee 10              sub    $0x10,%esi
   78d29: 0f 83 71 ff ff ff     jae    78ca0 <memchr+0xc0>
   78d2f: 83 fe f4              cmp    $0xfffffff4,%esi
   78d32: 72 5b                 jb     78d8f <memchr+0x1af>
   78d34: 8b 08                 mov    (%eax),%ecx
   78d36: bf ff fe fe fe        mov    $0xfefefeff,%edi
   78d3b: 31 d1                 xor    %edx,%ecx
   78d3d: 01 cf                 add    %ecx,%edi
   78d3f: 73 74                 jae    78db5 <memchr+0x1d5>
   78d41: 31 cf                 xor    %ecx,%edi
   78d43: 81 cf ff fe fe fe     or     $0xfefefeff,%edi
   78d49: 47                    inc    %edi
   78d4a: 75 69                 jne    78db5 <memchr+0x1d5>
   78d4c: 83 c0 04              add    $0x4,%eax
   78d4f: 83 fe f8              cmp    $0xfffffff8,%esi
   78d52: 72 3b                 jb     78d8f <memchr+0x1af>
   78d54: 8b 08                 mov    (%eax),%ecx
   78d56: bf ff fe fe fe        mov    $0xfefefeff,%edi
   78d5b: 31 d1                 xor    %edx,%ecx
   78d5d: 01 cf                 add    %ecx,%edi
   78d5f: 73 54                 jae    78db5 <memchr+0x1d5>
   78d61: 31 cf                 xor    %ecx,%edi
   78d63: 81 cf ff fe fe fe     or     $0xfefefeff,%edi
   78d69: 47                    inc    %edi
   78d6a: 75 49                 jne    78db5 <memchr+0x1d5>
   78d6c: 83 c0 04              add    $0x4,%eax
   78d6f: 83 fe fc              cmp    $0xfffffffc,%esi
   78d72: 72 1b                 jb     78d8f <memchr+0x1af>
   78d74: 8b 08                 mov    (%eax),%ecx
   78d76: bf ff fe fe fe        mov    $0xfefefeff,%edi
   78d7b: 31 d1                 xor    %edx,%ecx
   78d7d: 01 cf                 add    %ecx,%edi
   78d7f: 73 34                 jae    78db5 <memchr+0x1d5>
   78d81: 31 cf                 xor    %ecx,%edi
   78d83: 81 cf ff fe fe fe     or     $0xfefefeff,%edi
   78d89: 47                    inc    %edi
   78d8a: 75 29                 jne    78db5 <memchr+0x1d5>
   78d8c: 83 c0 04              add    $0x4,%eax
   78d8f: 83 e6 03              and    $0x3,%esi
   78d92: 74 14                 je     78da8 <memchr+0x1c8>
   78d94: 38 10                 cmp    %dl,(%eax)
   78d96: 74 30                 je     78dc8 <memchr+0x1e8>
   78d98: 40                    inc    %eax
   78d99: 4e                    dec    %esi
   78d9a: 74 0c                 je     78da8 <memchr+0x1c8>
   78d9c: 38 10                 cmp    %dl,(%eax)
   78d9e: 74 28                 je     78dc8 <memchr+0x1e8>
   78da0: 40                    inc    %eax
   78da1: 4e                    dec    %esi
   78da2: 74 04                 je     78da8 <memchr+0x1c8>
   78da4: 38 10                 cmp    %dl,(%eax)
   78da6: 74 20                 je     78dc8 <memchr+0x1e8>
   78da8: 31 c0                 xor    %eax,%eax
   78daa: eb 1c                 jmp    78dc8 <memchr+0x1e8>
   78dac: 83 c0 04              add    $0x4,%eax
   78daf: 83 c0 04              add    $0x4,%eax
   78db2: 83 c0 04              add    $0x4,%eax
   78db5: 84 c9                 test   %cl,%cl
   78db7: 74 0f                 je     78dc8 <memchr+0x1e8>
   78db9: 40                    inc    %eax
   78dba: 84 ed                 test   %ch,%ch
   78dbc: 74 0a                 je     78dc8 <memchr+0x1e8>
   78dbe: 40                    inc    %eax
   78dbf: f7 c1 00 00 ff 00     test   $0xff0000,%ecx
   78dc5: 74 01                 je     78dc8 <memchr+0x1e8>
   78dc7: 40                    inc    %eax
   78dc8: 5f                    pop    %edi
   78dc9: 5e                    pop    %esi
   78dca: c3                    ret    
   78dcb: 66 90                 xchg   %ax,%ax
   78dcd: 66 90                 xchg   %ax,%ax
   78dcf: 90                    nop




# doesn't work contains upper case
0x0003d5bb(null): inc %eax ; inc %eax ; ret

