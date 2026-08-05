from presto import Presto
import picographics
from touch import Button
import jpegdec
import time
from getinfo import *
from time_math import time_conversion
from homeassistant import *

presto = Presto(full_res=True)
display = presto.display
touch = presto.touch
button_1 = Button(10, 10, 80, 40)
width = display.measure_text("2,400km", 1, 3)
    
TEXT_BLUE = display.create_pen(34, 36, 91)
LIGHT_BLUE = display.create_pen(234, 248, 251)
BLACK = display.create_pen(0, 0, 0)

# clear the screen from what it was
display.set_pen(BLACK)
display.clear()

# welcome
display.set_pen(LIGHT_BLUE)
display.text("Welcome to Presto!", 20, 20, scale=4)

# fetch stuff
distance, times = fetch_data() # fetch home assistant data

time_data = fetch_time() # fetch the datetime string

time_string = time_data[11:16] # extract the time part of it and set this as time string
date_string = timedata_to_date(time_data) # call the function `timedata_to_date` to convert it into a date (basically the get_date without the fetching part)

seconds = int(timedata_to_seconds(time_data))

for i in range(60 - seconds):
    display.set_pen(LIGHT_BLUE)
    display.text("Waiting to get time.", 20, 60, scale=4)
    display.text("Welcome to Presto!", 20, 20, scale=4)
    presto.update()
    time.sleep_ms(333)
    display.set_pen(BLACK)
    display.clear()
    
    display.set_pen(LIGHT_BLUE)
    display.text("Waiting to get time..", 20, 60, scale=4)
    display.text("Welcome to Presto!", 20, 20, scale=4)   
    presto.update()
    time.sleep_ms(333)
    display.set_pen(BLACK)
    display.clear()
    
    display.set_pen(LIGHT_BLUE)
    display.text("Waiting to get time...", 20, 60, scale=4)
    display.text("Welcome to Presto!", 20, 20, scale=4)
    presto.update()
    time.sleep_ms(333)
    display.set_pen(BLACK)
    display.clear()

time_data = fetch_time() # fetch the datetime string
time_string = time_data[11:16] # extract the time part of it and set this as time string


btn1 = Button(30, 160, 60, 60)
btn4 = Button(30, 240, 80, 40)
btn7 = Button(30, 320, 80, 40)
btn2 = Button(110, 160, 80, 40)
btn5 = Button(110, 240, 80, 40)
btn8 = Button(110, 320, 80, 40)
btn0 = Button(110, 400, 80, 40)
btn3 = Button(190, 160, 80, 40)
btn6 = Button(190, 240, 80, 40)
btn9 = Button(190, 320, 80, 40)
btn_reset = Button(190, 400, 80, 40)
add_to_distance = Button(290, 160, 160, 100)
add_to_time = Button(290, 280, 160, 100)
confirm = Button(290, 400, 160, 60)
decimal = Button(30, 400, 60, 60)


number_input_string = ""

def buttons_screen():
    display.set_pen(LIGHT_BLUE)
    display.rectangle(30, 160, 60, 60) # first column, 1
    display.rectangle(30, 240, 60, 60) # 4
    display.rectangle(30, 320, 60, 60) # 7
    display.rectangle(30, 400, 60, 60) # .

    display.rectangle(110, 160, 60, 60) # second column, 2
    display.rectangle(110, 240, 60, 60)# 5
    display.rectangle(110, 320, 60, 60) # 8
    display.rectangle(110, 400, 60, 60) # 0

    display.rectangle(190, 160, 60, 60) # third column, 3
    display.rectangle(190, 240, 60, 60) # 6
    display.rectangle(190, 320, 60, 60) # 9
    display.rectangle(190, 400, 60, 60) # reset button

    display.rectangle(270, 160, 190, 100) # add to distance
    display.rectangle(270, 280, 190, 100) # add to time
    display.rectangle(270, 400, 190, 60) # confirm
    
    display.set_font("bitmap8")
    display.set_pen(TEXT_BLUE)
    display.text("1", 52, 170, scale=6)
    display.text("2", 128, 170, scale=6)
    display.text("3", 208, 170, scale=6)
    display.text("4", 48, 250, scale=6)
    display.text("5", 128, 250, scale=6)
    display.text("6", 206, 250, scale=6)
    display.text("7", 46, 330, scale=6)
    display.text("8", 126, 330, scale=6)
    display.text("9", 206, 330, scale=6)
    display.text("0", 126, 410, scale=6)
    display.text("CL", 194, 406, scale=6)
    display.text(".", 54, 374, scale=10)

    display.text("Add to", 280, 180, scale=4) # add to distance text string
    display.text("distance", 280, 210, scale=4)

    display.text("Add to", 280, 300, scale=4) # add to time text string
    display.text("time", 280, 330, scale=4)

    display.text("Confirm", 280, 416, scale=4)
    
    display.text("Input:", 20, 30, scale=4) # input:
    display.text(f"{number_input_string}", 140, 30, scale=4) # input value
    
    display.text("Distance adding:", 20, 70, scale=4) # distance adding
    display.text("km", 430, 70, scale=4) # distance unit
    
    display.text("Time adding:", 20, 110, scale=4) # time adding
    display.text("min", 418, 110, scale=4) # time unit

    presto.update()

def leds_off():
    presto.set_led_rgb(4, 0, 0, 0)
    presto.set_led_rgb(5, 0, 0, 0)
    presto.set_led_rgb(6, 0, 0, 0)
    presto.set_led_rgb(1, 0, 0, 0)
    presto.set_led_rgb(2, 0, 0, 0)
    presto.set_led_rgb(3, 0, 0, 0)
    presto.set_led_rgb(0, 0, 0, 0)

def leds_on():
    
    presto.set_led_rgb(4, 255, 255, 255)
    presto.set_led_rgb(5, 255, 255, 255)
    presto.set_led_rgb(6, 255, 255, 255)
    presto.set_led_rgb(1, 255, 255, 255)
    presto.set_led_rgb(2, 255, 255, 255)
    presto.set_led_rgb(3, 255, 255, 255)
    presto.set_led_rgb(0, 255, 255, 255)
            
def clocks():
    global times, distance
    # Create a new JPEG decoder for our PicoGraphics
    j = jpegdec.JPEG(display)

    # Open the JPEG file
    j.open_file("moon.jpeg")

    # Decode the JPEG
    j.decode(0, 0, jpegdec.JPEG_SCALE_FULL, dither=False)

    # Display the result

    display.set_pen(TEXT_BLUE)
    display.set_thickness(6)
    display.set_font("sans")
    display.text(f"{distance}km", 130, 160, scale=1.6) # distance_value_string + km
    
    display.set_thickness(4)
    display.text(time_conversion(times), 136, 120, scale=1.0) # how much time I have taken
    display.text("Out of 10,921", 126, 200, scale=1.0) # out of total distance needed to be covered
    display.set_thickness(2)
    display.text(f"{str(round((int(distance)/10921)*100, 2))}%", 190, 240, scale=1.4) #percentage

    display.set_pen(LIGHT_BLUE)
    display.set_thickness(6)
    display.text(f"{date_string}", 100, 440, scale=1.8) # date text

    display.set_pen(LIGHT_BLUE)
    display.set_thickness(16)
    display.text(f"{time_string}", 60, 360, scale=4)
    display.set_pen(LIGHT_BLUE)
    display.rectangle(10, 10, 80, 40)
    
    display.set_thickness(2)
    display.set_pen(TEXT_BLUE)
    display.set_font("sans")
    display.text("UPDATE", 16, 30, scale=0.6)
    presto.update()
    
def check_update_screen_buttons():
    global number_input_string, page, times, distance

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
        number_input_string = ""
        display.set_pen(BLACK)
        display.rectangle(80, 30, 400, 30)
        time.sleep_ms(200)
        presto.update()
        
    if decimal.is_pressed():
        number_input_string += "."
        time.sleep_ms(200)
        presto.update()
        
    if add_to_distance.is_pressed():
        display.text(f"{number_input_string}", 324, 70, scale=4) # distance value
        print(number_input_string)
        
                
        try:
            distance += float(number_input_string)
        except Exception as e:
            # clear the screen from what it was
            display.set_pen(BLACK)
            display.clear()

            # welcome
            display.set_pen(LIGHT_BLUE)
            display.text("There was an error...", 20, 20, scale=4)

        number_input_string = ""
        display.set_pen(BLACK)
        display.rectangle(80, 30, 400, 30)
        time.sleep_ms(200)
        presto.update()
    
    if add_to_time.is_pressed():
        display.text(f"{number_input_string}", 250, 110, scale=4) # distance value
        print(number_input_string)
        
        try:
            times += float(number_input_string)
        except Exception as e:
            # clear the screen from what it was
            display.set_pen(BLACK)
            display.clear()

            # welcome
            display.set_pen(LIGHT_BLUE)
            display.text("There was an error...", 20, 20, scale=4)

        number_input_string = ""
        display.set_pen(BLACK)
        display.rectangle(80, 30, 400, 30)
        time.sleep_ms(200)
        presto.update()
        
    if confirm.is_pressed():
        page = "home"
        update_distance(round(distance,2))
        update_time(round(times,2))
        presto.update()

touch_ticks = time.ticks_ms() # the current tick
last_fetch = time.ticks_ms()
presto.set_backlight(0.1)

page = "home"

def main():
    global page, touch_ticks, last_fetch, distance, times, time_string, date_string
    
    while True:
        touch.poll()

        if time.ticks_ms() >= last_fetch + (60*1000):
            print("time update")
            time_data = fetch_time() # fetch the datetime string
            time_string = time_data[11:16] # extract the time part of it and set this as time string
            date_string = timedata_to_date(time_data) # call the function `timedata_to_date` to convert it into a date (basically the get_date without the fetching part)
            distance, times = fetch_data()
            last_fetch = time.ticks_ms()
        
        if touch.state:
            touch_ticks = time.ticks_ms()
            leds_on()
            presto.set_backlight(1)
            
        if time.ticks_ms() >= touch_ticks + (10*1000):
            leds_off()
            presto.set_backlight(0.1)
            
        if page == "home":
            clocks()
            presto.update()
            
            if button_1.is_pressed(): # time to switch views (only does this once)
                page = "update"
                display.set_pen(BLACK)
                display.clear()
            

        elif page == "update":
            buttons_screen()
            check_update_screen_buttons()
            presto.update()
            
if __name__ == "__main__":
    main()