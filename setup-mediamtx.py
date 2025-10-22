#!/home/pi/gopro2vimeo/mediamtx/.venv/bin/python
import os
import re
import yaml
import requests
import json

# Get username, don't assume its pi.
USER = os.getenv('USER')
UUID_PATTERN = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$', re.I)

def inital_setup():
    filename = f'/home/{ USER }/gopro2vimeo/mediamtx/config/mediamtx.yml'

    os.system('cls' if os.name == 'nt' else 'clear')
    rtsp = input('rtsp? y/n: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    hls = input('hls? y/n: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    webrtc = input('webrtc? y/n: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    srt = input('src? y/n: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Your Vimeo Stream ID')
    stream_id = input('Stream ID: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if not bool(UUID_PATTERN.match(stream_id)):
        print('Error: Stream ID appears to be invalid.')
        return

    yaml_config = {
        'api': True,
        'rtsp': True if rtsp == 'y' else False,
        'hls': True if hls == 'y' else False,
        'webrtc': True if webrtc == 'y' else False,
        'srt': True if srt == 'y' else False,
        'paths': {
            'all': {
                'source': 'publisher'
            },
        },
        'pathDefaults': {
            'runOnReady': "ffmpeg -i rtmp://localhost:1935/live/1 " +
                          "-c copy " +
                          f"-f mpegts \"srt://srt-global.cloud.vimeo.com:9999?streamid={ stream_id }&mode=caller&latency=5000&pkt_size=1316\"",
            'runOnReadyRestart': True
        }
    }

    with open(filename, 'w') as conf_file:
        yaml.dump(yaml_config, conf_file, sort_keys=False)

    print('# Mediamtx Configutarion File.')
    print(f'# Configuration file location: {filename}')
    print(yaml.dump(yaml_config, sort_keys=False, indent=2))


def get_path_list():
    r = requests.get(
        'http://localhost:9997/v3/config/paths/list',
        headers={'Content-Type': 'application/json'},
    )
    if r.status_code != 200:
        return {'api error': 'something went wrong..', 'http_status': r.status_code}
    data = r.json()
    for i, _ in enumerate(data['items']):
        print(f'Path {i}: {_['name']}')
    return


def get_paths():
    r = requests.get(
        'http://localhost:9997/v3/config/paths/get/all',
        headers={'Content-Type': 'application/json'},
    )
    if r.status_code != 200:
        return {'api error': 'something went wrong..', 'http_status': r.status_code}
    # data = r.json()
    return r.json()


def set_paths(stream_id):
    if not bool(UUID_PATTERN.match(stream_id)):
        print('\n', 'Error: Stream ID appears to be invalid.', '\n')
        return

    r = requests.patch(
        url='http://localhost:9997/v3/config/paths/patch/all',
        json={
            "name": "all",
            "source": "publisher",
            "sourceFingerprint": "",
            "sourceOnDemand": False,
            "sourceOnDemandStartTimeout": "10s",
            "sourceOnDemandCloseAfter": "10s",
            "maxReaders": 0,
            "srtReadPassphrase": "",
            "fallback": "",
            "useAbsoluteTimestamp": False,
            "record": False,
            "recordPath": "./recordings/%path/%Y-%m-%d_%H-%M-%S-%f",
            "recordFormat": "fmp4",
            "recordPartDuration": "1s",
            "recordMaxPartSize": "50M",
            "recordSegmentDuration": "1h0m0s",
            "recordDeleteAfter": "1d",
            "overridePublisher": True,
            "srtPublishPassphrase": "",
            "rtspTransport": "automatic",
            "rtspAnyPort": False,
            "rtspRangeType": "",
            "rtspRangeStart": "",
            "rtspUDPReadBufferSize": 0,
            "mpegtsUDPReadBufferSize": 0,
            "rtpSDP": "",
            "rtpUDPReadBufferSize": 0,
            "sourceRedirect": "",
            "rpiCameraCamID": 0,
            "rpiCameraSecondary": False,
            "rpiCameraWidth": 1920,
            "rpiCameraHeight": 1080,
            "rpiCameraHFlip": False,
            "rpiCameraVFlip": False,
            "rpiCameraBrightness": 0,
            "rpiCameraContrast": 1,
            "rpiCameraSaturation": 1,
            "rpiCameraSharpness": 1,
            "rpiCameraExposure": "normal",
            "rpiCameraAWB": "auto",
            "rpiCameraAWBGains": [0, 0],
            "rpiCameraDenoise": "off",
            "rpiCameraShutter": 0,
            "rpiCameraMetering": "centre",
            "rpiCameraGain": 0,
            "rpiCameraEV": 0,
            "rpiCameraROI": "",
            "rpiCameraHDR": False,
            "rpiCameraTuningFile": "",
            "rpiCameraMode": "",
            "rpiCameraFPS": 30,
            "rpiCameraAfMode": "continuous",
            "rpiCameraAfRange": "normal",
            "rpiCameraAfSpeed": "normal",
            "rpiCameraLensPosition": 0,
            "rpiCameraAfWindow": "",
            "rpiCameraFlickerPeriod": 0,
            "rpiCameraTextOverlayEnable": False,
            "rpiCameraTextOverlay": "%Y-%m-%d %H:%M:%S - MediaMTX",
            "rpiCameraCodec": "auto",
            "rpiCameraIDRPeriod": 60,
            "rpiCameraBitrate": 5000000,
            "rpiCameraHardwareH264Profile": "main",
            "rpiCameraHardwareH264Level": "4.1",
            "rpiCameraSoftwareH264Profile": "baseline",
            "rpiCameraSoftwareH264Level": "4.1",
            "rpiCameraMJPEGQuality": 60,
            "runOnInit": "",
            "runOnInitRestart": False,
            "runOnDemand": "",
            "runOnDemandRestart": False,
            "runOnDemandStartTimeout": "10s",
            "runOnDemandCloseAfter": "10s",
            "runOnUnDemand": "",
            "runOnReady": f"ffmpeg -i rtmp://localhost:1935/live/1 -c copy -f mpegts \"srt://srt-global.cloud.vimeo.com:9999?streamid={stream_id}&mode=caller&latency=5000000&pkt_size=1316\"\n",
            "runOnReadyRestart": True,
              "runOnNotReady": "",
              "runOnRead": "",
              "runOnReadRestart": False,
              "runOnUnread": "",
              "runOnRecordSegmentCreate": "",
              "runOnRecordSegmentComplete": ""
        },
        headers={'Content-Type': 'application/json'},
    )
    if r.status_code != 200:
        return {'api error': 'something went wrong patching...', 'http_status': r.status_code}
    print(r)
    return r


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~ nowiresfil/gopro2vimeo Setup ~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('1.  Initial setup')
        print('2.  Current Settings')
        print('3.  Update Stream ID')
        print('5.  All Paths Lists')
        print('10. Docker Container Status')
        print('11. Docker Container Restart')
        print('c.  Clear Terminal')
        print('q.  Quit & Exit\n')

        try:
            menu_choice = input('Option: ')
            if menu_choice == '1':
                inital_setup()
            elif menu_choice == '2':
                print(json.dumps(get_paths(), indent=2))
            elif menu_choice == '3':
                stream_id = input('New Stream ID: ')
                set_paths(stream_id=stream_id)
            elif menu_choice == 'c':
                os.system('cls' if os.name == 'nt' else 'clear')
            elif menu_choice == '5':
                print('Collecting all path names...')
                get_path_list()
            elif menu_choice == '10':
                print(os.system('docker ps -a'))
            elif menu_choice == '11':
                print(os.system('docker compose down --remove-orphans && docker compose up -d'))
            elif menu_choice == 'q':
                break
            else:
                break
        except EOFError as e:
            print('Error:', e)
            pass
