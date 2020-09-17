class FilePath:
    file_path_part: str
    file_name: str

    def __init__(self, file_path):
        try:
            last_slash_index = file_path.rindex('/') + 1
            self.file_path_part = file_path[:last_slash_index]
            self.file_name = file_path[last_slash_index:]
        except:
            self.file_path_part = ''
            self.file_name = file_path

    def get_path_part(self):
        return self.file_path_part

    def get_filename_part(self):
        return self.file_name

    def get_extension(self):
        try:
            last_dot_index = self.file_name.rindex('.')
            return self.file_name[last_dot_index + 1:]
        except:
            return ''


assert(FilePath("log/cups/access_log").file_path_part == "log/cups/")
assert(FilePath("log/cups/access_log").file_name == "access_log")
assert(FilePath("log/cups/access_log").get_path_part() == "log/cups/")
assert(FilePath("log/cups/").get_path_part() == "log/cups/")
assert(FilePath("cups/access_log").get_path_part() == "cups/")
assert(FilePath("access_log").get_path_part() == "")
assert(FilePath("log/cups/access_log").get_filename_part() == "access_log")
assert(FilePath("log/cups/").get_filename_part() == "")
assert(FilePath("cups/access_log").get_filename_part() == "access_log")
assert(FilePath("access_log").get_filename_part() == "access_log")
assert(FilePath("log/cups/access_log").get_extension() == "")
assert(FilePath("base/FileHelper.cpp").get_extension() == "cpp")
assert(FilePath("base/FileHelper.cpp.bak").get_extension() == "bak")
assert(FilePath("src/base.tmp/").get_extension() == "")