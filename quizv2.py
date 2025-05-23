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

def show_questions(questions):
    score = 0
    for dictionary_questions in questions:
        print(f'Pergunta: {dictionary_questions['Question']}')
        print()

        for options_index, options_values in enumerate(dictionary_questions['Option']):
            print(f'{options_index}) {options_values}')
        print()
        while True:
            try:
                user_answer = int(input('Chose one option: '))
                
                if user_answer < 0 or user_answer >= len(dictionary_questions['Option']):
                    print('Invalid Option. Try Again.')
                    continue
                
                break

            except (ValueError, IndexError, TypeError):
                print('Invalid Option. Try Again.')

        if dictionary_questions['Answer'] == dictionary_questions['Option'][user_answer]:
            print('Voce acertou')
            score +=1
            print()

    print(f'Parabéns você acertou {score}x')

       

show_questions(list_questions)
