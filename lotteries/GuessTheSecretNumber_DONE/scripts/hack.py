#!/usr/bin/python3
from brownie import web3
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

answerHash = "0xdb81b4d58595fbbbb592d3661a34cdca14d7ab379441400cbfa1b78bc447c365"


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

    i = 0
    print(f"{red}Bruteforing the hashes{reset}")

    while i != 255:
        # print(web3.keccak(i).hex())
        if web3.keccak(i).hex() == answerHash:
            break
        i += 1
        # print(f"{red}Current i: {magenta}{i}{reset}")

    print(f"{green}Value found: {i}{reset}")
    target.guess(i, {"from": attacker, "value": "1 ether"}).wait(1)

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    hack()


if __name__ == "__main__":
    main()
