'''
THIS MODULE ACTS AS A ServerStub. It responses to the client, and it loads the data from the pickle to the lower layers.
Besides, it receives the data from the MemoryInterface Layer and pickles the data to send responses to the client.
'''

import SimpleXMLRPCServer, MemoryInterface4, pickle, sys

Interface = MemoryInterface4

class MyObject():

	#REQUEST TO BOOT THE FILE SYSTEM
	
	def Initialize_My_FileSystem(self):
		Interface.Initialize_My_FileSystem()


	#REQUEST TO FETCH THE INODE FROM INODE NUMBER FROM SERVER
	def inode_number_to_inode(self, p_inode_number):
		inode_number = pickle.loads(p_inode_number)
		inti = Interface.inode_number_to_inode(inode_number)
		pinti = pickle.dumps(inti)
		return pinti


	#REQUEST THE DATA FROM THE SERVER
	def get_data_block(self, p_block_number):
		block_number = pickle.loads(p_block_number)
		gbt = ''.join(Interface.get_data_block(block_number))
		pgbt = pickle.dumps(gbt)
		return pgbt


	#REQUESTS THE VALID BLOCK NUMBER FROM THE SERVER 
	def get_valid_data_block(self):
		gvdb = Interface.get_valid_data_block()
		pgvdb = pickle.dumps(gvdb)
		return pgvdb


	#REQUEST TO MAKE BLOCKS RESUABLE AGAIN FROM SERVER
	def free_invalid_data_block(self, p_block_number):
		block_number = pickle.loads(p_block_number)
		Interface.free_invalid_data_block((block_number))


	#REQUEST TO WRITE DATA ON THE THE SERVER
	def update_data_block(self, p_block_number, p_block_data):
		block_number = pickle.loads(p_block_number)
		block_data = pickle.loads(p_block_data)
		Interface.update_data_block(block_number, block_data)
	

	#REQUEST TO UPDATE THE UPDATED INODE IN THE INODE TABLE FROM SERVER
	def update_inode_table(self, p_inode, p_inode_number):
		inode = pickle.loads(p_inode)
		inode_number = pickle.loads(p_inode_number)
		Interface.update_inode_table(inode, inode_number)


	#REQUEST FOR THE STATUS OF FILE SYSTEM FROM SERVER
	def status(self):
		sta = Interface.status()
		psta = pickle.dumps(sta)
		return psta

obj = MyObject()
port = sys.argv[1]
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", int(port)), allow_none=True)
server.register_instance(obj)

print("Listening on port " + port)
server.serve_forever()
