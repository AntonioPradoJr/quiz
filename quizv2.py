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
    
    for dictionary_questions in questions:
        print(f'Pergunta: {dictionary_questions['Question']}')
        print()
        for options_index, options_values in enumerate(dictionary_questions):
            print(f'{options_index}) {options_values}')
        print()

print(show_questions(list_questions))