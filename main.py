import json
import random
import webbrowser
import sys
# --- Colorama-ს იმპორტი ---
from colorama import Fore, Style, init
init(autoreset=True) # ეს უზრუნველყოფს, რომ ფერები ავტომატურად აღდგეს

def load_episodes():
    try:
        with open('episodes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(Fore.RED + "შეცდომა: ფაილი 'episodes.json' ვერ მოიძებნა." + Style.RESET_ALL)
        sys.exit(1)
    except json.JSONDecodeError:
        print(Fore.RED + "შეცდომა: ფაილი 'episodes.json' არ შეიცავს სწორ JSON ფორმატს." + Style.RESET_ALL)
        sys.exit(1)

def get_user_choice(episodes):
    seasons = list(episodes.keys())  # ['season_1', 'season_2', ...]
    season_numbers = [s.split('_')[1] for s in seasons]

    # ფერადი სათაური ემოჯით
    print(Fore.YELLOW + Style.BRIGHT + "\n🌭 --- ცხელი ძაღლის სერიის ამორჩევა --- 🌭" + Style.RESET_ALL)
    print(f"ხელმისაწვდომი სეზონები: {Fore.GREEN + ', '.join(season_numbers) + Style.RESET_ALL}")
    print(Fore.BLUE + "შეიყვანეთ 'random' შემთხვევითი სეზონის ასარჩევად, ან 'exit' პროგრამიდან გამოსასვლელად." + Style.RESET_ALL)
    
    # მომხმარებლის შეყვანა (ფერიანი)
    choice = input(Fore.MAGENTA + "-> გთხოვთ, მიუთითეთ სეზონის ნომერი (მაგალითად: 2) ან 'random': " + Style.RESET_ALL).lower().strip()

    if choice == 'exit':
        print(Fore.RED + "პროგრამა გამორთულია." + Style.RESET_ALL)
        sys.exit(0)
    elif choice == 'random':
        chosen_season = random.choice(seasons)
        print(f"შემთხვევით არჩეული სეზონი: {Fore.YELLOW + chosen_season.split('_')[1] + Style.RESET_ALL}")
    else:
        try:
            chosen_number = int(choice)
            chosen_season = f"season_{chosen_number}"
        except ValueError:
            chosen_season = choice 
        
        if chosen_season not in episodes:
            print(Fore.RED + "შეყვანილი სეზონი არ არსებობს ან მნიშვნელობა არასწორია." + Style.RESET_ALL)
            sys.exit(1)
        
    return chosen_season

def select_episode(episodes, season):
    episode_links = episodes.get(season, [])
    if not episode_links:
        print(Fore.RED + f"შეცდომა: სეზონში ({season}) სერიები ვერ მოიძებნა." + Style.RESET_ALL)
        sys.exit(1)
        
    chosen_link = random.choice(episode_links)
    return chosen_link

if __name__ == "__main__":
    episodes = load_episodes()
    season = get_user_choice(episodes)
    link = select_episode(episodes, season)
    
    # შედეგის ფერადი ჩვენება
    print(Fore.CYAN + Style.BRIGHT + "\n--- არჩეულია! ---" + Style.RESET_ALL)
    print(f"სეზონი: {Fore.YELLOW + season.split('_')[1] + Style.RESET_ALL}")
    print(f"ბმული: {Fore.BLUE + link + Style.RESET_ALL}")
    
    try:
        webbrowser.open(link)
        print(Fore.GREEN + "ბმული გაიხსნა ბრაუზერში. სასიამოვნო ყურებას გისურვებთ!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"შეცდომა ბრაუზერის გახსნისას: {e}. გთხოვთ, ბმული ხელით გახსნათ." + Style.RESET_ALL)
