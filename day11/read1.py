def main():
    f = open('hello.txt','r', encoding='utf-8')
    print(f.read())
    f.close()


if __name__ == "__main__":
    main()

