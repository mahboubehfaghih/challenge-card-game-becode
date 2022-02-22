class Hand(Deck):
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0
        
    def __str__(self):
        return self.label + ': ' + ' '.join([str(card) for card in self.deck])
    
    def get_label(self):
        return self.label
    
    def get_win_count(self):
        return self.win_count
    
    def round_winner(self):
        self.win_count = self.win_count + 1        
 
deck = Deck()
hands = []
for i in range(1, 5):
    hands.append(Hand(f'P{i}'))
    
while len(deck) > 0:
    for hand in hands:
        hand.add_card(deck.pop_card())

for hand in hands: 
  print(hand)        
print(hands[0])
for i in range(13):
    input()
    played_cards = []
    for hand in hands:
        played_cards.append(hand.pop_card())
    
    winner_card = max(played_cards)
    winner_hand = hands[played_cards.index(winner_card)]
    winner_hand.round_winner()
    
    print(f"R{i}: " + ' '.join([str(card) for card in played_cards]) + f' Winner: {winner_hand.get_label()} {str(winner_card)}')
    
for hand in hands:
    print(f"Score for {hand.get_label()}: {hand.get_win_count()}")      