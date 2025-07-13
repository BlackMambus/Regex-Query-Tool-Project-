import re

def regex_query_tool():
    print("🔍 Welcome to the Regex Query Tool!")
    print("Enter your regular expression and the target text to find matches.\n")

    # Get user input
    pattern = input("Enter your regex pattern: ")
    text = input("Enter the text to search in: ")

    try:
        # Compile the regex pattern
        regex = re.compile(pattern)
        matches = regex.findall(text)

        if matches:
            print(f"\n✅ Found {len(matches)} match(es):")
            for i, match in enumerate(matches, 1):
                print(f"{i}. {match}")
        else:
            print("\n❌ No matches found.")
    except re.error as e:
        print(f"\n⚠️ Invalid regex pattern: {e}")

if __name__ == "__main__":
    regex_query_tool()



