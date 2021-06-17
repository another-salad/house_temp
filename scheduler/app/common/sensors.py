"""All Temp sensor values"""


from common import SENSOR_TEMP_KEY, SENSOR_ERROR_KEY, SENSOR_LOCATION_KEY
from common.enums import RequestTypes
from common.exceptions import SensorError
from common.requester import Requester


class Sensors(Requester):
    """All temp sensors, inherits from Requester"""

    @property
    def temps(self):
        """The sensor temps"""
        all_temps = []
        for sensor in self.hosts.sensors:
            error, resp = self.request(uri=sensor, method=RequestTypes.GET)
            if error or not all(False for x in [SENSOR_TEMP_KEY, SENSOR_ERROR_KEY, SENSOR_LOCATION_KEY] if x not in resp.keys()):
                # For now, print this to the console - logging will come later
                print(f"Error returned from sensor: {sensor}. Response: {resp}")
                continue

            all_temps.append(resp)

        if not all_temps:
            raise SensorError(f'None of the sensors returned a valid response. Sensors: {self.hosts.sensors}')

        return all_temps
