# exclusive network
print("\tPrivate network")
print("\tFor registered users only!\n")
security = 0
username = ""
while not username :
    username = input("Login : ")
password = ""
while not password :
    password = input("Password: ")
if username == "M .Dawson" and password == "secret" :
    print("Hi. Mike.")
    security = 5
elif username == "S.Meier" and password == "civilization":
    print("Hi. Sid")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros" :
    print("Good time. Syreru.")
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("How your business. Will?")
    security = 3
elif username == "guest" or password == "guest":
    print("Wellcome, guests !")
    security = 1
else:
    print("Access denied\n")
input("\n\nPress Enter, to exit.")