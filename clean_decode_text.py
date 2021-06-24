

string_with_nonASCII = "àa string withé fuünny charactersß."


encoded_string = string_with_nonASCII.encode("ascii", "ignore")
decode_string = encoded_string.decode()

print(decode_string)

string_with_nonASCII ="The SANDF has been deployed to assist in the provinceâ€™s response to the COVID-19 pandemic."
encoded_string = string_with_nonASCII.encode("ascii", "ignore")
decode_string = encoded_string.decode()

print(decode_string)