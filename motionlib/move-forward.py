# -*- encoding: UTF-8 -*-

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    # tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    # tts.post.say("前进，，前进.")

    audiodevice = ALProxy("ALAudioDevice", robotIP, PORT)
    currentVoice = audiodevice.getOutputVolume()
    audiodevice.setOutputVolume(currentVoice + 10)

    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    postureProxy.goToPosture("StandInit", 0.5)

    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    # Wake up robot
    motionProxy.wakeUp()
    motionProxy.setMoveArmsEnabled(True, True)
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    motionProxy.post.moveTo(0.8, 0, 0)
    motionProxy.waitUntilMoveIsFinished()

    print "Robot Move forward"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
