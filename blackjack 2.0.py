import random

suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":1}

playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def __str__(self):
        return "\n".join([str(card) for card in self.all_cards])
         

    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self,name):
        self.name = name
        
class Gameplay(Player):
    def starting_game(self,deck):
        self.add_card(deck.deal_one())
        self.add_card(deck.deal_one())
    @staticmethod    
    def play_again():
        playagain = input("Do you want to play gain? Y/N")
        return playagain.upper()
        
class Chips(Gameplay):
    def __init__(self,name):
        super().__init__(name)
        self.total = 0
        self.bet = 0
       
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
    
    def take_bet(self):
        while True:
            bet = input("Please place your bet:")
            if bet.isdigit():
                self.bet = int(bet)
                break
            else:
                print("Please enter a number")
                continue


        
class Winning_scenarios(Chips):
    def busts(self):
        if self.value > 21:
            print("{} busted, {} loss".format(self.name,self.name))
            return True
        
    @staticmethod
    def push (player,dealer):
        if player.value == dealer.value:
            print("Push, no winner")
            return True
        
    @staticmethod
    def winner(chips,player,dealer):
        if player.value > dealer.value:
            print ("{} wins {}$".format(player.name,chips.bet))
            chips.win_bet()
            
        elif player.value < dealer.value:
            print("{} wins, {} loss {}$".format(dealer.name,player.name,chips.bet))
            chips.lose_bet()
        
        
        
            
    
        
    
    
class Hand(Winning_scenarios):
    def __init__(self,name):
        super().__init__(name)
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1
        

    def adjust_for_aces(self):
        if self.value < 12 and self.aces > 0:
            self.value += 10
            
    
    def __str__(self):
        return ", ".join([str(card) for card in self.cards])
    
    def show_first_card(self):
        print(self.cards[0])
        
        
    def hit(self,deck):
        while self.value < 22:
            hit = input("Do you want to hit? Y/N")
            if hit == "Y" or hit == "y":
                self.add_card(deck.deal_one())
                self.adjust_for_aces()
                print(self)
            
            else:
                break
                
    def dealer_hit(self,deck):
        while self.value < 17:
            self.adjust_for_aces()
            self.add_card(deck.deal_one())
            self.adjust_for_aces()
                
    def replay(self):
        self.aces = 0
        self.cards = []
        self.value = 0


#Asking for name of player
name = input("Please enter your name:")               

#Creating player

player = Hand(name)
dealer = Hand("Dealer")

#setup chips

chips = Chips(player.name)

while True:
    deck = Deck()
    deck.shuffle()
    print("Welcome to the Blackjack Game")
    
    #passing the cards to dealer and player
    player.starting_game(deck)
    dealer.starting_game(deck)
    
    
    #asking for player bet
    chips.take_bet()
    
    #show cards
    print(player)
    dealer.show_first_card()
    
    while True:
        #ask to hit or stands
        player.hit(deck)
        
        #check if player busts
        if player.busts() == True:
            chips.lose_bet()
            break
        
        #dealer hit until 17
        dealer.dealer_hit(deck)
        
        #show all cards
        print(player)
        print(dealer)
        
        #check if dealer busts
        if dealer.busts() == True:
            chips.win_bet()
            break
    
        #checking the winning scenarios
        if Winning_scenarios.push(player,dealer) == True:
            break

        if Winning_scenarios.winner(chips,player,dealer) == True:
            break
        
        break


    #inform player of their chips total
    
    print("Total chips: {}".format(chips.total))
    
    if Gameplay.play_again() == "Y":
        player.replay()
        dealer.replay()
        continue
    
    
    break
    




    