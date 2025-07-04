from post_generator import generate_post

def run_edge_case_tests():
    test_cases = [
        {
            "name": "Empty Input",
            "length": "Short",
            "language": "Hinglish",
            "tag": "",
        },
        {
            "name": "Only Emojis",
            "length": "Medium",
            "language": "Hinglish",
            "tag": "💪🔥🎯",
        },
        {
            "name": "Very Long Input",
            "length": "Long",
            "language": "Hinglish",
            "tag": "Success " * 200,  # very long repeated word
        },
        {
            "name": "Non-Hinglish Characters",
            "length": "Short",
            "language": "Hinglish",
            "tag": "これはテストです",  # Japanese
        },
        {
            "name": "Tagged Input",
            "length": "Medium",
            "language": "Hinglish",
            "tag": "#motivation #grind 💼🚀",
        },
        {
            "name": "Repetitive Text",
            "length": "Short",
            "language": "Hinglish",
            "tag": "work work work work work",
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        print(f"\n--- Test Case {i}: {case['name']} ---")
        try:
            result = generate_post(case["length"], case["language"], case["tag"])
            print("Input Tag:", case["tag"])
            print("Output:\n", result)
        except Exception as e:
            print("❌ Error occurred:", str(e))

if __name__ == "__main__":
    run_edge_case_tests()
