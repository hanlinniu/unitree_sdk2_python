import time
import sys
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize

from unitree_sdk2py.idl.default import unitree_go_msg_dds__SportModeState_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import SportModeState_


def HighStateHandler(msg: SportModeState_):

    print('#' * 20)
    print("Position: ", msg.position)
    print("Velocity: ", msg.velocity)
    print("Yaw velocity: ", msg.yaw_speed)
    print("Foot position in body frame: ", msg.foot_position_body)
    print("Foot velocity in body frame: ", msg.foot_speed_body)


    print('#' * 20)
    print("stamp : ", msg.stamp)
    print("error_code : ", msg.error_code)
    print("imu_state : ", msg.imu_state)
    print("mode : ", msg.mode)
    print("progress : ", msg.progress)
    print("gait_type : ", msg.gait_type)
    print("foot_raise_height : ", msg.foot_raise_height)
    print("position : ", msg.position)
    print("body_height : ", msg.body_height)
    print("velocity : ", msg.velocity)
    print("yaw_speed : ", msg.yaw_speed)
    print("range_obstacle : ", msg.range_obstacle)
    print("foot_force : ", msg.foot_force)
    print("foot_position_body : ", msg.foot_position_body)
    print("foot_speed_body : ", msg.foot_speed_body)
    print("path_point : ", msg.path_point)
    

    # stamp: 'unitree_sdk2py.idl.unitree_go.msg.dds_.TimeSpec_'
    # error_code: types.uint32
    # imu_state: 'unitree_sdk2py.idl.unitree_go.msg.dds_.IMUState_'
    # mode: types.uint8
    # progress: types.float32
    # gait_type: types.uint8
    # foot_raise_height: types.float32
    # position: types.array[types.float32, 3]
    # body_height: types.float32
    # velocity: types.array[types.float32, 3]
    # yaw_speed: types.float32
    # range_obstacle: types.array[types.float32, 4]
    # foot_force: types.array[types.int16, 4]
    # foot_position_body: types.array[types.float32, 12]
    # foot_speed_body: types.array[types.float32, 12]
    # path_point: types.array['unitree_sdk2py.idl.unitree_go.msg.dds_.PathPoint_', 10]




if __name__ == "__main__":
    # sys.argv[1]: name of the network interface
    ChannelFactoryInitialize(0, sys.argv[1])
    sub = ChannelSubscriber("rt/sportmodestate", SportModeState_)
    sub.Init(HighStateHandler, 10)

    while True:
        time.sleep(10.0)
