# gopro2vimeo

Use this code to make a RaspberryPi into a realtime transcoder to allow sending reliable video streams from a mobile gopro camera to Vimeo live events

The tested configuration is Gopro (wifi) starlink_mini--(ethernet)--Rpi5 >> Vimeo, although other combinations should be possible

# TL#DR
Copy and paste the following command into your Rpi terminal and hit enter. 

```bash
curl fsSL https://github.com/nowiresfil/gopro2vimeo/blob/main/setup.sh | bash
```

# Why
  The intention is for an offroad rally car/truck/buggy/ATV/SxS to be able to fit the starlink mini, gopro and RPi and use it to stream live in-car video to Vimeo, and then onto other platforms YT, FB, X, TT, IG

  Gopro provides a rugged, affordable, stabilised camera, with a good mounting system... however other RTMP over wifi streaming cameras should also work

  Offroad racing usually takes place in locations with poor 4g/5g cell coverage, therefor starlink provides a workable solution. Starlink mini is an afforable, all-in-one solution with lots of mounting accessories available

  Why the transcoder... Gopro only streams using RTMP protocol, which can be unreliable over lossy internet connections. Vimeo live events accepts mpeg-ts inside SRT, which provides a much more robust stream over starlink/4g/5g

  Why the Raspberry Pi hardware... Affordable, available, most widely known. Arguably the easiest for a beginner to get working... however, code will work with other hardware platforms

# Tech
  The RPi sets up a local RTMP server on port 1935 with a publishing point /live/1

  Once a valid stream is detected, it sends the stream onto a preconfigured Vimeo live event using the SRT protocol

  Script installs docker, sets up mediamtx and dependancies, setting up container config and a menu for adding your vimeo streamid
