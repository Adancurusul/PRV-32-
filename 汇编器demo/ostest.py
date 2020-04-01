import os
import re

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


def check_check( DD):
    length = len(DD)  # 求长度

    # 创建一个list，将传入的str的每两个数合在一起，再求和
    list1 = []
    if (length % 2 == 1):  # 如果str长度为单数，则抛出错误
        print('数据长度有误')
    else:
        for i in range(0, length, 2):  # range（开始，结束-1，每次加多少）  这里即0——length-1  每次循环i+2
            hex_digit = DD[i:i + 2]  # 将传入的str的每两个数合在一起
            list1.append('0x' + hex_digit)  # 再每个字符前+0x  但是它仍然是字符，但更便于下面通过int(list1[i], 16)转换成16进制
    print(list1)

    sum = 0
    for i in range(int(length / 2)):  # 求和
        sum = int(list1[i], 16) + sum  # int(list1[i], 16)将16进制转换成10进制 int类型
    sum = sum % 256
    sum = 256 - sum

    # print('校验码: '+hex(sum))   #将sum和结果转换成16进制  hex(sum)
    return dec2hex(sum)
def do_gcc(st):

    #st = fname[0]
    #st = r'C:\Users\user\Desktop\c\test.c'
    sts = st[:-1]+"s"
    sto = st[:-1]+"o"
    print(sts)
    print(st)
    pattern = r'\w+'

    m = re.findall(pattern,st)
    l = len(m[-1]+m[-2])+1
    st1 = st[:-6]
    st2 = st[-6:]
    print(st2)
    print(m)
    print(l)
    print(st1)
    cmds1="riscv-nuclei-elf-gcc -march=rv32i  -mabi=ilp32  -S "+st
    cmds2="riscv-nuclei-elf-gcc -march=rv32i  -mabi=ilp32  -c "+sts
    cmds3 = "riscv-nuclei-elf-objdump  -d "+sto
    os.system("cd "+st1+'&&'+cmds1+'&&'+"cmds2")
    f = os.popen("cd "+st1+'&&'+cmds3)

    #f = os.popen(r"riscv-nuclei-elf-objdump  -d "+sto, "r")
    d = f.read()
    afile = st1+"t.txt"
    hex_file = st1 +st2[:-1]+'hex'
    print(d)
    with open(afile,"w+") as a:
        a.write(d)
    print("*"*10)
    print(type(d))
    print(d)
    f.close()
    p_h = r'^\s+(\w+):\s+(\w+)\s+(.+)'



    with open(afile,"r") as a:
        with open(hex_file,"w+") as b:
            first_to_write = ':020000040800F2\n'
            b.write(first_to_write)
            main_begin = ':0400000508000000ef' + '\n'  # 本汇编器出来的代码默认0000开始
            #sl.write(self.main_begin)
            last_to_write = ':00000001FF' + '\n'  # 文件结束
            #sl.write(self.last_to_write)

            for line in a:
                res = re.match(p_h,line)
                try:

                    pa = res.groups()
                    loc = pa[0].zfill(4)
                    cod = pa[1]
                    #cod = cod.upper()
                    str_hex = '04'+loc+'00'+cod
                    str_check = check_check(str_hex)
                    #print('asdfasdgasdgsdgasdgasdasdg')
                    str_hex = ':'+str_hex+str_check
                    str_hex = str_hex.upper()

                    #print(str_hex)
                    b.write(str_hex+'\n')
                    #print(loc)
                    #print(pa[1])
                except:
                    print('not')
            b.write(main_begin)
            b.write(last_to_write)





do_gcc()

