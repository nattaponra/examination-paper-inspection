import hashlib
class CreateID(object):
    def __init__(self, arg):
	    super(CreateID, self).__init__()
	    self.arg = arg
    def Create(self,username,password):
        U=hashlib.md5()
        P=hashlib.md5()
        U.update(username)
        P.update(password)

        file = open("setting/username.txt", "w")
        file.write(str(U.hexdigest())+"\n")
        file.write(str(P.hexdigest())+"\n")
        file.close()
        print U.hexdigest(),P.hexdigest()
M=CreateID(0)
M.Create('admin','1234')

    
