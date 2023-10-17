#!/usr/bin/python3
from brownie import DeployChallenge
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def print_colour(target, solved=False):
    if solved:
        print(f"{blue}Is complete: {green}{target.isComplete()}{reset}")
    else:
        print(f"{blue}Is complete: {red}{target.isComplete()}{reset}")


def hack(contract_address=None, attacker=None):
    target, _ = deploy()

    # print(target.address)
    print_colour(target, target.isComplete())

    assert target.isComplete() == True


def main():
    hack()


if __name__ == "__main__":
    main()
