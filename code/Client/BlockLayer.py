'''
THIS MODULE IS THE BLOCK LAYER OF THE FILE SYSTEM. IT ONLY DEALS WITH THE BLOCKS. THIS IS THE LOWEST LAYER OF THE FILE SYSTEM AND USES
HANDLE OF CLIENT STUDB TO CALL API FUNCTIONS OF STUB TO CONTACT TO SERVER.

'''
import ClientStub

interface = ClientStub.ClientStub()


class BlockLayer():

    #RETURNS DATA BLOCK FROM THE BLOCK NUMBER
    def BLOCK_NUMBER_TO_DATA_BLOCK(self, block_number):
        return ''.join(interface.get_data_block(block_number))


    #ASKS FOR VALID DATA BLOCK NUMBER
    def get_valid_data_block(self):
        return interface.get_valid_data_block()


    #PROVIDES BLOCK NUMBER TO MAKE BLOCK REUSABLE BY FLUSHING IT. 
    def free_invalid_data_block(self, block_number):
        interface.free_invalid_data_block(block_number)


    #PROVIDES DATA AND BLOCK NUMBER ON WHICH DATA IS TO BE WRITTEN
    def update_data_block(self, block_number, block_data):
        interface.update_data_block(block_number, block_data)
