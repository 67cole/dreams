import pytest
from src.auth import auth_register_v1, auth_login_v1
from src.error import InputError, AccessError
from src.channel import channel_messages_v1
from src.channels import channels_create_v1
from src.database import accData, channelList

def clear_v1():
    '''
    Reset Everything to default state
    '''
    global accData, channelList
    accData.clear() 
    channelList.clear() 


def search_v1(auth_user_id, query_str):
    return {
        'messages': [
            {
                'message_id': 1,
                'u_id': 1,
                'message': 'Hello world',
                'time_created': 1582426789,
            }
        ],
    }