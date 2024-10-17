def main():
    path_to_file = "frankenstein.txt"
    with open(path_to_file) as f:
        
        file_contents = f.read()
        number_of_words = len(file_contents.split())
        
    character_number = {}
    for character in file_contents:
        character = character.lower()
        if character in character_number:
            character_number[character] += 1
        else:
            character_number[character] = 1
    
    character_number.sort(reverse=True)
    print(character_number)



if __name__ == "__main__":
    main()