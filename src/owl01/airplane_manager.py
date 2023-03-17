from typing import Dict, Optional
from .control_command import AirplaneController
from .relay import Relay


class AirplaneManager(object):
    _instance = None

    _relay = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._relay = Relay()
        pass

    airplanes_table: Dict[str, AirplaneController] = {}

    def ping(self):
        return None

    def start(self):
        return None

    def get_airplane(self, id: str) -> Optional[AirplaneController]:
        """
        获取指定无人机
        :param id: 无人机的 keyName
        :return: AirplaneController
        """
        if self.airplanes_table.get(id) == None:
            self.airplanes_table[id] = AirplaneController(id, self._relay)
        return self.airplanes_table.get(id)
        pass

    def sleep(self, wait_time: int) -> None:
        self._relay.sleep(wait_time)

    def get_airplane_extended(self, id: str) -> Optional[AirplaneController]:
        """
        获取扩展飞机对象
        这个函数获取的API在完全适配PhantasyIslandPythonRemoteControl的API基础上，添加了FH0A无人机特有功能API
        :param keyName: 无人机的 keyName
        :return: AirplaneController
        """
        return self.get_airplane(id)
        pass



    def flush(self):
        pass
        """
        更新当前管理器所管理的所有飞机的状态
        """
        # airplane_status: Dict[str, Dict[str, any]] = process_airplane(get_all_airplane_status())
        # if airplane_status is not None:
            # print('airplane_status', airplane_status)
        #     for k, status in airplane_status.items():
        #         # print('k', k)
        #         if self.airplanes_table.get(k) is None:
        #             self.airplanes_table[k] = AirplaneControllerExtended(
        #                 keyName=status['keyName'],
        #                 typeName=status['typeName'],
        #                 updateTimestamp=status['updateTimestamp'],
        #                 status=status['status'],
        #             )
        #         else:
        #             a: AirplaneController = self.airplanes_table.get(k)
        #             a.keyName = status['keyName']
        #             a.typeName = status['typeName']
        #             a.updateTimestamp = status['updateTimestamp']
        #             # a.status = make_AirplaneFlyStatus(status['status'])
        #             a.cameraFront = status['cameraFront']
        #             a.cameraDown = status['cameraDown']
        #         pass
        #     pass
        # else:
        #     return None

    def destroy(self):
        """反注册所有无人机"""
        for i in self.airplanes_table.values():
            i.shutdown()
            pass
        self.airplanes_table = {}
        pass

def get_airplane_manager():
    """
    AirplaneManager是以单例模式工作的，故而需要使用这个函数来获取AirplaneManager单例对象
    :return: AirplaneManager单例对象
    """
    return AirplaneManager()
