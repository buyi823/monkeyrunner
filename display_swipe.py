# write by xulinlin 20190402
# test NX629 Automatic Brightness 

# import the monkeyrunner modules

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import sys

# connect ot the current device 
device = MonkeyRunner.waitForConnection()


MonkeyRunner.sleep(2)

for i in range(100):
    device.drag((116,781),(1003,766), 0.1,10)
    MonkeyRunner.sleep(2)
    device.drag((1003,766),(116,781), 0.1,10)
    print('this is %d test ' % (i+1))
    MonkeyRunner.sleep(2)

print('test completed')
    



