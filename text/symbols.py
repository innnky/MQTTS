import os

punctuation = ['!', '?', '…', ",", ".", '-']
pu_symbols = punctuation + ["SP", "UNK"]
pad = '_'

c = ['AA', 'EE', 'OO', 'b', 'c', 'ch', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'sh', 't', 'w', 'x', 'y', 'z', 'zh']
v = ['E1', 'En1', 'a1', 'ai1', 'an1', 'ang1', 'ao1', 'e1', 'ei1', 'en1', 'eng1', 'er1', 'i1', 'i01', 'ia1', 'ian1', 'iang1', 'iao1', 'ie1', 'in1', 'ing1', 'iong1', 'ir1', 'iu1', 'o1', 'ong1', 'ou1', 'u1', 'ua1', 'uai1', 'uan1', 'uang1', 'ui1', 'un1', 'uo1', 'v1', 'van1', 've1', 'vn1', 'E2', 'En2', 'a2', 'ai2', 'an2', 'ang2', 'ao2', 'e2', 'ei2', 'en2', 'eng2', 'er2', 'i2', 'i02', 'ia2', 'ian2', 'iang2', 'iao2', 'ie2', 'in2', 'ing2', 'iong2', 'ir2', 'iu2', 'o2', 'ong2', 'ou2', 'u2', 'ua2', 'uai2', 'uan2', 'uang2', 'ui2', 'un2', 'uo2', 'v2', 'van2', 've2', 'vn2', 'E3', 'En3', 'a3', 'ai3', 'an3', 'ang3', 'ao3', 'e3', 'ei3', 'en3', 'eng3', 'er3', 'i3', 'i03', 'ia3', 'ian3', 'iang3', 'iao3', 'ie3', 'in3', 'ing3', 'iong3', 'ir3', 'iu3', 'o3', 'ong3', 'ou3', 'u3', 'ua3', 'uai3', 'uan3', 'uang3', 'ui3', 'un3', 'uo3', 'v3', 'van3', 've3', 'vn3', 'E4', 'En4', 'a4', 'ai4', 'an4', 'ang4', 'ao4', 'e4', 'ei4', 'en4', 'eng4', 'er4', 'i4', 'i04', 'ia4', 'ian4', 'iang4', 'iao4', 'ie4', 'in4', 'ing4', 'iong4', 'ir4', 'iu4', 'o4', 'ong4', 'ou4', 'u4', 'ua4', 'uai4', 'uan4', 'uang4', 'ui4', 'un4', 'uo4', 'v4', 'van4', 've4', 'vn4', 'E5', 'En5', 'a5', 'ai5', 'an5', 'ang5', 'ao5', 'e5', 'ei5', 'en5', 'eng5', 'er5', 'i5', 'i05', 'ia5', 'ian5', 'iang5', 'iao5', 'ie5', 'in5', 'ing5', 'iong5', 'ir5', 'iu5', 'o5', 'ong5', 'ou5', 'u5', 'ua5', 'uai5', 'uan5', 'uang5', 'ui5', 'un5', 'uo5', 'v5', 'van5', 've5', 'vn5']

v_without_tone = ['E', 'En', 'a', 'ai', 'an', 'ang', 'ao', 'e', 'ei', 'en', 'eng', 'er', 'i', 'i0', 'ia', 'ian', 'iang', 'iao', 'ie', 'in', 'ing', 'iong', 'ir', 'iu', 'o', 'ong', 'ou', 'u', 'ua', 'uai', 'uan', 'uang', 'ui', 'un', 'uo', 'v', 'van', 've', 'vn']

symbols = [pad] + c + v + pu_symbols

