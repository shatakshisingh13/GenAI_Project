from preprocess import extract_metadata

test_cases = [
    "Feeling low today 😞 but not giving up!",
    "Just cleared my interviews at Google! #grateful",
    "Apna time aayega 💪 #struggle",
    "Aaj ka din productive raha! Learned new things. 🚀",
    "This post is very long and consists of multiple sentences to test how the metadata extractor handles large input posts. It talks about motivation, job search and AI."
]

for i, post in enumerate(test_cases, 1):
    print(f"\n🧪 Test Case {i}")
    print(f"Input Post:\n{post}")
    try:
        result = extract_metadata(post)
        print("✅ Output:")
        print(result)
    except Exception as e:
        print("❌ Failed with error:", e)
