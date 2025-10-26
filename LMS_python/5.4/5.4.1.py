class File:
    def __init__(self, name, creation_datetime, content):
        self.name = name
        self.creation_datetime = creation_datetime
        self.content = content

    def get_name(self):
        return self.name

    def get_creation_datetime(self):
        return self.creation_datetime

    def get_content(self):
        return self.content
