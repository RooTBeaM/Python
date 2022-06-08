player = int(input("How many player : "))
i = 1
with open('text csv/test_text_3.txt','w+') as score_file:
    while player !=0:
        print("player {:2}".format(i))
        score = int(input("score : "))
        data = f"Player {i:2} score = {score:3}"
        score_file.write(data)
        score_file.write('\n')
        player -= 1
        i += 1
    score_file.seek(0)
    print("\n********* all recorded score *********")
    print(score_file.read())

