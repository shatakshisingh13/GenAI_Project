from post_generator import generate_post

# Sample Hinglish inputs
test_inputs = [
    "Aaj mood off hai, kal se fir grind ",
    "Kya din tha aaj! Full productivity mode ON ",
    "Bas kar yaar padhai, job chahiye ab toh "
]

# Parameters
length = "Short"
language = "Hinglish"
tag = "Motivation"

# Run test and save outputs
test_results = []

for i, input_text in enumerate(test_inputs, 1):
    print(f"Test Case {i}:")
    output = generate_post(length, language, tag)
    print(output)
    test_results.append((input_text, output))
