from pathlib import Path
import os
from write_example_file import write_example_file


def move_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    command_type, source_file_name, destination_file_name = command_parts

    if command_type == "mv":

        if source_file_name == destination_file_name:
            return

        if not Path(source_file_name).is_file():
            return

        if not Path(destination_file_name).parent.is_dir():
            os.makedirs(Path(destination_file_name).parent)

        if destination_file_name.endswith("/"):
            destination_file_name += Path(source_file_name).name

        with (open(source_file_name, "r") as source_file_object,
              open(destination_file_name, "w") as destination_file_object):
            destination_file_object.write(source_file_object.read())

        os.remove(source_file_name)


# "mv www_text_small.txt www_text_small_2.txt"
move_file("mv www_text_small.txt www_text_small_2.txt")

write_example_file()

# "mv www_text_small.txt a/b/www_text_small.txt"
move_file("mv www_text_small.txt a/b/www_text_small.txt")

write_example_file()

# "mv www_text_small.txt a/"
move_file("mv www_text_small.txt a/")

write_example_file()
