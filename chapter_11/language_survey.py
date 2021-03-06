from urllib import response
from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and store the responses.
my_survey.show_question()
print("enter 'q' at any time to quit.\n")

while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
my_survey.show_results()