import tkinter as tk

import tkinter.messagebox


headfile = '''
--This mif file is made by PRV32_v0.0.2
--by Adancurusul
--if you have any questions
--you can email 1016867898@qq.com


DEPTH = 4096;
WIDTH = 32;
ADDRESS_RADIX = UNS;
DATA_RADIX = BIN;
CONTENT BEGIN
'''

def str_split(str):#将汇编代码分割成每一段并去除空格
    l1=[]
    #str = str.strip(';')
    print(str)

    l = str.lower().split(",")
    h=l[0].split()

    l.pop(0)
    f = h+l

    for i in range(0,len(f)):
        s = ''.join(f[i].split())
        l1.append(s)
    print(l1)
    s = l1[-1]
    if s[-1]==';':
        s = s[0:-1]
    l1.pop(-1)
    l1.append(s)
    return l1




def change16(wei,str1):
    q = int(str1,16)
    a  = str(bin(q))[2:].zfill(wei)
    #Zero = int(wei-len(a))
    #s = '0'*Zero+a
    return a
def change(wei,str1):
    a = str(bin(int(str1[-1])))[2:].zfill(wei)
    return a


'''
def str_split(str):#将汇编代码分割成每一段并去除空格
    l1=[]

    l = str.lower().split(",")
    h=l[0].split()

    l.pop(0)
    f = h+l
    for i in range(0,len(f)):
        s = ''.join(f[i].split())
        l1.append(s)

    return l1

'''





def ADDI(list):

    str = change16(12,list[3])+change(5,list[2])+'000'+change(5,list[1])+'0010011'
    return str
def SLTI(list):
    str = change16(12,list[3])+change(5,list[2])+'010'+change(5,list[1])+'0010011'
    return str
def SLTIU(list):
    str = change16(12,list[3])+change(5,list[2])+'011'+change(5,list[1])+'0010011'
    return str
def ANDI(list):
    str = change16(12,list[3])+change(5,list[2])+'111'+change(5,list[1])+'0010011'
    return str
def ORI(list):
    str = change16(12,list[3])+change(5,list[2])+'110'+change(5,list[1])+'0010011'
    return str
def XORI(list):
    str = change16(12,list[3])+change(5,list[2])+'100'+change(5,list[1])+'0010011'
    return str
def SLLI(list):
    str = '0000000'+change16(5,list[-1])+change(5,list[2])+'001'+change(5,list[1])+'0010011'
    return str
def SRLI(list):
    str = '0000000'+change16(5,list[-1])+change(5,list[2])+'101'+change(5,list[1])+'0010011'
    return str
def SRAI(list):
    str = '0100000'+change16(5,list[-1])+change(5,list[2])+'101'+change(5,list[1])+'0010011'
    return str
def ADD(list):
    str = '0000000'+change(5,list[-1])+change(5,list[2])+'101'+change(5,list[1])+'0110011'
    return str
def SUB(list):
    str = '0100000'+change(5,list[-1])+change(5,list[2])+'101'+change(5,list[1])+'0010011'
    return str
def SLL(list):
    str = '0000000'+change(5,list[-1])+change(5,list[2])+'001'+change(5,list[1])+'0010011'
    return str
def SLT(list):
    str = '0000000'+change(5,list[-1])+change(5,list[2])+'010'+change(5,list[1])+'0010011'
    return str
def SLTU(list):
    str = '0000000'+change(5,list[-1])+change(5,list[2])+'011'+change(5,list[1])+'0010011'
    return str
def XOR(list):
    str = '0000000'+change(5,list[-1])+change(5,list[2])+'100'+change(5,list[1])+'0010011'
    return str
def SRL(list):
    str = '0000000'+change(5,list[-1])+change(5,list[2])+'101'+change(5,list[1])+'0010011'
    return str
def SRA(list):
    str = '0100000'+change(5,list[-1])+change(5,list[2])+'101'+change(5,list[1])+'0010011'
    return str
def OR(list):
    str = '0000000'+change(5,list[-1])+change(5,list[2])+'110'+change(5,list[1])+'0010011'
    return str
def AND(list):
    str = '0000000'+change(5,list[-1])+change(5,list[2])+'111'+change(5,list[1])+'0010011'
    return str
def LUI(list):
    str = change16(20,list[-1])+change(5,list[1])+'0110111'
    return str
def AUIPC(list):
    str = change16(20,list[-1])+change(5,list[1])+'0010111'
    return str
def JAL(list):
    str = change16(20,list[-1])+change(5,list[1])+'1101111'
    return str
def JALR(list):
    str = change16(12,list[-1])+change(5,list[2])+'000'+change(5,list[1])+'1100111'
    return str
def BEQ(list):
    s = change16(12,list[-1])
    st1 = s[0:7]
    st2 = s[7:12]
    str = st1 +change(5,list[2])+change(5,list[1])+'000'+st2+'1100011'
    return str
def BNE(list):
    s = change16(12,list[-1])
    st1 = s[0:7]
    st2 = s[7:12]
    str = st1 +change(5,list[2])+change(5,list[1])+'001'+st2+'1100011'
    return str
def BLT(list):
    s = change16(12,list[-1])
    st1 = s[0:7]
    st2 = s[7:12]
    str = st1 +change(5,list[2])+change(5,list[1])+'100'+st2+'1100011'
    return str
def BGE(list):
    s = change16(12,list[-1])
    st1 = s[0:7]
    st2 = s[7:12]
    str = st1 +change(5,list[2])+change(5,list[1])+'101'+st2+'1100011'
    return str
def BLTU(list):
    s = change16(12,list[-1])
    st1 = s[0:7]
    st2 = s[7:12]
    str = st1 +change(5,list[2])+change(5,list[1])+'110'+st2+'1100011'

    return str
def BGEU(list):
    s = change16(12,list[-1])
    st1 = s[1:7]
    st2 = s[7:12]
    str = st1 +change(5,list[2])+change(5,list[1])+'111'+st2+'1100011'
    return str
def LW(list):
    l1 =list[2].partition("(")
    t = l1[-1][0:-1]
    str = change16(12,l1[0])+change(5,t)+'010'+change(5,list[1])+'0000011'
    return str
def LH(list):
    l1 =list[2].partition("(")
    t = l1[-1][0:-1]
    str = change16(12,l1[0])+change(5,t)+'001'+change(5,list[1])+'0000011'
    return str


def LB(list):
    l1 =list[2].partition("(")
    t = l1[-1][0:-1]
    str = change16(12,l1[0])+change(5,t)+'000'+change(5,list[1])+'0000011'
    return str
def LHU(list):
    l1 =list[2].partition("(")
    t = l1[-1][0:-1]
    str = change16(12,l1[0])+change(5,t)+'101'+change(5,list[1])+'0000011'
    return str
def LBU(list):
    l1 =list[2].partition("(")
    t = l1[-1][0:-1]
    str = change16(12,l1[0])+change(5,t)+'100'+change(5,list[1])+'0000011'
    return str
def SW(list):
    l1 =list[2].partition("(")
    t = l1[-1][0:-1]
    s = change16(12,l1[0])
    str =s[0:7] +change(5,list[1])+change(5,t)+'010'+s[7:12]+'0100011'
    return str
def SH(list):
    l1 =list[2].partition("(")
    t = l1[-1][0:-1]
    s = change16(12,l1[0])
    str =s[0:7] +change(5,list[1])+change(5,t)+'001'+s[7:12]+'0100011'
    return str
def SB(list):
    l1 =list[2].partition("(")
    t = l1[-1][0:-1]
    s = change16(12,l1[0])
    str =s[0:7] +change(5,list[1])+change(5,t)+'000'+s[7:12]+'0100011'
    return str
def CSRRW(list):
    str = change16(12,list[-2])+change(5,list[-1])+'001'+change(5,list[1])+'1110011'
    return str
def CSRRS(list):
    str = change16(12,list[-2])+change(5,list[-1])+'010'+change(5,list[1])+'1110011'
    return str
def CSRRC(list):
    str = change16(12,list[-2])+change(5,list[-1])+'011'+change(5,list[1])+'1110011'
    return str
def CSRRWI(list):
    str = change16(12,list[-2])+change16(5,list[-1])+'101'+change(5,list[1])+'1110011'
    return str
def CSRRCI(list):
    str = change16(12,list[-2])+change(5,list[-1])+'111'+change(5,list[1])+'1110011'
    return str
def CSRRSI(list):
    str = change16(12,list[-2])+change(5,list[-1])+'110'+change(5,list[1])+'1110011'
    return str
def FENCE_I():
    str = '00000000000000000001000000001111'
    return str
def ECALL():
    str = '00000000000000000000000001110011'
    return str
def EBREAK():
    str = '00000000000100000000000001110011'
    return str



#test = str_split("    addi   x6, x0   , 0xffc  ")
#test = str_split("sb x8,0x001(x6)")
#print(test)
#print(SB(test))
#print(len(SB(test)))





head = {
    'addi':ADDI,
    'lui':LUI,
    'auipc':AUIPC,
    'jal':JAL,
    'jalr':JALR,
    'beq':BEQ,
    'bne':BNE,
    'blt':BLT,
    'bge':BGE,
    'bltu':BLTU,
    'bgeu':BGEU,
    'lb':LB,
    'lh':LH,
    'lw':LW,
    'lbu':LBU,
    'lhu':LHU,
    'sb':SB,
    'sh':SH,
    'sw':SW,
    'slti':SLTI,
    'sltiu':SLTIU,
    'xori':XORI,
    'ori':ORI,
    'andi':ANDI,
    'slli':SLLI,
    'srli':SRLI,
    'srai':SRAI,
    'add':ADD,
    'sub':SUB,
    'sll':SLL,
    'slt':SLT,
    'sltu':SLTU,
    'xor':XOR,
    'srl':SRL,
    'sra':SRA,
    'or':OR,
    'and':AND,
    #'fence':FENCE,
    'fence.i':FENCE_I,
    'ecall':ECALL,
    'ebreak':EBREAK,
    'cssrrw':CSRRW,
    'csrrs':CSRRS,
    'csrrc':CSRRC,
    'csrrwi':CSRRWI,
    'csrrsi':CSRRSI,
    'csrrci':CSRRCI,

}










window = tk.Tk()
window.title('RISC-V 汇编器 V0.0.1')
window.geometry('400x400')
window.resizable()

t = tk.Text(window)

#l = tk.Label(window, text='      ', bg='green')
counter = 0


def Save():
    global yt,u0,x
    yt=tk.Tk() #创建Tk对象
    yt.title("文件名") #设置窗口标题
    yt.geometry("300x300") #设置窗口尺寸
    l1=tk.Label(yt,text="文件名字")

    l1.pack()
    #指定包管理器放置组件
    u0=tk.Entry(yt)

    u0.pack()



    tk.Button(yt,text="确定",command=S_name).pack() #command绑定获取文本框内容方法
    yt.mainloop()

def S_name():

    x = u0.get()
    l = tk.Label(yt, text='保存名字为：', justify='left').pack(side='left')
    l = tk.Label(yt, text=x, justify='left').pack(side='left')


    with open('save_location.txt','r') as b_file:    #d:/文本文件/1.txt

          k = b_file.read()
          m = k+'/'+x+'.txt'
    with open(m,'w+') as write_file:
          m= t.get(0.0, 'end')
          write_file.write(m)




def Select():
    global u,n,ytm
    n=0
    ytm=tk.Tk() #创建Tk对象
    ytm.title("保存位置") #设置窗口标题
    ytm.geometry("300x150") #设置窗口尺寸
    l1=tk.Label(ytm,text="保存位置")
    l4= tk.Label(ytm, text='保存格式eg:C:/Users/adan/Desktop')
    l4.pack()
    l1.pack()
    #指定包管理器放置组件
    u=tk.Entry(ytm)

    u.pack()


    tk.Button(ytm,text="确定",command=S_location).pack() #command绑定获取文本框内容方法
    ytm.mainloop()

def S_location():

    global SAVE_L,n,ytm


    #m = tkinter.messagebox.askyesno(title='渣男', message='确定保存选择位置？')
    SAVE_L = u.get()
    l = tk.Label(ytm, text='保存位置为：', justify='left').pack(side='left')
    l = tk.Label(ytm, text=SAVE_L, justify='left').pack(side='left')
    with open('save_location.txt','w+') as save_l:
            save_l.write(SAVE_L)
    n+=1

def Save_a():
    global yt,u0,x
    yt=tk.Tk() #创建Tk对象
    yt.title("文件名") #设置窗口标题
    yt.geometry("300x300") #设置窗口尺寸
    l1=tk.Label(yt,text="文件名字")

    l1.pack()
    #指定包管理器放置组件
    u0=tk.Entry(yt)

    u0.pack()



    tk.Button(yt,text="确定",command=S_name_a).pack() #command绑定获取文本框内容方法
    yt.mainloop()

def S_name_a():


    x = u0.get()

    l = tk.Label(yt, text='保存名字为：', justify='left').pack(side='left')
    l = tk.Label(yt, text=x, justify='left').pack(side='left')


    with open('save_location.txt','r') as b_file:    #d:/文本文件/1.txt

          k = b_file.read()
          m = k+'/'+x+'.txt'
    pr = t.get(0.0, 'end')
    with open('prepare.txt','w+') as pre:
        pre.write(pr)
    with open('prepare.txt','r') as chan:
        with open(m,'w+') as b:
            for line in chan:
                l1=str_split(line)
                cjf = head[l1[0]](l1)
                b.write(cjf)
                b.write('\n')
    l = tk.Label(yt, text='保存完毕', justify='left').pack(side='left')

    '''
    with open(m,'w+') as write_file:
          with open('bi.txt','r')as re:
              for line in re:
                with open('')




                l = tk.Label(win, text=line).pack(side='top')
                m= t.get(0.0, 'end')
                write_file.write(m)
    '''


def save_as_b():
    Save_a()




def save_as_mif():
    with open('save_location.txt','r') as b_file:    #d:/文本文件/1.txt

          k = b_file.read()




    m = ut.get()
    m = k+'/'+m+'.mif'
    l = tk.Label(yt_p, text='保存名字为：', justify='left').pack(side='left')
    l = tk.Label(yt_p, text=m, justify='left').pack(side='left')

    A2B()
    with open('bi.txt','r')as b_r:

        with open(m, 'w') as mif:
            mif.writelines(headfile)
            i = 0
            for line in b_r:
                str0 = str(i)+' : '
                str1=line[0:-2]
                str2 =';\n'
                '''
                mif.writelines(str(i))
                mif.writelines(' : ')
                mif.writelines(line)
               '''
                mif.write(str0)
                mif.write(str1)
                mif.write(str2)

                i+=1
            if i<4095:
                s = '['+str(i)+'..'+'4095'+']'+' : '+'0'*32+';\n'
                mif.write(s)

            mif.write('END;')
    l = tk.Label(yt_p, text='完成', justify='left').pack(side='left')

def Save_mif():
    global yt_p,ut,x
    yt_p=tk.Tk() #创建Tk对象
    yt_p.title("文件名") #设置窗口标题
    yt_p.geometry("300x300") #设置窗口尺寸
    l1=tk.Label(yt_p,text="文件名字")

    l1.pack()
    #指定包管理器放置组件
    ut=tk.Entry(yt_p)

    ut.pack()



    tk.Button(yt_p,text="确定",command=save_as_mif).pack() #command绑定获取文本框内容方法
    yt_p.mainloop()











def fun():
    # 获取文本内内容
    win = tk.Tk()
    win.title('二进制代码')
    win.geometry('400x400')
    A2B()
    with open('bi.txt','r')as re:
        for line in re:


            l = tk.Label(win, text=line).pack(side='top')




def quit():
    a = tkinter.messagebox.askquestion(title='警告', message='退出后代码将不被保存')
    if a == 'yes':
        window.quit()
def hit_me():
     #tk.messagebox.showinfo(title='Hi', message='你好！')              # 提示信息对话窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    # tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    #print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    q = tkinter.messagebox.askyesno(title='no', message='叫你别点，不给你用了')     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
    if q =='True':
        window.quit()
    else:
        window.quit()


def do_job():
    global counter

    counter += 1

def A2B():
    pr = t.get(0.0, 'end')
    with open('prepare.txt','w+') as pre:
        pre.write(pr)
    with open('prepare.txt','r') as chan:
        with open('bi.txt','w+') as b:
            for line in chan:
                l1=str_split(line)
                cjf = head[l1[0]](l1)
                b.write(cjf)
                b.write('\n')





menubar = tk.Menu(window)
#创建一个File菜单项
filemenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为File，放在菜单栏中
menubar.add_cascade(label='文件', menu=filemenu)
# 在File中加入New、Open、Save等小菜单，每一个小菜单对应命令操作。
filemenu.add_command(label='新建', command=do_job)
filemenu.add_command(label='打开', command=do_job)
filemenu.add_command(label='选择保存位置', command=Select)

filemenu.add_command(label='保存', command=Save)

filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='关闭', command=quit) # 用tkinter里面自带的quit()函数
# 创建一个Edit菜单项
editmenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名
menubar.add_cascade(label='编辑', menu=editmenu)
# 同样的在 编辑中加入一些功能单元，点击这些单元, 就会触发相应功能
editmenu.add_command(label='转化为二进制', command=do_job)
editmenu.add_command(label='转化为二进制并保存', command=save_as_b)
editmenu.add_command(label='转化为mif并保存', command=Save_mif)

editmenu.add_separator()    # 添加一条分隔线

editmenu.add_command(label='待开发', command=do_job)

# 创建第二级菜单
submenu = tk.Menu(filemenu) # File上创建一个空的菜单
filemenu.add_cascade(label='Import(待开发)', menu=submenu, underline=0) # 给放入的菜单submenu命名为Import

submenu.add_command(label='nothing', command=do_job)   # 创建第三级菜单命令

# 创建菜单menubar
window.config(menu=menubar)
tk.Button(window, text='不要按这个', bg='green', font=('Arial', 14), command=hit_me).pack()#messagebox
t.pack()
bt = tk.Button(window, text='浏览转换后的代码', command=fun).pack()

window.mainloop()



