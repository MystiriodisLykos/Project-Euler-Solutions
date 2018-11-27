import base64
import click
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def _make_fernet(password, salt):
    """ Creates a fernet instance based off the password and salt provided

    :param password: The password used for encryption
    :param salt: The salt used for encryption

    :return:
        A fernet instance that can encrypt files and decrypt files that where
        encrypted with the given password and salt
    """
    password = password.encode('utf-8')
    salt = str(salt).encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    return f


def _read_file(file):
    """ Reads a file defined by a click.Path and returns the contents in UTF-8

    :param file: file to read

    :return: contents of file in UTF-8 encoding
    """
    with open(click.format_filename(file)) as file:
        return file.read().encode('utf-8')


def _write_file(file,message):
    """ Writes a UTF-8 message to a file defined by a click.Path

    :param file: file to write to
    :param message: message to write
    """
    with open(click.format_filename(file), 'w') as file:
        file.write(message.decode('utf-8'))


@click.group(context_settings = {'help_option_names': ['-h', '--help']})
def _cli():
    pass


def add_arguments(func):
    func = _cli.command()(func)
    func = click.argument('number', type = int)(func)
    func = click.argument('password', type = str)(func)
    func = click.argument('src', type = click.Path(exists = True))(func)
    func = click.argument('dst', type = click.Path())(func)
    return func


@add_arguments
def encrypt(number, password, src, dst):
    """ encrypts the SRC file to the DST file with the PASSWRORD and problem NUMBER \f

    :param number: Project Euler problem number
    :param password: password for encryption
    :param src: source file
    :param dst: encrypted file destination
    """
    f = _make_fernet(password,number)
    encrypted = f.encrypt(_read_file(src))
    _write_file(dst, encrypted)


@add_arguments
def decrypt(number, password, src, dst):
    """ decryptes the SRC file to the DST file with the PASSWRORD and problem NUMBER \f

    :param number: Project Euler problem number
    :param password: password for decryption
    :param src: source file
    :param dst: decrypted file destination
    """
    f = _make_fernet(password,number)
    decrypted = f.decrypt(_read_file(src))
    _write_file(dst, decrypted)


if __name__ == '__main__':
    _cli()
