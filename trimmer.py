#https://kkroening.github.io/ffmpeg-python/  DOCUMENTATION
# must pip install python ffmpeg only,  if you installed just ffmpeg.. uninstall both then reinstall python-ffmpeg
#must install software from their website and install environmental variables then restart computer

import ffmpeg
import sys

sys.path.append(r"C:\Users\johnc\Desktop\ffmpeg\bin")
stream = ffmpeg.input(r"C:/Users/johnc/Desktop/krystal.mp4",ss=57, t=55)  # ss is start time,  t IS DURATION

## SEPARATES AUDIO AND VIDEO INDEPENDENTLY BECAUSE SOMETIMES IT DOESNT HAVE AUDIO UNLESS YOU DO THIS>

audio = stream.audio 
video = stream.video   #.trim(start=60,end=115).filter('setpts','PTS-STARTPTS') ## CURRENTLY IS GOOD BUT DOESNT CUT DURATION AFTER 55 seconds

#overwrite_output overwrites it automatically if i dont want it just use output
stream = ffmpeg.output(audio, video, r'C:\Users\johnc\Desktop\output.mp4')


ffmpeg.run(stream)

