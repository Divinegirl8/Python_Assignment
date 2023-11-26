from diary_package.entry import Entry


class Diary:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__is_locked = True
        self.__entry_size = 0
        self.__entries = []

    def unlock_diary(self, password):
        self.validate_password(password)
        self.__is_locked = False

    def validate_password(self, password):
        if self.__password != password:
            raise RuntimeError("Invalid password")
        return self.__password == password

    def is_locked(self):
        return self.__is_locked

    def lock_diary(self):
        self.__is_locked = True

    def create_entry(self, title, body):
        if self.__is_locked:
            raise RuntimeError("cannot create entry because diary is locked")
        self.__entry_size += 1
        entry = Entry(self.generate_entry_id(), title, body)
        self.__entries.append(entry)

    def get_number_of_entry(self):
        return len(self.__entries)

    def generate_entry_id(self):
        return int(f"19{self.__entry_size}")

    def delete_entry(self, id_number):
        self.__entries.remove(self.find_entry_by_id(id_number))

    def find_entry_by_id(self, id_number):
        if self.__is_locked:
            raise RuntimeError("cannot create entry because diary is locked")
        for value in self.__entries:
            if value.get_id() == id_number:
                return value
        raise RuntimeError("Entry id not found")

    def update(self, id_number, title, body):
        if self.__is_locked:
            raise RuntimeError("cannot create entry because diary is locked")
        entry = self.find_entry_by_id(id_number)
        entry.edit_entry(title, body)
        self.__entries[self.find_index_of(id_number)] = entry

    def find_index_of(self, id_number):
        for index, value in enumerate(self.__entries):
            if value.get_id() == id_number:
                return index
        raise RuntimeError("Entry id not found")

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
