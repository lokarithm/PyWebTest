class InvalidDomTypeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'InvalidDomTypeError, {0} '.format(self.message)
        else:
            return 'InvalidDomTypeError has been raised'


# raise InvalidDomTypeError

raise InvalidDomTypeError('We have a problem')
