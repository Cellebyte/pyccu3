from enum import Enum


class MultiValueEnum(Enum):
    """
    This is an enum which supports multiple values for serialization.
    The output is everytime the first item when you serialize it to a string.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(self, args, kwargs)
        self._all_values = []

    def __new__(cls, *values):
        obj = object.__new__(cls)
        # first value is canonical value
        obj._value_ = values[0]
        for other_value in values[1:]:
            cls._value2member_map_[other_value] = obj
        obj._all_values = values
        return obj

    def __str__(self) -> str:
        return f"{self.values[0]}"

    @property
    def values(self) -> list:
        return self._all_values

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}("{self.__str__()}")'


class AESState(Enum):
    DISABLED = 0
    ENABLED = 1


class BOOLEAN(MultiValueEnum):
    TRUE = True, "true", "yes"
    FALSE = False, "false", "no"


class DataPointType(Enum):
    ACTIVITY_STATE = "ACTIVITY_STATE"
    ACTUAL_TEMPERATURE = "ACTUAL_TEMPERATURE"
    ACTUAL_TEMPERATURE_STATUS = "ACTUAL_TEMPERATURE_STATUS"
    ACTIVE_PROFILE = "ACTIVE_PROFILE"
    BOOST_MODE = "BOOST_MODE"
    BOOST_TIME = "BOOST_TIME"
    CARRIER_SENSE_LEVEL = "CARRIER_SENSE_LEVEL"
    CMD_KILL = "CMD_KILL"
    CMD_EXEC = "CMD_EXEC"
    COMBINED_PARAMETER = "COMBINED_PARAMETER"
    CONFIG_PENDING = "CONFIG_PENDING"
    CONTROL_DIFFERENTIAL_TEMPERATURE = "CONTROL_DIFFERENTIAL_TEMPERATURE"
    CONTROL_MODE = "CONTROL_MODE"
    CURRENT = "CURRENT"
    DATE_TIME_UNKNOWN = "DATE_TIME_UNKNOWN"
    DEW_POINT_ALARM = "DEW_POINT_ALARM"
    DURATION_UNIT = "DURATION_UNIT"
    DURATION_VALUE = "DURATION_VALUE"
    DUTY_CYCLE = "DUTY_CYCLE"
    DUTY_CYCLE_LEVEL = "DUTY_CYCLE_LEVEL"
    EMERGENCY_OPERATION = "EMERGENCY_OPERATION"
    ENERGY_COUNTER = "ENERGY_COUNTER"
    ERROR_CODE = "ERROR_CODE"
    ERROR_OVERHEAT = "ERROR_OVERHEAT"
    EXTERNAL_CLOCK = "EXTERNAL_CLOCK"
    FREQUENCY = "FREQUENCY"
    FROST_PROTECTION = "FROST_PROTECTION"
    HEATING_COOLING = "HEATING_COOLING"
    HUMIDITY = "HUMIDITY"
    HUMIDITY_ALARM = "HUMIDITY_ALARM"
    HUMIDITY_LIMITER = "HUMIDITY_LIMITER"
    HUMIDITY_STATUS = "HUMIDITY_STATUS"
    INCLUSION_UNSUPPORTED_DEVICE = "INCLUSION_UNSUPPORTED_DEVICE"
    IP_ADDRESS = "IP_ADDRESS"
    LEVEL = "LEVEL"
    LEVEL_STATUS = "LEVEL_STATUS"
    LOW_BAT = "LOW_BAT"
    OPERATING_VOLTAGE = "OPERATING_VOLTAGE"
    OPERATING_VOLTAGE_STATUS = "OPERATING_VOLTAGE_STATUS"
    PARTY_MODE = "PARTY_MODE"
    PARTY_SET_POINT_TEMPERATURE = "PARTY_SET_POINT_TEMPERATURE"
    PARTY_TIME_END = "PARTY_TIME_END"
    PARTY_TIME_START = "PARTY_TIME_START"
    QUICK_VETO_TIME = "QUICK_VETO_TIME"
    PRE_HUMIDITY_LIMITER = "PRE_HUMIDITY_LIMITER"
    PRESS_LONG = "PRESS_LONG"
    PRESS_LONG_RELEASE = "PRESS_LONG_RELEASE"
    PRESS_LONG_START = "PRESS_LONG_START"
    PRESS_SHORT = "PRESS_SHORT"
    PROCESS = "PROCESS"
    RSSI_DEVICE = "RSSI_DEVICE"
    RSSI_PEER = "RSSI_PEER"
    POWER = "POWER"
    SABOTAGE = "SABOTAGE"
    SECTION = "SECTION"
    SECTION_STATUS = "SECTION_STATUS"
    SET_POINT_MODE = "SET_POINT_MODE"
    SET_POINT_TEMPERATURE = "SET_POINT_TEMPERATURE"
    STATE = "STATE"
    STOP = "STOP"
    SWITCH_POINT_OCCURED = "SWITCH_POINT_OCCURED"
    TEMPERATURE_LIMITER = "TEMPERATURE_LIMITER"
    TEMPERATURE_OUT_OF_RANGE = "TEMPERATURE_OUT_OF_RANGE"
    TOGGLE = "TOGGLE"
    UNREACH = "UNREACH"
    UPDATE_PENDING = "UPDATE_PENDING"
    VALVE_STATE = "VALVE_STATE"
    VALVE_ADAPTION = "VALVE_ADAPTION"
    VOLTAGE = "VOLTAGE"
    WEEK_PROGRAM_CHANNEL_LOCKS = "WEEK_PROGRAM_CHANNEL_LOCKS"
    WEEK_PROGRAM_TARGET_CHANNEL_LOCK = "WEEK_PROGRAM_TARGET_CHANNEL_LOCK"
    WEEK_PROGRAM_TARGET_CHANNEL_LOCKS = "WEEK_PROGRAM_TARGET_CHANNEL_LOCKS"
    WINDOW_STATE = "WINDOW_STATE"
    WORKING = "WORKING"


class DataPointUnit(MultiValueEnum):
    CELSIUS = "°C"
    DECIMAL_PERCENT = "%", "% rF"
    PERCENT = "100%"
    VOLTAGE = "V"
    WATT_HOUR = "Wh"
    MILLI_AMPERE = "mA"
    HERTZ = "Hz"
    WATT = "W"
    UNKNOWN = "", '""'


class RFInterface(Enum):
    HMIP_RF = "HmIP-RF"
    VirtualDevices = "VirtualDevices"
    CUxD = "CUxD"


class RxMode(Enum):
    RX_UNKNOWN = 0x00
    RX_ALWAYS = 0x01
    RX_BURST = 0x02
    RX_UNKNOWN_3 = 0x03
    RX_CONFIG = 0x04
    RX_WAKEUP = 0x08
    RX_LAZY_CONFIG = 0x10


class XMLDirection(Enum):
    UNKNOWN = "UNKNOWN"
    SENDER = "SENDER"
    RECEIVER = "RECEIVER"


class Direction(Enum):
    UNKNOWN = 0
    SENDER = 1
    RECEIVER = 2


class FirmwareUpdateState(Enum):
    UP2DATE = "UP_TO_DATE"
    RDY4UPDATE = "READY_FOR_UPDATE"
    UNKNOWN = ""
