# PPT
之前领导要去做演讲，全是我做好了PPT给他用，然后弄成演讲者模式双屏的，他照着念就可以。不过这种模式用了几年之后，他突然提出要拿着IPAD来讲，然后我来操作PPT播放，这样逼格高一点儿。
参考网上程序，做了这个自动截屏的PYTHON程序，果然好用，只要几行就可以搞定。
不过有几个知识点：
1、利用pyautogui来自动发送右键和截屏，然后pyautogui.screenshot('images/page_%d.jpg' % i)就可以连续存盘下来了。
2、要用pyinstaller来把程序转换成EXE（注意pip install pyinstaller，用的时候pyinstaller -F xxx.py即可）
3、然后把这个生成的EXE拿到他的电脑上运行，出错，发现win7 64位，要安装vc_redist.x64 后完美解决。
4、终于可以自动生成PPT的带备注截屏图片了，不过把图片传入IPAD之后，发现顺序全乱！
5、研究后发现IPAD的排序是按照图片EXIF和修改的时间排序的。下载了ACDSEE5PRO把这些图片时间戳全部改成一样。ITUNES同步一下上传，仍然不行。
6、用ACDSEE5PRO的批量修改功能，把照片的文件名改成AAA##，##选择字母的编码方式。
终于搞定！
