# -*- encoding: UTF-8 -*-

import argparse
import time

from naoqi import ALProxy


def main(robotIP, PORT=9559):
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    tts.post.say("接下来我跟大家表演一段太极，，好不好?")
    time.sleep(1.5)
    # tts.post.say('''拳经总歌,,,,,,
    #     纵放屈伸人莫知，,诸靠缠绕我皆依。
    #     劈打推压得进步，,搬撂横采也难敌。
    #     钩棚逼揽人人晓，,闪惊取巧有谁知？
    #     佯输诈走谁云败，,引诱回冲致胜归。
    #     滚拴搭扫灵微妙，,横直劈砍奇更奇。
    #     截进遮拦穿心肘，,迎风接步红包捶；
    #     二换扫压挂面脚，,左右边簪庄跟腿；
    #     截前压后无缝锁，,声东击西要熟识；
    #     上笼下提君须记，,进攻退闪莫迟迟。
    #     藏头盖面天下有，,攒心剁肋世间稀。
    #     教师不识此中理，,难将武艺论高低。
    #     ''')
    behavior = 'taichi-dance-free'
    alBehaviorManager = ALProxy("ALBehaviorManager", robotIP, PORT)
    alBehaviorManager.post.runBehavior(behavior)
    print "Robot Behavior:", behavior


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="nao.local", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
