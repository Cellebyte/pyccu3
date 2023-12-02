from dataclasses import dataclass, field
from typing import Union, List, Optional
from pyccu3.objects.base import XMLAPIBaseSerializer
from pyccu3.enums import (
    XMLDirection,
    DataPointType,
    BOOLEAN,
    DataPointUnit,
    RFInterface,
)


@dataclass
class HomeMaticChannel(XMLAPIBaseSerializer):
    name: str
    type: int
    address: str
    ise_id: int
    direction: XMLDirection
    parent_device: int
    index: int
    group_partner: str
    aes_available: bool
    transmission_mode: str
    visible: bool
    ready_config: bool
    operate: bool


@dataclass
class HomeMaticDatapoint(XMLAPIBaseSerializer):
    name: str
    type: DataPointType
    ise_id: int
    value: Union[float, BOOLEAN]
    valuetype: int
    valueunit: DataPointUnit
    timestamp: int
    operations: int


@dataclass
class HomeMaticStateChannel(XMLAPIBaseSerializer):
    name: str
    ise_id: int
    index: int
    visible: bool
    operate: bool
    datapoint: List[HomeMaticDatapoint] = field(default_factory=list)


@dataclass
class HomeMaticDevice(XMLAPIBaseSerializer):
    name: str
    address: str
    ise_id: int
    interface: RFInterface
    device_type: str
    ready_config: bool
    channel: List[HomeMaticChannel] = field(default_factory=list)


@dataclass
class HomeMaticState(XMLAPIBaseSerializer):
    name: str
    ise_id: int
    unreach: Optional[bool]
    config_pending: Optional[bool]
    channel: List[HomeMaticStateChannel] = field(default_factory=list)


@dataclass
class HomeMaticRoomChannel(XMLAPIBaseSerializer):
    ise_id: int


@dataclass
class HomeMaticRoom(XMLAPIBaseSerializer):
    name: str
    ise_id: int
    channel: List[HomeMaticRoomChannel] = field(default_factory=list)


@dataclass
class HomeMaticProgram(XMLAPIBaseSerializer):
    id: int
    active: bool
    timestamp: int
    name: str
    description: str
    visible: bool
    operate: bool


@dataclass
class HomeMaticDevices(XMLAPIBaseSerializer):
    device: List[HomeMaticDevice] = field(default_factory=list)


@dataclass
class HomeMaticDeviceList(XMLAPIBaseSerializer):
    deviceList: HomeMaticDevices


@dataclass
class HomeMaticStates(XMLAPIBaseSerializer):
    device: List[HomeMaticState] = field(default_factory=list)


@dataclass
class HomeMaticRooms(XMLAPIBaseSerializer):
    room: List[HomeMaticRoom] = field(default_factory=list)


@dataclass
class HomeMaticPrograms(XMLAPIBaseSerializer):
    program: List[HomeMaticProgram]


@dataclass
class HomeMaticStateList(XMLAPIBaseSerializer):
    stateList: HomeMaticStates


@dataclass
class HomeMaticRoomList(XMLAPIBaseSerializer):
    roomList: HomeMaticRooms


@dataclass
class HomeMaticProgramList(XMLAPIBaseSerializer):
    programList: HomeMaticPrograms
