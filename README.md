# gopro2vimeo

Use this code to make a RaspberryPi into a realtime transcoder to allow sending reliable video streams from a mobile gopro camera to Vimeo live events

The tested configuration is ... Gopro (wifi) starlink_mini--(ethernet)--Rpi5 >> Vimeo ... although other combinations should be possible

# Tech
The RPi sets up a local RTMP server on port 1935 with a publishing point ```/live/1```

Once a valid stream is detected, RPi sends the stream onto a preconfigured Vimeo live event using the SRT protocol

Script installs docker, sets up dependancies, sets up container config and a menu for adding/updating your vimeo ```streamid```

# TL#DR
Copy and paste the following command into your Rpi terminal and hit enter.

```bash
curl fsSL https://raw.githubusercontent.com/nowiresfil/gopro2vimeo/refs/heads/main/setup.sh | bash
```

# Why
The intention is for an offroad rally car/truck/buggy/ATV/SxS to be able to fit the starlink mini, gopro and RPi and use it to stream live in-car video to Vimeo, and then onto other platforms YT, FB, X, TT, IG

Gopro provides a rugged, affordable, stabilised camera, with a good mounting system... however other RTMP over wifi streaming cameras should also work

Offroad racing usually takes place in locations with poor 4g/5g cell coverage, therefor starlink provides a workable solution. Starlink mini is an afforable, all-in-one solution with lots of mounting accessories available

Why the transcoder... Gopro only streams using RTMP protocol, which can be unreliable over lossy internet connections. Vimeo live events accepts mpeg-ts inside SRT, which provides a much more robust stream over starlink/4g/5g

Why the Raspberry Pi hardware... Affordable, available, most widely known. Arguably the easiest for a beginner to get working... however, code will work with other hardware platforms


# Step 1 - Requirements

[Raspberrypi 5 - 4GB RAM (8GB, 16GB will work)](https://core-electronics.com.au/raspberry-pi-5-model-b-4gb.html)

[microSD card - 32GB (64GB, 128GB, 256GB will work)](https://core-electronics.com.au/32gb-microsd-card-with-noobs-for-all-raspberry-pi-boards.html)

[Heatsink Case for RPi5](https://core-electronics.com.au/aluminium-armour-heatsink-case-raspberry-pi-5.html)

[Diecast aluminium enclosure, to weatherproof the RPi and PSU](https://www.jaycar.com.au/ip65-sealed-diecast-aluminium-boxes-flanged-171-w-x121-d-x55-h-mm/p/HB5041)

[Automotive USB-C power supply, capable of at least 3amps @ 5volts](https://www.jaycar.com.au/usb-type-c-car-charger-5-4a-total-output/p/MP3684)

### Starlink Mini Kit

You can either get direct from [starlink.com](https://www.starlink.com/), [Bunnings](https://www.bunnings.com.au/starlink-mini_p0674372), [Officeworks](https://www.officeworks.com.au/shop/officeworks/p/starlink-mini-stlnkmini), [JB-HiFi](https://www.jbhifi.com.au/products/starlink-mini) usually have the kits on the shelf.

[Reccomend starlink business 'Local Priority' plan + 50GB data](https://www.starlink.com/au/service-plans/business)<br />
This will get around 12hrs of livestream per month for ~$108. Auto top-up buys more data at $42/50GB if you run out.

[Ethernet cable for starlink mini](https://campervanbuilders.com.au/products/starlink-gen3-cables)

[Automotive power supply for starlink mini](https://campervanbuilders.com.au/products/starlink-easy-12-volt-mini-booster)

[Vimeo Account - 'Advanced Plan' ($168mth or $1200pa)](https://vimeo.com/checkout/advanced/)

***A suitable mounting system for Starlink Mini to suit your vehicle***

(Any prices as of Oct 25).

