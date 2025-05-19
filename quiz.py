# Exercício - sistema de perguntas e respostas
list_questions = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Option': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
]

for dict_questions in list_questions:
    for keys in dict_questions:
        if keys == 'Pergunta':
            print(f'{keys}: {dict_questions[keys]}')
        elif keys == 'Option':
            for position, value in enumerate(dict_questions[keys]):
                print(f'{position}) {value}')
                user_choice = input('Escolha a alternativa:')
                if user_choice == dict_questions[keys]:
                print('você acertou')

        # print(f'{keys}: {dict_questions[keys]}')
        # resp_user = input('Escolha uma opção: ')
        # if resp_user == 4:
        #     print('você acertou')


        

