import hashlib

n = hashlib.md5()
 
n.update(str(1234))
 
while True:
	m = hashlib.md5()
	password=raw_input("Enter Password:")
 
	m.update(str(password))
	if(m.hexdigest()==n.hexdigest()):
		print "Yes"
	else:
		print "NO"
		print password
		print m.hexdigest() 
		print n.hexdigest()
 