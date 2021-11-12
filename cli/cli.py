import shutil
from pathlib import Path

import click

from .customer import Customer, customer
from .item import Item, item
from .order import Order, order
from .user import User, user


@click.command('init', help='Initialize app')
def init() -> None:
    try:
        Customer.init()
        Item.init()
        Order.init()
        User.init()
        print('Initialization complete')
    except OSError:
        print('Error occurred during initialization')


@click.command('destroy', help='Destroy initialized app')
def destroy() -> None:
    try:
        shutil.rmtree(Path.cwd() / 'db')
    finally:
        print('App destroyed')


@click.group()
def cli() -> None:
    pass


cli.add_command(init)
cli.add_command(destroy)
cli.add_command(customer)
cli.add_command(item)
cli.add_command(order)
cli.add_command(user)
