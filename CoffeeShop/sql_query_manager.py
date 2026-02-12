DB_PATH = "CoffeeShop/caffee/caffee.db"

DRAFT_DB_PATH = "CoffeeShop/caffee/draft_db/caffee.db"

EMPLOYEE_TABLE = "Employee"
EMPLOYEE_TABLE_COLUMNS = "('start.date', 'role')"
EMPLOYEE_VALUES_STARTDATE_ROLE = "(?, ?)"

MENU_TABLE = "Menu"
MENU_TABLE_COLUMNS = "('name', 'price')"
MENU_VALUES_NAME_PRICE = "(?, ?)"

ORDERS_TABLE = "Orders"
ORDERS_TABLE_COLUMNS = "('name', 'qty', 'client_id','timestamp', 'casier_id')"
ORDERS_VALUES_NAME_QTY_CLIENTID_TIMESTAMP_CASHIERID = "(?, ?, ?, ?, ?)"
