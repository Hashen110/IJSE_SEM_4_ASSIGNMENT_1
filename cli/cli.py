import click

from .customer import Customer, customer


@click.command('init', help='Initialize app')
def init() -> None:
    Customer.init()


@click.group()
def cli() -> None:
    pass


cli.add_command(init)
cli.add_command(customer)
