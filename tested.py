class Player:
    def __init__(self,name,score,skip,fifty,hlps):
        self.name=name
        self.score=score
        self.skip=skip
        self.fifty=fifty
        self.hlps=hlps

    def morepoints(self):
        if self.skip and self.fifty == 1: 
            self.score+=10
        elif self.skip or self.fifty == 1: 
            self.score+=5
        else: 
            self.score+=0

    def finalscore(self): #κανει print το τελικο σκορ ενος παικτη
        print(self.name, " has scored: " + str(self.score) +" points!")
		

#ολες οι ερωτησεις, οι πιθανες απαντησεις και οι σωστες απαντησεις θα μπουν μεσα σε λιστες γιατι βολευει πολυ καλυτερα
questions = ["Who is the most awarded female artist at the Grammys?","How many octaves is Mariah Carey's vocal range?","How many keys are on most baby grand pianos?","How many Grammys has Adele won?","Who was the lead singer of the band 'Queen'?","What was Elvis Presley's middle name?","Who holds the record for most Billboard Music Awards won?","How many members are in the group BTS?","What Teen Choice Award was Twenty One Pilots nominated for in 2015?","What is Ed Sheeran's full name?"]

options = ["a. Beyoncé\nb. Mariah Carey\nc. Adele\nd. Taylor Swift\n","a. 2\nb. 3\nc. 4\nd. 5\n","a. 100\nb. 88\nc. 234\nd. 55\n","a. 7\nb. 20\nc. 15\nd. 21\n","a. Bob Dylan\nb. Mike Jagger\nc. Freddie Mercury\nd. Axl Rose\n","a. Aaron\nb. John\nc. Thomas\nd. David\n","a. Justin Bieber\nb. Adele\nc. Taylor Swift\nd. Janet Jackson\n","a. 3\nb. 4\nc. 5\nd. 7\n","a. Choice Rock Song for 'Tear In My Heart'\nb. Choice Rock Song for 'Stressed Out'\nc. Choice Music Group: Male\nd. Choice Summer Music Star: Group\n","a. Edward Arthur Sheeran\nb. Edwin Dylan Sheeran\nc. Edward Christopher Sheeran\nd. Edwin James Sheeran\n"]

lessoptions = ["a. Beyoncé\nb. Mariah Carey\n", "a. 4\nb. 5\n","a. 88\nb. 100\n","a. 21\nb. 15\n","a. Mike Jagger\nb. Freddie Mercury\n","a. Aaron\nb. Thomas\n","a. Janet Jackson\nb. Taylor Swift\n","a. 7\nb. 4\n","a. Choice Rock Song for 'Stressed Out'\nb. Choice Rock Song for 'Tear In My Heart'\n","a. Edward Arthur Sheeran\nb. Edward Christopher Sheeran\n"]

correctanswers = ["a","d","b","c","c","a","c","d","a","c"]

correctanswersfifty=["a","b","a","b","b","a","b","a","b","b"]

#η επιπλεον ερωτηση, οι πιθανες απαντησεις της και η σωστη απαντηση
extra = ["How many instruments can Park Chanyeol play?", "a. 1\nb. 2\nc. 3\nd. 4\n","c"]

print ("Welcome to the quiz!\nINSTRUCTIONS:\nThe quiz consists of 10 questions about music. Each player has 2 helps, skip and 50/50. You can only use each help once. To use the helps:\n1. Press 'skip' if you want to skip the question.\n2. Press '50/50' if you want to minimize the number of answers to 2.\nThe game ends when all players have answered the questions.\nThe players who haven't used any of their helps, will be awarded with 10 points each and the ones that have used only one help, will be awarded with 5 points each.\nLet the game begin!\n")

player1=Player(input("Name of first player: "),0,1,1,2) 
player2=Player(input("Name of second player: "),0,1,1,2)
player3=Player(input("Name of third player: "),0,1,1,2)


p=0
while p<10:
    i=0
    while i<3:
        if (i==0 and player1.hlps!=0):
            print(player1.name,", you have ",player1.skip," skips and ",player1.fifty," 50/50 helps left.")
        elif (i==1 and player2.hlps!=0):
            print(player2.name,", you have ",player2.skip," skips and ",player2.fifty," 50/50 helps left.")
        elif (i==2 and player3.hlps!=0):
            print(player3.name,", you have ",player3.skip," skips and ",player3.fifty," 50/50 helps left.")
        print(questions[p])
        print(options[p])
        answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
        if answer == (correctanswers[p]):
            print("Correct answer!\n")
            if i==0:
                player1.score +=10
            elif i==1:
                player2.score +=10
            else:
                player3.score+=10
        elif answer=="skip": #START OF SKIP          
            if i == 0:
                if player1.skip==1:
                    print(extra[0])
                    print(extra[1])
                    answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
                    if answer== (extra[2]):
                        print("Correct answer!\n")
                        player1.score +=10
                    else:
                        print("Wrong answer.\n")
                    player1.skip = 0
                    player1.hlps -= 1
                else:
                    print("You can't skip a question again.\n")#YOU CAN'T USE SKIP AGAIN!!!
                    print(questions[p])#ΟΠΟΤΕ ΤΟΥ ΞΑΝΑΒΓΑΖΕΙ ΤΗΝ ΙΔΙΑ ΕΡΩΤΗΣΗ ΠΟΥ ΕΚΑΝΕ ΣΚΙΠ
                    print(options[p])
                    answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
                    if answer == (correctanswers[p]):
                        print("Correct answer!\n")
                        player1.score +=10
                    else:
                        print("Wrong answer.")
            elif i == 1:
                if player2.skip==1:
                    print(extra[0])
                    print(extra[1])
                    answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
                    if answer== (extra[2]):
                        print("Correct answer!\n")
                        player2.score +=10
                    else:
                        print("Wrong answer.\n")
                    player2.skip = 0
                    player2.hlps -= 1
                else:
                    print("You can't skip a question again.\n")#YOU CAN'T USE SKIP AGAIN!!!
                    print(questions[p])
                    print(options[p])
                    answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
                    if answer == (correctanswers[p]):
                        print("Correct answer!\n")
                        player2.score +=10
                    else:
                        print("Wrong answer.")                  
            else:
                if player3.skip==1:
                    print(extra[0])
                    print(extra[1])
                    answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
                    if answer== (extra[2]):
                        print("Correct answer!\n")
                        player3.score +=10
                    else:
                        print("Wrong answer.\n")
                    player3.skip = 0
                    player3.hlps -= 1
                else:
                    print("You can't skip a question again.\n")#YOU CAN'T USE SKIP AGAIN!!!
                    print(questions[p])
                    print(options[p])
                    answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
                    if answer == (correctanswers[p]):
                        print("Correct answer!\n")
                        player3.score +=10
                    else:
                        print("Wrong answer.")
        elif answer=="50/50": #start of 50/50
            if i == 0:
                if player1.fifty == 1:
                    print(questions[p])
                    print(lessoptions[p])
                    answer = input("Hit 'a' or 'b' for your answer\n")
                    if answer== (correctanswersfifty[p]):
                        print("Correct answer!")
                        player1.score +=10
                    else:
                        print("Wrong answer.\n")
                    player1.fifty=0
                    player1.hlps-=1
                else:
                    print("You can't use 50/50 again.")
                    print(questions[p])
                    print(options[p])
                    answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
                    if answer == (correctanswers[p]):
                        print("Correct answer!\n")
                        player1.score +=10
                    else:
                        print("Wrong answer.")                    
            elif i == 1:
                if player2.fifty == 1:
                    print(questions[p])
                    print(lessoptions[p])
                    answer = input("Hit 'a' or 'b' for your answer\n")
                    if answer== (correctanswersfifty[p]):
                        print("Correct answer!")
                        player2.score +=10
                    else:
                        print("Wrong answer.\n")
                    player2.fifty=0
                    player2.hlps-=1
                else:
                    print("You can't use 50/50 again.")
                    print(questions[p])
                    print(options[p])
                    answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
                    if answer == (correctanswers[p]):
                        print("Correct answer!\n")
                        player2.score +=10
                    else:
                        print("Wrong answer.") 
            else:
                if player3.fifty == 1:
                    print(questions[p])
                    print(lessoptions[p])
                    answer = input("Hit 'a' or 'b' for your answer\n")
                    if answer== (correctanswersfifty[p]):
                        print("Correct answer!")
                        player3.score +=10
                    else:
                        print("Wrong answer.\n") #end of 50/50
                    player3.fifty=0
                    player3.hlps-=1
                else:
                    print("You can't use 50/50 again.")
                    print(questions[p])
                    print(options[p])
                    answer = input("Hit 'a', 'b', 'c' or 'd' for your answer\n")
                    if answer == (correctanswers[p]):
                        print("Correct answer!\n")
                        player3.score +=10
                    else:
                        print("Wrong answer.")                   
        else:
            print("Wrong answer.\n")
        i+=1
    p+=1
        

player1.morepoints()
player2.morepoints()		
player3.morepoints()

player1.finalscore()
player2.finalscore()		
player3.finalscore()


max1 = -1
max2 = -1
firstplace = ""
secondplace= ""
thirdplace = ""


if player1.score < player2.score:
    max1= player2.score
    max2=player1.score
    firstplace = player2.name
    secondplace = player1.name
    
else:
    max1=player1.score
    max2=player2.score
    firstplace = player1.name
    secondplace = player2.name

thirdplace = player3.name


if player3.score >  max1:
    max2= max1
    max1=player3.score
    thirdplace = secondplace
    secondplace = firstplace
    firstplace = player3.name
    secondplace
elif player3.score > max2:
    max2= player3.score
    thirdplace = secondplace
    secondplace = player3.name

print("The winner is: ",firstplace,"!")
print("Second place is won by: ",secondplace,"!")
print("Third place is won by: ",thirdplace,"!")
