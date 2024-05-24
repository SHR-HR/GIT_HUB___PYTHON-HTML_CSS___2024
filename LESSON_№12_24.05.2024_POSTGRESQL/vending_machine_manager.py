from db import query_db, logging

def add_vending_machine(location, status, installation_date):
    sql = "INSERT INTO vending_machines (location, status, installation_date) VALUES (%s, %s, %s)"
    query_db(sql, (location, status, installation_date), fetch=False)

def update_vending_machine_status(vending_machine_id, new_status):
    sql = "UPDATE vending_machines SET status = %s WHERE id = %s"
    query_db(sql, (new_status, vending_machine_id), fetch=False)

def delete_vending_machine(vending_machine_id):
    sql = "DELETE FROM vending_machines WHERE id = %s"
    query_db(sql, (vending_machine_id,), fetch=False)

def get_vending_machines():
    sql = """
    SELECT v.id, v.location, v.status, v.installation_date, m.maintenance_date, m.description
    FROM vending_machines v
    LEFT JOIN maintenance_records m ON v.id = m.vending_machine_id
    WHERE m.maintenance_date = (
        SELECT MAX(maintenance_date) FROM maintenance_records WHERE vending_machine_id = v.id
    ) OR m.maintenance_date IS NULL
    ORDER BY v.id;
    """
    return query_db(sql, fetch=True)

def add_maintenance_record(vending_machine_id, maintenance_date, description):
    sql = "INSERT INTO maintenance_records (vending_machine_id, maintenance_date, description) VALUES (%s, %s, %s)"
    query_db(sql, (vending_machine_id, maintenance_date, description), fetch=False)
