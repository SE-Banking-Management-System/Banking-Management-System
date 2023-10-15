import sqlite3

db = sqlite3.connect("bank_dat.db")
c = db.cursor()
current_login = 0

def init_db():
    c.execute("CREATE TABLE IF NOT EXISTS admin(id VARCHAR(32), password VARCHAR(32), PRIMARY KEY (id))")
    c.execute("CREATE TABLE IF NOT EXISTS customer(id VARCHAR(32), password VARCHAR(32), balance INT, phone_number "
              "VARCHAR(10), address TEXT, dob VARCHAR(10), PRIMARY KEY (id))")
    db.commit()


def register_customer(customer_id, password, balance, phone_number, address, dob):
    query = f"INSERT INTO customer VALUES (\"{customer_id}\", \"{password}\", {balance}, \"{phone_number}\", \"{address}\", \"{dob}\")"
    c.execute(query)
    db.commit()


def retrieve_admins():
    c.execute("SELECT * FROM admin")
    result = c.fetchall()
    return result


def retrieve_customers():
    c.execute("SELECT * FROM customer")
    result = c.fetchall()
    return result


def get_next_customer_id():
    i = len(retrieve_customers())
    return 12000 + i


def validate_customer(customer_id, password):
    customers = retrieve_customers()

    for customer in customers:
        if customer[0] == customer_id and customer[1] == password:
            return True

    return False


def validate_admin(admin_id, password):
    admins = retrieve_admins()

    for admin in admins:
        if admin[0] == admin_id and admin[1] == password:
            return True

    return False


def get_balance(customer_id):
    customers = retrieve_customers()

    for customer in customers:
        if customer[0] == customer_id:
            return customer[2]

    return 0


def set_balance(customer_id, balance):
    query = f"UPDATE customer SET balance = {balance} WHERE id = {customer_id}"
    c.execute(query)
    db.commit()


def is_balance_sufficient(customer_id, amount):
    return get_balance(customer_id) >= amount


def withdraw(amount):
    flag = is_balance_sufficient(current_login, amount)

    if flag:
        current_balance = get_balance(current_login)
        new_balance = current_balance - amount
        set_balance(current_login, new_balance)

    return flag


def deposit(amount):
    current_balance = get_balance(current_login)
    new_balance = current_balance + amount
    set_balance(current_login, new_balance)


def transfer(to_account, amount):
    flag = is_balance_sufficient(current_login, amount)

    if flag:
        current_balance = get_balance(current_login)
        new_balance = current_balance - amount
        set_balance(current_login, new_balance)

        to_current_balance = get_balance(to_account)
        to_new_balance = to_current_balance + amount
        set_balance(to_account, to_new_balance)

    return flag

