import vending_machine_manager as vmm

def admin_menu():
    while True:
        print("\n[Меню Администратора]")
        print("1. Добавить водомат")
        print("2. Обновить статус водомата")
        print("3. Удалить водомат")
        print("4. Показать все водоматы")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            city = input("Введите город: ")
            street = input("Введите улицу: ")
            building = input("Введите номер дома: ")
            zip_code = input("Введите почтовый индекс: ")
            location = f"{city}, {street}, д. {building}, {zip_code}"
            status = input("Введите статус: ")
            install_date = input("Введите дату установки (ГГГГ-ММ-ДД): ")
            vmm.add_vending_machine(location, status, install_date)
        elif choice == '2':
            machine_id = int(input("Введите ID водомата: "))
            new_status = input("Введите новый статус: ")
            vmm.update_vending_machine_status(machine_id, new_status)
        elif choice == '3':
            machine_id = int(input("Введите ID водомата для удаления: "))
            vmm.delete_vending_machine(machine_id)
        elif choice == '4':
            machines = vmm.get_vending_machines()
            for machine in machines:
                print(f"ID: {machine[0]}, Местоположение: {machine[1]}, Статус: {machine[2]}, Дата установки: {machine[3]}, Последнее техническое обслуживание: {machine[4] if machine[4] else 'None'}, Описание: {machine[5] if machine[5] else 'None'}")
        elif choice == '5':
            break
        else:
            print("Неверный выбор.")

def technician_menu():
    while True:
        print("\n[Меню Технической Службы]")
        print("1. Показать все водоматы")
        print("2. Обновить статус водомата")
        print("3. Добавить запись о техническом обслуживании")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            machines = vmm.get_vending_machines()
            for machine in machines:
                print(f"ID: {machine[0]}, Местоположение: {machine[1]}, Статус: {machine[2]}, Дата установки: {machine[3]}, Последнее техническое обслуживание: {machine[4] if machine[4] else 'None'}, Описание: {machine[5] if machine[5] else 'None'}")
        elif choice == '2':
            machine_id = int(input("Введите ID водомата: "))
            new_status = input("Введите новый статус: ")
            vmm.update_vending_machine_status(machine_id, new_status)
        elif choice == '3':
            machine_id = int(input("Введите ID водомата: "))
            maintenance_date = input("Введите дату обслуживания (ГГГГ-ММ-ДД): ")
            description = input("Описание проведенных работ: ")
            vmm.add_maintenance_record(machine_id, maintenance_date, description)
        elif choice == '4':
            break
        else:
            print("Неверный выбор.")

def user_menu():
    while True:
        print("\n[Меню Пользователя]")
        print("1. Показать все водоматы")
        print("2. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            machines = vmm.get_vending_machines()
            for machine in machines:
                print(f"ID: {machine[0]}, Местоположение: {machine[1]}, Статус: {machine[2]}, Дата установки: {machine[3]}, Последнее техническое обслуживание: {machine[4] if machine[4] else 'None'}, Описание: {machine[5] if machine[5] else 'None'}")
        elif choice == '2':
            break
        else:
            print("Неверный выбор.")

def main():
    role = input("Введите тип пользователя (admin/technician/user): ").lower()
    if role == "admin":
        admin_menu()
    elif role == "technician":
        technician_menu()
    elif role == "user":
        user_menu()
    else:
        print("Неверный тип пользователя. Попробуйте снова.")

if __name__ == "__main__":
    main()
