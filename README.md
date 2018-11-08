<!-- TOC -->

- [INSTALL](#install)
	- [1. preinstall](#1-preinstall)
	- [2. capstone source compile](#2-capstone-source-compile)
	- [3. virtualenvwrapper](#3-virtualenvwrapper)
	- [4. claripy](#4-claripy)
	- [5. angr](#5-angr)
	- [6. shellphish-qemu](#6-shellphish-qemu)
	- [7. shellphish-afl](#7-shellphish-afl)
	- [8. tracer](#8-tracer)
	- [9. redis](#9-redis)
	- [10. fuzzer](#10-fuzzer)
	- [11. driller](#11-driller)
	- [12. binaries](#12-binaries)
- [cgc samples](#cgc-samples)
- [test](#test)
	- [1. control_dependency our](#1-control_dependency-our)
	- [2 shellphuzz two branch](#2-shellphuzz-two-branch)

<!-- /TOC -->

# INSTALL

## 1. preinstall  
	sudo apt-get install python-dev libffi-dev build-essential python-pip git  
	sudo apt-get build-dep qemu-system  

## 2. capstone source compile  
	./make.sh  
	sudo ./make.sh install

## 3. virtualenvwrapper
	sudo apt-get install virtualenvwrapper  
	pip install virtualenv
	virtualenv -p /usr/bin/python3 py3env
	source py3env/bin/activate

## 4. readcode
	mkdir driller
	git clone https://github.com/CAFA1/driller1.git  

## 5. angr  
	cd driller
	git clone https://github.com/CAFA1/angr.git  
	pip install -r requirements.txt  
	pip install -v -e .

## 6. shellphish-qemu  
	git clone https://github.com/CAFA1/shellphish-qemu.git  
	sudo apt-get install libpixman-1-dev  
	./rebuild.sh  
	pip install -v -e . 

## 7. shellphish-afl  
	git clone https://github.com/CAFA1/shellphish-afl.git  
	python setup.py develop  
	~/driller/shellphish-afl/bin/afl-cgc$ cp tracers/i386/afl-qemu-trace ./  
	pip install -v -e .

## 8. tracer  
	git clone https://github.com/CAFA1/tracer.git  
	sudo apt-get install libacl1-dev  
	pip install -r requirements.txt  
	pip install -v -e .  
 
## 9. redis  
	http://blog.fens.me/linux-redis-install/  
	sudo apt-get install redis-server  
	pip install redis  

## 10. fuzzer  
	git clone https://github.com/CAFA1/fuzzer.git  
	pip install tqdm  
	pip install IPython  
	sudo apt-get install build-essential gcc-multilib libtool automake autoconf bison debootstrap debian-archive-keyring  
	sudo apt-get build-dep qemu  
	python setup.py build  
	pip install -v -e .  
## 11. driller  
	git clone https://github.com/CAFA1/driller.git 
	pip install -r requirements.txt  
	python setup.py build  
	pip install -v -e .  
## 12. binaries  
	git clone --depth 1 https://github.com/angr/binaries.git  

# cgc samples
	http://www.lungetech.com/cgc-corpus/cwe/cfe/
	
# test
## 1. control_dependency our
	cd test
	python driller_explore.py -d 1 control_flow/control_dependency

## 2 shellphuzz two branch
	./shellphuzz -c 1 -d 1 -f 6 --no-dictionary ../test/control_flow/control_dependency  
	./shellphuzz -c 1 -d 1 -f 6 /vagrant/samples-master/examples/CADET_00001/bin/CADET_00001  