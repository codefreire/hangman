import random
import os

def title():
    print(""" 
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/                       """)


def hangman(indice):
    hangman = ["""
                          ____
                          |/  |
                          |   
                          |    
                          |    
                          |    
                          |
                          |_____
                            """,
                            """
                          ____
                          |/  |
                          |  (_)
                          |    
                          |    
                          |    
                          |
                          |_____
                            """,
                            """
                          ____
                          |/  |
                          |  (_)
                          |   |
                          |   |
                          |    
                          |
                          |_____
                            """,
                            """
                          ____
                          |/  |
                          |  (_)
                          |  \|
                          |   |
                          |    
                          |
                          |_____
                            """,
                            """
                          ____
                          |/  |
                          |  (_)
                          |  \|/
                          |   |
                          |    
                          |
                          |_____
                            """,
                            """
                          ____
                          |/  |
                          |  (_)
                          |  \|/
                          |   |
                          |  / 
                          |
                          |_____
                            """,
                            r"""
                          ____
                          |/  |
                          |  (_)
                          |  \|/
                          |   |
                          |  / \
                          |
                          |_____
                            """,
                            r"""
                          ____
                          |/  |
                          |  (_)
                          |  /|\
                          |   |
                          |  | |
                          |
                          |_____
                            """
            ]
    print(hangman[indice])


def run():
    word_list = ['CRIPTOGRAFIA', 'METAVERSO', 'JAVASCRIPT', 'DATABASE',
                'INTERNET', 'CONTRATAME', 'AUTOMATIZACION', 'FULLSTACK']
    word = word_list[random.randint(0,len(word_list)-1)]
    spaces = '_'*len(word)
    aux = list(spaces)
    attempts = 0
    verify = False

    while attempts != 8:
        os.system('cls')
        title()
        hangman(attempts)
        verify = False
        print('\t\t\t',spaces)
        if spaces == word:
            print('YOU WIN!')
            break
        if attempts == 7:
            print('The word was: {}'.format(word))
            break
        letter = input('Enter a letter: ')
        for e in range(len(word)):
            if word[e] == letter.upper():
                aux[e] = letter.upper()
                spaces = ''.join(aux)
                verify = True
        if verify == False:
            attempts += 1


if __name__=='__main__':
    run()