import click

from .customer import Customer, customer
from .item import Item, item


@click.command('init', help='Initialize app')
def init() -> None:
    try:
        Customer.init()
        Item.init()
        print('Initialization complete')
    except (FileNotFoundError, OSError):
        print('Error occurred during initialization')


@click.group()
def cli() -> None:
    pass


cli.add_command(init)
cli.add_command(customer)
cli.add_command(item)
