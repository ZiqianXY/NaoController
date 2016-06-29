# -*- encoding: UTF-8 -*-

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    tts.post.say("stop")

    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    motionProxy.killAll()

    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    print ('\n=======posture=====before=====')
    print postureProxy.getPosture()
    postureProxy.stopMove()
    print ('=======after=====')
    print postureProxy.getPosture()

    audioDeviceProxy = ALProxy("ALAudioDevice", robotIP, PORT)
    print 'muted:', audioDeviceProxy.isAudioOutMuted()
    audioDeviceProxy.flushAudioOutputs()
    print 'muted:', audioDeviceProxy.isAudioOutMuted()

    audioPlayerProxy = ALProxy("ALAudioPlayer", robotIP, PORT)
    print ('\n=======audio=====before=====')
    allItems = audioPlayerProxy.getLoadedSoundSetsList()
    for i in allItems:
        print i
    # audioPlayerProxy.unloadAllFiles()
    # print ('=======afterUnload=====')
    # allItems = audioPlayerProxy.getLoadedSoundSetsList()
    # for i in allItems:
    #     print i
    audioPlayerProxy.stopAll()
    print ('=======afterStop=====')
    allItems = audioPlayerProxy.getLoadedSoundSetsList()
    for i in allItems:
        print i

    alBehaviorManagerProxy = ALProxy("ALBehaviorManager", robotIP, PORT)
    print ('\n=======behavior=====before=====')
    allItems = alBehaviorManagerProxy.getRunningBehaviors()
    for i in allItems:
        print i
    alBehaviorManagerProxy.stopBehavior('gangnam-style')
    alBehaviorManagerProxy.stopBehavior('taichi-dance-free')
    alBehaviorManagerProxy.stopBehavior('caravan-palace')
    print ('=======after=====')
    allItems = alBehaviorManagerProxy.getRunningBehaviors()
    for i in allItems:
        print i


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
