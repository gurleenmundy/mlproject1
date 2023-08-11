import sys
import os

# Get the absolute path of the directory containing the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the project root directory (mlproject1)
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Add the project root directory to sys.path
sys.path.append(project_root)

from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message


        