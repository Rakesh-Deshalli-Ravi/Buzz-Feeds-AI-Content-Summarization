from .db_operations.db_user_interest import *

def set_user_interests(useremail,interests):
    print(useremail,interests)
    return set_userinterest(useremail,interests)