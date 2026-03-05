import oracledb
from django.utils.hashable import make_hashable

user_name = "system"
password = "12345"
dsn = "localhost:1521/orcl"

connection=oracledb.connect(user=user_name, password=password, dsn=dsn)
cursor =connection.cursor()

cursor .execute(""" SELECT d.d_ad,i.i_maas
from departament d join isciler i on d.d_id=i.d_id""")

max = 0
for row in cursor:
    if int(row[1]) > max:
        max = row[1]
print("---- MAKSIMUM MAAS----")
print(f"Departament:{row[0]},Maksimum maas:{max}")

print("\n" + "=" * 50  + "\n")

print("----HER DEPARTAMENT UZRE MAKSIMUM MAAS----")

cursor .execute(""" SELECT d.d_ad,i.i_maas
from departament d join isciler i on d.d_id=i.d_id""")

max1 = 0
max2 = 0
max3 = 0
max4 = 0
max5 = 0
for row in cursor:
    departament = row[0].lower()
    maas = int(row[1])
    if departament=='muhasibat':
        if maas > max1:
            max1=maas
    elif departament == 'maliyye':
       if maas > max2:
        max2=maas
    elif departament == 'it':
       if maas > max3:
        max3=maas
    elif departament == 'menecment':
        if maas > max4:
            max4=maas
    elif departament == 'ictimai tehlukesizlik':
        if maas > max5:
            max5=maas

print(f"Muhasibat maksimum maas:{max1}")
print(f"Maliyye maksimum maas:{max2}")
print(f"IT maksimum maas:{max3}")
print(f"Menecment maksimum maas:{max4}")
print(f"Ictimai tehlukesizlik maksimum maas:{max5}")

cursor.close()
connection.close()