nombre = input("Como te llamas: ")
apellido = input("Cual es tu primer apellido: ")
print("Gastos:")

# Gasto 1
n1 = input("No. Campo (máx. 5 dígitos): ")
descripcion1 = input("Descripción (máx. 20 letras): ")
monto1 = input("Monto mensual: $")

# Gasto 2
n2 = input("No. Campo (máx. 5 dígitos): ")
descripcion2 = input("Descripción (máx. 20 letras): ")
monto2 = input("Monto mensual: $")

# Gasto 3
n3 = input("No. Campo (máx. 5 dígitos): ")
descripcion3 = input("Descripción (máx. 20 letras): ")
monto3 = input("Monto mensual: $")

# Gasto 4
n4 = input("No. Campo (máx. 5 dígitos): ")
descripcion4 = input("Descripción (máx. 20 letras): ")
monto4 = input("Monto mensual: $")

# Gasto 5
n5 = input("No. Campo (máx. 5 dígitos): ")
descripcion5 = input("Descripción (máx. 20 letras): ")
monto5 = input("Monto mensual: $")

print(f"Registro de egresos de: {apellido}, {nombre}")
print('{:>5} --- {:<20} --- {:>9}'.format('"Id"', '"Descripción"', '"Monto"'))


print('{:>5} --- {:<20} --- ${:>9}'.format(n1, descripcion1, f"{float(monto1):,.2f}"), end='\n\n')
print('{:>5} --- {:<20} --- ${:>9}'.format(n2, descripcion2, f"{float(monto2):,.2f}"), end='\n\n')
print('{:>5} --- {:<20} --- ${:>9}'.format(n3, descripcion3, f"{float(monto3):,.2f}"), end='\n\n')
print('{:>5} --- {:<20} --- ${:>9}'.format(n4, descripcion4, f"{float(monto4):,.2f}"), end='\n\n')
print('{:>5} --- {:<20} --- ${:>9}'.format(n5, descripcion5, f"{float(monto5):,.2f}"))

