def main():
    path_to_file = "/root/workspace/github.com/kacpergh1/bookbot/books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

if __name__ == "__main__":
    main()
