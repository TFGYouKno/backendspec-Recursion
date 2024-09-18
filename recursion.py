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


def finder(folder, file):
    for x in folder:
        if x == file:
            print(f"HOORAH Target found: {file}")
            return "HOORAH"
        elif isinstance(x, list):                        
                print("list found")
                result = finder(x, file)
                if result:
                    return result


finder(file_system, target)