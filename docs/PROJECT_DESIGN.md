# Project Design

## Init
- Command - `python main.py init`
- Input
  - None
- Output
  - None
- Process
  - Create necessary folders and files if not exists

## Destroy
- Command - `python main.py destroy`
- Input
  - None
- Output
  - None
- Process
  - Delete folders and files which created by `init` command

## Customer

### Create
- Command - `python main.py customer create`
- Input
  - Name
  - Address
  - Salary
- Output
  - `Customer`
- Process
  - Create customer with uuid value as json format

### Find
- Command - `python main.py customer find`
- Input
  - Id
- Output
  - `Customer` or `None`
- Process
  - Find customer by given id. If customer not found return `None`

### All
- Command - `python main.py customer all`
- Input
  - Limit (optional)
- Output
  - `Customer` list
- Process
  - Get all customers and return as a list of `Customer`

### Update
- Command - `python main.py customer update`
- Input
  - Id
  - Name (optional)
  - Address (optional)
  - Salary (optional)
- Output
  - `Customer` or `None`
- Process
  - Find customer by id and update customer fields by given values. If customer not found return `None`

### Remove
- Command - `python main.py customer remove`
- Input
  - Id
- Output
  - `Customer` or `None`
- Process
  - Find customer by id and remove customer. If customer not found return `None`


## Item

### Create
- Command - `python main.py item create`
- Input
  - Name
  - Price
  - Quantity
- Output
  - `Item`
- Process
  - Create item with uuid value as json format

### Find
- Command - `python main.py item find`
- Input
  - Code
- Output
  - `Item` or `None`
- Process
  - Find item by given code. If item not found return `None`

### All
- Command - `python main.py item all`
- Input
  - Limit (optional)
- Output
  - `Item` list
- Process
  - Get all items and return as a list of `Item`

### Update
- Command - `python main.py item update`
- Input
  - Code
  - Name (optional)
  - Price (optional)
  - Quantity (optional)
- Output
  - `Item` or `None`
- Process
  - Find item by code and update item fields by given values. If item not found return `None`

### Remove
- Command - `python main.py item remove`
- Input
  - Code
- Output
  - `Item` or `None`
- Process
  - Find item by code and remove item. If item not found return `None`


## Order

### Create
- Command - `python main.py order create`
- Input
  - Customer id
  - Date (optional)
  - Items
- Output
  - `Order`
- Process
  - Check if a customer is exists. If not Abort.
  - If date isn't provided add current timestamp to the date
  - Add items by item code. Before add item to the order item code and quantity will validate

### Find
- Command - `python main.py order find`
- Input
  - Id
- Output
  - `Order` or `None`
- Process
  - Find an order by given id. If order not found return `None`

### All
- Command - `python main.py order all`
- Input
  - Limit (optional)
- Output
  - `Order` list
- Process
  - Get all orders and return as a list of `Order`

### Update
- Command - `python main.py order update`
- Input
  - Id
  - Customer id (optional)
  - Date (optional)
- Output
  - `Order` or `None`
- Process
  - Find an order by id and update order fields by given values. Items in the order cannot update. If item not found return `None`

### Remove
- Command - `python main.py order remove`
- Input
  - Id
- Output
  - `Order` or `None`
- Process
  - Find an order by id and remove order. If order not found return `None`