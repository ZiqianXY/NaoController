# -*- encoding: UTF-8 -*-

'''Move To: Small example to make Nao Move To an Objective'''

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    postureProxy.stopMove()
    motionProxy.killAll()
    motionProxy.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
