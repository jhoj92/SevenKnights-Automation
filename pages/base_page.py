from airtest.core.api import *

class BasePage:

    def step(self, target, timeout=None):

        if isinstance(target, tuple):
            sleep(1.0)  # 좌표 클릭 전 잠시 대기
            touch(target)
            
        else:
            if timeout:
                pos = wait(target, timeout=timeout)
            else:
                pos = wait(target)
            sleep(1.0)
            touch(pos)