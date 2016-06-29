# -*- encoding: UTF-8 -*-

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    motionProxy.wakeUp()
    postureProxy.goToPosture("Stand", 0.8)

    behavior = 'animations/Stand/Waiting/DriveCar_1'
    alBehaviorManager = ALProxy("ALBehaviorManager", robotIP, PORT)
    alBehaviorManager.runBehavior(behavior)
    print "Robot Behavior:", behavior


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
