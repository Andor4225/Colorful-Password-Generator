# Password generator application
# This script generates a random password of a specified length using letters, digits, and punctuation.

import random
import string
import time
import os
import sys
from colorama import Fore, Style

# Ensure colorama is initialized for colored output

if os.name == 'nt':
    import colorama
    colorama.init(autoreset=True)


def generate_password(length=12):
    """Generate a random password of specified length."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    """Main function to run the password generator."""
    try:
        length = int(input(Fore.MAGENTA + Style.BRIGHT +
                     "Enter the desired password length (minimum 4): "))
        password = generate_password(length)
        print(f"{Fore.CYAN}Generating your password...{Style.RESET_ALL}")
        time.sleep(2)

        print(
            f"{Fore.GREEN}Generated Password: {Style.BRIGHT}{password}{Style.RESET_ALL}")
    except ValueError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
    finally:
        print(f"{Fore.YELLOW}Exiting the password generator.{Style.RESET_ALL}")
        time.sleep(2)
        clear_choice = input(
            f"{Fore.YELLOW}Would you like to clear the terminal? (y/n): {Style.RESET_ALL}").strip().lower()
        if clear_choice == 'y':
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
            except Exception:
                print(
                    f"{Fore.RED}Warning: Unable to clear the terminal in this environment.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Terminal will not be cleared. Note: Clearing may not work in all environments (e.g., some IDEs).{Style.RESET_ALL}")
        sys.exit(0)


if __name__ == "__main__":
    main()

# This code is a simple password generator that prompts the user for a desired password length,
