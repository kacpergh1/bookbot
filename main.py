def main():
    path_to_file = "frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        
        number_of_words = len(file_contents.split())
        print(number_of_words)
        


if __name__ == "__main__":
    main()


