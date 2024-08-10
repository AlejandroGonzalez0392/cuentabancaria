from db import Database
from user import User

def main():
    db = Database()

    while True:
        print("\n--- Cajero Automático ---")
        print("1. Crear cuenta")
        print("2. Ver saldo")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Eliminar cuenta")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            name = input("Ingrese su nombre: ")
            user = User(name)
            db.insert_user(user.to_dict())
            print(f"Cuenta creada con éxito. ID de usuario: {user.user_id}")

        elif choice == "2":
            user_id = input("Ingrese su ID de usuario: ")
            user_data = db.find_user(user_id)
            if user_data:
                print(f"Saldo disponible: {user_data['balance']}")
            else:
                print("Usuario no encontrado.")

        elif choice == "3":
            user_id = input("Ingrese su ID de usuario: ")
            amount = float(input("Ingrese el monto a depositar: "))
            user_data = db.find_user(user_id)
            if user_data:
                new_balance = user_data['balance'] + amount
                db.update_balance(user_id, new_balance)
                print(f"Depósito realizado con éxito. Saldo disponible: {new_balance}")
            else:
                print("Usuario no encontrado.")

        elif choice == "4":
            user_id = input("Ingrese su ID de usuario: ")
            amount = float(input("Ingrese el monto a retirar: "))
            user_data = db.find_user(user_id)
            if user_data:
                if amount <= user_data['balance']:
                    new_balance = user_data['balance'] - amount
                    db.update_balance(user_id, new_balance)
                    print(f"Retiro realizado con éxito. Saldo disponible: {new_balance}")
                else:
                    print("Fondos insuficientes.")
            else:
                print("Usuario no encontrado.")

        elif choice == "5":
            user_id = input("Ingrese su ID de usuario: ")
            db.delete_user(user_id)
            print("Cuenta eliminada con éxito.")

        elif choice == "6":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()