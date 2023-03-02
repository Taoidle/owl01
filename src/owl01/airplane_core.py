import dataclasses

from typing import Dict

@dataclasses.dataclass()
class AirplaneFlyStatus(object):
    """
    每个飞机的飞行状态
    """
    landing: bool
    isStop: bool
    x: float
    y: float
    h: float
    rX: float
    rY: float
    rZ: float
    pass


def make_AirplaneFlyStatus(
        fly_status: Dict[str, any]
):
    return AirplaneFlyStatus(
        landing=fly_status['landing'],
        isStop=fly_status['isStop'],
        x=fly_status['x'],
        y=fly_status['y'],
        h=fly_status['h'],
        rX=fly_status['rX'],
        rY=fly_status['rY'],
        rZ=fly_status['rZ'],
    )
    pass


# @dataclasses.dataclass()
class AirplaneCore(object):
    """
    每个飞机的基本信息
    """
    keyName: str
    typeName: str
    updateTimestamp: int
    status: AirplaneFlyStatus
