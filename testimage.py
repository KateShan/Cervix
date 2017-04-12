import warnings
from PIL import Image
import os,glob
def fxn():
	for i in ll:
        	#print "i",i
        	im = Image.open(i)
        	try:
                	if not im._getexif():
                        	print "image name",i
        	except IndexError:
                	print "image name",i
                	import traceback
                	s = traceback.format_exc()
                	serr = "> stderr:\n%s\n" % (s)
                	print serr

ll = glob.glob('/Users/20163/anaconda/envs/train/Type_1/*.jpg')


with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	fxn()
'''
for i in ll: 
	#print "i",i
	im = Image.open(i)
	try:
		if not im._getexif():
			print "image name",i
	except IndexError:
		print "image name",i
		import traceback
                s = traceback.format_exc()
                serr = "> stderr:\n%s\n" % (s)
                print serr
	
'''

