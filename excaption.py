class NotValidURL(Exception):
    def __init__(self, if_obj, message='URL Is Not Str but he'):
        self.if_obj = if_obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} {type(self.if_obj)}'

