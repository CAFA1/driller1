#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import angr
import os
import sys
# os.environ['LD_LIBRARY_PATH'] = os.getcwd()

FIND_ADDR = 0x00400626#0x004006eb 
def main(elf,start_address,end_address):
	proj = angr.Project(elf, load_options={"auto_load_libs": False})
	#start manager
	state = proj.factory.blank_state(addr=start_address)
	sm = proj.factory.simulation_manager(state)
	sm.explore(find=end_address) #, avoid=AVOID_ADDR)
	#return sm.found[0].posix.dumps(0).lstrip('+0').rstrip('B\n')
	found0=sm.found[0]#.regs.rax
	eax=found0.regs.eax
	#flag = found0.memory.load(rdi, 40)

	#cond_0 = flag.get_byte(0)
	#cond_1 = flag.get_byte(1)
	print eax
	
if __name__ == '__main__':
	#print(repr(main()))
	#elf=sys.argv[0]
	#address=sys.argv[1]
	elf='/home/l/driller/cgc/samples-master/examples/CROMU_00046/bin/CROMU_00046'
	start_address=0x8048a60
	end_address=0x8048330
	main(elf,start_address,end_address)


