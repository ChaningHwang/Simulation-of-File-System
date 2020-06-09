import xmlrpclib, ClientStub, AbsolutePathNameLayer, tablemap, time


def Initialize_My_FileSystem():
	ClientStub.ClientStub().Initialize_My_FileSystem()
	AbsolutePathNameLayer.AbsolutePathNameLayer().new_entry('/', 1)
	

#HANDLE TO ABSOLUTE PATH NAME LAYER
interface = AbsolutePathNameLayer.AbsolutePathNameLayer()

class FileSystemOperations():

    #MAKES NEW DIRECTORY
	def mkdir(self, path):
		interface.new_entry(path, 1)

    #CREATE FILE
	def create(self, path):
		interface.new_entry(path, 0)
        

    #WRITE TO FILE
	def write(self, path, data, offset=0):
		interface.write(path, offset, data)
      

    #READ
	def read(self, path, offset=0, size=-1):
		read_buffer = interface.read(path, offset, size)
		if read_buffer != -1: print(path + " : " + read_buffer)

    
    #DELETE
	def rm(self, path):
		interface.unlink(path)


    #MOVING FILE
	def mv(self, old_path, new_path):
		interface.mv(old_path, new_path)


    #CHECK STATUS
	def status(self):
		print(ClientStub.ClientStub().status())


if __name__ == '__main__':
    #DO NOT MODIFY THIS
	
	print(" 4 servers are running.")
	wait_time = raw_input("Please enter waiting time:__s ")
	port = raw_input("Please enter the starting port number:")
	my_object = FileSystemOperations()

	while(True):
		suibian = raw_input("press enter after starting the server ")
		if(suibian==""):
			break
		else:
			time.sleep(600)

	time_initial = time.time()
	for i in range(4):
		try:
			tablemap.tablemap[0] = int(port) + i
			Initialize_My_FileSystem()
			print("connection established from server" + str(i+1) + ".py")
		except xmlrpclib.socket.error as err:
			print("ERROR! The server " + str(i+1) + " is down!")
			pass
	print("FileSystems are initialized.")
	print("time_initial = ", time.time() - time_initial)
	
	while(True):
		message=raw_input("Enter your command: $ ")
		if(message=="exit"):
			break
		message_array = message.split(' ')
		fun = message_array[0]

		if fun =="mkdir":
			time_mkdir = time.time()
			cc = message_array[1]
			for i in range(4):
				try:
					tablemap.tablemap[0] = int(port) + i
					my_object.mkdir(cc)
					my_object.status()
				except xmlrpclib.socket.error as err:
					print("ERROR! The server " + str(tablemap.tablemap[0]-int(port) + 1) + " is down!")
					pass
			print("time_mkdir = ", time.time() - time_mkdir)

		if fun =="status":
			time_status = time.time()
			for i in range(4):
				try:
					tablemap.tablemap[0] = int(port) + i
					my_object.status()
				except xmlrpclib.socket.error as err:
					print("ERROR! The server " + str(tablemap.tablemap[0]-int(port) + 1) + " is down!")
					pass
			print("time_status = ", time.time() - time_status)
				
		if fun =="create":
			time_create = time.time()
			cc = message_array[1]
			tablemap.write[0]+=1
			tablemap.filename.append(cc)
			for i in range(2):
				try:
					if tablemap.write[0]%4 == 1:
						tablemap.tablemap[0] = int(port) + tablemap.pair1[i]
						print(cc+" is writing on Server1,2\n\n\n\n")
					if tablemap.write[0]%4 == 2:
						tablemap.tablemap[0] = int(port) + tablemap.pair2[i]
						print(cc+" is writing on Server2,3\n\n\n\n")
					if tablemap.write[0]%4 == 3:
						tablemap.tablemap[0] = int(port) + tablemap.pair3[i]
						print(cc+" is writing on Server3,4\n\n\n\n")
					if tablemap.write[0]%4 == 0:
						tablemap.tablemap[0] = int(port) + tablemap.pair4[i]
						print(cc+" is writing on Server4,1\n\n\n\n")
					my_object.create(cc)
					my_object.status()
					print("tablemap.filename",tablemap.filename)
				except xmlrpclib.socket.error as err:
					print("ERROR! The server " + str(tablemap.tablemap[0]-int(port) + 1) + " is down!")
					if tablemap.tablemap[0]-int(port) == 3:
						tablemap.pair3[1] = 1
						tablemap.pair4[0] = 1
						print("down 4")
					if tablemap.tablemap[0]-int(port) == 0:
						tablemap.pair1[0] = 2
						tablemap.pair4[1] = 2
						print("down 1")
					if tablemap.tablemap[0]-int(port) == 1:
						tablemap.pair1[1] = 3
						tablemap.pair2[0] = 3
						print("down 2")
					if tablemap.tablemap[0]-int(port) == 2:
						tablemap.pair2[1] = 0
						tablemap.pair3[0] = 0
						print("down 3")
					if tablemap.write[0]%4 == 1:
						tablemap.tablemap[0] = int(port) + tablemap.pair1[i]
						print(cc+" is writing on Server1,2\n\n\n\n")
					if tablemap.write[0]%4 == 2:
						tablemap.tablemap[0] = int(port) + tablemap.pair2[i]
						print(cc+" is writing on Server2,3\n\n\n\n")
					if tablemap.write[0]%4 == 3:
						tablemap.tablemap[0] = int(port) + tablemap.pair3[i]
						print(cc+" is writing on Server3,4\n\n\n\n")
					if tablemap.write[0]%4 == 0:
						tablemap.tablemap[0] = int(port) + tablemap.pair4[i]
						print(cc+" is writing on Server4,1\n\n\n\n")
					my_object.create(cc)
					my_object.status()
					pass
			print("time_create = ", time.time() - time_create)
			
			
		if fun =="write":
			time_write = time.time()
			cc = message_array[1]
			cm = message_array[2]
			cw = int(message_array[3])
			place = tablemap.filename.index(cc)
			for i in range(2):
				try:
					if place%4 == 1:
						print(cm+" will be writen on Server"+str(tablemap.pair1[i]+1))
						time.sleep(int(wait_time))
						tablemap.tablemap[0] = int(port) + tablemap.pair1[i]
						print(cm+" is writing on Server" + str(tablemap.pair1[i]+1))
						time.sleep(int(wait_time))
					if place%4 == 2:
						print(cm+" will be writen on Server"+str(tablemap.pair2[i]+1))
						time.sleep(int(wait_time))
						tablemap.tablemap[0] = int(port) + tablemap.pair2[i]
						print(cm+" is writing on Server" + str(tablemap.pair2[i]+1))
						time.sleep(int(wait_time))
					if place%4 == 3:
						print(cm+" will be writen on Server"+str(tablemap.pair3[i]+1))
						time.sleep(int(wait_time))
						tablemap.tablemap[0] = int(port) + tablemap.pair3[i]
						print(cm+" is writing on Server" + str(tablemap.pair3[i]+1))
						time.sleep(int(wait_time))
					if place%4 == 0:
						print(cm+" will be writen on Server"+str(tablemap.pair4[i]+1))
						time.sleep(int(wait_time))
						tablemap.tablemap[0] = int(port) + tablemap.pair4[i]
						print(cm+" is writing on Server" + str(tablemap.pair4[i]+1))
						time.sleep(int(wait_time))
					my_object.write(cc,cm,cw)
					my_object.status()
					print("tablemap.filename",tablemap.filename)
					if i == 0:
						print("waiting to write in another replica")
						time.sleep(int(wait_time))
				except xmlrpclib.socket.error as err:
					print("ERROR! The server " + str(tablemap.tablemap[0]-int(port) + 1) + " is down!")
					time.sleep(int(wait_time))
					if tablemap.tablemap[0]-int(port) == 3:
						tablemap.pair3[1] = 1
						tablemap.pair4[0] = 1
						print("down 4")
					if tablemap.tablemap[0]-int(port) == 0:
						tablemap.pair1[0] = 2
						tablemap.pair4[1] = 2
						print("down 1")
					if tablemap.tablemap[0]-int(port) == 1:
						tablemap.pair1[1] = 3
						tablemap.pair2[0] = 3
						print("down 2")
					if tablemap.tablemap[0]-int(port) == 2:
						tablemap.pair2[1] = 0
						tablemap.pair3[0] = 0
						print("down 3")
					if place%4 == 1:
						tablemap.tablemap[0] = int(port) + tablemap.pair1[i]
						print(cm+" is writing on Server" + str(tablemap.pair1[i]+1))
						time.sleep(int(wait_time))
					if place%4 == 2:
						tablemap.tablemap[0] = int(port) + tablemap.pair2[i]
						print(cm+" is writing on Server" + str(tablemap.pair2[i]+1))
						time.sleep(int(wait_time))
					if place%4 == 3:
						tablemap.tablemap[0] = int(port) + tablemap.pair3[i]
						print(cm+" is writing on Server" + str(tablemap.pair3[i]+1))
						time.sleep(int(wait_time))
					if place%4 == 0:
						tablemap.tablemap[0] = int(port) + tablemap.pair4[i]
						print(cm+" is writing on Server" + str(tablemap.pair4[i]+1))
						time.sleep(int(wait_time))
					my_object.write(cc,cm,cw)
					my_object.status()
					pass
			print("time_write = ", time.time() - time_write)
				

		if fun =="read":
			time_read = time.time()
			cc = message_array[1]
			place = tablemap.filename.index(cc)
			try:
				if place%4 == 1:
					print("your data is in Server"+str(tablemap.pair1[0]+1)+" and Server"+str(tablemap.pair1[1]+1))
					time.sleep(int(wait_time))
					tablemap.tablemap[0] = int(port) + tablemap.pair1[0]
					print(cc+" is reading from Server"+str(tablemap.pair1[0]+1))
					time.sleep(int(wait_time))
				if place%4 == 2:
					print("your data is in Server"+str(tablemap.pair2[0]+1)+" and Server"+str(tablemap.pair2[1]+1))
					time.sleep(int(wait_time))
					tablemap.tablemap[0] = int(port) + tablemap.pair2[0]
					print(cc+" is reading from Server"+str(tablemap.pair2[0]+1))
					time.sleep(int(wait_time))
				if place%4 == 3:
					print("your data is in Server"+str(tablemap.pair3[0]+1)+" and Server"+str(tablemap.pair3[1]+1))
					time.sleep(int(wait_time))
					tablemap.tablemap[0] = int(port) + tablemap.pair3[0]
					print(cc+" is reading from Server"+str(tablemap.pair3[0]+1))
					time.sleep(int(wait_time))
				if place%4 == 0:
					print("your data is in Server"+str(tablemap.pair4[0]+1)+" and Server"+str(tablemap.pair4[1]+1))
					time.sleep(int(wait_time))
					tablemap.tablemap[0] = int(port) + tablemap.pair4[0]
					print(cc+" is reading from Server"+str(tablemap.pair4[0]+1))
					time.sleep(int(wait_time))
				my_object.read(cc)
				time.sleep(int(wait_time))
				my_object.status()
			except xmlrpclib.socket.error as err:
				print("ERROR! The server " + str(tablemap.tablemap[0]-int(port) + 1) + " is down!")
				time.sleep(int(wait_time))
				if place%4 == 1:
					tablemap.tablemap[0] = int(port) + tablemap.pair1[1]
					print(cc+" is reading from Server"+str(tablemap.pair1[1]+1))
					time.sleep(int(wait_time))
				if place%4 == 2:
					tablemap.tablemap[0] = int(port) + tablemap.pair2[1]
					print(cc+" is reading from Server"+str(tablemap.pair2[1]+1))
					time.sleep(int(wait_time))
				if place%4 == 3:
					tablemap.tablemap[0] = int(port) + tablemap.pair3[1]
					print(cc+" is reading from Server"+str(tablemap.pair3[1]+1))
					time.sleep(int(wait_time))
				if place%4 == 0:
					tablemap.tablemap[0] = int(port) + tablemap.pair4[1]
					print(cc+" is reading from Server"+str(tablemap.pair4[1]+1))
					time.sleep(int(wait_time))
				my_object.read(cc)
				time.sleep(int(wait_time))
				my_object.status()
				pass	
			print("time_read = ", time.time() - time_read)

		
		if fun =="mv":
			time_mv = time.time()
			cc = message_array[1]
			cm = message_array[2]
			place = tablemap.filename.index(cc)
			path_array = cc.split('/')
			ccfile = path_array[-1]
			new = cm + "/"+ ccfile
			for i in range(2):
				try:
					if place%4 == 1:
						tablemap.tablemap[0] = int(port) + tablemap.pair1[i]
						print(ccfile+" is moving on Server1,2\n\n\n\n")
					if place%4 == 2:
						tablemap.tablemap[0] = int(port) + tablemap.pair2[i]
						print(ccfile+" is moving on Server1,2\n\n\n\n")
					if place%4 == 3:
						tablemap.tablemap[0] = int(port) + tablemap.pair3[i]
						print(ccfile+" is moving on Server1,2\n\n\n\n")
					if place%4 == 0:
						tablemap.tablemap[0] = int(port) + tablemap.pair4[i]
						print(ccfile+" is moving on Server1,2\n\n\n\n")
					my_object.mv(cc,cm)
					my_object.status()
				except xmlrpclib.socket.error as err:
					print("ERROR! The server " + str(tablemap.tablemap[0]-int(port) + 1) + " is down!")
					if tablemap.tablemap[0]-int(port) == 3:
						tablemap.pair3[1] = 1
						tablemap.pair4[0] = 1
						print("down 4")
					if tablemap.tablemap[0]-int(port) == 0:
						tablemap.pair1[0] = 2
						tablemap.pair4[1] = 2
						print("down 1")
					if tablemap.tablemap[0]-int(port) == 1:
						tablemap.pair1[1] = 3
						tablemap.pair2[0] = 3
						print("down 2")
					if tablemap.tablemap[0]-int(port) == 2:
						tablemap.pair2[1] = 0
						tablemap.pair3[0] = 0
						print("down 3")
					if place%4 == 1:
						tablemap.tablemap[0] = int(port) + tablemap.pair1[i]
						print(ccfile+" is moving on Server1,2\n\n\n\n")
					if place%4 == 2:
						tablemap.tablemap[0] = int(port) + tablemap.pair2[i]
						print(ccfile+" is moving on Server1,2\n\n\n\n")
					if place%4 == 3:
						tablemap.tablemap[0] = int(port) + tablemap.pair3[i]
						print(ccfile+" is moving on Server1,2\n\n\n\n")
					if place%4 == 0:
						tablemap.tablemap[0] = int(port) + tablemap.pair4[i]
						print(ccfile+" is moving on Server1,2\n\n\n\n")
					my_object.mv(cc,cm)
					my_object.status()
					pass
				tablemap.filename[place] = new
				print(tablemap.filename)
			print("time_mv = ", time.time() - time_mv)

		if fun =="rm":
			time_rm = time.time()
			cc = message_array[1]
			place = tablemap.filename.index(cc)
			for i in range(2):
				try:
					if place%4 == 1:
						tablemap.tablemap[0] = int(port) + tablemap.pair1[i]
						print(cc+" is deleting on Server1,2\n\n\n\n")
					if place%4 == 2:
						tablemap.tablemap[0] = int(port) + tablemap.pair2[i]
						print(cc+" is deleting on Server1,2\n\n\n\n")
					if place%4 == 3:
						tablemap.tablemap[0] = int(port) + tablemap.pair3[i]
						print(cc+" is deleting on Server1,2\n\n\n\n")
					if place%4 == 0:
						tablemap.tablemap[0] = int(port) + tablemap.pair4[i]
						print(cc+" is deleting on Server1,2\n\n\n\n")
					my_object.rm(cc)
					my_object.status()
				except xmlrpclib.socket.error as err:
					print("ERROR! The server " + str(tablemap.tablemap[0]-int(port) + 1) + " is down!")
					if tablemap.tablemap[0]-int(port) == 3:
						tablemap.pair3[1] = 1
						tablemap.pair4[0] = 1
						print("down 4")
					if tablemap.tablemap[0]-int(port) == 0:
						tablemap.pair1[0] = 2
						tablemap.pair4[1] = 2
						print("down 1")
					if tablemap.tablemap[0]-int(port) == 1:
						tablemap.pair1[1] = 3
						tablemap.pair2[0] = 3
						print("down 2")
					if tablemap.tablemap[0]-int(port) == 2:
						tablemap.pair2[1] = 0
						tablemap.pair3[0] = 0
						print("down 3")
					if place%4 == 1:
						tablemap.tablemap[0] = int(port) + tablemap.pair1[i]
						print(cc+" is deleting on Server1,2\n\n\n\n")
					if place%4 == 2:
						tablemap.tablemap[0] = int(port) + tablemap.pair2[i]
						print(cc+" is deleting on Server1,2\n\n\n\n")
					if place%4 == 3:
						tablemap.tablemap[0] = int(port) + tablemap.pair3[i]
						print(cc+" is deleting on Server1,2\n\n\n\n")
					if place%4 == 0:
						tablemap.tablemap[0] = int(port) + tablemap.pair4[i]
						print(cc+" is deleting on Server1,2\n\n\n\n")
					my_object.rm(cc)
					my_object.status()
				tablemap.filename[place] = 0
				print(tablemap.filename)
			print("time_rm = ", time.time() - time_rm)


