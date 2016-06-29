# -*- encoding: UTF-8 -*-

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    tts.post.say("鸟叔来了，，，，，你会跳么?")

    behavior = 'gangnam-style'
    alBehaviorManager = ALProxy("ALBehaviorManager", robotIP, PORT)
    alBehaviorManager.post.runBehavior(behavior)
    print "Robot Behavior:", behavior


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
