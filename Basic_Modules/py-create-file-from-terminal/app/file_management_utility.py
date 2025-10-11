import sys
import os
from datetime import datetime
from typing import LiteralString


class MissingArgumentError(Exception):

    def __init__(self,
                 flag: str = "",
                 message: str = "A required argument is missing."
                 ) -> None:
        self.message = message
        self.flag = flag
        super().__init__(self.message)

    def __str__(self) -> str:
        message_map = {
            "-d": "A directory name is required.",
            "-f": "A file name is required."
        }
        if self.flag in message_map:
            return f"{self.message} \n\n{message_map[self.flag]}"
        return self.message


class MissingFlagError(MissingArgumentError):

    def __init__(
            self,
            message: str = "A required flag is missing."
    ) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return (
            f"{self.message} \n\n"
            f"You must provide at least a -d flag "
            f"and a directory name to create a directory. \n"
            f"Usage: python {sys.argv[0]} -d <directory_name> \n"
            f"Usage for recursive directories: "
            f"python {sys.argv[0]} "
            f"-d <directory_name> <directory_name> \n\n"
            f"You must provide at least a -f flag "
            f"and a file name to create a file. \n"
            f"Usage: python {sys.argv[0]} -f <file_name> \n\n"
            f"Usage for recursive files: "
            f"python {sys.argv[0]} -d <directory_name> -f <file_name> \n"
        )


def make_path(parts: list) -> LiteralString | str | bytes:
    path = ""

    if len(parts) == 1:
        path = os.path.join(parts[0])
    else:
        path = os.path.join(parts[0], *parts[1:])

    return path


def create_directories(directory_path: LiteralString | str | bytes) -> bool:
    try:
        os.makedirs(directory_path, exist_ok=True)
    except OSError as ex:
        print(f"Error creating directory: {ex}")
        return False
    else:
        return True


def write_to_file(filename: LiteralString | str | bytes) -> None:
    open_mode = "x"

    if os.path.exists(filename):
        open_mode = "a"

    with open(filename, "a") as file:

        input_counter = 1

        while True:
            user_input = input("Enter content line: ")

            if user_input == "stop":
                break

            if input_counter == 1:

                if open_mode == "a":
                    file.write("\n")

                date_format = "%Y-%m-%d %H:%M:%S"

                file.write(f"{datetime.now().strftime(date_format)}\n")

            file.write(f"{input_counter} {user_input}\n")

            input_counter += 1


def get_args_for_flag(flag: str, args_list: list[str]) -> list[str]:
    """Extrahiert die Argumente für ein bestimmtes Flag aus einer Liste von Argumenten."""
    try:
        flag_index = args_list.index(flag)
        next_flag_index = len(args_list)
        # Findet den Index des nächsten Flags oder das Ende der Liste
        for i in range(flag_index + 1, len(args_list)):
            if args_list[i].startswith('-'):
                next_flag_index = i
                break
        return args_list[flag_index + 1:next_flag_index]
    except ValueError:
        return [] # Flag nicht gefunden


def process_arguments() -> None:
    command_line_args = sys.argv[1:] # Skriptname ausschließen

    if not command_line_args:
        raise MissingFlagError()

    has_d_flag = "-d" in command_line_args
    has_f_flag = "-f" in command_line_args

    if has_d_flag:
        dir_args = get_args_for_flag("-d", command_line_args)
        if not dir_args:
            raise MissingArgumentError("-d")
        
        dir_path = make_path(dir_args)
        if create_directories(dir_path):
            if has_f_flag:
                file_args = get_args_for_flag("-f", command_line_args)
                if not file_args:
                    raise MissingArgumentError("-f")
                filename = file_args[0]
                file_path = make_path([dir_path, filename])
                write_to_file(file_path)
    elif has_f_flag: # Wenn nur -f vorhanden ist (oder -f das erste Flag ist)
        file_args = get_args_for_flag("-f", command_line_args)
        if not file_args:
            raise MissingArgumentError("-f")
        filename = file_args[0]
        write_to_file(make_path([filename]))
    else:
        # Weder -d noch -f wurde als gültiges Start-Flag gefunden
        raise MissingFlagError()


# Hauptausführung des Skripts
if __name__ == "__main__":
    try:
        process_arguments()

    except MissingFlagError as e: # Die spezifischere Fehlermeldung zuerst abfangen
        print(f"Error: {e}")
        sys.exit(2)
    except MissingArgumentError as e: # Dann die allgemeinere Fehlermeldung
        print(f"Error: {e}")
        sys.exit(2)
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
        sys.exit(1)
