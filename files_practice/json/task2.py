programming_languages = ["Python", "JavaScript", "Java", "PHP", "Go", "Ruby", "C#", "Kotlin", "C++"]

with open ("programming_languages.txt", "w") as file:
    for language in programming_languages:
        file.write(language + "\n")