def count_vowels(string):
    vowels = "aeiouy" #это все гласные
    return sum(1 for char in string.lower() if char in vowels)

def main():
    user_input = input("Введите строку: ")
    vowel_count = count_vowels(user_input)
    print(f"Кол-во гласных в строке: {vowel_count}")

if __name__ == "__main__":
    main()
#Буква Y (по крайней мере, в англ. и фр. языках) обозначает ГЛАСНЫЙ звук,
#поскольку при произношении ни зубы, ни язык не создают «преград» выходу воздух