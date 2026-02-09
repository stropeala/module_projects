"""
first time we write all the clients
then we update the exit time
then we calculate the park time
then we update pariah
then we read the different kinds of clients
    pariah = true
    <2 hr new table
    >2 hr new table
    >3 days new table
"""

from db import db
from helpers import read_and_write_extra_tables

PARKING_DB_PATH = (
    "ParkingLot/at-home/SQLite/data/parkinglot.db"  # change if dir changes
)

if __name__ == "__main__":
    # We add a client with each db() func call
    db(PARKING_DB_PATH, "Lynn", "Newton", "(717) 550-1675", "Seattle, WA")
    db(PARKING_DB_PATH, "Genaro", "Willis", "(206) 342-8631", "Harrisburg, PA")
    db(PARKING_DB_PATH, "Rosanne", "Maldonado", "(248) 762-0356", "Farmington, MIV")
    db(PARKING_DB_PATH, "Pauline", "Figueroa", "(253) 644-2182", "Auburn, WA")
    db(PARKING_DB_PATH, "Rickey", "Clements", "(212) 658-3916", "New York City, NY")
    db(PARKING_DB_PATH, "Jeanne", "Wolf", "(209) 300-2557", "Ceres, CAA")
    db(PARKING_DB_PATH, "Dustin", "Carrillo", "(262) 162-1585", "Menomonee Falls, W")
    db(PARKING_DB_PATH, "Sally", "Reeves", "(252) 258-379", "Greenville, NC")
    db(PARKING_DB_PATH, "Jaclyn", "Andersen", "(234) 109-6666", "Akron, OH")
    db(PARKING_DB_PATH, "Esteban", "Shelton", "(201) 874-8593", "Bayonne, NJ")
    # After that we can make extra tables with different parking times
    read_and_write_extra_tables(PARKING_DB_PATH)
