# Night Owls Detector

This program receives data from the devman.org API about the users who submitted the task for verification and print to the console the users who sent the task to the console from 00.00 to 6.00.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:
```bash
pip install -r requirements.txt # alternatively try pip3
```
Remember, it is recommended to use virtualenv/venv for better isolation.

# Quickstart

The program must be run using the console.

How to run:
```bash
$ python3 seek_dev_nighters.py
```
Example:
```bash
$ python3 seek_dev_nighters.py 
id306803365 sent for review: 
03/21/18 00:06
03/20/18 00:33
03/20/18 00:20
artstr16 sent for review: 
03/17/18 04:15
03/17/18 01:47
03/17/18 01:23
03/17/18 01:19
03/17/18 00:55
03/17/18 00:49
03/17/18 00:38
03/17/18 00:05
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
