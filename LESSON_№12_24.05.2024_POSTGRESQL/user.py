from vending_machine_manager import get_vending_machines

def run_user_interface():
    while True:
        print("\nВыберите действие:")
        print("1 - Показать все водоматы")
        print("2 - Выход")

        choice = input()
        if choice == '1':
            machines = get_vending_machines()
            for machine in machines:
                print(machine)
        elif choice == '2':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
