print("Придумайте надежный пароль.(Длина пароля не менее 8 символов.)")
password1=input("Ведите пароль: ")
password2=input("Ведите пароль: ")

s1="abcdefghijklmnopqrstuvwxyz"
s2="0123456789"
s3="!@#$%^&*(),.?\:{}|<>"

def chek_pass(p):
    if len(p)<8:
        return "Ваш пароль слишком короткий."

    if not any(x in p for x in s1):
        return "Пароль должен содержать хотя бы одну строчную букву."

    if not any(x in p for x in s1.upper()):
        return "Пароль должен содержать хотя бы одну прописную букву."

    if not any(x in p for x in s2):
        return "Пароль должен содержать хотя бы одну цифру."

    if not any(x in p for x in s3):
        return "Пароль должен содержать хотя бы один спецсимвол."

    else: return "Пароль принят."

if password1==password2:
    print(chek_pass(password1))
else: print("Пароли не совпадают.")
