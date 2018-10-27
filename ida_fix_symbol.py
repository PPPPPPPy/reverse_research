# coding:utf-8
from idaapi imprt *
import time

Load_Address = 0x10000 # Base Address
Symbol_Start = 0x301e64 + Load_Address # Symbol table enrty address
Symbol_End = 0x3293a4 + Load_Address # Symbol table end address

ea = Symbol_Start
eaEnd = Symbol_End

while ea < eaEnd:
	# Loop over all and fix function name
	offset = 0
	MakeStr(Dword(ea - offset), BADADDR)
	sName = GetString(Dword(ea - offset), -1, ASCSTR_C)
	print sName
	if sName:
		eaFunc = Dword(ea - offset + 4)
		MakeName(eaFunc, sName)
		MakeCode(eaFunc)
		MakeFunction(eaFunc, BADADDR)
	ea = ea + 16
	#time.sleep(1)
	
  
  # reference: https://hk.saowen.com/a/e194e97f3591fd568aa89be6431ac81a3b5ebb636d1cc55147e68f36af4dadd8
