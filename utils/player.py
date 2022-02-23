import random

class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
              if suit == '\u2666' or suit=='\u2665' :
                   self.deck.append(Card(suit, rank, "red"))
              else :
                   self.deck.append(Card(suit, rank, "black" ))
               #for color in ["red" , "black" ]:
                 # self.deck.append(Card(suit, rank, color))
        self.shuffle()
        
    def __len__(self):      #the number of card
        return len(self.deck)
    
    def add_card(self, card):
        self.deck.append(card)
        
    def pop_card(self):
        return self.deck.pop()
    
    def shuffle(self):
        random.shuffle(self.deck)    


#deck= Deck()
#card1= Card(1, 1, 0)
#deck.add_card(card1)
#deck.shuffle()
#print(deck.pop_card())
#print(len(deck ))

