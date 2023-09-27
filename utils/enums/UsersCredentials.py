from enum import Enum


class UsersCredentials(Enum):
    def __init__(self, login, password):
        self.login = login
        self.password = password

    STANDARTUSER = 'standard_user', 'secret_sauce'
    AT_ADMIN_ROLE = 'at', 'at'
    LOCKEDOUTUSER = 'locked_out_user', 'secret_sauce'
    PROBLEM_USER = 'problem_user', 'secret_sauce'
    PERFORMANCE_GLITCH_USER = 'performance_glitch_user', 'secret_sauce'



