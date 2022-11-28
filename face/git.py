# https://blog.csdn.net/m0_45234510/article/details/120181503
'''
git branch  查看当前分支
git branch wenjing(分支名字)    新建分支
git checkout wenjing    将当前分支切换到新建分支上面
git push -u origin BugFixWenjing    本地分支推送到远程分支
git config --global user.email "wenjing.ma@pacteraedge.com"
git config --global user.name "WenjingMa"

git config
git config user.name
git config user.email

正常部署代码的步骤：
1.查看有哪些文件发送变动
git status
2.新增文件
git add .
3.
    第一种方法；
        3.1git commit .
        https://blog.csdn.net/qq_41767905/article/details/122443837
        3.2按键盘左上角"Esc"
        3.3输入":wq",注意是冒号+wq,按回车键即可
    第二种方法：
        git commit -m "commit message here"
5.push文件
git push
6.输出git生成的密码


git commit -m "备注内容"
branch 合并到master
假如我们现在在branch1分支上，刚开发完项目，执行了下列命令
git add .
git commit -m ‘branch1'
git push -u origin branch1
然后我们要把branch1分支的代码合并到master分支上 该如何？
打开git bash命令框，也可以在idea里进行操作

一、分支代码合并到主分支上
1、切换到分支（已经是branch1就略过）
    git checkout branch1
2、.把本地分支拉取下来
    git pull origin branch1
3、切换到主分支
    git checkout master
4.合并代码到主分支上
    git merge branch1
------如果出现冲突 ，手动解决 ，再git add . ,git commit -m ""  git push origin master
------如果没有冲突 git push origin master（可能会有冲突，呵呵）

二.主分支代码拉取到自己分支上
1.首先检查自己现在在哪个分支，如果在branch1开发分支，看是否有最新代码没有提交，如果有，先 git add . git commit -m 提交本地代码、提交完之后，切换到主分支
    git checkout master
2.把主分支代码拉取下来
    git pull 或者 git pull origin master
3.切换到开发分支branch1
    git checkout branch1
4.合并主分支的代码到开发分支上
    git merge master
5.可以 git status 检查一下是否合并成功，是否有冲突
6.检查没问题，推送代码
    git commit -m ''
    git push 或者 git push origin branch1


三.常用git操作命令扩展，待更新，欢迎留言常用的操作命令
1.查看所有分支
    git branch -a
2.创建新分支并切换到新分支
    git checkout -b test
3.回退版本,
    回退到上一个版本
        git reset –hard HEAD^
    回退到上2个版本
        git reset –hard HEAD~2
    回退到指定版本，可以先git log查看版本号
        git reset --hard 版本号

'''