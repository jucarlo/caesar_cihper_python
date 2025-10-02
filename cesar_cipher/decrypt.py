from alphabet import alphabet

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    char_list = list(original_text)
    for char in char_list:
        #print("decrypt:CHAR: " + char)
        index = alphabet.index(char)
        #print("decrypt:INDEX: " + str(index))
        index_shifted = index - shift_amount
        #print("decrypt:INDEX-SHIFTED: " + str(index_shifted))
        if index_shifted < 0:
            # 'z' is at index 25; index start at zero; 'a' is at index zero
            #print("decrypt:Index reached end of alphabet, so let's start at index " + str(len(alphabet) + index_shifted))
            char_shifted = alphabet[len(alphabet) + index_shifted]
        else:
            char_shifted = alphabet[index_shifted]
        decrypted_text = decrypted_text + char_shifted
    return decrypted_text