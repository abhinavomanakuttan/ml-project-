import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)
 
    
    
    
    
    
    
    
'''
==================== PROPER DETAILED EXPLANATION ====================

1) import sys
----------------
The `sys` module provides access to system-specific information.
Here, it is used to get detailed information about exceptions
like:
- which file caused the error
- which line number caused the error
- traceback details

Without `sys`, we cannot access `exc_info()`.


2) from src.logger import logging
--------------------------------
This imports a custom logging configuration.
It allows errors to be logged into files or console instead of
only printing them.

WHY logging is used:
- Helps in debugging production-level applications
- Keeps a permanent record of errors
- Better than using print statements


3) def error_message_detail(error, error_detail: sys):
----------------------------------------------------
This function extracts **detailed information about an exception**
and formats it into a clean, readable error message.

Parameters:
- error        → the actual error message
- error_detail → system-level error details (sys module)

Step-by-step inside the function:

a) _, _, exc_tb = error_detail.exc_info()
-----------------------------------------
`exc_info()` returns 3 things:
1. exception type
2. exception value
3. traceback object

We only need the traceback, so the first two values are ignored
using `_`.

b) file_name = exc_tb.tb_frame.f_code.co_filename
-------------------------------------------------
This line extracts the **file name** where the error occurred.

c) exc_tb.tb_lineno
-------------------
This gives the **exact line number** where the error happened.

d) error_message = "Error occured in python script name..."
-----------------------------------------------------------
This creates a formatted error message that includes:
- File name
- Line number
- Actual error message

e) return error_message
-----------------------
Returns the final formatted error message.


4) class CustomException(Exception):
-----------------------------------
This is a **custom exception class**.
It extends Python's built-in `Exception` class.

WHY CustomException is needed:
- To standardize error handling across the project
- To give more meaningful and detailed error messages
- To avoid repeating error-handling logic everywhere


5) def __init__(self, error_message, error_detail: sys):
-------------------------------------------------------
This constructor runs when `CustomException` is raised.

Steps inside:
- Calls parent Exception constructor using `super()`
- Generates a detailed error message using
  `error_message_detail()`
- Stores the detailed message in `self.error_message`


6) def __str__(self):
--------------------
This method defines **what is printed when the exception is shown**.

Instead of printing a generic message, it prints:
- File name
- Line number
- Actual error message

This makes debugging much easier.


==================== WHY THIS DESIGN IS IMPORTANT ====================

• Makes debugging faster
• Provides clean and readable error messages
• Helps in large projects and production systems
• Used widely in ML, Data Science, and backend projects
• Industry-level exception handling pattern


==================== SIMPLE REAL EXAMPLE ====================

try:
    x = 10 / 0
except Exception as e:
    raise CustomException(e, sys)

Output will clearly show:
- File name
- Line number
- Division by zero error

====================================================================
''' 