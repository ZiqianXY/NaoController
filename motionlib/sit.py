# -*- encoding: UTF-8 -*-

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    # tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    # tts.post.say("看，我要坐下了.")
    # alBehaviorManager = ALProxy("ALBehaviorManager", robotIP, PORT)
    # alBehaviorManager.getRunningBehaviors ()
    # alBehaviorManager.stopAllBehaviors ()
    postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    postureProxy.post.goToPosture("Sit", 0.8)
    # postureProxy.post.goToPosture("SitRelax", 0.8)
    print postureProxy.getPostureFamily()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
