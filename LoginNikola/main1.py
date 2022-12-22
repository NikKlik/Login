users = {
    "username" : "",
    "password" : "",
    "fullName" : ""
}
print ("1. Sing in "  
       "2. Sing up")
firstLog = int(input("Dobrodosli u program."
                     "Da bi ste pristupili odaberite:  "))

if firstLog == 1:
    output = users.get()
    
elif firstLog == 2:
    print("Drugi pristup")
else:
    print("Niste lepo uneli komandu, unesite opet")
    