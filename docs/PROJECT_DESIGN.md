# Project Design

## Init
- Command - `python main.py init`
- Input
  - None
- Output
  - None
- Process
  - Create necessary folders and files if not exists

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