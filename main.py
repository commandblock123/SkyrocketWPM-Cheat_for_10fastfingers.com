from art import text2art
import SkyrocketWPM

def start():
    title = text2art("SkyrocketWPM")
    print(title)
    selection()

def selection():
    print('\n')
    print('[1] Singleplayer/Competition')
    print('[2] Anticheat (not implemented yet)')
    print('[3] EXIT')
    print('')
    selection = input('Please choose an option. ')


    if selection == '1':
        selection = input('singleplayer or competition? ')
        # singleplayer: browser.get("https://10fastfingers.com/typing-test/english")
        # multiplayer: browser.get("https://10fastfingers.com/competitions")
        # singleplayer: wordElement = browser.find_element(By.XPATH, f'/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[{counter}]')
        # multiplayer: wordElement = browser.find_element(By.XPATH, f'/html/body/div[4]/div/div[4]/div/div[1]/div[3]/div[1]/div/span[{counter}]')
        if selection == 'singleplayer':
            website_link = 'https://10fastfingers.com/typing-test/english'
            XPATH1 = '/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span['
            XPATH2 = ']'
            SkyrocketWPM.start(website_link, XPATH1, XPATH2)
        if selection == 'competition':
            website_link = 'https://10fastfingers.com/competitions'
            XPATH1 = '/html/body/div[4]/div/div[4]/div/div[1]/div[3]/div[1]/div/span['
            XPATH2 = ']'
            SkyrocketWPM.start(website_link, XPATH1, XPATH2)

    if selection == '2':
        print('not implemented yet')
        exit()

    if selection == '3':
        exit()

    print('invalid selection')

if __name__ == '__main__':
    start()
