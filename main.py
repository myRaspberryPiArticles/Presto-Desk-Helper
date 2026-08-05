from presto import Presto
import picographics
from touch import Button
import jpegdec
import time
from getinfo import *
from time_math import time_conversion
from homeassistant import *

presto = Presto()
display = presto.display
touch = presto.touch
button_1 = Button(5, 5, 40, 20)
width = display.measure_text("2,400km", 1, 3)
    
TEXT_BLUE = display.create_pen(34, 36, 91)
LIGHT_BLUE = display.create_pen(234, 248, 251)
BLACK = display.create_pen(0, 0, 0)

# clear the screen from what it was
display.set_pen(BLACK)
display.clear()

# welcome
display.set_pen(LIGHT_BLUE)
display.text("Welcome to Presto!", 10, 10, scale=2)

# fetch stuff
distance, times = fetch_data() # fetch home assistant data

time_data = fetch_time() # fetch the datetime string

time_string = time_data[11:16] # extract the time part of it and set this as time string
date_string = timedata_to_date(time_data) # call the function `timedata_to_date` to convert it into a date (basically the get_date without the fetching part)

seconds = int(timedata_to_seconds(time_data))

for i in range(60 - seconds):
    display.set_pen(LIGHT_BLUE)
    display.text("Waiting to get time.", 10, 30, scale=2)
    display.text("Welcome to Presto!", 10, 10, scale=2)
    presto.update()
    time.sleep_ms(333)
    display.set_pen(BLACK)
    display.clear()
    
    display.set_pen(LIGHT_BLUE)
    display.text("Waiting to get time..", 10, 30, scale=2)
    display.text("Welcome to Presto!", 10, 10, scale=2)   
    presto.update()
    time.sleep_ms(333)
    display.set_pen(BLACK)
    display.clear()
    
    display.set_pen(LIGHT_BLUE)
    display.text("Waiting to get time...", 10, 30, scale=2)
    display.text("Welcome to Presto!", 10, 10, scale=2)
    presto.update()
    time.sleep_ms(333)
    display.set_pen(BLACK)
    display.clear()

time_data = fetch_time() # fetch the datetime string
time_string = time_data[11:16] # extract the time part of it and set this as time string


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


number_input_string = ""

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
    
    display.set_font("bitmap8")
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
    display.text("km", 215, 35, scale=2) # distance unit
    
    display.text("Time adding:", 10, 55, scale=2) # time adding
    display.text("min", 209, 55, scale=2) # time unit

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
    display.set_thickness(3)
    display.set_font("sans")
    display.text(f"{distance}km", 65, 80, scale=0.8) # distance_value_string + km
    
    display.set_thickness(2)
    display.text(time_conversion(times), 68, 60, scale=0.5) # how much time I have taken
    display.text("Out of 10,921", 63, 100, scale=0.5) # out of total distance needed to be covered
    display.set_thickness(1)
    display.text(f"{str(round((int(distance)/10921)*100, 2))}%", 95, 120, scale=0.7) #percentage

    display.set_pen(LIGHT_BLUE)
    display.set_thickness(3)
    display.text(f"{date_string}", 50, 220, scale=0.9) # date text

    display.set_pen(LIGHT_BLUE)
    display.set_thickness(8)
    display.text(f"{time_string}", 30, 180, scale=2)
    display.set_pen(LIGHT_BLUE)
    display.rectangle(5, 5, 40, 20)
    
    display.set_thickness(1)
    display.set_pen(TEXT_BLUE)
    display.set_font("sans")
    display.text("UPDATE", 8, 15, scale=0.3)
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
        display.rectangle(40, 15, 200, 15)
        time.sleep_ms(200)
        presto.update()
        
    if decimal.is_pressed():
        number_input_string += "."
        time.sleep_ms(200)
        presto.update()
        
    if add_to_distance.is_pressed():
        display.text(f"{number_input_string}", 162, 35, scale=2) # distance value
        print(number_input_string)
        distance += float(number_input_string)
        number_input_string = ""
        display.set_pen(BLACK)
        display.rectangle(40, 15, 200, 15)
        time.sleep_ms(200)
        presto.update()
    
    if add_to_time.is_pressed():
        display.text(f"{number_input_string}", 125, 55, scale=2) # distance value
        print(number_input_string)
        times += float(number_input_string)
        number_input_string = ""
        display.set_pen(BLACK)
        display.rectangle(40, 15, 200, 15)
        time.sleep_ms(200)
        presto.update()
        
    if confirm.is_pressed():
        page = "home"
        update_distance(distance)
        update_time(times)
        presto.update()

touch_ticks = time.ticks_ms() # the current tick
last_fetch = time.ticks_ms()
presto.set_backlight(0.1)

page = "home"

def main():
    global page, touch_ticks, last_fetch, distance, times
    
    while True:
        touch.poll()
        
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
            
if __name__ == "__main__":
    main()