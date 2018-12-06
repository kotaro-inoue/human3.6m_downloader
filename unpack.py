import glob
import subprocess

### Params ###
use_pigz = False # True: Utilize Multicore 
dl_scenario = False  # If you downloaded scenario type, please set True

class cmcolor:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

if use_pigz:
    basecmd = 'tar -I pigz -xf '    
else:
    basecmd = 'tar -zxvf '
    
### unpack training dataset
flist = glob.glob('./training/subject/**/*.tgz', recursive=True)
for fname in flist:
    cmd = basecmd+fname
    print(cmd)
    ret = subprocess.call(cmd, shell=True)
cmd = 'rm -r ./training/subject/*'
ret = subprocess.call(cmd, shell=True)
for subject in [1,5,6,7,8,9,11]:
    cmd = 'mv -f S%d ./training/subject/'%(subject)
    print(cmd)
    ret = subprocess.call(cmd, shell=True)

### unpack testing dataset
flist = glob.glob('./testing/subject/**/*.tgz', recursive=True)
for fname in flist:
    cmd = basecmd+fname
    print(cmd)
    ret = subprocess.call(cmd, shell=True)
cmd = 'rm -r ./testing/subject/*'
ret = subprocess.call(cmd, shell=True)
for subject in [1,7,8,9]:
    cmd = 'mv -f S%d ./testing/subject/'%(subject)
    print(cmd)
    ret = subprocess.call(cmd, shell=True)

### unpack scenario dataset
if dl_scenario:
    flist = glob.glob('./training/scenario/**/*.tgz', recursive=True)
    for fname in flist:
        cmd = basecmd+fname
        print(cmd)
        ret = subprocess.call(cmd, shell=True)
    cmd = 'rm -r ./training/scenario/*'
    ret = subprocess.call(cmd, shell=True)
    for subject in range(1,12):
        cmd = 'mv -f S%d ./testing/scenario/'%(subject)
        print(cmd)
        ret = subprocess.call(cmd, shell=True)
