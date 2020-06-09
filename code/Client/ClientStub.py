'''
THIS MODULE ACTS AS A ClientStub. It receives the data from BlockLayer, and it pickles the data to send request to the server.
Besides, it receives the data from the server and loads the data from the pickle to the upper layers.
'''
import xmlrpclib, pickle, tablemap

class ClientStub():
	
	
	#REQUEST TO BOOT THE FILE SYSTEM
	def Initialize_My_FileSystem(self):
		server = xmlrpclib.ServerProxy("http://localhost:"+str(tablemap.tablemap[0]), allow_none=True)
		server.Initialize_My_FileSystem()
		print("File System Initialized!")


	#REQUEST TO FETCH THE INODE FROM INODE NUMBER FROM SERVER
	def inode_number_to_inode(self, inode_number):
		server = xmlrpclib.ServerProxy("http://localhost:"+str(tablemap.tablemap[0]), allow_none=True)
		p_inode_number = pickle.dumps(inode_number)
		into = server.inode_number_to_inode(p_inode_number)
		return pickle.loads(into)


	#REQUEST THE DATA FROM THE SERVER
	def get_data_block(self, block_number):
		server = xmlrpclib.ServerProxy("http://localhost:"+str(tablemap.tablemap[0]), allow_none=True)
		p_block_number = pickle.dumps(block_number)
		gdb = ''.join(server.get_data_block(p_block_number))
		return pickle.loads(gdb)


	#REQUESTS THE VALID BLOCK NUMBER FROM THE SERVER 
	def get_valid_data_block(self):
		server = xmlrpclib.ServerProxy("http://localhost:"+str(tablemap.tablemap[0]), allow_none=True)
		gvdb = server.get_valid_data_block()
		return pickle.loads(gvdb)


	#REQUEST TO MAKE BLOCKS RESUABLE AGAIN FROM SERVER
	def free_invalid_data_block(self, block_number):
		server = xmlrpclib.ServerProxy("http://localhost:"+str(tablemap.tablemap[0]), allow_none=True)
		p_block_number = pickle.dumps(block_number)
		server.free_invalid_data_block((p_block_number))


	#REQUEST TO WRITE DATA ON THE THE SERVER
	def update_data_block(self, block_number, block_data):
		server = xmlrpclib.ServerProxy("http://localhost:"+str(tablemap.tablemap[0]), allow_none=True)
		p_block_number = pickle.dumps(block_number)
		p_block_data = pickle.dumps(block_data)
		server.update_data_block(p_block_number, p_block_data)

	#REQUEST TO UPDATE THE UPDATED INODE IN THE INODE TABLE FROM SERVER
	def update_inode_table(self, inode, inode_number):
		server = xmlrpclib.ServerProxy("http://localhost:"+str(tablemap.tablemap[0]), allow_none=True)
		p_inode = pickle.dumps(inode)
		p_inode_number = pickle.dumps(inode_number)
		server.update_inode_table(p_inode, p_inode_number)


	#REQUEST FOR THE STATUS OF FILE SYSTEM FROM SERVER
	def status(self):
		server = xmlrpclib.ServerProxy("http://localhost:"+str(tablemap.tablemap[0]), allow_none=True)
		sta = server.status()
		return pickle.loads(sta)


