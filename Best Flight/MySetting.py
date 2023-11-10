import time
class MySetting:
    @staticmethod
    def print_animated(str):
        for c in str:
            print(c, end='')
            time.sleep(0.2)