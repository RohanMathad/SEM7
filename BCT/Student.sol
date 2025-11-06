// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    // Structure to store student details
    struct Student {
        uint id;
        string name;
        uint age;
    }

    // Array to store multiple students
    Student[] public students;

    // Function to add new student
    function addStudent(uint _id, string memory _name, uint _age) public {
        students.push(Student(_id, _name, _age));
    }

    // Function to get total number of students
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // Fallback function
    fallback() external payable {
        // This gets triggered if any unknown function or ether is sent
    }

        // Receive function (optional)
    receive() external payable {
        // This runs when Ether is sent without data
    }

}
