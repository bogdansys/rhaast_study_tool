import os
import random
import time

def get_input(prompt):
    return input(prompt)

def get_courses():
    courses = []
    if os.path.exists('courses'):
        courses = os.listdir('courses')
    return courses

def add_course(course):
    os.makedirs(f'courses/{course}', exist_ok=True)

def get_topics(course):
    topics = []
    if os.path.exists(f'courses/{course}'):
        topics = os.listdir(f'courses/{course}')
    return topics

def add_topic(course, topic):
    os.makedirs(f'courses/{course}/{topic}', exist_ok=True)

def get_questions(course, topic):
    questions = []
    if os.path.exists(f'courses/{course}/{topic}/questions.txt'):
        with open(f'courses/{course}/{topic}/questions.txt', 'r') as f:
            questions = [line.strip() for line in f]
    return questions

def add_questions(course, topic, questions):
    with open(f'courses/{course}/{topic}/questions.txt', 'a') as f:
        f.write(questions)
    print("Questions have been saved.")
    time.sleep(5)

def study(course, topic):
    questions = get_questions(course, topic)
    if not questions:
        print(f'No questions found for {topic} in {course}.')
        questions = get_input('Enter your questions (separated by new lines): ')
        add_questions(course, topic, questions)
        questions = get_questions(course, topic)
    random.shuffle(questions)
    answers = []
    for i, question in enumerate(questions, 1):
        print(f'Question {i} of {len(questions)}: {question}')
        answer = get_input('Your answer (or enter "000" to save and return to main menu): ')
        if answer == '000':
            break
        answers.append((question, answer))
    with open(f'courses/{course}/{topic}/answers.txt', 'w') as f:
        for question, answer in answers:
            f.write(f'Question: {question}\nAnswer: {answer}\n')
    print("You have completed this topic. Your answers have been saved.")
    time.sleep(5)

def main():
    print("""
 _______   __                                        __     
|       \\ |  \\                                      |  \\    
| $$$$$$$\\| $$____    ______    ______    _______  _| $$_   
| $$__| $$| $$    \\  |      \\  |      \\  /       \\|   $$ \\  
| $$    $$| $$$$$$$\\  \\$$$$$$\\  \\$$$$$$\\|  $$$$$$$ \\$$$$$$  
| $$$$$$$\\| $$  | $$ /      $$ /      $$ \\$$    \\   | $$ __ 
| $$  | $$| $$  | $$|  $$$$$$$|  $$$$$$$ _\\$$$$$$\\  | $$|  \\
| $$  | $$| $$  | $$ \\$$    $$ \\$$    $$|       $$   \\$$  $$
 \\$$   \\$$ \\$$   \\$$  \\$$$$$$$  \\$$$$$$$ \\$$$$$$$     \\$$$$                                                            
""")
    while True:
        courses = get_courses()
        print('Courses:')
        for i, course in enumerate(courses, 1):
            print(f'{i}. {course}')
        course = get_input('Enter a course number (or "add" to add a new course): ')
        if course == 'add':
            course = get_input('Enter the name of the new course: ')
            add_course(course)
        elif course.isdigit() and int(course) <= len(courses):
            course = courses[int(course) - 1]
            while True:
                topics = get_topics(course)
                print('Topics:')
                for i, topic in enumerate(topics, 1):
                    print(f'{i}. {topic}')
                topic = get_input('Enter a topic number (or "add" to add a new topic): ')
                if topic == 'add':
                    topic = get_input('Enter the name of the new topic: ')
                    add_topic(course, topic)
                elif topic.isdigit() and int(topic) <= len(topics):
                    topic = topics[int(topic) - 1]
                    study(course, topic)
                    break
                else:
                    print('Invalid topic. Please try again.')
        else:
            print('Invalid course. Please try again.')

if __name__ == '__main__':
    main()
