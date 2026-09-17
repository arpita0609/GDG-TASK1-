import json
import random
import string
import webbrowser

FILE = "/Users/arpitasinha/Downloads/urls.json"
# Load saved URLs
try:
    with open(FILE, "r") as f:
        urls = json.load(f)
except:
    urls = {}

# Generate short code
def generate_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))


while True:

    command = input("\nEnter command: ").split()

    # SHORTEN 
    if command[0] == "shorten":

        if len(command) < 2:
            print("Please enter a URL.")
            continue

        url = command[1]

        # Check URL
        if not (url.startswith("http://") or url.startswith("https://")):
            print("Invalid URL.")
            continue

        # Check duplicate URL
        already_exists = False
        for code in urls:
            if urls[code] == url:
                print("URL already exists.")
                print("Short code:", code)
                already_exists = True
                break
        if already_exists:
            continue
        # Generate unique code
        code = generate_code()
        while code in urls:
            code = generate_code()

        urls[code] = url

        # Save data
        with open(FILE, "w") as f:
            json.dump(urls, f, indent=4)

        print("Short code:", code)


  # RESOLVE
    elif command[0] == "resolve":

        if len(command) < 2:
            print("Please enter a code.")
            continue

        code = command[1]

        if code not in urls:
            print("Code not found.")
            continue

        url = urls[code]

        print("Original URL:", url)

        choice = input("Open URL? (y/n): ")

        if choice.lower() == "y":
            webbrowser.open(url)


    # LIST
    elif command[0] == "list":

        if len(urls) == 0:
            print("No URLs saved.")
        else:
            for code in urls:
                print(code, "->", urls[code])


    # EXIT
    elif command[0] == "exit":
        print("End")
        break


    else:
        print("Invalid command.")
