#Name:Nana Kwasi Owusu
#Date: 29 April 2024
#Purpose: Class to handle all possible question types

from abc import ABC, abstractmethod
#this is the base class that all the other questions will derive from 
class Question(ABC):
    def __init__(self,prompt,correctAnswer='',points=0):
        self.__prompt = prompt
        self.__correctAnswer = correctAnswer
        self.__points = points
        
    @abstractmethod
    def displayForTest(self):
        pass
    
    def __str__(self):
        return f"Prompt: {self.__prompt.strip()}\nCorrect Answer: {self.__correctAnswer}\nPoints: {self.__points}"
    
    #getters
    def getPrompt(self):
        return self.__prompt
    
    def getCorrectAnswer(self):
        return self.__correctAnswer
    
    def getPoints(self):
        return self.__points
    
    
    #setters
    def setPrompt(self,prompt):
        self.__prompt = prompt
    
    def setCorrectAnswer(self,correctAnswer):
        self.__correctAnswer = correctAnswer
    
    def setPoints(self,points):
        self.__points = points
        
#this is the multiple choice class that handles multiple choice questions 
class MultipleChoice(Question):
    def __init__(self,prompt,choices,correctAnswer='',points=0):
        super().__init__(prompt,correctAnswer,points)
        self.__choices = choices
    
    #getters
    def getChoices(self):
        return self.__choices
    
    def addChoice(self,newChoice):
        self.__choices.append(newChoice)
    
    def updateChoice(self,index,choiceToUpdate):
        self.__choices[index] = choiceToUpdate
    
    
    def displayForTest(self):
        textDisplay = f"{self.getPrompt()}\n"
        for choice in self.__choices:
            textDisplay += f"{choice}\n"
        return textDisplay
    
        
    def __str__(self):
        return f"{super().__str__()}\nChoices: {self.__choices}"

#this is the short answer class that handels short answer questions
class ShortAnswer(Question):
    def __init__(self,prompt,length,correctAnswer='',points=0):
        super().__init__(prompt,correctAnswer,points)
        self.__length = length
    
    #getter
    def getLength(self):
        return self.__length
    
    #setter
    def setLength(self, lengthToSet):
        self.__length = lengthToSet
        
    def displayForTest(self):
        return f"{self.getPrompt()} (up to {self.__length} characters)"

    
    def __str__(self):
        return super().__str__() + f"\nCharacter limit: {self.__length}"
        
#this is the fill in the blank class that handles fill in the blank questions 
class FillInTheBlank(Question):
    def __init__(self,prompt,correctAnswer='',points=0):
        super().__init__(prompt,correctAnswer,points)
    
    def displayForTest(self):
        return f"Fill in the blank:\n{self.getPrompt()}"
    
    def __str__(self):
        return f"{super().__str__()}\n"
    
