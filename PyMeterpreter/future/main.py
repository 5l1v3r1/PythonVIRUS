#https://github.com/enthought/Python-2.7.3/blob/master/Lib/getpass.py

def getuser():
    """Get the username from the environment or password database.
    First try various environment variables, then the password
    database.  This works on Windows as long as USERNAME is set.
    """
    import os
    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
        user = os.environ.get(name)
        if user:
            return user
