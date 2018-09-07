# main.py -- put your code here!
# main.py -- put your code here!
# 2 DIGITS BINARY ADD.
from pyb import Pin
B1Value = 0
B2Value = 0
B1ValueS = 0
B2ValueS = 0
addBtnValue = 0
isEqualPressed = 0
button1 = Pin('X1', pyb.Pin.IN)
button2 = Pin('X2', pyb.Pin.IN)
AddBtn = Pin('X3', pyb.Pin.IN)
equalBtn = Pin('X4', pyb.Pin.IN)
LEDBTN1 = Pin('X5', pyb.Pin.OUT_PP)
LEDBTN2 = Pin('X6', pyb.Pin.OUT_PP)
CLED = Pin('X10', pyb.Pin.OUT_PP)
AddLEDBTN = Pin('X7', pyb.Pin.OUT_PP)
R1LEDBTN3 = Pin('X8', pyb.Pin.OUT_PP)
R2LEDBTN4 = Pin('X9', pyb.Pin.OUT_PP)
while True:
    B1 = button1.value()
    B2 = button2.value()
    ABtn = AddBtn.value()
    RBtn = equalBtn.value()
    if B1:
        if B1Value == 0:
            LEDBTN1.high()
            B1Value = 1
            pyb.delay(25)
        elif B1Value == 1:
            LEDBTN1.low()
            B1Value = 0
    elif B2:
        if B2Value == 0:
            LEDBTN2.high()
            B2Value = 1
            pyb.delay(25)
        else:
            B2Value = 0
            LEDBTN2.low()
    elif ABtn:
        if addBtnValue == 0:
            AddLEDBTN.high()
            addBtnValue = 1
            B1ValueS = B1Value
            B2ValueS = B2Value
            LEDBTN1.low()
            LEDBTN2.low()
            pyb.delay(25)
            B1Value = 0
            B2Value = 0
            pyb.delay(250)
        else:
            pyb.delay(170)
            LEDBTN1.low()
            LEDBTN2.low()
            AddLEDBTN.low()
            R1LEDBTN3.low()
            R2LEDBTN4.low()
            CLED.low()
            B1ValueS = 0
            B2ValueS = 0
            B1Value = 0
            B2Value = 0
            addBtnValue = 0
    elif RBtn:
        carry1 = 0
        if B1ValueS != 0 or B1Value != 0:
            if B1ValueS == 1 and B1Value == 1:
                if B2ValueS == 1 or B2Value == 1:
                    R2LEDBTN4.low()
                    CLED.high()
                    carry1 = 1
                    pyb.delay(100)
                else:
                    R2LEDBTN4.high()
                    R1LEDBTN3.low()
                    pyb.delay(100)
            elif B1ValueS == 1 or B1Value == 1:
                R1LEDBTN3.high()
        pyb.delay(200)
        if B2ValueS != 0 or B2Value != 0:
            if B2ValueS == 1 and B2Value == 1:
                    R2LEDBTN4.low()
                    CLED.high()
            elif B2ValueS == 1 and B2Value == 1 and carry1 == 1:
                    R2LEDBTN4.high()
                    CLED.high()
            elif B2ValueS == 1 or B2Value == 1 and carry1 != 1:
                    R2LEDBTN4.low()
            else:
                    R2LEDBTN4.low()
