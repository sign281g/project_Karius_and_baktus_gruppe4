import sqlite3
from bottle import default_app, route, template, run, app, request, post
import log_manager
import db_manager


#How to log: use log_manager.log_func(). This func has 3 string arguments: 1) is for exceptions. If not used, leave blank. 2) The message we want to log. 3) Log type (See log_manager.py)
logger=log_manager.logging.getLogger(__name__)



def log_test():
    print(log_manager.log_func("","startup failed","error"))
    
def start():
    try:
        db_manager.init_db()
        db_manager.find_db()
        db_manager.create_db_user_table()
        db_manager.create_db_login_table()
        #db_manager.add_user("Bob","21", "Male","Kaktusbæk 54, Rødby","ESP32-5130","150.122.69.123","9c:51:6f:19:3c:0f")
        #db_manager.change_user_info("4feb8613-e1d6-4457-87ad-e738d3dda8d3", "emil", "69", "female", "Holgasville 25", "", "", "", "")
        #db_manager.add_admin("test_admin", "admin", "")
        #log_test()
    except Exception as e:
        print(log_manager.log_func(e,"startup failed","error"))
        exit()

#If running the application locally, keep this setting on 'True'. If running through pythonanywhere, set to 'False'
local_app=True
try:
    start()
    if local_app==False:
        @route('/')
        def hello_world():
            return template("templates/test.html")
        application = default_app()
    elif local_app==True:
        @route('/')
        def home():
            return template("templates/test.html")
        run(host='localhost', port=8000, debug=True)
    
except Exception as e:
    print(log_manager.log_func(e,"Could not determine local or online","error"))
    exit()




#Password: BørstDineTænder555!