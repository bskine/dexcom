from pydexcom import Dexcom
from statistics import mean
from dexcom import creds

dexcom = Dexcom(creds.usr, creds.pwd)
# current_bg = dexcom.get_current_glucose_reading()
# print(current_bg.value)


def glucose_current():
    current_bg = dexcom.get_current_glucose_reading().value
    # print(f'Current glucose reading is {current_bg.value}')
    return [0, current_bg]


def glucose_average_1hour():
    bg_1hour_int_list = []
    bg_1hour_object_list = dexcom.get_glucose_readings(minutes=60)
    for i in bg_1hour_object_list:
        bg_1hour_int_list.append(i.value)
    bg_1hour_average_long = mean(bg_1hour_int_list)
    bg_1hour_average = round(bg_1hour_average_long, 2)
    # print(f'1 hour blood glucose average is {bg_1hour_average}')
    return [1, bg_1hour_average]


def glucose_average_3hour():
    bg_3hour_int_list = []
    bg_3hour_object_list = dexcom.get_glucose_readings(minutes=180)
    for i in bg_3hour_object_list:
        bg_3hour_int_list.append(i.value)
    bg_3hour_average_long = mean(bg_3hour_int_list)
    bg_3hour_average = round(bg_3hour_average_long, 2)
    # print(f'3 hour blood glucose average is {bg_3hour_average}')
    return [3, bg_3hour_average]


def glucose_average_6hour():
    bg_6hour_int_list = []
    bg_6hour_object_list = dexcom.get_glucose_readings(minutes=360)
    for i in bg_6hour_object_list:
        bg_6hour_int_list.append(i.value)
    bg_6hour_average_long = mean(bg_6hour_int_list)
    bg_6hour_average = round(bg_6hour_average_long, 2)
    # print(f'6 hour blood glucose average is {bg_6hour_average}')
    return [6, bg_6hour_average]


def glucose_average_12hour():
    bg_12hour_int_list = []
    bg_12hour_object_list = dexcom.get_glucose_readings(minutes=720)
    for i in bg_12hour_object_list:
        bg_12hour_int_list.append(i.value)
    bg_12hour_average_long = mean(bg_12hour_int_list)
    bg_12hour_average = round(bg_12hour_average_long, 2)
    # print(f'12 hour blood glucose average is {bg_12hour_average}')
    return [12, bg_12hour_average]


def glucose_average_24hour():
    bg_24hour_int_list = []
    bg_24hour_object_list = dexcom.get_glucose_readings(minutes=1440)
    for i in bg_24hour_object_list:
        bg_24hour_int_list.append(i.value)
    bg_24hour_average_long = mean(bg_24hour_int_list)
    bg_24hour_average = round(bg_24hour_average_long, 2)
    # print(f'24 hour blood glucose average is {bg_24hour_average}')
    return [24, bg_24hour_average]


def main():
    print(f'\n{("*" * 75)}\n')
    glucose_current()
    print(f'\n{("*"*75)}\n')
    glucose_average_1hour()
    print(f'\n{("*"*75)}\n')
    glucose_average_3hour()
    print(f'\n{("*" * 75)}\n')
    glucose_average_6hour()
    print(f'\n{("*" * 75)}\n')
    glucose_average_12hour()
    print(f'\n{("*" * 75)}\n')
    glucose_average_24hour()
    print(f'\n{("*" * 75)}\n')


if __name__ == "__main__":
    main()
# for i in bg2:
#     print(f" {i.time}        {i.value}         {i.trend_arrow}")
