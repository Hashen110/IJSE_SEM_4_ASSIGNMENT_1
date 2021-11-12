import base64
import datetime
import json
import os
import uuid
from pathlib import Path

import click


class User:
    __path = 'db/users'

    def __init__(self, id=None, username=None, password=None, timestamp=None) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.timestamp = timestamp

    @classmethod
    def init(cls):
        Path(Path.cwd() / cls.__path).mkdir(parents=True, exist_ok=True)

    def save(self):
        data = {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'timestamp': self.timestamp
        }
        if self.id is None:
            self.id = str(uuid.uuid4())
            data['id'] = self.id
        with open(f'{self.__path}/{self.id}.json', 'w') as file:
            json.dump(data, file)

    @classmethod
    def __load(cls, id):
        try:
            with open(f'{cls.__path}/{id}', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return None

    @classmethod
    def find_by_id(cls, id):
        data = cls.__load(f'{id}.json')
        if data is None:
            return None
        return User(**data)

    def login(self):
        data = {
            'id': self.id,
            'timestamp': str(datetime.datetime.now())
        }
        with open(f'{self.__path}/_session.json', 'w') as file:
            json.dump(data, file)

    @classmethod
    def logout(cls):
        if os.path.exists(f'{cls.__path}/_session.json'):
            os.remove(f'{cls.__path}/_session.json')

    @classmethod
    def verify(cls, username, password):
        files = os.listdir(cls.__path)
        for file in files:
            data = cls.__load(file)
            if data is not None:
                dec_password = base64.b64decode(data['password']).decode('utf-8')
                if data['username'] == username and dec_password == password:
                    return User(**data)

    def __str__(self):
        return f'User(id={self.id}, username={self.username}, password={self.password}, timestamp={self.timestamp})'

    def __repr__(self):
        return f'User(id={self.id}, username={self.username}, password={self.password}, timestamp={self.timestamp})'


@click.command('register', help='User register')
@click.option('--username', prompt='User username', required=True)
@click.option('--password', prompt='User password', required=True, hide_input=True, confirmation_prompt=True)
def register(username, password):
    enc_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    usr = User(username=username, password=enc_password, timestamp=str(datetime.datetime.now()))
    usr.save()
    usr.login()
    print('User registered -', usr)


@click.command('logout', help='User logout')
def logout():
    User.logout()
    print('User logged out')


@click.command('login', help='User login')
@click.option('--username', prompt='User username', required=True)
@click.option('--password', prompt='User password', required=True, hide_input=True)
def login(username, password):
    usr = User.verify(username, password)
    if usr:
        usr.login()
        print('User logged in -', usr)
    else:
        print('Error: Invalid username or password')


@click.group()
def user():
    pass


user.add_command(register)
user.add_command(logout)
user.add_command(login)
