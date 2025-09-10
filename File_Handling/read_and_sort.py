def read_from_file(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        return sorted([word.lower() for word in file.read().split() if word[0] in ["w", "W"]])

# "Width world Wide web"
print(read_from_file("www_text_small.txt"))
# Result: ["web", "wide", "width", "world"]

# "WWW Four-bedroom farmhouse in the countryside Wave All of the four double bedrooms are en suite"
print(read_from_file("www_text_big.txt"))
# Result: ["wave", "www"]

