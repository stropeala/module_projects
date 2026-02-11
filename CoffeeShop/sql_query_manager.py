DB_PATH = "CoffeeShop/caffee/caffee.db"

DRAFT_DB_PATH = "CoffeeShop/caffee/draft_db/caffee.db"

EMPLOYEE_TABLE = "Employee"
EMPLOYEE_TABLE_COLUMNS = "('start.date', 'role')"

MENU_TABLE = "Menu"
MENU_TABLE_COLUMNS = "('name', 'price')"

ORDERS_TABLE = "Orders"
ORDERS_TABLE_COLUMNS = "('name', 'qty', 'client_id','timestamp', 'casier_id')"

ADD_EMPLOYEE = """
INSERT INTO Employee
('start.date', 'role')
VALUES
(?, ?)
"""

GET_QTY_SUM = """
SELECT client_id, SUM(qty)
FROM Orders
GROUP BY client_id;
"""
