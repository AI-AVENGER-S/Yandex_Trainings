class File:
    def __init__(self, name, creation_datetime, content=""):
        self.name = name
        self.creation_datetime = creation_datetime
        self.content = content
        self._published = False
        self._edited = False
        self._parent_archive = None

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
        if self._parent_archive:
            self._parent_archive._files.remove(self)
            self._parent_archive = None

    def is_in_archive(self, archive):
        current = self._parent_archive
        while current:
            if current is archive:
                return True
            current = current._parent_archive
        return False

    def __lt__(self, other):
        if isinstance(other, ZipFile):
            return True
        return False

    def __gt__(self, other):
        if isinstance(other, File):
            return True
        return False

    def __repr__(self):
        archive_repr = repr(self._parent_archive) if self._parent_archive else None
        return f"File({self.name}, {self.creation_datetime}, {archive_repr})"

    def __str__(self):
        return f"[{self.name} ({self.creation_datetime})]\n{self.content}\n"


class ZipFile(File):
    def __init__(self, name, creation_datetime):
        super().__init__(name, creation_datetime, "")
        self._files = []

    def is_in_archive(self, archive):
        current = self._parent_archive
        while current:
            if current is archive:
                return True
            current = current._parent_archive
        return False

    def wrap(self, file):
        if file._parent_archive:
            file._parent_archive._files.remove(file)
        file._parent_archive = self
        self._files.append(file)

        if isinstance(file, ZipFile):
            for f in file.get_files():
                self.wrap(f)

    def get_files(self):
        return self._files.copy()

    def __ilshift__(self, file):
        self.wrap(file)
        return self

    def __repr__(self):
        return f"ZipFile({self.name}, {self.creation_datetime})"


# Пример использования
a = File("hello.txt", "01-06-2023 12:03", "Hello, world!")
print(repr(a))
b = ZipFile("hello.zip", "02-06-2023 10:50")
b <<= a
c = File("hello2.txt", "02-06-2023 10:53", "Привет, мир!")
b.wrap(c)
print(b.get_files())
a.extract()
print(b.get_files())
print(repr(b))
d = ZipFile("hello2.zip", "02-06-2023 11:07")
d <<= b
print("---")
print(d.get_files())
print("---")
print(c < d, c > d, d < c, d > c)  # Здесь будет вывод True False False True
d.wrap(c)
print(b.get_files(), d.get_files())
