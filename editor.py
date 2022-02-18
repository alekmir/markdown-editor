result = str()
legal = ['plain',
         'bold',
         'italic',
         'inline-code',
         'link',
         'header',
         'new-line',
         'ordered-list',
         'unordered-list',
         '!help',
         '!done']


def header():
    global result
    level = int(input('Level: '))
    if 0 < level < 7:
        text = input('Text: ')
        result += "#" * level + " " + text + "\n"
    else:
        print("The level should be within the range of 1 to 6")
        header()


def ordered_list():
    global result
    rows_count = int(input("Number of rows: "))
    ord_list = str()
    if rows_count > 0:
        start_pos = 1
        while start_pos <= rows_count:
            ord_list += f"{start_pos}. " + input(f"Row #{start_pos}: ") + "\n"
            start_pos += 1
    else:
        print("The number of rows should be greater than zero")
        ordered_list()
    result += ord_list


def unordered_list():
    global result
    rows_count = int(input("Number of rows: "))
    unord_list = str()
    start_pos = 1
    if rows_count > 0:
        while rows_count > 0:
            unord_list += f"* " + input(f"Row #{start_pos}: ") + "\n"
            rows_count -= 1
            start_pos += 1
    else:
        print("The number of rows should be greater than zero")
        unordered_list()
    result += unord_list


while True:
    user_input = input('Choose a formatter: ')
    if user_input not in legal:
        print('Unknown formatting type or command')
    elif user_input == "!help":
        print('Available formatters: plain bold italic inline-code link header new-line\n'
              'Special commands: !help !done')
    elif user_input == "!done":
        with open('output.md', 'w') as file:
            file.write(result)
        break
    else:
        if user_input == "plain":
            result += input("Text: ")
        elif user_input == "bold":
            result += "**" + input("Text: ") + "**"
        elif user_input == "italic":
            result += "*" + input("Text: ") + "*"
        elif user_input == "inline-code":
            result += "`" + input("Text: ") + "`"
        elif user_input == "link":
            result += "[" + input('Label: ') + "]" + "(" + input('URL: ') + ")"
        elif user_input == "header":
            header()
        elif user_input == "new-line":
            result += "\n"
        elif user_input == "ordered-list":
            ordered_list()
        elif user_input == "unordered-list":
            unordered_list()
        else:
            print('Something went wrong!')
        print(result)
