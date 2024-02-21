import json

def main():
    config = {
        "title": "",
        "description": "",
        "author": "",
        "key_mappings": {}
    }

    print("Welcome to the JSON Configuration Creator for Syn MSP!")
    config["title"] = input("Enter the title of your configuration: ")
    config["description"] = input("Enter a description for your configuration: ")
    config["author"] = input("Enter the author's name: ")

    keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    print("\nPlease enter the audio file path for each key (You can also Drag N' Drop.) (WAV, FLAC, OGG supported):")
    for key in keys:
        file_path = input(f"File for key {key}: ")
        config["key_mappings"][key] = file_path

    filename = input("\nEnter the filename to save the JSON configuration (without extension): ")
    with open(f"{filename}.json", 'w') as json_file:
        json.dump(config, json_file, indent=4)

    print(f"\nConfiguration saved successfully as {filename}.json!")

if __name__ == "__main__":
    main()
