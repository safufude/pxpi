import time
from sender2 import Sender
import pymavlink.mavutil as mavutil

'''
Send testing stream video to receiver, when program start
Connect Mavlink and watch the RC channel 6
If switch on middle, send streaming video
If swicth on bottom, send streaming video and save high-res video to disk
'''

def testingVideo(sender):
    print("--- Testing streaming video start ---")
    sender.streamStart()
    time.sleep(5)
    sender.streamStop()
    print("--- Testing streaming video end ---")

def connectMavlink():
    # Connect to mavlink
    print("Connecting Mavlink")
    mav = mavutil.mavlink_connection("udpin:127.0.0.1:14551")
    mav.wait_heartbeat()
    print("Mavlink heartbeat received!")
    return mav

def watchChannel(mav, sender):
    print("Watch RC channel 6")
    while True:
        #  Watch channel 6
        channels = mav.recv_match(type='RC_CHANNELS', blocking=True)
        v = channels.chan6_raw

        # switch on bottom
        if v<1200: 
            sender.recordingStart()
            sender.streamStart()

        # switch on middle
        if v>=1200 and v<1800: 
            sender.recordingStop()
            sender.streamStart()

        # switch on top
        if v>=1800:
            sender.recordingStop()
            sender.streamStop()



video_sender = Sender()
time.sleep(0.1)  # Wait camera init
testingVideo(video_sender)
# mav = connectMavlink()
# watchChannel(mav, video_sender)

streaming = False
recording = False

while True:
    print("")
    c = raw_input("Input (s)tream (r)ecord (q)uit: ")
    if c=="s":
        if streaming:
            video_sender.streamStop()
            streaming = False
        else:
            video_sender.streamStart()
            streaming = True
    if c=="r":
        if recording:
            video_sender.recordingStop()
            recording = False
        else:
            video_sender.recordingStart()
            recording = True
            
    if c=="q":
        break

    time.sleep(0.1)

video_sender.recordingStop()
video_sender.streamStop()
