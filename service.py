# -*- encoding: UTF-8 -*-
import web
import os
import sys
from naoqi import ALProxy

basedir = sys.path[0]
template = os.path.join(basedir, 'templates/')
render = web.template.render(template)
urls = ('/(.*)', 'index')

class index:

    def __init__(self):
        self.isRunning = False
    def GET(self, name):

        if((not self.isRunning) and name and (name!='favicon.ico')):
            self.isRunning = True
            if(name=='power-off'):
                print 'stop service'
                self.powerOff()
            else:
                self.startFile(name)
            self.isRunning = False
        return render.index(name)

    def startFile (self, name):
        filename = name+".py"
        path = os.path.join(basedir, "lib", filename)
        command = 'python '+path
        print command
        os.system(command)

    def powerOff (self):
        tts = ALProxy("ALTextToSpeech", 'nao.local', 9559)
        tts.say("即将执行关机操作！")
        command1 = 'sudo shutdown -h now'
        os.system(command1)
        command2 = 'root\r'
        os.system(command2)

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app = web.application(urls, globals())
    app.run()
