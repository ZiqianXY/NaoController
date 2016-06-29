# -*- encoding: UTF-8 -*-
import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    tts.post.say("来，，我教你照相.")

    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    postureProxy.goToPosture("Stand", 0.5)

    behavior = 'animations/Stand/Waiting/TakePicture_1'
    alBehaviorManager = ALProxy("ALBehaviorManager", robotIP, PORT)
    alBehaviorManager.runBehavior(behavior)
    print "Robot Behavior:", behavior


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
