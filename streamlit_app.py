import streamlit as st
import google.generativeai as genai
import datetime

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Numerology Analysis with Ever AI")
st.write("Enter your name and birthdate for a comprehensive numerology analysis.")

name = st.text_input("Enter your full name:")
birthdate = st.date_input("Enter your birthdate:")

def calculate_life_path(birthdate):
    day = birthdate.day
    month = birthdate.month
    year = birthdate.year
    total = sum(map(int, str(day) + str(month) + str(year)))
    while total > 9 and total != 11 and total != 22 and total != 33:
        total = sum(map(int, str(total)))
    return total

def calculate_expression(name):
    name = name.lower()
    vowel_values = {'a': 1, 'e': 5, 'i': 9, 'o': 6, 'u': 3}
    consonant_values = {
        'b': 2, 'c': 3, 'd': 4, 'f': 8, 'g': 3, 'h': 8, 'j': 1, 'k': 2, 'l': 3,
        'm': 4, 'n': 5, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2, 'v': 6, 'w': 6,
        'x': 5, 'y': 1, 'z': 7
    }
    vowel_sum = 0
    consonant_sum = 0
    for char in name:
        if 'a' <= char <= 'z':
            if char in vowel_values:
                vowel_sum += vowel_values[char]
            else:
                consonant_sum += consonant_values[char]
    total = vowel_sum + consonant_sum
    while total > 9 and total != 11 and total != 22 and total != 33:
        total = sum(map(int, str(total)))
    return total

def calculate_soul_urge(name):
    name = name.lower()
    vowel_values = {'a': 1, 'e': 5, 'i': 9, 'o': 6, 'u': 3}
    vowel_sum = 0
    for char in name:
        if 'a' <= char <= 'z' and char in vowel_values:
            vowel_sum += vowel_values[char]
    while vowel_sum > 9 and vowel_sum != 11 and vowel_sum != 22 and vowel_sum != 33:
        vowel_sum = sum(map(int, str(vowel_sum)))
    return vowel_sum

def calculate_personality(name):
    name = name.lower()
    consonant_values = {
        'b': 2, 'c': 3, 'd': 4, 'f': 8, 'g': 3, 'h': 8, 'j': 1, 'k': 2, 'l': 3,
        'm': 4, 'n': 5, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2, 'v': 6, 'w': 6,
        'x': 5, 'y': 1, 'z': 7
    }
    consonant_sum = 0
    for char in name:
        if 'a' <= char <= 'z' and char not in ['a', 'e', 'i', 'o', 'u']:
            consonant_sum += consonant_values[char]
    while consonant_sum > 9 and consonant_sum != 11 and consonant_sum != 22 and consonant_sum != 33:
        consonant_sum = sum(map(int, str(consonant_sum)))
    return consonant_sum

def calculate_birthday(birthdate):
    return birthdate.day if birthdate.day <= 9 else sum(map(int, str(birthdate.day)))

def calculate_attitude(birthdate):
    month = birthdate.month
    day = birthdate.day
    total = month + day
    while total > 9:
        total = sum(map(int, str(total)))
    return total

def calculate_karmic_numbers(name, birthdate):
    name = name.lower()
    birthdate_str = str(birthdate.day) + str(birthdate.month) + str(birthdate.year)
    total_str = name + birthdate_str
    karmic_numbers = []
    for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if str(total_str).count(num) == 0:
            karmic_numbers.append(int(num))
    return karmic_numbers

def calculate_master_numbers(life_path, expression, soul_urge, personality):
    master_numbers = []
    if life_path in [11, 22, 33]:
        master_numbers.append(life_path)
    if expression in [11, 22, 33]:
        master_numbers.append(expression)
    if soul_urge in [11, 22, 33]:
        master_numbers.append(soul_urge)
    if personality in [11, 22, 33]:
        master_numbers.append(personality)
    return master_numbers

def calculate_maturity(life_path, expression):
    mature = life_path + expression
    while mature > 9 and mature != 11 and mature != 22 and mature != 33:
        mature = sum(map(int, str(mature)))
    return mature

def calculate_current_year(birthdate):
    today = datetime.date.today()
    current_year = today.year
    personal_year = calculate_personal_year(birthdate, current_year)
    return personal_year

def calculate_personal_year(birthdate, year):
    month = birthdate.month
    day = birthdate.day
    total = day + month + year
    while total > 9:
        total = sum(map(int, str(total)))
    return total

def calculate_personal_month(birthdate):
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    personal_year = calculate_personal_year(birthdate, current_year)
    personal_month = personal_year + current_month
    while personal_month > 9:
        personal_month = sum(map(int, str(personal_month)))
    return personal_month

def calculate_personal_day(birthdate):
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    current_day = datetime.date.today().day
    personal_year = calculate_personal_year(birthdate, current_year)
    personal_month = personal_year + current_month
    personal_day = personal_month + current_day
    while personal_day > 9:
        personal_day = sum(map(int, str(personal_day)))
    return personal_day

def calculate_challenge_numbers(birthdate):
    day = birthdate.day
    month = birthdate.month
    year = birthdate.year
    challenges = [abs(day - month), abs(month - year), abs(day - year)]
    challenges = [sum(map(int, str(ch))) for ch in challenges]
    return challenges

def calculate_pinnacle_numbers(birthdate):
    day = birthdate.day
    month = birthdate.month
    year = birthdate.year
    pinnacle1 = sum(map(int, str(day + month)))
    pinnacle2 = sum(map(int, str(month + year)))
    pinnacle3 = sum(map(int, str(day + year)))
    pinnacle4 = sum(map(int, str(pinnacle1 + pinnacle2 + pinnacle3)))
    return [pinnacle1, pinnacle2, pinnacle3, pinnacle4]

def calculate_essence_number(birthdate):
    today = datetime.date.today()
    current_year = today.year
    personal_year = calculate_personal_year(birthdate, current_year)
    essence_number = sum(map(int, str(personal_year)))
    return essence_number

def calculate_balance_number(name):
    name = name.lower()
    vowel_values = {'a': 1, 'e': 5, 'i': 9, 'o': 6, 'u': 3}
    consonant_values = {
        'b': 2, 'c': 3, 'd': 4, 'f': 8, 'g': 3, 'h': 8, 'j': 1, 'k': 2, 'l': 3,
        'm': 4, 'n': 5, 'p': 7, 'q': 8, 'r': 9, 's': 1, 't': 2, 'v': 6, 'w': 6,
        'x': 5, 'y': 1, 'z': 7
    }
    vowel_sum = 0
    consonant_sum = 0
    for char in name:
        if 'a' <= char <= 'z':
            if char in vowel_values:
                vowel_sum += vowel_values[char]
            else:
                consonant_sum += consonant_values[char]
    balance_number = abs(vowel_sum - consonant_sum)
    return balance_number

def calculate_habit_challenges(birthdate):
    day = birthdate.day
    month = birthdate.month
    year = birthdate.year
    habit_challenges = [sum(map(int, str(abs(day - month)))),
                        sum(map(int, str(abs(month - year)))),
                        sum(map(int, str(abs(day - year))))]
    return habit_challenges

def calculate_personal_day_number(birthdate):
    today = datetime.date.today()
    personal_year = calculate_personal_year(birthdate, today.year)
    personal_month = calculate_personal_month(birthdate)
    personal_day = personal_year + personal_month + today.day
    while personal_day > 9:
        personal_day = sum(map(int, str(personal_day)))
    return personal_day

def calculate_subconscious_self(name):
    name = name.lower()
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowel_count = sum([1 for char in name if char in vowels])
    consonant_count = sum([1 for char in name if char in consonants])
    subconscious_self = abs(vowel_count - consonant_count)
    return subconscious_self

def calculate_hidden_passions(name):
    name = name.lower()
    passions = {char: name.count(char) for char in set(name) if name.count(char) > 1}
    return passions

def calculate_birth_year_number(birthdate):
    return sum(map(int, str(birthdate.year)))

def calculate_birth_month_number(birthdate):
    return sum(map(int, str(birthdate.month)))

def calculate_destiny_number(birthdate):
    return calculate_life_path(birthdate)

if st.button("Calculate Numerology"):
    if name and birthdate:
        life_path = calculate_life_path(birthdate)
        expression = calculate_expression(name)
        soul_urge = calculate_soul_urge(name)
        personality = calculate_personality(name)
        birthday = calculate_birthday(birthdate)
        attitude = calculate_attitude(birthdate)
        karmic_numbers = calculate_karmic_numbers(name, birthdate)
        master_numbers = calculate_master_numbers(life_path, expression, soul_urge, personality)
        maturity_number = calculate_maturity(life_path, expression)
        current_year_number = calculate_current_year(birthdate)
        current_month_number = calculate_personal_month(birthdate)
        personal_day_number = calculate_personal_day(birthdate)
        challenge_numbers = calculate_challenge_numbers(birthdate)
        pinnacle_numbers = calculate_pinnacle_numbers(birthdate)
        essence_number = calculate_essence_number(birthdate)
        balance_number = calculate_balance_number(name)
        habit_challenges = calculate_habit_challenges(birthdate)
        personal_day_number = calculate_personal_day_number(birthdate)
        subconscious_self = calculate_subconscious_self(name)
        hidden_passions = calculate_hidden_passions(name)
        birth_year_number = calculate_birth_year_number(birthdate)
        birth_month_number = calculate_birth_month_number(birthdate)
        destiny_number = calculate_destiny_number(birthdate)

        st.write(f"Life Path Number: {life_path}")
        st.write(f"Expression Number: {expression}")
        st.write(f"Soul Urge Number: {soul_urge}")
        st.write(f"Personality Number: {personality}")
        st.write(f"Birthday Number: {birthday}")
        st.write(f"Attitude Number: {attitude}")
        st.write(f"Karmic Numbers: {karmic_numbers}")
        st.write(f"Master Numbers: {master_numbers}")
        st.write(f"Maturity Number: {maturity_number}")
        st.write(f"Current Year Number: {current_year_number}")
        st.write(f"Current Month Number: {current_month_number}")
        st.write(f"Personal Day Number: {personal_day_number}")
        st.write(f"Challenge Numbers: {challenge_numbers}")
        st.write(f"Pinnacle Numbers: {pinnacle_numbers}")
        st.write(f"Essence Number: {essence_number}")
        st.write(f"Balance Number: {balance_number}")
        st.write(f"Habit Challenges: {habit_challenges}")
        st.write(f"Personal Day Number: {personal_day_number}")
        st.write(f"Subconscious Self: {subconscious_self}")
        st.write(f"Hidden Passions: {hidden_passions}")
        st.write(f"Birth Year Number: {birth_year_number}")
        st.write(f"Birth Month Number: {birth_month_number}")
        st.write(f"Destiny Number: {destiny_number}")
