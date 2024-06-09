import os, sys
from .quote import Quote

INVALID_COMMAND = 'Invalid command, check the usage by running `fortune-cookie --help`'
USAGE = '''              
🥠 fortune-cookie [command]
              
fortune-cookie get
- Get a random fortune cookie quote
                        
fortune-cookie add (to be added soon)
- Add a new fortune cookie quote
'''

_directory = os.path.dirname(os.path.abspath(__file__))
_file_path = os.path.join(_directory, 'quotes.txt')


def main():
    args = sys.argv[1:]

    if len(args) > 1:
        print(INVALID_COMMAND)
        return
    
    quote = Quote(_file_path)

    if not args:
        arg = 'get'
    
    command = args[0]

    if command == 'get':
        quote.get()
    
    elif command == 'add':
        print('Please enter the new quote:')
        new_quote = input()
        quote.add(new_quote)
    
    elif command == '--help':
        print(USAGE)
    
    else:
        print(INVALID_COMMAND)
        return    


if __name__ == '__main__':
    main()
