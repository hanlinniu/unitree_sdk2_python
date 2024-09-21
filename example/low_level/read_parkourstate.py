import time
import sys
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.default import unitree_go_msg_dds__LowState_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import LowState_

import unitree_legged_const as go2


def LowStateHandler(msg: LowState_):
    
    # print front right hip motor states
    print("#######################################################")
    print("FR_0 motor state: ", msg.motor_state[go2.LegID["FR_0"]])
    print("IMU state: ", msg.imu_state)
    print("Battery state: voltage: ", msg.power_v, "current: ", msg.power_a)


    ######################################################################
    print("#######################################################")
    print("head: ", msg.head)
    print("level_flag: ", msg.level_flag)
    print("frame_reserve : ", msg.frame_reserve)
    print("sn : ", msg.sn)
    print("version : ", msg.version)
    print("bandwidth : ", msg.bandwidth)
    print("imu_state : ", msg.imu_state)
    print("motor_state : ", msg.motor_state)
    print("bms_state : ", msg.bms_state)
    print("foot_force : ", msg.foot_force)
    print("foot_force_est : ", msg.foot_force_est)
    print("tick : ", msg.tick)
    print("wireless_remote : ", msg.wireless_remote)
    print("bit_flag : ", msg.bit_flag)
    print("adc_reel : ", msg.adc_reel)
    print("temperature_ntc1 : ", msg.temperature_ntc1)
    print("temperature_ntc2 : ", msg.temperature_ntc2)
    print("power_v : ", msg.power_v)
    print("power_a : ", msg.power_a)
    print("fan_frequency : ", msg.fan_frequency)
    print("reserve : ", msg.reserve)
    print("crc : ", msg.crc)


    # head: types.array[types.uint8, 2]
    # level_flag: types.uint8
    # frame_reserve: types.uint8
    # sn: types.array[types.uint32, 2]
    # version: types.array[types.uint32, 2]
    # bandwidth: types.uint16
    # imu_state: 'unitree_sdk2py.idl.unitree_go.msg.dds_.IMUState_'
    # motor_state: types.array['unitree_sdk2py.idl.unitree_go.msg.dds_.MotorState_', 20]
    # bms_state: 'unitree_sdk2py.idl.unitree_go.msg.dds_.BmsState_'
    # foot_force: types.array[types.int16, 4]
    # foot_force_est: types.array[types.int16, 4]
    # tick: types.uint32
    # wireless_remote: types.array[types.uint8, 40]
    # bit_flag: types.uint8
    # adc_reel: types.float32
    # temperature_ntc1: types.uint8
    # temperature_ntc2: types.uint8
    # power_v: types.float32
    # power_a: types.float32
    # fan_frequency: types.array[types.uint16, 4]
    # reserve: types.uint32
    # crc: types.uint32


if __name__ == "__main__":
    if len(sys.argv)>1:
        ChannelFactoryInitialize(0, sys.argv[1])
    else:
        ChannelFactoryInitialize(0)
    sub = ChannelSubscriber("rt/lowstate", LowState_)
    sub.Init(LowStateHandler, 10)

    while True:
        time.sleep(10.0)
