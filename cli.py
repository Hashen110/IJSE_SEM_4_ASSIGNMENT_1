import click
from pathlib import Path

__db_path__ = 'db'
__customer_path__ = f'{__db_path__}/customers'
__item_path__ = f'{__db_path__}/items'
__order_path__ = f'{__db_path__}/orders'
__order_details_path__ = f'{__db_path__}/orders_details'
__session_path__ = f'{__db_path__}/session.db'


@click.command('init', help='Initialize app')
def init() -> None:
    Path(Path.cwd() / __customer_path__).mkdir(parents=True, exist_ok=True)
    Path(Path.cwd() / __item_path__).mkdir(parents=True, exist_ok=True)
    Path(Path.cwd() / __order_path__).mkdir(parents=True, exist_ok=True)
    Path(Path.cwd() / __order_details_path__).mkdir(parents=True, exist_ok=True)
    Path(Path.cwd() / __session_path__).touch()


@click.group()
def cli() -> None:
    pass


cli.add_command(init)
