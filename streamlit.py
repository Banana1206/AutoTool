import os
try: 
    import streamlit as st
    import concurrent.futures
except:
    os.system("pip install streamlit")
    os.system("pip install futures")

import streamlit as st
import concurrent.futures
import time
from function import ADB, DEVICE
from position import CALENDAR_POSITION, SLOT_POISITION
from ppadb.client import Client as AdbClient
import threading
from datetime import datetime, timedelta
import time
import pytz

calender5 = True
index = 0

def Selection(device_name):
    st.header(device_name)
    option = st.selectbox(
        'Chọn khung giờ mà bạn muốn đặt',
        ('05:00-06:00', '06:00-07:00', '07:00-08:00',
            '08:00-09:00', '09:00-10:00', '10:00-11:00',
            '11:00-12:00', '12:00-13:00', '13:00-14:00',
            '14:00-15:00', '15:00-16:00', '16:00-17:00',
            '17:00-18:00', '18:00-19:00', '19:00-20:00',
            '20:00-21:00', '21:00-22:00'), index=16, key=device_name)

    st.write('You selected:', option)

    list_time = ['05:00-06:00', '06:00-07:00', '07:00-08:00',
            '08:00-09:00', '09:00-10:00', '10:00-11:00',
            '11:00-12:00', '12:00-13:00', '13:00-14:00',
            '14:00-15:00', '15:00-16:00', '16:00-17:00',
            '17:00-18:00', '18:00-19:00', '19:00-20:00',
            '20:00-21:00', '21:00-22:00']

    for i in range(len(list_time)):
        if list_time[i]== option:
            print("Khung h đã đặt" ,list_time[i])
            print("index list time: ", i)
            index = i
            x = SLOT_POISITION[i][1]
            y = SLOT_POISITION[i][0]
            print("X, Y: ", x, y)
        
    
        
    return option , x,y

def five_second_timer():
    timer = 5
    with st.empty():
        for i in range(5):
            time.sleep(1)
            
            st.title(timer - i)
        

def timer():
        
    # Get the current date and time
    now = datetime.now()

    # Calculate the next day's start time (00:00)
    next_day = now + timedelta(days=1)
    next_day_start = datetime(next_day.year, next_day.month, next_day.day, 0, 0, 0)

    # Calculate the time difference between now and the next day's start time
    time_difference = next_day_start - now

    # Extract hours, minutes, and seconds from the time difference
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds % 3600) // 60
    seconds = time_difference.seconds % 60

    print(f"Time remaining until next day: {hours} hours, {minutes} minutes, {seconds} seconds")

    # Count down to the next day
    with st.empty():
        while time_difference.total_seconds() > 0:
            time.sleep(1)
            time_difference -= timedelta(seconds=1)
            st.title(time_difference)

    print("It's the next day!")

def timer_by_timezone():
    # Get the 'Asia/Ho_Chi_Minh' timezone
    tz_VN = pytz.timezone('Asia/Ho_Chi_Minh')

    # Get the current time in the 'Asia/Ho_Chi_Minh' timezone
    now = datetime.now(tz_VN)

    # Calculate the next day's start time (00:00)
    next_day = now + timedelta(days=1)
    next_day_start = tz_VN.localize(datetime(next_day.year, next_day.month, next_day.day, 0, 0, 0))

    # Calculate the time difference between now and the next day's start time
    time_difference = next_day_start - now

    # Count down to the next day
    with st.empty():
        while time_difference.total_seconds() > 0:
            time.sleep(1)
            now = datetime.now(tz_VN)
            time_difference = next_day_start - now
            hours = int(time_difference.total_seconds() // 3600)
            minutes = int((time_difference.total_seconds() % 3600) // 60)
            seconds = int(time_difference.total_seconds() % 60)
            st.title(f"Đếm ngược: {hours}:{minutes}:{seconds}")


    
    
def capture(device):
    global index, calender5
    d = ADB(device)
    index, calender5 = d.screen_capture()
    st.image(f"./images/{device}.png")

    
def click_pick_time5(device, x_time, y_time, index):
    d = ADB(device)
    
    # index = d.get_calendar_next_position()
    x_calendar , y_calendar = CALENDAR_POSITION[index][1], CALENDAR_POSITION[index][0]
    
    # Đặt lịch 
    d.click(x_calendar, y_calendar)
    # d.click(x_calendar, y_calendar)
    time.sleep(1.5)
    
    # # chọn khung thời gian và trượt xuống
    d.click(x_time,y_time)

    d.swipe()
    
    # # nhấn nút accept
    d.click(815,1305)
    
    # click nút send
    d.click(445,1457)
    
    # =========================
    # lan 2
    
    # chọn khung thời gian và trượt xuống
    d.rev_swipe()
    d.click(x_time,y_time)

    d.swipe()
    
    # # nhấn nút accept
    # d.click(815,1305)
    
    # click nút send
    d.click(445,1457)
    
    # =========================
    # lan 3
    
    # chọn khung thời gian và trượt xuống
    d.rev_swipe()
    d.click(x_time,y_time)

    d.swipe()
    
    # # nhấn nút accept
    d.click(815,1305)
    
    # click nút send
    d.click(445,1457)
    
    print("đã hoàn thành việc click device: ", device)


def click_pick_time6(device, x_time, y_time, index):
    d = ADB(device)
    
    # index = d.get_calendar_next_position()
    x_calendar , y_calendar = CALENDAR_POSITION[index][1], CALENDAR_POSITION[index][0]
    
    # Đặt lịch 
    d.click(x_calendar, y_calendar)
    # d.click(x_calendar, y_calendar)
    time.sleep(1.5)
    
    # # chọn khung thời gian và trượt xuống
    d.click(x_time,y_time)

    d.swipe()
    
    # # nhấn nút accept
    d.click(815,1305)
    
    # click nút send
    d.click(445,1457)
    
    # =========================
    # lan 2
    
    # chọn khung thời gian và trượt xuống
    d.rev_swipe2()
    d.click(x_time,y_time)

    d.swipe()
    
    # # nhấn nút accept
    # d.click(815,1305)
    
    # click nút send
    d.click(445,1457)
    
    # =========================
    # lan 3
    
    # chọn khung thời gian và trượt xuống
    d.rev_swipe2()
    d.click(x_time,y_time)

    d.swipe()
    
    # # nhấn nút accept
    d.click(815,1305)
    
    # click nút send
    d.click(445,1457)
    
    print("đã hoàn thành việc click device: ", device)

def main(devices):
    
    print("======================/n")
        
    columns = st.columns(len(devices))
    option = []
    x_slot = []
    y_slot = []
    for device, col in zip(devices, columns):
        with col:
           opt, x_s, y_s = Selection(device)
           x_slot.append(x_s)
           y_slot.append(y_s)
           option.append(opt)
    
    print("option: ", option)
    
    

    if st.button('Bắt đầu'):
        
        threads = []
        for i in range(len(devices)):
            t1 = threading.Thread(target=capture, args=[devices[i]])
            t1.start()

            threads.append(t1)

        for t in threads:
            t.join()


        for device, col in zip(devices, columns):
            with col:
                try:
                    st.image(f"./images/{device}_draw.png")
                except:
                    st.image("https://static.streamlit.io/examples/dog.jpg")
        
        if calender5:
            print("Đây là lịch 5 và index là: ", index)
        else:
            print("Đây là lịch 6 và index là: ", index)
        # ======================
        timer()
        # five_second_timer()
        # timer_by_timezone()
        # =======================
        # time.sleep(0.3)
        
        # Số luồng bạn muốn sử dụng
        num_threads = len(devices)
        print("num_threads: ", num_threads)
        
        if calender5:
            # Tạo một ThreadPoolExecutor với số luồng mong muốn
            with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
                # Bắt đầu thực hiện công việc cho từng thiết bị
                for i in range(num_threads):
                    executor.submit(click_pick_time5, devices[i], x_slot[i], y_slot[i],index)
        else:
            # Tạo một ThreadPoolExecutor với số luồng mong muốn
            with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
                # Bắt đầu thực hiện công việc cho từng thiết bị
                for i in range(num_threads):
                    executor.submit(click_pick_time6, devices[i], x_slot[i], y_slot[i]+100,index)
        
            
        
        st.title(f"Device {devices[0]} đã hoàn thành xong việc đặt lịch")
        
    

    # try:
    #     st.image(path_image)
    # except:
    #     st.image("https://static.streamlit.io/examples/dog.jpg")
               
def run_streamlit():
    st.set_page_config(
    page_title="AutoApp",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    )
    st.title("Ứng dụng tự động đặt lịch")
    client = AdbClient(host="127.0.0.1", port=5037)
    
    try:
        devices = DEVICE(client).get_device()
        print("Devices: ",devices)
        main(devices)
    except:
        st.title("Chưa có devices nào được bật lên")
        folder_path = "./images"  # Đường dẫn đến thư mục chứa hình ảnh

        # Lấy danh sách tên tệp tin trong thư mục
        file_list = os.listdir(folder_path)

        # Lặp qua từng tệp tin trong danh sách và xóa nó
        for file_name in file_list:
            if file_name.endswith(".jpg") or file_name.endswith(".png"):
                file_path = os.path.join(folder_path, file_name)  # Đường dẫn đầy đủ đến tệp tin
                os.remove(file_path)
                print(f"Đã xóa tệp tin: {file_name}")



if __name__ == "__main__":
    os.system("./adb.exe devices")
    run_streamlit()



