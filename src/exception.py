import sys
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
    


'''
DETAILED EXPLANATION OF THE CODE

1. import sys
   - The sys module provides access to system-level information.
   - In this code, sys is used to fetch exception details such as
     traceback, file name, and line number where the error occurred.

2. from src.logger import logging
   - This imports a custom logging object.
   - Logging is typically used to store error messages in log files
     instead of printing them on the console.
   - Although logging is not directly used here, it is commonly
     included for future error logging in production systems.

3. error_message_detail(error, error_detail)
   - This function extracts detailed information about an exception.
   - error       → the actual exception message.
   - error_detail → the sys module used to access exception metadata.

4. error_detail.exc_info()
   - Returns a tuple: (exception_type, exception_value, traceback).
   - The traceback object contains information about where the error occurred.
   - The first two values are ignored using '_'.

5. exc_tb.tb_frame.f_code.co_filename
   - Retrieves the name of the Python file in which the error occurred.

6. exc_tb.tb_lineno
   - Retrieves the line number where the exception was raised.

7. Formatted error message
   - Combines file name, line number, and error message
     into a clean, readable string.

8. CustomException class
   - This is a user-defined exception class.
   - It inherits from Python’s built-in Exception class.
   - Used to raise meaningful and detailed errors in large applications.

9. __init__ method
   - Calls the parent Exception constructor using super().
   - Generates a detailed error message using error_message_detail().

10. __str__ method
    - Defines what is displayed when the exception is printed.
    - Returns the formatted detailed error message instead of
      a generic Python error.

OVERALL PURPOSE:
- This code provides structured and detailed error handling.
- It helps identify:
  • Which file caused the error
  • At which line number
  • What the exact error message is
- Commonly used in Machine Learning, Data Science, and
  production-level Python projects.
'''