# -*- encoding: UTF-8 -*-

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    # 连环动作
    postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    postureProxy.goToPosture("StandInit", 0.8)
    postureProxy.goToPosture("SitRelax", 0.8)
    postureProxy.goToPosture("StandZero", 0.8)
    postureProxy.goToPosture("LyingBelly", 0.8)
    postureProxy.goToPosture("LyingBack", 0.8)
    postureProxy.goToPosture("Stand", 0.8)
    postureProxy.goToPosture("Crouch", 0.8)
    postureProxy.goToPosture("Sit", 0.8)

    print postureProxy.getPostureFamily()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
