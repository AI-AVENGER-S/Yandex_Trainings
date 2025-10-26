class File:
    def __init__(self, name, creation_datetime, content=""):
        self.name = name
        self.creation_datetime = creation_datetime
        self.content = content
        self._published = False
        self._edited = False
        self._is_archive = False

    def get_name(self):
        return self.name

    def get_creation_datetime(self):
        return self.creation_datetime

    def get_content(self):
        return self.content

    def publish(self):
        self._published = True

    def is_published(self):
        return self._published

    def edit(self, new_content):
        self.content = new_content
        self._edited = True
        self._published = False

    def is_edited(self):
        return self._edited

    def extract(self):
        if self._is_archive:
            self._files.remove(self)
            self._is_archive = False

    def __lt__(self, other):
        return self._is_archive

    def __gt__(self, other):
        return self._is_archive

    def __repr__(self):
        return f"File({self.name}, {self.creation_datetime} )"

    def __str__(self):
        return f"[{self.name} ({self.creation_datetime})]\n{self.content}\n"


class ZipFile(File):
    def __init__(self, name, creation_datetime):
        super().__init__(name, creation_datetime, "")
        self._files = []

    def wrap(self, file: File):
        self._files.append(file)
        file._is_archive = True

    def get_files(self):
        return self._files.copy()

    def __ilshift__(self, file):
        self.wrap(file)

    def __repr__(self):
        return f"ZipFile({self.name}, {self.creation_datetime})"
