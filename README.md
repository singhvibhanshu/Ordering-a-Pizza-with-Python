# pizzapy

*This has been forked from @Magicjarvis; the readme below is the same as his repository.*

## Disclaimer

This is my fork of [https://github.com/gamagori/pizzapi](https://github.com/gamagori/pizzapi). It's heavily modified and not well documented, but I'm going to get to that. The below example should work though.

Sorry! Was kind of in a rush this morning.

## Setup

1. Install Python 3.
2. Download this repository.
3. Install the requirements of the repository:
   ```bash
   pip install -r requirements.txt
   ```
4. Start a Python session or create a Python script.

## Usage Example

Here is an example of how to use the library:

```python
from pizzapy import Customer, StoreLocator, Order

customer = Customer("John", "Doe", "john.doe@example.com", "1234567890", "123 Pizza Street, Pizzaville")
store = StoreLocator.find_closest_store_to_customer(customer)
menu = store.get_menu()
order = Order.begin_customer_order(customer, store, menu)
order.add_item("14SCREEN") # Add a large pizza
order.pay_with(card_number="1234567812345678", exp_month="12", exp_year="25", cvv="123")
print("Order placed successfully!")
```

## Contributions

Feel free to submit pull requests or issues if you find bugs or have ideas for improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
