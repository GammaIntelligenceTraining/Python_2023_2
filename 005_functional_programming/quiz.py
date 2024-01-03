def ask_question(q):
    print(q['question'])
    for i in range(4):
        print(f'{i + 1}. {q["answers"][i]}')

def get_answer():
    while True:
        user_answer = input('Your answer: ')
        if user_answer in ['1', '2', '3', '4']:
            return user_answer
        print('Try again!')


def play():
    global user_score
    for question in quiz.values():
        ask_question(question)
        answer = get_answer()
        user_answer = question['answers'][int(answer) - 1]
        if user_answer == question['correct_answer']:
            user_score += 1

quiz = {
    'q1': {
        'question': 'What color the sky is?',
        'answers': ['Red', 'Green', 'Blue', 'Yellow'],
        'correct_answer': 'Blue'
    },
    'q2': {
        'question': 'What color the sun is?',
        'answers': ['Red', 'Green', 'Blue', 'Yellow'],
        'correct_answer': 'Yellow'
    },
    'q3': {
        'question': 'What color the grass is?',
        'answers': ['Red', 'Green', 'Blue', 'Yellow'],
        'correct_answer': 'Green'
    }
}
user_score = 0

play()
print(f'You answered {user_score} questions correctly.')