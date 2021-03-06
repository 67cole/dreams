import re
from src.database import accData, channelList
from src.auth import auth_register_v1, auth_login_v1
from src.error import InputError, AccessError


def channel_invite_v1(auth_user_id, channel_id, u_id):
    return {
    }

def channel_details_v1(auth_user_id, channel_id):
    return {
        'name': 'Hayden',
        'owner_members': [
            {
                'u_id': 1,
                'name_first': 'Hayden',
                'name_last': 'Jacobs',
            }
        ],
        'all_members': [
            {
                'u_id': 1,
                'name_first': 'Hayden',
                'name_last': 'Jacobs',
            }
        ],
    }

def channel_messages_v1(auth_user_id, channel_id, start):

    #Check if user is authorised to be in the channel
    authorisation = False
    for channel in channelList:
        if channel["id"] is channel_id:
            for user in channel["member_ids"]:
                if user is auth_user_id:
                    authorisation = True
                    break
    if authorisation is False:
        raise AccessError("User is not in channel")

    # Check if user id is valid
    if valid_userid is False:
        raise AccessError("Error: Invalid user id")

    # Check if channel id is valid
    if valid_channelid is False:
        raise AccessError("Error: Invalid channel")

    # Return Function
    for channel in channelList:
        if channel["id"] is channel_id:
            messages = channel["messages"]
            
    if start > len(messages):
        raise InputError("Start is greater than total number of messages")

    # 0th index is the most recent message... therefore must reverse list?
    messages.reverse()
    
    # start + 50 messages is what is shown, so must create a list with these
    # messages within and transfer data from messages to messages_shown
    messages_shown = []
    end = start + 50
    msg_amt = 0
    while msg_amt < 50:
        # Where we start and increment from
        starting_index = start + msg_amt
        if starting_index >= end or starting_index >= len(messages):
            break
        # TO-do once iteration 2 is released
        msg = {
            'message_id': 1,
            'u_id': 1,
            'message': "Not completed send function yet",
            'time_created': 0,
        }
        messages_shown.append(msg)
        msg_amt = msg_amt + 1
    if len(messages) is 0 or counter < 50:
        end = -1
    return {
        'messages': messages_shown,
        'start': start,
        'end': end,
    }

def channel_leave_v1(auth_user_id, channel_id):
    return {
    }

def channel_join_v1(auth_user_id, channel_id):
    return {
    }

def channel_addowner_v1(auth_user_id, channel_id, u_id):
    return {
    }

def channel_removeowner_v1(auth_user_id, channel_id, u_id):
    return {
    }

# Helper Functions

def valid_userid(auth_user_id):
    # Check if user id is valid
    for user in accData:
        if user.get("id") is auth_user_id:
            return True
    return False

def valid_channelid(channel_id):
    # Check if channel id is valid
    for channel in channelList:
        if channel.get("id") is channel_id:
            return True
    return False
