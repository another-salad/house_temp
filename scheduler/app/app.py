"""Run time application"""

from common import STORED_PROC_KEY, TEMP_STORED_PROC, SENSOR_ERROR_KEY, SENSOR_LOCATION_KEY, SENSOR_TEMP_KEY, DB_ARGS_KEY
from common.db import DB
from common.exceptions import SetTempError
from common.sensors import Sensors
from common.enums import RequestTypes


def main():
    """The main application"""
    sensor_data = Sensors().temps
    db = DB()
    fails = []
    for data in sensor_data:
        args = {STORED_PROC_KEY: TEMP_STORED_PROC} | {DB_ARGS_KEY: [data[SENSOR_TEMP_KEY], data[SENSOR_ERROR_KEY], data[SENSOR_LOCATION_KEY]]}
        error, resp = db.request(method=RequestTypes.POST, uri=f"{db.db_host}/{db.call}", args=args)
        if error:
            fails.append(resp)

    if fails:
        raise SetTempError(f"The following errored when saving to the DB: {fails}")


if __name__ == "__main__":
    main()
