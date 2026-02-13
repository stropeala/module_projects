DB_PATH = "CoffeeShop/caffee/caffee.db"

TEST_DB_PATH = "CoffeeShop/test_db/caffee.db"

EMPLOYEE_TABLE = "Employee"
EMPLOYEE_TABLE_COLUMNS = "('start.date', 'role')"
EMPLOYEE_STARTDATE_ROLE = "(?, ?)"

MENU_TABLE = "Menu"
MENU_TABLE_COLUMNS = "('name', 'price')"
MENU_NAME_PRICE = "(?, ?)"

ORDERS_TABLE = "Orders"
ORDERS_TABLE_COLUMNS = "('name', 'qty', 'client_id','timestamp', 'casier_id')"
ORDERS_NAME_QTY_CLIENTID_TIMESTAMP_CASHIERID = "(?, ?, ?, ?, ?)"

MARIUSICA_ORDER = ("FRIPTURA", "3", "MARIUSICA BOSSULICA", "2025-06-07 20:45", "TEST")

ORDERS_GET_QTY_SUM = "client_id, SUM(qty)"
ORDERS_GET_QTY_SUM_GROUPED = "GROUP by client_id"

MENU_ESPRESSO_PRICE = "name='Espresso' AND price='10,99'"
MENU_ESPRESSO_NEW_PRICE = "price='12,99'"
