from datetime import datetime
from subprocess import Popen


class TestEnv():
    def __init__(self, platform='Android'):
        self.adb = lib.utilities.Adb()

        self.srv = Appium_server()

        desired_caps = dict()
        if platform == 'Android':
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '4.4'
            desired_caps['deviceName'] = 'Nexus'
            desired_caps['app'] = os.path.abspath('../apk/test_app.apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',\
                desired_caps)

    def __exit__(self):
        self.driver.quit()
        self.srv.terminate_server()

    def make_screenshot_android(self):
        now = datetime.now().strftime('%H-%M-%S-%f')

        self.adb.cmd("adb shell screencap -p /mnt/sdcard/android_failure_screen_{timestamp}.png".
                     format(timestamp=now))

        self.adb.cmd("adb pull /mnt/sdcard/android_failure_screen_{timestamp}.png ../screens/android_failure_screen_{timestamp}.png".
                     format(timestamp=now, logcatdir=self.log.logdir))

        self.adb.cmd("adb shell rm /mnt/sdcard/android_failure_screen_{timestamp}.png".
                     format(timestamp=now))


class Appium_server():
    def __init__(self):
        # Make sure that no appium server running
        Popen('taskkill /F /IM node.exe', shell=True)

        sleep(2) # previous kill might kill following appium instance

        self.server_process = Popen('PATH TO APPIUM -a localhost -p 4723')

        sleep(10)

    def terminate_server(self):
        print('Appium Server terminate')
        self.server_process.terminate()