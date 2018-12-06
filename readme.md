# Human3.6M downloader
[Human3.6M](http://vision.imar.ro/human3.6m/description.php) is 3.6 million 3D human poses dataset.  
It is an unofficial downloader for Human3.6M using Python.  
There is an [awesome repository](https://github.com/anibali/h36m-fetch) already but I made it for lazy guys.  
There are just 2 commands after setup your account.  

`python3 download.py`  
`python3 unpack.py`

## Pre-requirements
Python 3, wget, awesome internet(Download: 267GB without scenario)  
pigz is optionally required for fast(multi-core) unpacking.

## Step
1. Make your account and wait their acceptance (it takes about a week). [Human3.6M](http://vision.imar.ro/human3.6m/description.php)
1. Clone this repository
1. Set your ID and Password by modifying download.py
1. Run 'download.py' and 'unpack.py' 

## Trouble?
### "302 Found" is happened / saved files are too small
Please check your ID ,password and their acceptance(you will get a mail).
If it is correct, please remove 'cookies.txt' and failed files, and then re-run 'download.py'

### Failed when unpacking
Please check your permission.

### Is there a way to multi-connection for fast downloading?
I don't recommend it because their server is not powerful.
Please use it gently.

## Tested environment
Ubuntu 18.04, 16.04, Raspbian and OSX 10.13.6
