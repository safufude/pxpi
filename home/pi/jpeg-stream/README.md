# JPEG Stream
It provides a low bandwidth, low latency video stream service.

## The Purpose
For long-range FPV flight, it doesn't care about the image quality. It provides just enough information to let the pilot knows how to control the plane. The most important thing is that it can provide low latency video and use low bandwidth.

## Low bandwidth
Test streaming video is transmitted at 10FPS at 341 x 256 frames, using a bandwidth of approximately 100 Kb-150 Kb per second. It can stream real-time video in a low bandwidth network. (e.g. a weak signal 4G network)

## Low latency
In actual tests on a weak signal a 4G network, the streaming video latency can be as low as 50ms.
![](references/video-latency.png)

[Demo video](https://www.youtube.com/embed/BpVMlIxjAsc)

## Low CPU load
In actual tests on a Raspberry PI 3, the sender.py script used under 20% CPU load.

## Save high-res. video at same time
It streams the low-resolution video and saves a high-resolution video to file.\
Use this script to convert .h264 to mp4

    /usr/bin/MP4Box -add test.h264 test.mp4 -flat
    rm test.h264

---
## Hardware Requirements
### Sender
- Raspberry PI
- Raspberry Pi Camera Module\
(Tested: Raspberry PI 3 and Raspberry Pi Camera v1.3)

### Receiver
Moved to:
https://github.com/rc-bellergy/groundstation

## How to strat?
1. Change the TCP_IP setting in the sender.py. Set it to the receiver IP.
2. Start the receiver.py on your PC/Mac
2. Start the control2.py on Raspberry PI
3. When the `control2` started, the receiver will show
```
    ('Connected by', ('192.168.192.168', 35302))
    Waitting video stream ...
```
4. Input 's' (strat stream) in the `control2`
5. The video will start

## Commands List
| Commands | Description |
| --- | ---|
| s | Start / Stop the video stream |
| r | Strat  / Stop recording video |
| / | Split the recarding video |
| h | Stream HD video |
| l | Stream Low-res. video (default) |
| (0-9) | Change stream video quality (default:2) |
| f(1-30) | Change the FPS of stream video |

---
## Credit
The code video streaming code was created by `Maxcr1`:
https://github.com/Maxcr1/TinyStream
