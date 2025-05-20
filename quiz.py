# Exercício - sistema de perguntas e respostas
list_questions = [
    {
        'Question': 'What is the largest planet in our solar system?',
        'Option': ['Earth', 'Jupiter', 'Saturn', 'Mars'],
        'Answer': 'Jupiter',
    },
    {
        'Question': 'Who painted the Mona Lisa?',
        'Option': ['Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Michelangelo'],
        'Answer': 'Leonardo da Vinci',
    },
    {
        'Question': 'Which country is known as the “Land of the Rising Sun”?',
        'Option': ['China', 'Japan', 'South Korea', 'Thailand'],
        'Answer': 'Japan',
    },
]
hit = 0 
while True: 
    for dict_questions in list_questions:
        for keys in dict_questions:
            if keys == 'Question':
                print(f'{keys}: {dict_questions[keys]}')
            elif keys == 'Option':
                for position, value in enumerate(dict_questions[keys]):
                    print(f'{position}) {value}')

                try:
                    user_index_choice = int(input('Chose one option:\n >'))
                    user_answer_value = dict_questions[keys][user_index_choice]
                    if user_answer_value == dict_questions['Answer']:
                        print('You Got It!✅')
                        print(50*'-')
                        hit += 1
                    else:
                        print('You Got got It Wrong!❌')
                        print(50*'-')
                except (ValueError, IndexError):
                    print('Invalid Option. Please Try Again.')
    print(f'You Got {hit} right')
    continue_option = input('Do you want to try again (s/n)?: ').lower()
    if continue_option != 's':
        print('Closing the game...')
        break

           