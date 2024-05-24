from vending_machine_manager import get_vending_machines, update_vending_machine

def run_technician_interface():
    while True:
        print("\nВыберите действие:")
        print("1 - Показать все водоматы")
        print("2 - Обновить статус водомата")
        print("3 - Выход")

        choice = input()
        if choice == '1':
            machines = get_vending_machines()
            for machine in machines:
                print(machine)
        elif choice == '2':
            id = int(input("Введите ID водомата для обновления статуса: "))
            status = input("Введите новый статус водомата (active/maintenance): ")
            update_vending_machine(id, status)
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
