import connectwifi
from machine import Pin, I2C
import time
import network
import ssd1306
import framebuf
import _thread

connectwifi.connect('kali', 'adaM3131')
iic = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
# oled = ssd1306.SSD1306_I2C(128,64, i2c)
oled = ssd1306.SSD1306_I2C(width=128, height=64, i2c=iic, addr=0x3c, external_vcc=False)
oled.text('connected wifi', 0, 0)
oled.show()
time.sleep(0.5)
rst = Pin(22, Pin.OUT)
beep = Pin(25, Pin.OUT)
beep.value(1)
rst.value(1)


def pix(x, y, t):
    for i in range(0, t):
        oled.pixel(x + 2 * i, y, 1)
        oled.pixel(x + 2 * i + 1, y, 1)
        oled.pixel(x + 2 * i, y + 1, 1)
        oled.pixel(x + 2 * i + 1, y + 1, 1)
        oled.show()

        time.sleep(0.1)


def reset_jttag():
    beep.value(0)
    rst.value(0)
    time.sleep(0.5)
    beep.value(1)


def get_hex():
    pix(0, 20, 15)
    oled.text('get hex from PC', 0, 25)
    oled.show()


def downloading():
    time.sleep(0.5)
    pix(0, 43, 10)
    oled.text('no hex found', 0, 35)
    oled.show()
    pix(0, 43, 10)
    oled.text('prepare to rst', 0, 48)
    reset_jttag()

    oled.show()
    time.sleep(1)
    # oled.fill(0)
    # oled.show()


def msg():
    oled.fill(0)
    oled.show()
    oled.text('msg from board', 0, 0)
    oled.hline(0, 8, 120, 1)
    oled.show()
    oled.text('PVS332', 0, 10)
    oled.show()
    print('PVS332')
    time.sleep(0.5)
    oled.text('HELLO WORLD!', 0, 17)
    oled.show()
    print('HELLO WORLD!')
    oled.text('core prv332', 0, 24)
    oled.show()
    time.sleep(0.5)
    print('core prv332')
    oled.text('ocram test...', 0, 35)
    oled.show()
    time.sleep(0.5)
    print('ocram test...')
    oled.text('ocram ok', 0, 48)
    oled.show()
    time.sleep(0.5)
    print('ocram ok')


def show_str():
    # oled.fill(0)
    oled.text('wait for hex', 0, 8)
    oled.show()
    get_hex()
    downloading()
    msg()

    # pix(0,43,10)
    # oled.text('finished',0,48)
    # oled.show()
    # time.sleep(1)
    # oled.fill(0)


def msg2():
    oled.fill(0)
    oled.show()
    oled.text('msg from board', 0, 0)
    oled.hline(0, 8, 120, 1)
    oled.show()
    oled.text('PVS332', 0, 10)
    print('PVS332')
    oled.show()
    time.sleep(0.5)
    oled.text('HELLO WORLD!', 0, 17)
    oled.show()

    print('HELLO WORLD!')
    oled.text('core prv332', 0, 24)
    time.sleep(0.5)
    oled.show()
    print('core prv332')
    oled.text('ocram test...', 0, 35)
    oled.show()
    time.sleep(0.5)
    print('ocram test...')
    oled.text('ocram ok', 0, 48)
    oled.show()
    time.sleep(0.5)
    print('ocram ok')


def rst_thread():
    while 1:

        k = input('press 0 to reset:')
        if k == 0:
            print('begin to reset')
            reset_jttag()
            # beep.value(0)
            # rst.value(1)
            # time.sleep(0.5)
            # beep.value(1)

            msg2()


_thread.start_new_thread(show_str, ())
_thread.start_new_thread(rst_thread, ())