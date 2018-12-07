import os
import fnmatch
import subprocess

username = 'yourname'
password = 'yourpass'
debug = False  # Debug mode: If you want to download them, please set False
# I think scenario is not required but,
dl_scenario = False  # If you want to download with scenario type, please set True


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

def get_cookie(username,password):
    cmd = 'rm cookies.txt checklogin.php'
    ret = subprocess.call(cmd, shell=True)
    print('Authentication is started')
    cmd = 'wget --no-check-certificate --keep-session-cookies --save-cookies cookies.txt --post-data \'username=%s&password=%s\' \'https://vision.imar.ro/human3.6m/checklogin.php\'' % (username, password)
    ret = subprocess.call(cmd, shell=True)

### Authentication ###
get_cookie(username,password)

### Human36 params ###
baseurl = 'http://vision.imar.ro/human3.6m/filebrowser.php?download=1&filepath='
datatypes = ['Videos', 'Segments/', 'Features/', 'TOF', 'Poses/', 'Meshes', 'PointCloud']
segments = ['mat_gt_bb', 'mat_gt_bs', 'mat_gt_pl', 'mat_gt_rd', 'mat_gt_scd', 'gt_bs']
features = ['pHoG_BoundingBoxes', 'pHoG_BackgroundSubtraction']
poses = ['RawAngles', 'D3_Angles', 'D3_Angles_mono', 'D3_Positions', 'D3_Positions_mono', 'D3_Positions_mono_universal', 'D2_Positions', ]

subjects = [[1, 1], [6, 5], [7, 6], [2, 7], [3, 8], [4, 9], [5, 11]]
test_subjects = [[1, 2], [2, 3], [3, 4], [4, 10]]
scenarios = [[1, 'Directions'], [2, 'Discussion'], [3, 'Eating'], [4, 'Greeting'], [5, 'Phone_Call'],
             [6, 'Posing'], [7, 'Purchases'], [8, 'Sitting'], [9, 'Sitting_Down'], [10, 'Smoking'],
             [11, 'Taking_Photo'], [12, 'Waiting'], [13, 'Walking'], [14, 'Walking_Dog'], [15, 'Walking_Together']]

### URL generators ###
def get_url(subject, datatypes, is_scenario=False):
    if is_scenario:
        fname = '&filename=ActivitySpecific_%d.tgz&downloadname=%s' % (subject[0], subject[1])
    else:
        fname = '&filename=SubjectSpecific_%d.tgz&downloadname=S%d' % (subject[0], subject[1])
    extension = '.tgz'
    for datatype in datatypes:
        if datatype == 'Segments/':
            for ftype in segments:
                yield baseurl + datatype + ftype + fname, ftype + extension
        elif datatype == 'Features/':
            for ftype in features:
                yield baseurl + datatype + ftype + fname, ftype + extension
        elif datatype == 'Poses/':
            for ftype in poses:
                yield baseurl + datatype + ftype + fname, ftype + extension
        elif datatype == 'PointCloud' or datatype == 'Meshes':
            yield baseurl + datatype + '&filename=S%d.tgz&downloadname=S%d' % (subject[1], subject[1]), datatype + extension
        else:
            yield baseurl + datatype + fname, datatype + extension


def listdir_extension(dir, extension):
    flist = []
    for dirpath, dirs, files in os.walk(dir):
        for name in files:
            if fnmatch.fnmatch(name, '*.%s' % (extension)):
                flist.append(name)
    return flist


# Download Training dataset by subject
for subject in subjects:
    get_cookie(username,password)
    fdir = './training/subject/s%d/' % (subject[1])
    os.makedirs(fdir, exist_ok=True)
    flist = listdir_extension(fdir, 'tgz')
    download_urls = get_url(subject, datatypes)
    for url in download_urls:
        if url[1] not in flist:
            print(cmcolor.BLUE + 'Download to ' + fdir + url[1] + cmcolor.END)
            cmd = 'wget --no-check-certificate --load-cookies cookies.txt \'%s\' -O %s' % (url[0], fdir + url[1])
            if debug is False:
                ret = subprocess.call(cmd, shell=True)
            else:
                print('URL: ' + url[0])
                print(cmd)
        else:
            print(cmcolor.YELLOW + fdir + url[1] + ' is already downloaded' + cmcolor.END)

# Download Testing dataset by subject
for subject in test_subjects:
    get_cookie(username,password)
    fdir = './testing/subject/s%d/' % (subject[1])
    os.makedirs(fdir, exist_ok=True)
    flist = listdir_extension(fdir, 'tgz')
    download_urls = get_url(subject, datatypes[0:3])
    for url in download_urls:
        if url[1] not in flist:
            print(cmcolor.BLUE + 'Download to ' + fdir + url[1] + cmcolor.END)
            cmd = 'wget --no-check-certificate --load-cookies cookies.txt \'%s\' -O %s' % (url[0], fdir + url[1])
            if debug is False:
                ret = subprocess.call(cmd, shell=True)
            else:
                print('URL: ' + url[0])
                print(cmd)
        else:
            print(cmcolor.YELLOW + fdir + url[1] + ' is already downloaded' + cmcolor.END)

# Download Training dataset by scenario
if dl_scenario:
    for subject in scenarios:
        get_cookie(username,password)
        fdir = './training/scenario/%s/' % (subject[1])
        os.makedirs(fdir, exist_ok=True)
        flist = listdir_extension(fdir, 'tgz')
        download_urls = get_url(subject, datatypes[:-2], is_scenario=True)
        for url in download_urls:
            if url[1] not in flist:
                print(cmcolor.BLUE + 'Download to ' + fdir + url[1] + cmcolor.END)
                cmd = 'wget --no-check-certificate --load-cookies cookies.txt \'%s\' -O %s' % (url[0], fdir + url[1])
                if debug is False:
                    ret = subprocess.call(cmd, shell=True)
                else:
                    print('URL: ' + url[0])
                    print(cmd)
            else:
                print(cmcolor.YELLOW + fdir + url[1] + ' is already downloaded' + cmcolor.END)
