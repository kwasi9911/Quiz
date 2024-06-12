#Name:Nana Kwasi Owusu
#Date: 30 April 2024
#Program Description: This program is a simple quiz system that has a variety of question types

from questions import MultipleChoice, ShortAnswer, FillInTheBlank

#this function receives a question object, displays the question to the test taker and reads the user's input from the keyboard
def answerQuestion(question):
    print(question.displayForTest())
    answer = input('Enter your answer: ').strip().lower()
    return answer

#this function adds the set number of points to a users score if they answer the question right
def gradeQuestion(question, userAnswer):
    rightAnswer = question.getCorrectAnswer()
    if userAnswer.lower().strip() == rightAnswer.lower().strip():
        return question.getPoints()
    return 0
    
#main part of the program
if __name__ == "__main__":
    Question1 = MultipleChoice('What is the capital of Ghana?',['a. London','b. Accra','c. Abuja'],'b',5)
    Question2 = MultipleChoice('\nWhat is the largest city in Pennsylvania?',['a. Philadelphia','b. Brookhaven','c. Pittsburgh'],'a',5)
    Question3 = ShortAnswer('\nWhat is the suggested IDE for CS171 / CS172?',6,'thonny',5)
    Question4 = ShortAnswer('\nWhat programming language does CS171 / CS172 teach?',6,'python',5)
    Question5 = FillInTheBlank(' ______ City was the winner of the 2023 Champions League','Manchester',5)
    Question6 = FillInTheBlank("______ Messi is the soccer player with the most Ballon d'Ors",'Lionel',5)
    QuizQuestions = [Question1, Question2, Question3, Question4, Question5, Question6]
    
    totalPoints = 0
    for question in QuizQuestions:
        response = answerQuestion(question)
        pointsGained = gradeQuestion(question, response)
        totalPoints += pointsGained
        
    print(f"\nYou earned: {totalPoints} points")
    print(f"\nYour performance is below:")
    print(f"\n{Question1}")
    print(f"\n{Question2}")
    print(f"\n{Question3}")
    print(f"\n{Question4}")
    print(f"\n{Question5}")
    print(f"\n{Question6}")

