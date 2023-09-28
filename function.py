import os, time, sys
try:
    import numpy as np
    import cv2
    from ppadb.client import Client as AdbClient
except:
    os.system("pip install numpy")
    os.system("pip install opencv-python")
    os.system("pip install pure-python-adb")
import numpy as np
import cv2
from ppadb.client import Client as AdbClient
from position import CALENDAR_POSITION, SLOT_POISITION

class DEVICE:
    def __init__(self, client):
        self.client = client
        
    def get_device(self):
        devices = []
        for device in self.client.devices():
            devices.append(device.serial)
        return devices
    

class ADB:
    def __init__(self,handle, calendar = CALENDAR_POSITION):
        self.handle = handle
        self.name = handle
        self.calendar = calendar
        self.select_symbol_position5 = [93,862]
        self.select_symbol_position6 = [99, 950]
        # self.next_calender = [820,155]
        
        
    def screen_capture(self):
        os.system(f"adb -s {self.handle} exec-out screencap -p > ./images/{self.name}.png ")
        index, image, future5 = self.get_calendar_position()
        point_color = (0, 0, 255)  # Red color
        point_color2 = (0, 255, 0)
        image = cv2.circle(image, (CALENDAR_POSITION[index][1], CALENDAR_POSITION[index][0]), 15, point_color, -1)
        cv2.imwrite(f"./images/{self.name}_draw.png",image)
        return index,future5
                
    def click(self,x,y):
        os.system(f"adb -s {self.handle} shell input tap {x} {y}")
    
    def swipe(self):
        os.system(f"adb -s {self.handle} shell input swipe 724 1329 724 336 80")
    
    def rev_swipe(self):
        os.system(f"adb -s {self.handle} shell input swipe 724 800 724 1550 100")
    
    def rev_swipe2(self):
        os.system(f"adb -s {self.handle} shell input swipe 724 920 724 1550 100")
    
    
    def find(self,img='',template_pic_name=False,threshold=0.99):
        if template_pic_name == False:
            self.screen_capture(self.handle)
            template_pic_name = self.handle+'.png'
        else:
            self.screen_capture(template_pic_name)
        img = cv2.imread(img)
        img2 = cv2.imread(template_pic_name)
        result = cv2.matchTemplate(img,img2,cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        test_data = list(zip(*loc[::-1]))
        return test_data
    def get_calendar_position(self):
        image = cv2.imread(f"./images/{self.name}.png")
        index = 0
        for i, (y,x) in enumerate(CALENDAR_POSITION):
            if image[y,x][0] != 255:
                index = i
        future5 = image[self.select_symbol_position5[1], self.select_symbol_position5[0]][0] != 255
        return index, image, future5
    
    def get_calendar_next_position(self):
        try:    
            index, image = self.get_calendar_position()
            if image[self.select_symbol_position5[1], self.select_symbol_position5[0]][0] != 255:
                if index >=27:
                    self.click(self.next_calender[0], self.next_calender[1])
                    time.sleep(1)
                    index = index - 27 +7
                    # self.click(CALENDAR_POSITION[index][1],CALENDAR_POSITION[index][0])
                else:
                    index = index+8
                    time.sleep(1)
                    print("index.....", index)
                    # self.click(CALENDAR_POSITION[index][1],CALENDAR_POSITION[index][0])

            elif image[self.select_symbol_position6[1], self.select_symbol_position6[0]][0] != 255:
                
                if index >=34:
                    self.click(self.next_calender[0], self.next_calender[1])
                    time.sleep(1)
                    index = index - 34 +7
                    # self.click(CALENDAR_POSITION[index][1],CALENDAR_POSITION[index][0])
            
                else:
                    index = index+8
                    time.sleep(1)
                    print("index.....", index)
                    # self.click(CALENDAR_POSITION[index][1],CALENDAR_POSITION[index][0])
            os.system(f"adb -s {self.handle} exec-out screencap -p > ./images/{self.name}.png ")
            image2 = cv2.imread(f"./images/{self.name}.png")
            future5 = image2[self.select_symbol_position5[1], self.select_symbol_position5[0]][0] != 255
            return index, image2, future5
            
        except:
            print("không xác định được device: ", self.handle)
            return 0
