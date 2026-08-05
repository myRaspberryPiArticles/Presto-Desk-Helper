from presto import Presto
from touch import Button
import time

presto = Presto()
display = presto.display

TEXT_BLUE = display.create_pen(34, 36, 91)
LIGHT_BLUE = display.create_pen(234, 248, 251)
BLACK = display.create_pen(0, 0, 0)
CLICK = display.create_pen(200, 200, 200)

touch = presto.touch

btn1 = Button(15, 80, 30, 30)
btn4 = Button(15, 120, 40, 20)
btn7 = Button(15, 160, 40, 20)
btn2 = Button(55, 80, 40, 20)
btn5 = Button(55, 120, 40, 20)
btn8 = Button(55, 160, 40, 20)
btn0 = Button(55, 200, 40, 20)
btn3 = Button(95, 80, 40, 20)
btn6 = Button(95, 120, 40, 20)
btn9 = Button(95, 160, 40, 20)
btn_reset = Button(95, 200, 40, 20)
add_to_distance = Button(145, 80, 80, 50)
add_to_time = Button(145, 140, 80, 50)
confirm = Button(145, 200, 80, 30)
decimal = Button(15, 200, 30, 30)


number_input_string = " "

def buttons_screen():
    display.set_pen(LIGHT_BLUE)
    display.rectangle(15, 80, 30, 30) # first column, 1
    display.rectangle(15, 120, 30, 30) # 4
    display.rectangle(15, 160, 30, 30) # 7
    display.rectangle(15, 200, 30, 30) # .

    display.rectangle(55, 80, 30, 30) # second column, 2
    display.rectangle(55, 120, 30, 30)# 5
    display.rectangle(55, 160, 30, 30) # 8
    display.rectangle(55, 200, 30, 30) # 0

    display.rectangle(95, 80, 30, 30) # third column, 3
    display.rectangle(95, 120, 30, 30) # 6
    display.rectangle(95, 160, 30, 30) # 9
    display.rectangle(95, 200, 30, 30) # reset button

    display.rectangle(135, 80, 95, 50) # add to distance
    display.rectangle(135, 140, 95, 50) # add to time
    display.rectangle(135, 200, 95, 30) # confirm

    display.set_pen(TEXT_BLUE)
    display.text("1", 26, 85, scale=3)
    display.text("2", 64, 85, scale=3)
    display.text("3", 104, 85, scale=3)
    display.text("4", 24, 125, scale=3)
    display.text("5", 64, 125, scale=3)
    display.text("6", 103, 125, scale=3)
    display.text("7", 23, 165, scale=3)
    display.text("8", 63, 165, scale=3)
    display.text("9", 103, 165, scale=3)
    display.text("0", 63, 205, scale=3)
    display.text("CL", 97, 203, scale=3)
    display.text(".", 27, 187, scale=5)

    display.text("Add to", 140, 90, scale=2) # add to distance text string
    display.text("distance", 140, 105, scale=2)

    display.text("Add to", 140, 150, scale=2) # add to time text string
    display.text("time", 140, 165, scale=2)

    display.text("Confirm", 140, 208, scale=2)
    
    display.text("Input:", 10, 15, scale=2) # input:
    display.text(f"{number_input_string}", 70, 15, scale=2) # input value
    
    display.text("Distance adding:", 10, 35, scale=2) # distance adding
    display.text("km", 210, 35, scale=2) # distance unit
    
    display.text("Time adding:", 10, 55, scale=2) # time adding
    display.text("min", 165, 55, scale=2) # time unit

    presto.update()

def update_screen():
    global number_input_string
    while True:
        touch.poll()

        if btn1.is_pressed():
            number_input_string += "1"
            time.sleep_ms(200)
            presto.update()
            
        if btn2.is_pressed():
            number_input_string += "2"
            time.sleep_ms(200)
            presto.update()
        
        if btn3.is_pressed():
            number_input_string += "3"
            time.sleep_ms(200)
            presto.update()
            
        if btn4.is_pressed():
            number_input_string += "4"
            time.sleep_ms(200)
            presto.update()
            
        if btn5.is_pressed():
            number_input_string += "5"
            time.sleep_ms(200)
            presto.update()
            
        if btn6.is_pressed():
            number_input_string += "6"
            time.sleep_ms(200)
            presto.update()
            
        if btn7.is_pressed():
            number_input_string += "7"
            time.sleep_ms(200)
            presto.update()
            
        if btn8.is_pressed():
            number_input_string += "8"
            time.sleep_ms(200)
            presto.update()
            
        if btn9.is_pressed():
            number_input_string += "9"
            time.sleep_ms(200)
            presto.update()
            
        if btn0.is_pressed():
            number_input_string += "0"
            time.sleep_ms(200)
            presto.update()
        
        if btn_reset.is_pressed():
            number_input_string = " "
            display.set_pen(BLACK)
            display.rectangle(76, 15, 200, 15)
            time.sleep_ms(200)
            presto.update()
            
        if decimal.is_pressed():
            number_input_string += "."
            time.sleep_ms(200)
            presto.update()
            
        if add_to_distance.is_pressed():
            display.text(f"{number_input_string}", 172, 35, scale=2) # distance value
            number_input_string = " "
            display.set_pen(BLACK)
            display.rectangle(76, 15, 200, 15)
            time.sleep_ms(200)
            presto.update()
        
        if add_to_time.is_pressed():
            display.text(f"{number_input_string}", 130, 55, scale=2) # distance value
            number_input_string = " "
            display.set_pen(BLACK)
            display.rectangle(76, 15, 200, 15)
            time.sleep_ms(200)
            presto.update()
            
        if confirm.is_pressed():
            clock()
            pass
            
        else:
            buttons_screen()
            

if __name__ == "__main__":
    update_screen()
    presto.update()