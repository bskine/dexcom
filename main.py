from pydexcom import Dexcom
import creds

dexcom = Dexcom(creds.usr, creds.pwd)
current_bg = dexcom.get_current_glucose_reading()
print(current_bg)

bg2 = dexcom.get_glucose_readings()
for i in bg2:
    print(f" {i.time}        {i.value}         {i.trend_arrow}")
