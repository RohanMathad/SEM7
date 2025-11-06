// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    // variable to store balance
    uint256 public balance;

    // function to deposit money
    function deposit(uint256 amount) public {
        balance += amount;
    }

    // function to withdraw money
    function withdraw(uint256 amount) public {
        require(balance >= amount, "Not enough balance");
        balance -= amount;
    }

    // function to show balance
    function getBalance() public view returns (uint256) {
        return balance;
    }
}
