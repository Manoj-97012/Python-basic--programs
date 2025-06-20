

class Flashcard:
    def __init__(self,word,Meaning):
        self.word = word
        self.Meaning = Meaning

    def __str__(self):
        return self.word+'('+self.Meaning+')'

flash= []
print("welcome to flashcard application")

while(True):
    word = input("enter the name you want to add to flashcard : ")
    Meaning = input ("Enter a meaning the word :")

    flash.append(Flashcard(word,Meaning))
    option = int(input("enter 0 , if you want to add another flashcard : "))

    if (option):
        break
print("\nYour flashcards")
for i in flash:
    print(">", i)