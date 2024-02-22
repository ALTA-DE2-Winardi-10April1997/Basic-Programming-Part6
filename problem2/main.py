def caesar(offset, input_str):
    pattern = ""
    for char in input_str:
        if char.isalpha():
            is_lower = char.islower()
            index = ord(char) - ord('a' if is_lower else 'A')
            move_index = (index+offset) % 26
            move_char = chr(move_index+ord('a' if is_lower else 'A'))
            pattern += move_char
        else:
            pattern += char

    return pattern

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl