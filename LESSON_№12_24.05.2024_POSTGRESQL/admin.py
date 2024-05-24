from vending_machine_manager import create_vending_machine, delete_vending_machine, get_vending_machines, update_vending_machine

def run_admin_interface():
    while True:
        print("\nВыберите действие:")
        print("1 - Добавить водомат")
        print("2 - Удалить водомат")
        print("3 - Показать все водоматы")
        print("4 - Обновить статус водомата")
        print("5 - Выход")

        choice = input()
        if choice == '1':
            location = input("Введите адрес установки водомата: ")
            status = input("Введите статус водомата (active/maintenance): ")
            install_date = input("Введите дату установки (YYYY-MM-DD): ")
            create_vending_machine(location, status, install_date)
        elif choice == '2':
            id = int(input("Введите ID водомата для удаления: "))
            delete_vending_machine(id)
        elif choice == '3':
            machines = get_vending_machines()
            for machine in machines:
                print(machine)
        elif choice == '4':
            id = int(input("Введите ID водомата для обновления статуса: "))
            status = input("Введите новый статус водомата (active/maintenance): ")
            update_vending_machine(id, status)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
