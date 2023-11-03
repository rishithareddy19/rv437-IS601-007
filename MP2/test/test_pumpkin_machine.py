import pytest
from PumpkinMachine import PumpkinMachine
from PumpkinMachineExceptions import InvalidStageException, OutOfStockException, InvalidChoiceException
from PumpkinMachineExceptions import ExceededRemainingChoicesException# Import the required exception
from PumpkinMachineExceptions import InvalidPaymentException

# Fixture for simulating a face stencil out of stock
#rv437 and 10/22/23 here we are trying to implement the test cases for pumpkin machine
@pytest.fixture
def out_of_stock_face_stencil():
    machine = PumpkinMachine()
    machine.face_stencils[0].quantity = 0
    return machine

# Fixture for simulating an out-of-stock face stencil by index (change as needed)
@pytest.fixture
def out_of_stock_face_stencil_by_index():
    machine = PumpkinMachine()
    # Set the first face stencil (Happy Face) quantity to 0
    machine.face_stencils[0].quantity = 0
    return machine

# Create a fixture for the pumpkin vending machine
@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm

# Test 1 - Pumpkin must be the first selection
#rv437 and 10/22/23 In this test case we are making sure that pumpkin would be the first selection
def test_pumpkin_must_be_first(machine):
    with pytest.raises(InvalidStageException):
        machine.handle_face_stencil_choice("Happy Face")

# Test 2 - Can only add face stencils if they're in stock (test against the proper stencil)
#rv437 and 10/22/23 In this test case we are implementing that we can add  face stencils only if they're in stock
def test_add_face_stencil_out_of_stock(out_of_stock_face_stencil_by_index):
    out_of_stock_face_stencil_by_index.handle_pumpkin_choice("Medium Pumpkin")
    with pytest.raises(OutOfStockException):
        out_of_stock_face_stencil_by_index.handle_face_stencil_choice("Happy Face")  # Proper stencil

# Test 3 - Can only add extras if they're in stock
#rv437 and 10/22/23 In this test case we are implementing that we can add extras for the pumpkins only if they're in stock
def test_add_extra_out_of_stock(machine):
    machine.handle_pumpkin_choice("Large Pumpkin")
    with pytest.raises(InvalidStageException):
        machine.handle_extra_choice("Fake Extra")

# Test 4 - Can add up to 3 face stencils of any combination
#rv437 and 10/22/23 Here we are writing a test case to add up to 3 face stencils of any combination
def test_add_face_stencils_combination(machine):
    machine.handle_pumpkin_choice("Medium Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    with pytest.raises(InvalidStageException):
        machine.handle_face_stencil_choice("Scream Face")
        
# Test 5 - Can add up to 3 extras of any combination
#rv437 and 10/22/23 Here we are implementing a test case to add up to 3 extras of any combination
def test_add_extras_combination(machine):
    machine.handle_pumpkin_choice("Large Pumpkin")
    with pytest.raises(InvalidStageException):
        machine.handle_extra_choice("Small Candle")

# Test 6 - Cost must be calculated properly based on the choices
# rv437 and 10/22/23 This test is parameterized to cover different pumpkin choices and costs
@pytest.mark.parametrize("pumpkin_choice, expected_cost", [
    ("Mini Pumpkin", 1),
    ("Small Pumpkin", 2),
    ("Medium Pumpkin", 2.5),
    ("Large Pumpkin", 3),
])
def test_calculate_cost(machine, pumpkin_choice, expected_cost):
    machine.handle_pumpkin_choice(pumpkin_choice)
    assert machine.calculate_cost() == expected_cost

# Test 7 - Total Sales (sum of costs) must be calculated properly
# rv437 and 10/22/23 This test is parameterized to cover different combinations of choices and costs
@pytest.mark.parametrize("pumpkin_choice, stencil_choices, extras_choices, expected_total", [
    ("Medium Pumpkin", ["Toothy Face", "Happy Face", "next", "done"], ["Paint Kit", "Small Candle", "done"], 7.75),
    ("Small Pumpkin", ["Scream Face", "Scream Face", "next", "done"], ["Sticker Pack", "Small Candle", "done"], 5.25),
    ("Medium Pumpkin", ["Toothy Face", "next", "done"], ["Paint Kit", "Small Candle", "done"], 6.75),
])
def test_total_sales(machine, pumpkin_choice, stencil_choices, extras_choices, expected_total):
    machine.set_current_stage(machine.STAGE.Pumpkin)
    machine.handle_pumpkin_choice(pumpkin_choice)

    for choice in stencil_choices:
        if choice == "next":
            machine.set_current_stage(machine.STAGE.Extra)
        elif choice == "done":
            machine.set_current_stage(machine.STAGE.Pay)
        else:
            machine.set_current_stage(machine.STAGE.FaceStencil)
            machine.handle_face_stencil_choice(choice)

    for choice in extras_choices:
        if choice == "done":
            machine.set_current_stage(machine.STAGE.Pay)
        else:
            machine.set_current_stage(machine.STAGE.Extra)
            machine.handle_extra_choice(choice)

    # Calculate the total cost
    total_cost = machine.calculate_cost()

    try:
        machine.handle_pay(expected_total, total_cost)
        assert machine.get_total_sales() == expected_total
    except InvalidPaymentException as e:
        assert str(e) == "Invalid payment amount. Please enter the exact value."
    except Exception as e:
        assert False, f"Test failed with error: {e}"

# Test 8 -  rv437 and 10/22/23 Total products variable should properly increment after a successful purchase
def test_total_products_increment(machine):
    machine.handle_pumpkin_choice("Medium Pumpkin")
    machine.handle_extra_choice("done")
    assert machine.total_products == 0  # No successful purchase yet

    machine.handle_pay(2.5, 2.5)  # Successful payment
    assert machine.total_products == 1  # After a successful purchase

    machine.handle_pumpkin_choice("Large Pumpkin")
    machine.handle_extra_choice("done")
    assert machine.total_products == 1  # No successful purchase yet

    machine.handle_pay(3, 3)  # Successful payment
    assert machine.total_products == 2  # After a successful purchase

if __name__ == "__main__":
    pytest.main()