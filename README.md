# gopro2vimeo

Use this code to make a RaspberryPi5 into a realtime transcoder to allow sending reliable video streams from a mobile gopro camera to Vimeo live events

The tested configuration is Gopro (wifi) starlink_mini--(ethernet)--Rpi5 >> Vimeo, although other combinations should be possible

# Tech
  The RPi sets up a local RTMP server on port 1935 with a publishing point /live/1

  Once a valid stream is detected, it sends the stream onto a preconfigured Vimeo live event using the SRT protocol

  Script installs docker, sets up mediamtx and dependancies, setting up container config and a menu for adding your vimeo streamid

# TL#DR
Copy and paste the following command into your Rpi terminal and hit enter. 

```bash
curl fsSL https://github.com/nowiresfil/gopro2vimeo/blob/main/setup.sh | bash
```

