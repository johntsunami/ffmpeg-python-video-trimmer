# ffmpeg-python-video-trimmer
Using ffmpeg python to trim videos

Here's a simple use case for trimming videos with python.  A lot of people have issues running this so I'm uploading this one as an example 
for people to see and use.  

REQUIREMENTS:
pip install ffmpeg-python    # IF you previously installed ffmpeg you must uninstall both of them and reinstall this one. 

download ffmpeg from their website https://ffmpeg.org/download.html  # download appropriate program based on cpu... I used https://github.com/BtbN/FFmpeg-Builds/releases and downloaded the latest NON-SHARED Version
ex ffmpeg-master-latest-win64-gpl.zip   since im using windows 64B

#unzip ffmpeg to root.. aka C: drive ex. C:\ffmpeg-master-latest-win64-gpl

# search variables in windows ... click edit the system variables -evironmental variables- new - add ffmpeg to bariable name and and path to value ex.  "C:\ffmpeg-master-latest-win64-gpl" click ok-ok -restart computer

You should be good to go from there.  I don't like the way this libraries documentation is written.. not very user friendly in my opinion.  
