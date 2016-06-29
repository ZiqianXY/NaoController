# -*- encoding: UTF-8 -*-

'''Move To: Small example to make Nao Move To an Objective'''

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    tts.post.say("让一让，我要起来了")
    # alBehaviorManager = ALProxy("ALBehaviorManager", robotIP, PORT)
    # alBehaviorManager.getRunningBehaviors ()
    # alBehaviorManager.stopAllBehaviors ()
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    postureProxy.post.goToPosture("Stand", 0.5)

    print "Robot Stand"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
