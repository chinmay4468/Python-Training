def parse_encoded_string(encoded_string):
    parts = [part for part in encoded_string.split("0") if part]

    result = {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }
    return result

encoded_string = "Robert000Smith000123"
output = parse_encoded_string(encoded_string)
print(output)
