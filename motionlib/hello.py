# -*- encoding: UTF-8 -*-

import argparse

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    tts.post.say("大家好！！我是,Nao,机器人，,很高兴见到大家.")
    print "Robot Say Hello"

    behavior = 'animations/Stand/Gestures/Hey_1'
    alBehaviorManager = ALProxy("ALBehaviorManager", robotIP, PORT)
    alBehaviorManager.runBehavior(behavior)

    print "Robot Behavior:", behavior


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
