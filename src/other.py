import pytest
import re
from json import dumps
from src.auth import auth_register_v2, auth_login_v2, auth_logout_v1
from src.error import InputError, AccessError
from src.channel import channel_messages_v2
from src.channels import channels_create_v2
from src.database import data
from json import dumps, loads
from src.utils import saveData, get_user_id_from_token

def clear_v1():
    '''
    Reset Everything to default state
    '''
    data["accData"].clear() 
    data["channelList"].clear() 
    data["message_ids"].clear()
    data["dmList"].clear()
    with open("serverDatabase.json", "w") as dataFile:
        dataFile.write(dumps(data))



def search_v1(token, query_str):

    auth_user_id = get_user_id_from_token(token)
    
    if len(query_str) > 1000:
        raise InputError(description="Error: Query string is above 1000 characters")

    # Store every message in channels/dms that the user is a part of
    message_list = []
    for channel in data["channelList"]:
        if auth_user_id in channel.get("member_ids"):
            message_list.extend(channel["messages"])

    for dm in data["dmList"]:
        if auth_user_id in dm.get("member_ids"):
            message_list.extend(dm["messages"])
    
    filtered_message = list(filter(lambda message: re.search(query_str, message["message"]), message_list))
    return {
        'messages': filtered_message
    }
