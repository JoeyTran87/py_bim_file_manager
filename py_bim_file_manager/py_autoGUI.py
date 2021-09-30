#! python3
"""CONTROL MOUSE"""
import pyautogui, time

# print(width, height)
#-----------------------------------------#
# MOVE MOUSE BY EXCACT POSITON
#-----------------------------------------#
def move_mouse_rectange_absolute(repeat,x,y,w,h,time_duration):
    for i in range(repeat):
        pyautogui.move(x, y, duration=time_duration)
        pyautogui.move(x+w, y, duration=time_duration)
        pyautogui.move(x+w, y+h, duration=time_duration)
        pyautogui.move(x, y+h, duration=time_duration)
def move_mouse_rectange_absolute_infinite(x,y,w,h,time_duration):
    while True:
        pyautogui.move(x, y, duration=time_duration)
        pyautogui.move(x+w, y, duration=time_duration)
        pyautogui.move(x+w, y+h, duration=time_duration)
        pyautogui.move(x, y+h, duration=time_duration)
#-----------------------------------------#
# MOVE MOUSE FROM RELATIVE POSITON
#-----------------------------------------#
def move_mouse_rectange_relative_infinite(delta_x,delta_y,time_duration):
    while True:
        pyautogui.moveRel(delta_x, 0, duration=time_duration)
        pyautogui.moveRel(0, delta_y, duration=time_duration)
        pyautogui.moveRel(-delta_x, 0, duration=time_duration)
        pyautogui.moveRel(0, -delta_y, duration=time_duration)
def move_mouse_rectange_relative(repeat,delta_x,delta_y,time_duration):
    for i in range(repeat):
        pyautogui.moveRel(delta_x, 0, duration=time_duration)
        pyautogui.moveRel(0, delta_y, duration=time_duration)
        pyautogui.moveRel(-delta_x, 0, duration=time_duration)
        pyautogui.moveRel(0, -delta_y, duration=time_duration)
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':  
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True
    screen_width, screen_height = pyautogui.size()
    #-----------------------------------------#
    # GET MOUSE POSTION
    #-----------------------------------------#
    # try:
    #     while True:
    #         print(pyautogui.position())
    #         time.sleep(5)
    # except KeyboardInterrupt:
    #     quit()
    #-----------------------------------------#
    # MOUSE CLICK
    #-----------------------------------------#
    try:
        while True:
            move_mouse_rectange_relative_infinite(100,100,0.25)
            # pyautogui.click(1806, 14)
            # time.sleep(2)
    except KeyboardInterrupt:
        quit()