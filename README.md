# word_counter
Counts words in a given file

Created this script back in 2019 for testing my Python skills. I made some minor changes to it to make it a bit cleaner and added functionality with CLI argument file path.

# Before Running
- **Optional** Edit the file path in the code or run with a command cine argument
 - Ex: Add a full file path inbetween like this `source = **r'''PATH\PATH\File.txt'''**`

# Running The Script
**Note** If using Mac or Linux you may need to specific python as **python3** in the commands
- Run code in Powershell, Command Prompt, or Terminal
 - `python word_counter.py` if source is hardcoded
 - `python word_counter.py "C:\data\file.txt"` if no source hardcoded

# Features
- Open a single file and count all words in it. Words are defined as **any** characters next to each other and separated by spaces.

# Improvements
- Option to work in a directory with multiple files
