# Q:- What is the logging? 
# Ans:- Recording relevant information during the execution of your program is a good practice as a Python developer 
#     when you want to gain a better understanding of your code. This practice is called logging
#            
#           The records are called logs, and they can serve as an extra set of eyes that are constantly
#     looking at your application’s flow. Logs can store information, like which user or IP accessed
#     the application. If an error occurs, then logs may provide more insights than a stack trace by 
#     telling you the state of the program before the error and the line of code where it occurred.

import logging
print("print warning")

logging.basicConfig(level=logging.DEBUG ,
                    filename="app.log",
                    encoding="utf-8",
                     filemode="a",
                    format= "{asctime} - {levelname} - {message}",
                    style="{",
                     datefmt= "%Y-%m-%d %H:%M", )

logging.warning("Remain Calm!")

# Q:- What is the logger?
# The main component of the logging module is something called the *** logger ***. You can think of 
# the logger as a reporter in your code that decides what to record, at what level of detail, and 
# where to store or send these records.


# Q:- What are the log levels?
# Ans:- Log levels are an important aspect of logging. By default, there are five standard levels
# indicating the severity of events. Each has a corresponding function that can be used to log 
# events at that level of severity.

# ""Note:"" There’s also a NOTSET log level, 

# Log Level	Function	        Description
# DEBUG	 logging.debug()	Provides detailed information that’s valuable to you as a developer.
# INFO	 logging.info()	    Provides general information about what’s going on with your program.
# WARNING	 logging.warning()	Indicates that there’s something you should look into.
# ERROR	 logging.error()	Alerts you to an unexpected problem that’s occured in your program.
# CRITICAL logging.critical()	Tells you that a serious error has occurred and may have crashed your app.


logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


# Notice that the debug() and info() messages didn’t get logged. This is because, by default, the
# logging module logs the messages with a severity level of WARNING or above. You can change that 
# by configuring the logging module to log events of all levels.


    #   ********* imp note to understand *************
# Calling basicConfig() to configure the root logger only works if the root logger hasn’t been
# configured before. All logging functions automatically call basicConfig() without arguments if 
# basicConfig() has never been called. So, for example, once you call logging.debug(), you’ll no
#  longer be able to configure the root logger with basicConfig().

# logging.getLogger().setLevel(logging.DEBUG)

# THis is how i set the logger level then i can see the messages to that level 



logging.debug("This will get logged.")

name = "saif"

logging.debug(f"{name=}")

donuts = 5
guests = 0
try :
    donuts_per_guest = donuts/guests
except ZeroDivisionError:
    logging.error(f"Can't divide by zero", exc_info=True)

try:
    donuts_per_guest = donuts / guests
except ZeroDivisionError:
   logging.exception("DonutCalculationError")

# Calling logging.exception() is like calling logging.error(exc_info=True). Since the logging.exception() function always
# dumps exception information, you should only call logging.exception() from an exception handler.
#
# When you use logging.exception(), it shows a log at the level of ERROR. If you don’t want that, you can call any of the
# other logging functions from debug() to critical() and pass the exc_info parameter as True.