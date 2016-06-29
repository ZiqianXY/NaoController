# -*- encoding: UTF-8 -*-

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    # tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    # tts.post.say("我这就退后0.6米.")

    # lower the volume by 10%
    audioDevice = ALProxy("ALAudioDevice", robotIP, PORT)
    currentVoice = audioDevice.getOutputVolume()
    audioDevice.setOutputVolume(currentVoice - 10)

    # stand first
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    postureProxy.goToPosture("StandInit", 0.5)

    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    motionProxy.wakeUp()
    motionProxy.setMoveArmsEnabled(True, True)
    motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])
    # action move
    motionProxy.post.moveTo(-0.618, 0, 0)
    motionProxy.waitUntilMoveIsFinished()

    print "Robot Move: back"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
