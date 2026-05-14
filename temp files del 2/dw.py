import time as tt
import pyautogui as pp



def season1():
    print('executing temp clear')
    tt.sleep(1)
    pp.hotkey('super', 'r')
    tt.sleep(0.5)
    tt.sleep(1)
    pp.typewrite('temp')
    pp.hotkey('enter')
    print('setting up....')
    tt.sleep(1)
    print('running clear no jutsu.exe')
    ippo()

def ippo():

    while True:
        a = pp.locateOnScreen('b.png')
        if a != None:
            pp.click(a)
            print('clicked')
            break
        else:
            print('failed b')
            tt.sleep(2)

    tt.sleep(0.5)
    pp.click(489,182)
    pp.hotkey('shift','end')
    pp.hotkey('delete')
    tt.sleep(2)
    
    while True:
        b = pp.locateOnScreen('a.png',confidence=0.7)
        if b != None:
            pp.click(b)
            print('Tickied the box')
            tt.sleep(0.5)
            c = pp.locateOnScreen('c.png',confidence=0.7)
            pp.click(c)
            print('done')
            tt.sleep(1)
            break
        else:
            print('not present')
            tt.sleep(2)
            break
    
    while True:
        d = pp.locateOnScreen('d.png')
        if d != None:
            pp.click(d)
            print('done')
            break
        else:
            print('failed')
            tt.sleep(2)

    while True:
        e = pp.locateOnScreen('e.png')
        if e != None:
            pp.click(e)
            print('done')
            break
        else:
            print('failed')
            tt.sleep(2)
    dog()
    

def dog():
    print('..')
    print('......')
    print('.................')
    print('executing second procedure')
    tt.sleep(0.5)
    print("started")
    season2()

def ippoo():

    while True:
        a = pp.locateOnScreen('b.png')
        if a != None:
            pp.click(a)
            print('clicked')
            break
        else:
            print('failed b')
            tt.sleep(2)

    tt.sleep(0.5)
    pp.click(489,182)
    pp.hotkey('shift','end')
    pp.hotkey('delete')
    tt.sleep(2)
    
    while True:
        b = pp.locateOnScreen('a.png',confidence=0.7)
        if b != None:
            pp.click(b)
            print('Tickied the box')
            tt.sleep(0.5)
            c = pp.locateOnScreen('c.png',confidence=0.7)
            pp.click(c)
            print('done')
            tt.sleep(1)
            break
        else:
            print('not present')
            tt.sleep(2)
            break
    
    while True:
        d = pp.locateOnScreen('d.png')
        if d != None:
            pp.click(d)
            print('done')
            break
        else:
            print('failed')
            tt.sleep(2)

    while True:
        e = pp.locateOnScreen('e.png')
        if e != None:
            pp.click(e)
            print('done')
            break
        else:
            print('failed')
            tt.sleep(2)



def season2():
    print('executing temp clear season 2')
    tt.sleep(1)

    pp.hotkey('super', 'r')
    tt.sleep(0.5)

    tt.sleep(1)
    pp.typewrite('%temp%')
    pp.hotkey('enter')
    print('setting up....')
    tt.sleep(1)
    print('running clear no jutsu.exe')
    ippoo()

  

season1()