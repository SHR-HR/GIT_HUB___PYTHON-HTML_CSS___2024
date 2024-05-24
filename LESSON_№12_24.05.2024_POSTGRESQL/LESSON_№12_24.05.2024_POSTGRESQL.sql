-- CREATE TABLE vending_machines (
--     id SERIAL PRIMARY KEY,
--     location TEXT NOT NULL,
--     status TEXT NOT NULL
-- );

-- CREATE TABLE water_types (
--     id SERIAL PRIMARY KEY,
--     type_name TEXT NOT NULL,
--     price_per_liter DECIMAL NOT NULL
-- );

-- CREATE TABLE maintenance_records (
--     id SERIAL PRIMARY KEY,
--     vending_machine_id INTEGER NOT NULL REFERENCES vending_machines(id),
--     maintenance_date DATE NOT NULL,
--     description TEXT
-- );

-- CREATE TABLE filter_replacements (
--     id SERIAL PRIMARY KEY,
--     vending_machine_id INTEGER NOT NULL REFERENCES vending_machines(id),
--     replacement_date DATE NOT NULL
-- );

-- CREATE TABLE water_storage (
--     id SERIAL PRIMARY KEY,
--     vending_machine_id INTEGER NOT NULL REFERENCES vending_machines(id),
--     water_type_id INTEGER NOT NULL REFERENCES water_types(id),
--     quantity_in_storage INTEGER NOT NULL,
--     sold_quantity INTEGER NOT NULL
-- );

-- CREATE TABLE sales_records (
--     id SERIAL PRIMARY KEY,
--     vending_machine_id INTEGER NOT NULL REFERENCES vending_machines(id),
--     water_type_id INTEGER NOT NULL REFERENCES water_types(id),
--     quantity_sold INTEGER NOT NULL,
--     total_income DECIMAL NOT NULL
-- );


-- SELECT column_name FROM information_schema.columns WHERE table_name = 'vending_machines';
-- ALTER TABLE vending_machines ADD COLUMN installation_date DATE;
-- SELECT column_name FROM information_schema.columns WHERE table_name = 'vending_machines';

-- SELECT column_name
-- FROM information_schema.columns
-- WHERE table_schema = 'public' -- Или другая схема, если ваша таблица находится не в public
--   AND table_name = 'vending_machines'
--   AND column_name = 'installation_date';


