-- -- Создание таблицы водоматов
-- CREATE TABLE vending_machines (
--     id SERIAL PRIMARY KEY,
--     location VARCHAR(255) NOT NULL,
--     status VARCHAR(50) NOT NULL,
--     installation_date DATE NOT NULL,
--     last_service_date DATE
-- );

-- -- Создание таблицы типов воды
-- CREATE TABLE water_types (
--     id SERIAL PRIMARY KEY,
--     description TEXT NOT NULL,
--     price_per_liter DECIMAL(10,2) NOT NULL
-- );

-- -- Создание таблицы инвентаря
-- CREATE TABLE inventory (
--     id SERIAL PRIMARY KEY,
--     vending_machine_id INT NOT NULL,
--     water_type_id INT NOT NULL,
--     quantity DECIMAL(10, 2) NOT NULL,
--     last_restock DATE NOT NULL,
--     FOREIGN KEY (vending_machine_id) REFERENCES vending_machines(id),
--     FOREIGN KEY (water_type_id) REFERENCES water_types(id)
-- );

-- -- Создание таблицы транзакций
-- CREATE TABLE transactions (
--     id SERIAL PRIMARY KEY,
--     vending_machine_id INT NOT NULL,
--     water_type_id INT NOT NULL,
--     volume DECIMAL(10, 2) NOT NULL,
--     transaction_time TIMESTAMP NOT NULL,
--     FOREIGN KEY (vending_machine_id) REFERENCES vending_machines(id),
--     FOREIGN KEY (water_type_id) REFERENCES water_types(id)
-- );

-- -- Создание таблицы для записей обслуживания
-- CREATE TABLE maintenance_records (
--     id SERIAL PRIMARY KEY,
--     vending_machine_id INT NOT NULL,
--     service_date DATE NOT NULL,
--     details TEXT,
--     FOREIGN KEY (vending_machine_id) REFERENCES vending_machines(id)
-- );



-- -- Добавление данных в таблицу водоматов
-- INSERT INTO vending_machines (location, status, installation_date)
-- VALUES ('Центральный парк', 'active', '2021-01-10'),
--        ('Торговый центр "Восток"', 'maintenance', '2021-03-15');

-- -- Добавление данных в таблицу типов воды
-- INSERT INTO water_types (description, price_per_liter)
-- VALUES ('Осмосированная вода', 0.50),
--        ('Минеральная вода', 1.00);

-- -- Пример добавления данных в таблицу инвентаря
-- INSERT INTO inventory (vending_machine_id, water_type_id, quantity, last_restock)
-- VALUES (1, 1, 500.00, '2022-05-01'),
--        (1, 2, 200.00, '2022-05-01'),
--        (2, 1, 300.00, '2022-04-01');


-- Получение информации о всех водоматах и их статусах
-- SELECT * FROM inventory;
-- SELECT * FROM maintenance_records;
-- SELECT * FROM transactions;
SELECT * FROM vending_machines;
-- SELECT * FROM water_types;
