from enum import Enum
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException, InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if self.quantity < 0:
            raise OutOfStockException
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def __repr__(self) -> str:
        return self.name

class Pumpkin(Usable):
    pass

class FaceStencil(Usable):
    pass

class Extra(Usable):
    pass

class STAGE(Enum):
    Pumpkin = 1
    FaceStencil = 2
    Extra = 3
    Pay = 4

class PumpkinMachine:
    STAGE = STAGE 
    USES_UNTIL_CLEANING = 15
    MAX_STENCILS = 3
    MAX_EXTRAS = 3

    def __init__(self):
        #rv437 and 10/22/23 this is the init method
        self.pumpkins = [
            Pumpkin(name="Mini Pumpkin", cost=1),
            Pumpkin(name="Small Pumpkin", cost=2),
            Pumpkin(name="Medium Pumpkin", cost=2.5),
            Pumpkin(name="Large Pumpkin", cost=3)
        ]
        self.face_stencils = [
            FaceStencil(name="Happy Face", quantity=10, cost=1),
            FaceStencil(name="Scream Face", quantity=10, cost=1),
            FaceStencil(name="Toothy Face", quantity=10, cost=1),
            FaceStencil(name="Spooky Face", quantity=10, cost=1)
        ]
        self.extras = [
            Extra(name="Small Candle", quantity=10, cost=.25),
            Extra(name="LED Candle", quantity=10, cost=.25),
            Extra(name="Spooky Sound Effects", quantity=10, cost=1.25),
            Extra(name="Sticker Pack", quantity=10, cost=1.00),
            Extra(name="Paint Kit", quantity=10, cost=3),
            Extra(name="Dry Ice", quantity=10, cost=.25),
            Extra(name="Googly Eyes", quantity=10, cost=.25),
            Extra(name="Glitter", quantity=10, cost=.25)
        ]

        self.remaining_uses = PumpkinMachine.USES_UNTIL_CLEANING
        self.remaining_stencils = PumpkinMachine.MAX_STENCILS
        self.remaining_extras = PumpkinMachine.MAX_EXTRAS
        self.total_sales = 0
        self.total_products = 0
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin
        
    def set_current_stage(self, stage):
        #rv437 and 10/22/23 here we are taking the current stage 
        self.currently_selecting = stage

    def get_total_sales(self):
        #rv437 and 10/22/23 here we use this ti get total sales
        return self.total_sales

    def pick_pumpkin(self, choice):
        #rv437 and 10/22/23 by using method we can pick a pumpkin
        if self.currently_selecting != STAGE.Pumpkin:
            raise InvalidStageException

        for p in self.pumpkins:
            if p.name.lower() == choice.lower():
                p.use()
                self.inprogress_pumpkin.append(p)
                self.currently_selecting = STAGE.FaceStencil
                return

        raise InvalidChoiceException("Invalid pumpkin choice.")

    def pick_face_stencil(self, choice):
        #rv437 and 10/22/23 by using this we pick face stencils
        if self.currently_selecting != STAGE.FaceStencil:
            raise InvalidStageException

        if self.remaining_uses <= 0:
            raise NeedsCleaningException

        if self.remaining_stencils <= 0:
            raise ExceededRemainingChoicesException

        for fs in self.face_stencils:
            if fs.name.lower() == choice.lower():
                fs.use()
                self.inprogress_pumpkin.append(fs)
                self.remaining_stencils -= 1
                self.remaining_uses -= 1
                self.currently_selecting = STAGE.Extra
                return

        raise InvalidChoiceException("Invalid face stencil choice.")

    def pick_extras(self, choice):
        #rv437 and 10/22/23 and here we pick extras
        if self.currently_selecting != STAGE.Extra:
            raise InvalidStageException

        if self.remaining_extras <= 0:
            raise ExceededRemainingChoicesException

        for e in self.extras:
            if e.name.lower() == choice.lower():
                e.use()
                self.inprogress_pumpkin.append(e)
                self.remaining_extras -= 1
                return

        raise InvalidChoiceException("Invalid extra choice.")

    def reset(self):
        #rv437 and 10/22/23 this method is used to reset
        self.remaining_stencils = self.MAX_STENCILS
        self.remaining_extras = self.MAX_EXTRAS
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def clean_machine(self):
        #rv437 and 10/22/23 by using method we can clean the machine
        self.remaining_uses = self.USES_UNTIL_CLEANING

    def handle_pumpkin_choice(self, _pumpkin):
        #rv437 and 10/22/23 by using this method we can handle pumpkin choice 
        if self.currently_selecting == STAGE.Pumpkin:
            self.pick_pumpkin(_pumpkin)
        else:
            raise InvalidStageException

    def handle_face_stencil_choice(self, _face_stencil):
        #rv437 and 10/22/23 by using this method we can handle face stencil choice 
        if _face_stencil == "next":
            self.currently_selecting = STAGE.Extra
        else:
            self.pick_face_stencil(_face_stencil)

    def handle_extra_choice(self, _extra):
        #rv437 and 10/22/23 here we handle extra choice
        if _extra == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_extras(_extra)

    def handle_pay(self, expected, total):
        #rv437 and 10/22/23 in this method we handle payments for our purchase 
        if self.currently_selecting == STAGE.Pay:
            try:
                total_amount = float(total)
                expected_amount = self.calculate_cost()

                if abs(total_amount - expected_amount) < 0.001:
                    print("Thank you! Enjoy your Pumpkin and Happy Halloween!")
                    self.total_products += 1
                    self.total_sales += expected_amount
                    self.reset()
                else:
                    raise InvalidPaymentException("Invalid payment amount. Please enter the exact value.")

            except ValueError:
                raise InvalidPaymentException("Invalid payment amount. Please enter a valid numerical value.")
        else:
            raise InvalidStageException

    def print_current_pumpkin(self):
        #rv437 and 10/22/23 here we can print current pumpkin
        print(f"Current Pumpkin: {', '.join([x.name for x in self.inprogress_pumpkin])}")

    def calculate_cost(self):
        #rv437 and 10/22/23 we are using this method to calculate the cost of our purchase
        total_cost = 0
        for item in self.inprogress_pumpkin:
            total_cost += item.cost
        return total_cost

    def run(self):
        #rv437 and 10/22/23 we use this method to implement all the exceptions and stages of the pumpkin vending machine 
        try:
            while True:
                if self.currently_selecting == STAGE.Pumpkin:
                    pumpkin = input(
                        f"What type of pumpkin would you like {', '.join([p.name for p in self.pumpkins if p.in_stock()])}?\n")
                    self.handle_pumpkin_choice(pumpkin)
                    self.print_current_pumpkin()
                elif self.currently_selecting == STAGE.FaceStencil:
                    stencil = input(
                        f"What type of face stencil would you like {', '.join([s.name for s in self.face_stencils if s.in_stock()])}? Or type next.\n")
                    self.handle_face_stencil_choice(stencil)
                    self.print_current_pumpkin()
                elif self.currently_selecting == STAGE.Extra:
                    extra = input(
                        f"What extras would you like {', '.join([e.name for e in self.extras if e.in_stock()])}? Or type done.\n")
                    self.handle_extra_choice(extra)
                    self.print_current_pumpkin()
                elif self.currently_selecting == STAGE.Pay:
                    expected = self.calculate_cost()
                    total = input(f"Your total is {expected}, please enter the exact value.\n")
                    self.handle_pay(expected, total)

                    choice = input("What would you like to do? (order or quit)\n")
                    if choice == "quit":
                        print("Quitting the pumpkin machine")
                        return
        except KeyboardInterrupt:
            print("Quitting the pumpkin machine")
        except OutOfStockException as e:
            #rv437 and 10/22/23 outofexception
            print(str(e))
        except NeedsCleaningException:
            #rv437 and 10/22/23 needscleanexception
            clean_choice = input("The machine needs cleaning. Type 'clean' to clean the machine or any other key to ignore.\n")
            if clean_choice.lower() == 'clean':
                self.clean_machine()
                print("Machine cleaned.")
            else:
                print("Machine was not cleaned.")
        except InvalidChoiceException as e:
            #rv437 and 10/22/23 invalidchoiceexception
            print(str(e))
        except ExceededRemainingChoicesException as e:
            #rv437 and 10/22/23 exceededremainingexception
            print(str(e))
            if self.currently_selecting == STAGE.Pumpkin:
                self.currently_selecting = STAGE.FaceStencil
            elif self.currently_selecting == STAGE.FaceStencil:
                self.currently_selecting = STAGE.Extra
        except InvalidPaymentException as e:
            #rv437 and 10/22/23 invalidpaymentexception
            print(str(e))
        except Exception as e:
            #rv437 and 10/22/23 for any other exceptions
            print(f"Something went wrong and I didn't handle it: {e}")

    def start(self):
        self.run()

if __name__ == "__main__":
    pm = PumpkinMachine()
    pm.start()