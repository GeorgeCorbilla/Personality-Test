import sys
def main():
    print("======================================================")
    print("   PERSONALITY TEST - HOW PEOPLE SEE YOU AT SCHOOL    ")
    print("======================================================")
    print("\t[1]. Introduction")
    print("\t[2]. Test questionnaire")
    print("\t[3]. SDG Related to e-personality test")
    print("\t[4]. References")
    print("\t[5]. Exit")
    print("======================================================")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        introduction()
    elif choice == 2:
        test_questionnaire()
    elif choice == 3:
        SDG()
    elif choice == 4:
        references()
    elif choice == 5:
        print("Thank you for taking the e-Personality Test. Have a great day!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main()
        
def references():
    print("======================================================")
    print("                    REFERENCES    ")
    print("======================================================")
    print("\nMagic Quiz. (2021, October 14). HOW DO PEOPLE SEE YOU AT SCHOOL? Magic Quiz - Pick One Personality Test.")
    print("\tYouTube. https://www.youtube.com/watch?v=F-39W_OrGgg")
    print("======================================================")
    again()
def SDG():
    print("======================================================")
    print("       SDG  RELATED TO THE PERSONALITY TEST          ")
    print("======================================================")
    print("\nThe Sustainable Development Goals (SDGs) are a set of ")
    print("17 global goals by United nations to end poverty, protect")
    print("the planet, and ensure peace and prosperity for all.")
    print("Two SDG's that are related to our personality test are")
    print("as follows: ")
    
    print("\nSDG 4: QUALITY EDUCATION: The aim of this SDG is to")
    print("ensure inclusive and equitable quality education and")
    print("promote lifelong opportunities for all. A personality")
    print("test that provides insight into how people see you at")
    print("school can help you understand how you are perceived by")
    print("your peers, and how you can use that information to")
    print("improve your social skills and relationships. ")
    
    print("\nSDG 11: SUSTAINABLE CITIES AND COMMUNITIES: The aim")
    print("of this SDG is to make cities and human settlements")
    print("inclusive, safe, resilient, and sustainable. A")
    print("personality test that gives you a better understanding")
    print("of how others perceive you at school can help you")
    print("create a positive impact on your school community by")
    print("promoting harmonious relationship, cooperation, and ")
    print("collaboration among students, teachers, and other")
    print("steakholders. By fostering a sense of community and")
    print("and belonging at school, you can contribute to the goal")
    print("of creating sustainable and livable communities")
    print("======================================================")
    again()

def introduction():
    print("\n======================================================")
    print("                    INTRODUCTION                      ")
    print("======================================================")
    print("Welcome to the Personality Test! This test is designed\nto give you a glimpse into how others perceive you at \nschool. It's a fascinating journey to understand how \nyour actions, behavior, and attitude influence the way\npeople see you. \n\nThis test will ask you a series of questions about your\nhabits, interests, and personality traits. By \nanswering truthfully, you'll get a clear picture of \nyour strengths, weaknesses, and the impression you make \non those around you. So, get ready to embark on an \nexciting journey to discover the real you and how \nothers see you at school!")
    print("======================================================")
    again()

def interpret_result(score):
  print("\n\n======================================================")
  print("                      RESULT                           ")
  print("======================================================")
  print("SCORE: ", score)
  if score >= 12 and score <= 16:
      print("At school you are seen like a NERD! You prefer books")
      print("because they are clever and don’t bully you. ")
      print("You are seen as monstrously intelligent and lonely. ")
      print("======================================================\n")
  elif score >= 17 and score <= 21:
    print("At school, you are seen like an INTELLECTUAL INSIDER!")
    print("Almost everyone in the class ignores you. You are ")
    print("seen as quite odd and unsociable, but very smart!")
    print("======================================================\n")
  elif score >= 22 and score <= 26:
    print("At school, you are seen like a DRAMA QUEEN! You want to")
    print("get some attention at any cost. You are seen as super")
    print("emotional and exaggerated.")
    print("======================================================\n")
  elif score >= 27 and score <= 31:
    print("At school, you are seen like a STAR! You can be famous")
    print("for a number of reasons, you can play sports, you’re")
    print("an A-student, or you look good. You are seen as pretty") 
    print("fabulous!")
    print("======================================================\n")
  elif score >= 32 and score <= 36:
    print("At school, you are seen like a NATIONAL LEADER! You have")
    print("an inborn capacity to stand out like a sore thumb. You")
    print("are seen as an example to follow.")
    print("======================================================\n")
  else:
    print("Invalid score")
  again()
    
def test_questionnaire():
  score = 0
  print("\n======================================================")
  print("                  PERSONALITY TEST                      ")
  print("======================================================")
  print("1. How many friends do you have at school?")
  print("\ta. I don’t have")
  print("\tb. 1-3")
  print("\tc. 4 or more", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3

  print("\n------------------------------------------------------")
  print("2. How do teachers see you?")
  print("\ta. They don’t notice me so much")
  print("\tb. They don’t like me")
  print("\tc. They think I’m a good student", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3
  
  print("\n------------------------------------------------------")
  print("3. Are you shy?")
  print("\ta. Yes")
  print("\tb. A little")
  print("\tc. No", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3

  print("\n------------------------------------------------------")
  print("4. Your anxiety level is?")
  print("\ta. Pretty big")
  print("\tb. I guess normal")
  print("\tc. Low", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3

  print("\n------------------------------------------------------")
  print("5. Are you respected at school?")
  print("\ta. Not at all")
  print("\tb. YES")
  print("\tc. Yes, very much", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3

  print("\n------------------------------------------------------")
  print("6. The relationship with your parent is?")
  print("\ta. Not good at all")
  print("\tb. Depends on the day")
  print("\tc. Pretty good", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3

  print("\n------------------------------------------------------")
  print("7. Are you popular?")
  print("\ta. No")
  print("\tb. A little")
  print("\tc. Yes", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3
    
  print("\n------------------------------------------------------")
  print("8. Your grades are?")
  print("\ta. Mostly Good grades")
  print("\tb. Mostly Bad grades")
  print("\tc. Medium grades", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3

  print("\n------------------------------------------------------")
  print("9. Are you easily friendly?")
  print("\ta. No")
  print("\tb. Depends with who")
  print("\tc. Yes", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3

  print("\n------------------------------------------------------")
  print("10. Do you like going to school?")
  print("\ta. Yes")
  print("\tb. No")
  print("\tc. So and So", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3

  print("\n------------------------------------------------------")
  print("11. Online school is?")
  print("\ta. Awesome")
  print("\tb. Good")
  print("\tc. Boring", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3

  print("\n------------------------------------------------------")
  print("12. Pick how your personality is like?")
  print("\ta. I'm a dreamer")
  print("\tb. I'm an open heart")
  print("\tc. I'm a fighter", end="")
  answer = input("Enter your answer (a-c): ")
  if answer == "a":
    score += 1
  elif answer == "b":
    score += 2
  elif answer == "c":
    score += 3
  print("\n------------------------------------------------------")
  interpret_result(score)
  
def again():
    repeat = input("Do you want to perform another operation? [yes/no]: ")
    if repeat.lower() == "yes":
        main()
    elif repeat.lower() == "no":
        print("Thank you for taking the e-Personality Test. Have a great day!")
    else:
        print("Invalid input. Please try again.")
        again()
 
if __name__ == "__main__":
    main()
    
