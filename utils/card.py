class Symbol:
     suits = ["\u2666", "\u2665","\u2663" , "\u2660"] #["diamonds", "hearts", "clubs" , "spades" ]
     colors= ["red" , "black" ]
class Card(Symbol):
   
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    
    def __init__(self, suit, rank, color):
        self.suit = suit
        self.rank = rank
        self.color = color
    def __str__(self):
         d= f"{Card.ranks[self.rank]}{Card.suits[self.suit]}" 
         return d 
         # return self.rank , self.suit , self.color
         #a=Card.ranks[self.rank]
         #b= Card.suits[self.suit]
         #c=Card.colors[self.color] 
         #return a,b,c
          #return f"{ Card.ranks[self.rank] , Card.suits[self.suit] , self.color}" 
         # return '%s %s %s' % (Card.ranks[self.rank] , Card.suits[self.suit], Card.colors[self.color])   
     
    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank
     
#card= Card(0, 0, 1)
#card1= Card(1, 1, 0)

#print(card)
#print(card1)
#print(card> card1)
