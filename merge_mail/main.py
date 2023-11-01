

with open("merge_mail/Input/Letters/starting_letter.txt") as file:
    contents = file.read()

with open("merge_mail/Input/Names/invited_names.txt") as name:
    lists = name.readlines()
    
    print(lists)
    for _ in lists:
        nam = _.strip()
        letter = contents.replace("[name]", nam)
        with open(f"merge_mail/Output/ReadyToSend/{nam}.txt", mode="r+") as send_letter:
            send_letter.write(letter)


