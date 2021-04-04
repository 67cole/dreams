import sys
from json import dumps, loads
from flask import Flask, request, abort
from flask_cors import CORS
from src.error import InputError, AccessError
from src import config
from src.database import data, secretSauce
from src.auth import auth_register_v2, auth_login_v2, auth_logout_v1
from src.utils import saveData
from src.other import clear_v1

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)

# ##############################################################################
# DATABASE FUNCTIONS

# Open database
with open("serverDatabase.json", "r") as dataFile:
    global data
    data = loads(dataFile.read())
    
'''
# Returns serverDatabase
def getData():
    global data
    return data
'''

# ##############################################################################
# AUTH FUNCTIONS

@APP.route("/auth/register/v2", methods=["POST"])
def authRegister():
    inputData = request.get_json()
    returnData = auth_register_v2(
            inputData["email"], inputData["password"], inputData["name_first"], inputData["name_last"])
    saveData()

    return dumps(returnData)

@APP.route("/auth/login/v2", methods=["POST"])
def authLogin():
    inputData = request.get_json()
    returnData = auth_login_v2(inputData["email"], inputData["password"])
    saveData()
    return dumps(returnData)

@APP.route("/auth/logout/v1", methods=["POST"])
def authLogout():
    inputData = request.get_json()
    returnData = auth_logout_v1(inputData)
    saveData()
    return dumps(returnData)


# #############################################################################
#                                                                             #
#                           MESSAGE FUNCTIONS                                 #
#                                                                             #
# #############################################################################

@APP.route("/message/send/v2", methods=["POST"])
def messageSend():
    inputData = request.get_json()
    returnData = message_send_v2(inputData["token"], inputData["channel_id"], inputData["message"])
    saveData()
    return dumps(returnData)

@APP.route("/message/edit/v2", methods=["PUT"])
def messageEdit():
    inputData = request.get_json()
    returnData = message_edit_v2(inputData["token"], inputData["message_id"], inputData["message"])
    saveData()
    return dumps(returnData)

@APP.route("/message/remove/v1", methods=["DELETE"])
def messageRemove():
    inputData = request.get_json()
    returnData = message_remove_v1(inputdata["token"], inputData["message_id"])
    saveData()
    return dumps(returnData)
    





# #############################################################################
#                                                                             #
#                           CHANNEL FUNCTIONS                                 #
#                                                                             #
# #############################################################################

@APP.route("/channel/addowner/v1", methods=["POST"])
def channelAddowner():
    inputData = request.get_json()
    returnData = channel_addowner_v1(inputData["token"], inputData["channel_id"], inputData["u_id"])
    saveData()
    return dumps(returnData)




# ##############################################################################




@APP.route("/clear/v1", methods=["DELETE"])
def clearAll():
    clear_v1()
    return {}

# Example
@APP.route("/echo", methods=['GET'])
def echo():
    data = request.args.get('data')
    if data == 'echo':
   	    raise InputError(description='Cannot echo "echo"')
    return dumps({
        'data': data
    })

if __name__ == "__main__":
    APP.run(port=config.port) # Do not edit this port


