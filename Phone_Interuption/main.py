import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from time import sleep
import time

testcase_path = ".\\case"
report_path = ".\\report\\"

#每次运行脚本时清空screenshot文件夹
for root, dirs, files in os.walk('./'):
    for name in files:
        if(name.endswith(".png")):
            os.remove(os.path.join(root, name))

# 构建测试集,包含test case目录下的所有以test_开头的.py文件,并按顺序排列
suite = unittest.defaultTestLoader.discover(start_dir=testcase_path,pattern='test_2*.py')

# 执行测试
if __name__=="__main__":
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    fb = open(report_path+'TestReport_'+timestamp+'.html','wb')
    runner = HTMLTestRunner(stream=fb,title=u'蓝牙打断测试',description='description')
    runner.run(suite)
    fb.close()
    sleep(2)  # 设置睡眠时间，等待测试报告生成完毕
