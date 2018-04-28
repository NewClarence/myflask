This is a simple project of Flask.
======
flask练手小项目，首次运行按照如下操作
-----
第一步，搭建虚拟开发环境<br>
virtualenv ./venv<br>
第二步，安装依赖库<br>
source ./venv/bin/active<br>
./venv/bin/pip install -r requirements.txt<br>
第四步，创建数据库<br>
在config.py文件中修改成自己的mysql数据库<br>
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@hostname/database'<br>
然后执行<br>
./create_db.py<br>
第五步，启动<br>
./manage.py runserver -d 0.0.0.0 -d<br>
