#!/usr/bin/python3
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def print_colour(solved=0):
    if solved:
        print(f"{blue}Is complete: {green}{solved}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def hack(contract_address=None, attacker=None):
    target, nickname = deploy()
    _, attacker = get_account()

    print_colour(target.nicknameOf(attacker)[0])

    nick_name = "kalamity".encode()
    nick_name = nick_name + b"\x00" * (32 - len(nick_name))

    target.setNickname(nick_name, {"from": attacker}).wait(1)

    print_colour(target.nicknameOf(attacker)[0])

    assert target.nicknameOf(attacker)[0] != 0


def main():
    hack()


if __name__ == "__main__":
    main()
