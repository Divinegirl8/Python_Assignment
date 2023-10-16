user = input("What is your name: ")

print("Answer the following questions with (A or B)")

question = [
    "expend energy, enjoy groups", "conserve energy, enjoy one-on-one",
    "Interpret literally", "look for meaning and possibilities",
    "logical,thinking,questioning", "empathetic, feeling, accommodating",
    "organized,orderly", "flexible, adaptable",
    "more outgoing,think out loud", "more reserved, think to yourself",
    "practical, realistic, experiential", "imaginative, innovative, theoretical",
    "candid, straight, forward, frank", "tactful, kind, encouraging",
    "plan, schedule", "unplanned, spontaneous",
    "seek many tasks, public activities, interaction with others",
    "seek private, solitary activities with quiet to concentrate",
    "standard, usual, conventional", " different, novel, uniques",
    "firm, tend to criticize, hold the line", "gentle, tend to appreciate, conciliate ",
    "regulated, structured", "easy-going,live and let live",
    "external, communicative, express yourself", "internal, reticent, keep to yourself",
    "focus on here-and-now", "look to the future, global perspective, big picture",
    "tough-minded, just ", "tender-hearted, merciful",
    "preparation, plan ahead", "go with the flow, adapt as you go",
    "active, initiate", "reflective, deliberate ",
    "facts, things, what is ", "ideas, dreams, what could be, philosophical",
    "matter of fact, issue-oriented ", "sensitive, people-oriented, compassionate",
    "control, govern", "latitude, freedom"
]

store_answers = []
store_element = []

for count in range(0, (len(question)), 2):
    choice = input(f"A. {question[count]}\t B. {question[count + 1]}").upper()

    while choice != "A" and choice != "B":
        print("""
         Expected A or B as Response
         I know this is an error, please retry again
        """)
        choice = input(f"A. {question[count]}\t B. {question[count + 1]}").upper()

    if choice == "A":
        store_element.append(f"A. {question[count]}")

    if choice == "B":
        store_element.append(f"B. {question[count + 1]}")

    store_answers.append(choice)
print("\n")
increment = 5

print(f"Hello {user} you selected: ")
print()
for index in range(0, len(store_element), increment):
    countA = 0
    countB = 0
    for inner in range(index, index + increment, 1):
        print(store_element[inner])
        if store_answers[inner] == "A":
            countA += 1
        if store_answers[inner] == "B":
            countB += 1
    print(f"""
Number of A selected: {countA}
Number of B selected: {countB}
    """)
    print()

personality_type = ""
check = 0

while check < len(store_answers):
    personality_type += "E" if store_answers[check] == "A" else "I"
    personality_type += "S" if store_answers[check + 1] == "A" else "N"
    personality_type += "T" if store_answers[check + 2] == "A" else "F"
    personality_type += "J" if store_answers[check + 3] == "A" else "P"

    if len(personality_type) == 4:
        break
    check += 4

if personality_type == "INFP":
    print("""
INFP
         Healer
         The Thoughtful Idealist (MBTI)
         The Mediator (16Personalisties)


The INFP Personality Type
        INFPs are imaginative idealists, guided by their own core values and beliefs.
           To a Healer , possibilities are paramount; the realism of the moment is only
           of passing concern. They see potential for a better future, and pursue truth
           and meaning with their own individual flair.
        INFPs are sensitive, caring, and compassionate, and are deeply concerned with
            the personal growth of themselves and others. Individualistic and
            non judgemental, INFPs believe that each person must find their own path. They
            enjoy spending time exploring their own ideas and values, and are gently
            encouraging to others to do the same. INFPs are creative and often artistic;
            they enjoy finding new outlets for self-expression.

        What does INFP stand for?
            INFP is one of the sixteen personality types created by Katherine Briggs and
            Isabel Myers, creators of the Myers-Briggs Type Indicator (MBTI). INFP
            stands for Introversion, Intuition, Feeling, and Perceiving, which are four
            core personality traits based on the work of pyschologist C.G. Jung.
            Each of the four letters of the INFPs code signifies a key personality trait of
            this type. INFPs are energized by time alone (Introverted), focus on ideas
            and concepts rather than facts and details (iNtuitive), make decisions based
            on feelings and values (Feeling), and prefer to be spontaneous and flexible
            rather than planned and organized (Perceiving).
                    """)

if personality_type == "INFJ":
    print("""
INFJ
    The Advocate (16Personalisties)
    
                    
    The INFJ Personality Type
            Advocates (INFJs) may be the rarest personality type of all, but they certainly
            leave their mark on the world. Idealistic and principled, they aren’t content to
            coast through life – they want to stand up and make a difference. For Advocate personalities,
            success does not come from money or status but from seeking fulfillment, helping others,
            and being a force for good in the world.
                        
            While they have lofty goals and ambitions, Advocates shouldn’t be mistaken for idle dreamers.
            People with this personality type care about integrity, and they’re rarely satisfied until
            they’ve done what they know to be right. Conscientious to the core, they move through life with a clear
            sense of their values, and they aim never to lose sight of what truly matters – not according to other people
            or society at large, but according to their own wisdom and intuition.
                        
    Who is An Advocate (INFJ)?
            An Advocate (INFJ) is someone with the Introverted, Intuitive, Feeling, and Judging personality traits.
            They tend to approach life with deep thoughtfulness and imagination. Their inner vision, personal values,
            and a quiet, principled version of humanism guide them in all things.
  
   """)
