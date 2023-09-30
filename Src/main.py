import subprocess
import json
import os
from SpeedTest import SpeedTestParser
from datetime import datetime
import pandas as pd
import time
import matplotlib.pyplot as plt
from GifMaker import GifMaker
def run_speed_test() -> None:
   total_runs = 60
   seconds_per_day = 60*60  # Total seconds in a day
   interval = seconds_per_day / total_runs
   
   download_lst = []
   time_lst = []
   datetime_now_date = datetime.now().date()
   now_date = f'{datetime_now_date.day}-{datetime_now_date.month}-{datetime_now_date.year}'
   output_path = os.path.join(os.getcwd(),"Output",'Logs',f"{now_date}_{datetime.now().strftime('%H-%M-%S')}_output.json")
   for i in range(total_runs):
      with open(output_path,'w') as f:
         subprocess.run([r'CLI\speedtest.exe','--format','json-pretty'],stdout=f)
      print(f"--------Finished Speed test result are in {output_path}---------")
      with open(output_path,'r') as f:
         results = json.load(f)
      sp = SpeedTestParser(results)
      download_lst.append(sp.get_download_speed())
      time_lst.append(datetime.now().strftime('%H-%M-%S'))
      plt.plot(time_lst,download_lst)
      plt.xlabel("Download Speed")
      plt.ylabel("Upload Speed")
      plt.savefig(os.path.join(os.getcwd(),"Output",'Download-Graph',f"graph-{datetime.now().strftime('%H-%M-%S')}.png"))
      
      time.sleep(interval)
# print(sp.get_download_speed(),'Mb')
# print(sp.get_upload_speed(),'Mb')

if __name__ == '__main__':
   run_speed_test()
   g = GifMaker(os.path.join(os.getcwd(),'Output','Download-Graph'))
   g.generate_gif_from_images(os.path.join(os.getcwd(),'Output','gif','gif.gif'))
   