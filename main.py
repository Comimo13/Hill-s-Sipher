"""This is Hill's Sipher based on NumPy. Currently I'm learning NumPy as well don't judge strictly"""
from dbm import error

from Core import Encryption
try:
    Encryption.encrypt()
except Exception as e:
    print('fatal error: ',e)