from alphabet import alphabet

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    char_list = list(original_text)
    for char in char_list:
        #print("CHAR: " + char)
        index = alphabet.index(char)
        #print("INDEX: " + str(index))
        index_shifted = index + shift_amount
        #print("INDEX-SHIFTED: " + str(index_shifted))
        if index_shifted >= len(alphabet):
            # 'z' is at index 25; index start at zero; 'a' is at index zero
            #print("Index reached end of alphabet, so let's start at index " + str(index_shifted - len(alphabet)))
            char_shifted = alphabet[index_shifted - len(alphabet)]
        else:
            char_shifted = alphabet[index_shifted]
        encrypted_text = encrypted_text + char_shifted
    return encrypted_text