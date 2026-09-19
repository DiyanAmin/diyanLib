#Functions for inter-file data transfer
from json import load,dump,JSONDecodeError

#Simple file reading.
def store(file_path:str,data:str):
    '''
    Stores provided data to file path
    
    :param file_path: Path to file. Put the file name with extension
    :type file_path: str
    :param data: Data to be written
    :type data: str

    :return: Nothing
    :rtype: None
    '''
    with open(file_path,'w') as f:
        f.write(data)

def retrieve(file_path:str):
    '''
    Intended to be uses after store(). Retrieves the data to specified file/path
    
    :param file_path: Path to file. Put the file name with extension
    :type file_path: str

    :return: File content. New lines will use the escape sequence {backslash}n
    :rtype: str
    '''

    with open(file_path,'r') as f:
        return f.read()
    
class json_handler():
    '''
    Perfom data functions on json files.

    :param file: The json file name.
    :type file: str
    '''
    def __init__(self,file:str):
        self.file = file+'.json'

    def parse(self,data:dict):
        '''
        Parses dictionary to json file.
        
        :param data: The dictionary   
        :type data: dict
        '''
        with open(self.file,'w') as f:
            dump(data,f)
    
    def unparse(self):
        '''
        Returns the data from json file as dict
        
        :return: Data
        :rtype: dict
        '''

        try:
            with open(self.file,'r') as f:
                return load(f)
        except (FileNotFoundError,JSONDecodeError):
            return 'File not found'