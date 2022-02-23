deck = Deck()
hands = []

for i in range(1, 5):    # You can change the number of players.
     hands.append(player(f'P{i}'))
    
while len(deck) > 0:  # divide the cards
    for hand in hands:
        hand.add_card(deck.pop_card())

for hand in hands: 
  print(hand)        
#print(hands[0])

for i in range(13):   # you have 13 cards
    input()
    played_cards = []
    for hand in hands:
        played_cards.append(hand.pop_card())
    
    #for card in played_cards: 
    #     print(card)
    # print(max(played_cards))
    
    winner_card = max(played_cards)
    winner_hand = hands[played_cards.index(winner_card)]
    winner_hand.round_winner()
    
    print(f"R{i}: " + ' '.join([str(card) for card in played_cards]) + f' Winner: {winner_hand.get_label()} {str(winner_card)}')
    
for hand in hands:
    print(f"Score for {hand.get_label()}: {hand.get_win_count()}")  
