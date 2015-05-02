import subprocess
import configs


class Adb():
    """
	%adb devices
	List of phones attached
	ZX1G22NNJS  phone
    """
    def __init__(self, config):
        self.configs = configs
        self.cmd('adb get-serialno')
        self.serial = self.out[0]

        if self.serial == 'unknown':
            raise Exception('No phone attached')

    def __exit__(self):
        self.cmd('adb shell pm clear ' + self.configs.package, 'Success')
        print('Adb exit.  Clear Package data contents')

    def cmd(self, c, expect=''):
        print(c)
        self.out = subprocess.Popen(c, shell=True,\
                stdout=subprocess.PIPE).stdout.read().splitlines()
        print(self.out)
        self.out = filter(None, self.out)
        if expect:
            for line in self.out:
                if expect in line:
                    print('expected ' + expect + ' received ' + line)
                    return True
            print('expected ' + expect + ' received')
            print(self.out)
            return False
        else:
            return True