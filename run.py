import subprocess
import sys

p1 = subprocess.Popen([sys.executable, 'helper.py'])
p2 = subprocess.Popen([sys.executable, 'main.py'])

p1.wait()
p2.wait()
