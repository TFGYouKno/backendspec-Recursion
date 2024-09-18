Assignment: File Finder
The objective of this assignment is to create a recursive function that will continuously open and search through folders until it finds the target file (the target may not exist). To start you will be given a list that represents your systems file system, within this file system will be lists that represent folder, and strings that represent files. Each folder has the potential to hold more folders which could all contain our target file, so we need to be diligent about searching through each one of our folders no matter how deep into our file system we are. Once you have found your target print a "big HOORAY"

Tips:

- When opening a folder, you need to look through each of the contents and evaluate if the current item is the target file, and return "HOORAH" (base case)
- You also might want to check and see if the current item is another folder (hint: isinstance)
- If it is a folder you need to open that folder, and repeat the steps in this list (recursive case) (hint: remember to return your recursive calls)
Use the following code to test your 

file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"
