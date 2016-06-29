# -*- encoding: UTF-8 -*-

import argparse

from naoqi import ALProxy


def chat(robotIP, PORT=9559):
    behavior = 'interactwithmotion-b333ad/chat'
    alBehaviorManager = ALProxy("ALBehaviorManager", robotIP, PORT)
    alBehaviorManager.runBehavior(behavior)
    print "Robot Behavior:", behavior


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    print args.ip, args.port
    chat(args.ip, args.port)
