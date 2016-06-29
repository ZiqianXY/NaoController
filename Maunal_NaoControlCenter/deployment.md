
=============Deployment of NaoControlCenter on Nao================


0. 项目运行依赖webpy服务器框架，需要首先在Naoqi中安装webpy，运行以下命令即可

pip install web.py

1. 通过fileZilla软件远程连接Nao的linux系统Naoqi

nao@sftp://ip<nao.local>:port<22>	root	

2. 将文件夹nao拷贝至/var/www/robotsgate/nao目录（可选择其他目录）

3. 在配置文件中将start.py文件添加至naoqi自动启动列表，
配置文件为/var/persistent/home/nao/naoqi/preferences/autoload.ini

...
# load python_module.py

/var/www/robotsgate/nao/start.py
...

4. 开机后访问对应[nao-ip]:[port]即可