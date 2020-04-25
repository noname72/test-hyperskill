class CoffeeMachine:
    machine_state = ''

    def __init__(self, water, milk, coffee, bucks, cups):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.bucks = bucks
        self.cups = cups
        self.machine_state = '__init__'

    def make_coffee(self, water, milk, coffee, bucks):
        if self.water >= water:
            print('I have enough resources, making you a coffee!')
            self.water -= water
            self.milk -= milk
            self.coffee -= coffee
            self.bucks += bucks
            self.cups -= 1
        else:
            print('Sorry, not enough water!')

    def take_action(self, action):
        self.machine_state = '__acting__'
        if action == 'buy':
            coffee_type = input(
                'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            if coffee_type == '1':
                self.make_coffee(250, 0, 16, 4)
            elif coffee_type == '2':
                self.make_coffee(350, 75, 20, 7)
            elif coffee_type == '3':
                self.make_coffee(200, 100, 12, 6)
            elif coffee_type == 'back':
                return
        elif action == 'fill':
            self.machine_state == '__refill__'
            self.water += int(input('Write how many ml of water do you want to add:'))
            self.milk += int(input('Write how many ml of milk do you want to add:'))
            self.coffee += int(input('Write how many grams of coffee beans do you want to add:'))
            self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))
        elif action == 'take':
            print('I gave you $' + str(self.bucks) + '\n')
            self.bucks = 0
        elif action == 'remaining':
            print("""The coffee machine has:
            {} of water
            {} of milk
            {} of coffee beans
            {} of disposable cups
            ${} of money""".format(self.water, self.milk, self.coffee, self.cups, self.bucks))
        else:
            self.machine_state = '__exit__'

cm = CoffeeMachine(400, 540, 120, 550, 9)
while cm.machine_state != '__exit__':
    action = input('Write action (buy, fill, take, remaining, exit):')
    cm.take_action(action)