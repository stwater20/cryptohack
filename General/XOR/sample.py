line="tm bcsv qolfp f'dmvd xuhm exl tgak hlrkiv sydg hxm qiswzzwf qrf oqdueqe dpae resd wndo liva bu vgtokx sjzk hmb rqch fqwbg fmmft seront sntsdr pmsecq"
l=len(line)

for i in range(-100,100):
	p=""
	for j in range(0,l):
		if 0 < ord(line[j])+i < 256: 
			p+=chr(ord(line[j])+i)
	
	print(p)

# for j in range(len(line)):
# 	print ord(line[j])