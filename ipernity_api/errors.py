class IpernityError(Exception):
    """ Exception for Ipernity API Errors

    Parameters:
    -----------
    code: int
        Error code
    message: str
        Error message
    """
    def __init__(self, code, message):
        """Constructor

    Parameters:
    -----------
    code: int
        Error code
    message: str
        Error message
    """
        Exception.__init__(self, "%i : %s" % (code, message))
        self.code = code
        self.message = message
