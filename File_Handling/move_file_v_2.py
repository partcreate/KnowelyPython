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

        # 1. Prüfe, ob das Ziel ein bestehendes Verzeichnis ist.
        #    Oder ob der Name mit einem Pfadtrenner endet (z.B. "backup/").
        dir_sep = os.sep if os.sep in source_file_name else "/"

        is_destination_directory = (Path(destination_file_name).is_dir()
                                    or destination_file_name.endswith(dir_sep))

        # 2. Bilde den finalen Zielpfad korrekt.
        if is_destination_directory:
            # Wenn das Ziel ein Verzeichnis ist, füge den Dateinamen der Quelle hinzu.
            # os.path.join ist hier der korrekte Weg.
            final_destination = os.path.join(destination_file_name, os.path.basename(source_file_name))
        else:
            # Wenn das Ziel kein Verzeichnis ist, ist der Zielpfad der Dateiname selbst.
            final_destination = destination_file_name

        # 3. Stelle sicher, dass das Eltern-Verzeichnis existiert.
        parent_dir = os.path.dirname(final_destination)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        # 4. Verwende den finalen Pfad im with-Statement.
        with (open(source_file_name, "rb") as source_file_object,
              open(final_destination, "wb") as destination_file_object):
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
