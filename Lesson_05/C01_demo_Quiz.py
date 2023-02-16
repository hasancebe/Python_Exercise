#Question
class Question:
    def __init__(self,text,choises,answer):
        self.text=text
        self.choises=choises
        self.answer=answer

    def checkAnswer(self,answer):
        return self.answer==answer
q1=Question("which is the best program language",["C#","java","phyton","C++"],"java")
q2=Question("which is the most popular program language",["C#","java","phyton","C++"],"phyton")
q3=Question("which is the hardest program language",["C#","java","phyton","C++"],"C++")

#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionindex=0
    def getQuestion(self):

         return  quiz.questions[self.questionindex]

    def displayQuestion(self):
        question=self.getQuestion()
        print(f"Soru {self.questionindex +1}: {question.text}")

        for q in question.choises:
            print("-"+q)

        answer=input("cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question=self.getQuestion()
        if question.checkAnswer((answer)):
            self.score+=1
        self.questionindex+=1

    def loadQuestion(self):
        if len(self.questions)==self.questionindex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("score",self.score)

    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionindex+1

        if(questionNumber>totalQuestion):
            print("quiz bitti")
        else:
            print(f"Question{questionNumber} of {totalQuestion}".center(100,"*"))


questions=[q1,q2,q3]

quiz=Quiz(questions)
question=quiz.loadQuestion()
