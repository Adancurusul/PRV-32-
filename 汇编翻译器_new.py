#this is the first test of the prv32
#author Adancurusul
#
import re
import array
import numpy


#str00 = 'addi x  7,x0,0x0008;asdfja;;21,,,,'


 



class split_str:#can return as dict like{'opcode': 'addi', 'key': 'x7,x0,0x0008'}
    #正则表达式
    parttern_code = r'^\s*(?P<opcode>\w+)\b\s+(?P<key>.+)(;|#)?'#匹配汇编并拆分
    def __init__(self,str0):
        self.st = ''.join(str0.split())
        self.str0 = str0.split(';')[0]#分出代码区和注释区
        #print(self.str0)
        self.comma_count()
        self.code_split()
        self.dict_of_ass=self.code_split()
        self.change_to()

    def change_to(self):
            if(self.dict_of_ass):
                self.dict_of_ass['key'] =''.join(self.dict_of_ass['key'].split())
                self.opcode = self.dict_of_ass['opcode']
                self.key = self.dict_of_ass['key'].split(',')
            else:
                print('no')#去除空格
    def comma_count(self):#找到逗号的个数个数
        self.count = self.str0.count(',')
        print(self.count)
    def code_split(self):
        self.str0 = self.str0.lower()
        self.result = re.match(self.parttern_code,self.str0)
        if (self.result):
            self.opcode = self.result.group('opcode')
            self.str_key = self.result.group('key')
            self.dict ={'opcode':self.opcode,'key':self.str_key}#创建字典保存分割后的字符串

            return self.dict

        else :
            return None
'''
该类的使用方法
str = 'addi x  7,x0,0x0008;asdfja;;21,,,,'
l = split_str(str)
print(l.dict_of_ass)#{'opcode': 'addi', 'key': 'x7,x0,0x0008'}
'''

class change_into_bin(split_str):#直接将每行完成转化
    def __init__(self,str0):#继承split的属性
        super().__init__(str0)
        self.list = []
        self.list.append(self.opcode)
        self.list = self.list+self.key
        self.change_and_return()

    def change16(self,wei,str1):#将16进制数转化为二进制
        print(str1)
        q = int(str1,16)
        return str(bin(q))[2:].zfill(wei)
        #Zero = int(wei-len(a))
        #s = '0'*Zero+a

    def change(self,wei,str1):#将寄存器值转化出来
        return str(bin(int(str1[-1])))[2:].zfill(wei)
    '''
    def change16(self,wei,str1):
        q = int(str1,16)
        a  = str(bin(q))[2:].zfill(wei)
        #Zero = int(wei-len(a))
        #s = '0'*Zero+a
        return a
    def change(self,wei,str1):
        a = str(bin(int(str1[-1])))[2:].zfill(wei)
        return a
    '''
    def change_and_return(self):

        head = {#这是一个操作码的指向字典来模拟switch语句
            'addi':self.ADDI,
            'lui':self.LUI,
            'auipc':self.AUIPC,
            'jal':self.JAL,
            'jalr':self.JALR,
            'beq':self.BEQ,
            'bne':self.BNE,
            'blt':self.BLT,
            'bge':self.BGE,
            'bltu':self.BLTU,
            'bgeu':self.BGEU,
            'lb':self.LB,
            'lh':self.LH,
            'lw':self.LW,
            'lbu':self.LBU,
            'lhu':self.LHU,
            'sb':self.SB,
            'sh':self.SH,
            'sw':self.SW,
            'slti':self.SLTI,
            'sltiu':self.SLTIU,
            'xori':self.XORI,
            'ori':self.ORI,
            'andi':self.ANDI,
            'slli':self.SLLI,
            'srli':self.SRLI,
            'srai':self.SRAI,
            'add':self.ADD,
            'sub':self.SUB,
            'sll':self.SLL,
            'slt':self.SLT,
            'sltu':self.SLTU,
            'xor':self.XOR,
            'srl':self.SRL,
            'sra':self.SRA,
            'or':self.OR,
            'and':self.AND,
            #'fence':FENCE,
            'fence.i':self.FENCE_I,
            'ecall':self.ECALL,
            'ebreak':self.EBREAK,
            'cssrrw':self.CSRRW,
            'csrrs':self.CSRRS,
            'csrrc':self.CSRRC,
            'csrrwi':self.CSRRWI,
            'csrrsi':self.CSRRSI,
            'csrrci':self.CSRRCI,

        }
        self.after_change_str = head[self.list[0]]()
        

        print(self.after_change_str)
        




    def ADDI(self):

        st = self.change16(12,self.list[3])+self.change(5,self.list[2])+'000'+self.change(5,self.list[1])+'0010011'
        return st
    def SLTI(self):
        st = self.change16(12,self.list[3])+self.change(5,self.list[2])+'010'+self.change(5,self.list[1])+'0010011'
        return st
    def SLTIU(self):
        st = self.change16(12,self.list[3])+self.change(5,self.list[2])+'011'+self.change(5,self.list[1])+'0010011'
        return st
    def ANDI(self):
        st = self.change16(12,self.list[3])+self.change(5,self.list[2])+'111'+self.change(5,self.list[1])+'0010011'
        return st
    def ORI(self):
        st = self.change16(12,self.list[3])+self.change(5,self.list[2])+'110'+self.change(5,self.list[1])+'0010011'
        return st
    def XORI(self):
        st = self.change16(12,self.list[3])+self.change(5,self.list[2])+'100'+self.change(5,self.list[1])+'0010011'
        return st
    def SLLI(self):
        st = '0000000'+self.change16(5,self.list[-1])+self.change(5,self.list[2])+'001'+self.change(5,self.list[1])+'0010011'
        return st
    def SRLI(self):
        st = '0000000'+self.change16(5,self.list[-1])+self.change(5,self.list[2])+'101'+self.change(5,self.list[1])+'0010011'
        return st
    def SRAI(self):
        st = '0100000'+self.change16(5,self.list[-1])+self.change(5,self.list[2])+'101'+self.change(5,self.list[1])+'0010011'
        return st
    def ADD(self):
        st = '0000000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'000'+self.change(5,self.list[1])+'0110011'
        return st
    def SUB(self):
        st = '0100000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'000'+self.change(5,self.list[1])+'0110011'
        return st
    def SLL(self):
        st = '0000000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'001'+self.change(5,self.list[1])+'0110011'
        return st
    def SLT(self):
        st = '0000000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'010'+self.change(5,self.list[1])+'0110011'
        return st
    def SLTU(self):
        st = '0000000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'011'+self.change(5,self.list[1])+'0110011'
        return st
    def XOR(self):
        st = '0000000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'100'+self.change(5,self.list[1])+'0110011'
        return st
    def SRL(self):
        st = '0000000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'101'+self.change(5,self.list[1])+'0110011'
        return st
    def SRA(self):
        st= '0100000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'101'+self.change(5,self.list[1])+'0110011'
        return st
    def OR(self):
        st = '0000000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'110'+self.change(5,self.list[1])+'0110011'
        return st
    def AND(self):
        st = '0000000'+self.change(5,self.list[-1])+self.change(5,self.list[2])+'111'+self.change(5,self.list[1])+'0110011'
        return st
    def LUI(self):
        st = self.change16(20,self.list[-1])+self.change(5,self.list[1])+'0110111'
        return st
    def AUIPC(self):
        st = self.change16(20,self.list[-1])+self.change(5,self.list[1])+'0010111'
        return st
    def JAL(self):
        st = self.change16(20,self.list[-1])+self.change(5,self.list[1])+'1101111'
        return st
    def JALR(self):
        st = self.change16(12,self.list[-1])+self.change(5,self.list[2])+'000'+self.change(5,self.list[1])+'1100111'
        return st
    def BEQ(self):
        s = self.change16(12,self.list[-1])
        st1 = s[0:7]
        st2 = s[7:12]
        st = st1 +self.change(5,self.list[2])+self.change(5,self.list[1])+'000'+st2+'1100011'
        return st
    def BNE(self):
        s = self.change16(12,self.list[-1])
        st1 = s[0:7]
        st2 = s[7:12]
        st = st1 +self.change(5,self.list[2])+self.change(5,self.list[1])+'001'+st2+'1100011'
        return st
    def BLT(self):
        s = self.change16(12,self.list[-1])
        st1 = s[0:7]
        st2 = s[7:12]
        st= st1 +self.change(5,self.list[2])+self.change(5,self.list[1])+'100'+st2+'1100011'
        return st
    def BGE(self):
        s = self.change16(12,self.list[-1])
        st1 = s[0:7]
        st2 = s[7:12]
        st = st1 +self.change(5,self.list[2])+self.change(5,self.list[1])+'101'+st2+'1100011'
        return st
    def BLTU(self):
        s = self.change16(12,self.list[-1])
        st1 = s[0:7]
        st2 = s[7:12]
        st = st1 +self.change(5,self.list[2])+self.change(5,self.list[1])+'110'+st2+'1100011'

        return st
    def BGEU(self):
        s = self.change16(12,self.list[-1])
        st1 = s[1:7]
        st2 = s[7:12]
        st = st1 +self.change(5,self.list[2])+self.change(5,self.list[1])+'111'+st2+'1100011'
        return st
    def LW(self):
        l1 =self.list[2].partition("(")
        t = l1[-1][0:-1]
        st = self.change16(12,l1[0])+self.change(5,t)+'010'+self.change(5,self.list[1])+'0000011'
        return st
    def LH(self):
        l1 =self.list[2].partition("(")
        t = l1[-1][0:-1]
        str = self.change16(12,l1[0])+self.change(5,t)+'001'+self.change(5,self.list[1])+'0000011'
        return str


    def LB(self):
        l1 =self.list[2].partition("(")
        t = l1[-1][0:-1]
        st = self.change16(12,l1[0])+self.change(5,t)+'000'+self.change(5,self.list[1])+'0000011'
        return st
    def LHU(self):
        l1 =self.list[2].partition("(")
        t = l1[-1][0:-1]
        st = self.change16(12,l1[0])+self.change(5,t)+'101'+self.change(5,self.list[1])+'0000011'
        return st
    def LBU(self):
        l1 =self.list[2].partition("(")
        t = l1[-1][0:-1]
        str = self.change16(12,l1[0])+self.change(5,t)+'100'+self.change(5,self.list[1])+'0000011'
        return str
    def SW(self):
        l1 =self.list[2].partition("(")
        t = l1[-1][0:-1]
        s = self.change16(12,l1[0])
        st =s[0:7] +self.change(5,self.list[1])+self.change(5,t)+'010'+s[7:12]+'0100011'
        return st
    def SH(self):
        l1 =self.list[2].partition("(")
        t = l1[-1][0:-1]
        s = self.change16(12,l1[0])
        st =s[0:7] +self.change(5,self.list[1])+self.change(5,t)+'001'+s[7:12]+'0100011'
        return st
    def SB(self):
        l1 =self.list[2].partition("(")
        t = l1[-1][0:-1]
        s = self.change16(12,l1[0])
        st =s[0:7] +self.change(5,self.list[1])+self.change(5,t)+'000'+s[7:12]+'0100011'
        return st
    def CSRRW(self):
        st = self.change16(12,self.list[-2])+self.change(5,self.list[-1])+'001'+self.change(5,self.list[1])+'1110011'
        return st
    def CSRRS(self):
        st = self.change16(12,self.list[-2])+self.change(5,self.list[-1])+'010'+self.change(5,self.list[1])+'1110011'
        return st
    def CSRRC(self):
        st = self.change16(12,self.list[-2])+self.change(5,self.list[-1])+'011'+self.change(5,self.list[1])+'1110011'
        return st
    def CSRRWI(self):
        st = self.change16(12,self.list[-2])+self.change16(5,self.list[-1])+'101'+self.change(5,self.list[1])+'1110011'
        return st
    def CSRRCI(self):
        st = self.change16(12,self.list[-2])+self.change(5,self.list[-1])+'111'+self.change(5,self.list[1])+'1110011'
        return st
    def CSRRSI(self):
        st = self.change16(12,self.list[-2])+self.change(5,self.list[-1])+'110'+self.change(5,self.list[1])+'1110011'
        return st
    def FENCE_I(self):
        st = '00000000000000000001000000001111'
        return st
    def ECALL(self):
        st = '00000000000000000000000001110011'
        return st
    def EBREAK(self):
        st = '00000000000100000000000001110011'
        return st

'''
类用法：
l = change_into_bin(str00)
print(l.after_change_str)
'''



class check_label_or_opcode():#check if it is label or opcode 
    parttern_label = r'.section\s+'
    parttern_section = r''
    parttern_data = r''
    parttern_text = r''

    def __init__(self,str0):
        self.str0 = str0

    def if_label(self):
        re.match(self.parttern_label,self.str0)
    def if_section(self):
        se = re.match(self.parttern_section,self.str0)
        #if (se):



    


'''
主要扫描方式：
类2遍扫描
先给定义的量以及函数分配位置
利用字典查找
'''




class do_scan():#扫描类
    label_times =0#label出现次数
    defin_times = 0#定义出现次数
    label_lines = 0  #每个label下行数
    data_lines = 0#data的长度
    data_scan =0  #地址标志位
    line_of_file = 0

    parttern_label = r''#检测是不是label
    parttern_section = r''#检测是不是函数

    parttern_data = r''# 检测是不是data
    parttern_text = r''
    parttern_define=r''

    
    def __init__(self,filename):#得到文件名对其每行进行遍历
        self.filename = filename
        with open(self.filename,'w+') as file1:#打开文件
            scan_first()    #做第一次扫描
    
    def scan_first(self):#第一次扫描函数（扫描主函数）
        for line in file1:
            line_of_file +=1
            self.str0 = line
            self.if_label()
            if data_scan ==1 :
                self.scan_data()
            elif label_scan == 1:
                self.label_store()

    def scan_data(self):#bootloader写求不出来，先鸽着
        pass

    
    def label_store(self):
        pass

        
        
        

    def if_label(self):
        self.my_label = 'label'
        self.label_check = re.match(self.parttern_label,self.str0)
        if (self.label_check):
            self.data_or_text = self.label_check.group(1)
            if (self.data_or_text=='.data'):
                data_scan = 1
            

            elif (self.data_or_text == '.text'):#guguguugugugugugguguguguguguugu
                pass


            #self.give_location(self.label_check.group(0),self.my_label)

            return self.label_check.group(0)
    def if_define(self):
        self.mydefine = 'define'
        self.define_check = re.match(self.parttern_define,self.str0)
        if (self.define_check):
            self.give_location(self.define_check.group(0),"define")
            return self.define_check.group(0)
    



   
   


    def give_location(self,str,type):
        if type =='label':
            pass

    def write_hex(self):
        pass






def bin2hex(string_num):
    base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
    num = int(string_num,2)
    #num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

    


def change_file():
    with open('ass.txt','r+') as assfile:
        with open('bin.txt','w+') as binfile:
            for line in assfile:
                changed = change_into_bin(line)
                chan = changed.after_change_str+'\n'
                binfile.write(chan)

            
change_file()










#class_change = change_into_bin(str00)


#print(class_change.after_change_str)







