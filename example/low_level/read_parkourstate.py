import time
import sys
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.default import unitree_go_msg_dds__LowState_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import LowState_

import unitree_legged_const as go2


def LowStateHandler(msg: LowState_):
    
    # print front right hip motor states
    print("#######################################################")
    print("FR_0 motor state: ", msg.motor_state[go2.LegID["FR_0"]])  # FR_0 motor state:  MotorState_(mode=1, q=-0.03379714488983154, dq=0.034879714250564575, ddq=0.0, tau_est=-0.07421484589576721, q_raw=0.0, dq_raw=0.0, ddq_raw=0.0, temperature=27, lost=0, reserve=[0, 638])
    print("IMU state: ", msg.imu_state)  # imu_state :  IMUState_(quaternion=[-0.9685593247413635, -0.0061267982237041, 0.0533742792904377, -0.2429129183292389], gyroscope=[-0.0010652643395587802, -0.0074568502604961395, -0.0063915858045220375], accelerometer=[0.8176198601722717, -0.011971008032560349, 9.576807022094727], rpy=[-0.01414297055453062, -0.10657048225402832, 0.4922139048576355], temperature=79)
    print("Battery state: voltage: ", msg.power_v, "current: ", msg.power_a)  # voltage:  31.24382972717285 current:  0.6494534611701965


    ######################################################################
    print("#######################################################")
    print("head: ", msg.head)  # b'\xfe\xef'
    print("level_flag: ", msg.level_flag)  # 0
    print("frame_reserve : ", msg.frame_reserve)  # 0
    print("sn : ", msg.sn)  # [0, 0]
    print("version : ", msg.version)  # [0, 0]
    print("bandwidth : ", msg.bandwidth)  # 0 
    print("imu_state : ", msg.imu_state)  # IMUState_(quaternion=[-0.9685593247413635, -0.0061267982237041, 0.0533742792904377, -0.2429129183292389], gyroscope=[-0.0010652643395587802, -0.0074568502604961395, -0.0063915858045220375], accelerometer=[0.8176198601722717, -0.011971008032560349, 9.576807022094727], rpy=[-0.01414297055453062, -0.10657048225402832, 0.4922139048576355], temperature=79)
    print("motor_state : ", msg.motor_state)  # 
    print("bms_state : ", msg.bms_state)  # BmsState_(version_high=1, version_low=14, status=8, soc=93, current=-939, cycle=5, bq_ntc=b'\x14\x14', mcu_ntc=b'\x18\x17', cell_vol=[4081, 4084, 4084, 4084, 4084, 4085, 4084, 4081, 0, 0, 0, 0, 0, 0, 0])
    print("foot_force : ", msg.foot_force)  # [15, 14, 16, 16]
    print("foot_force_est : ", msg.foot_force_est)  # [0, 0, 0, 0]
    print("tick : ", msg.tick)  # 1885451
    print("wireless_remote : ", msg.wireless_remote)
    print("bit_flag : ", msg.bit_flag)  # 36
    print("adc_reel : ", msg.adc_reel)  # 0.0
    print("temperature_ntc1 : ", msg.temperature_ntc1)  # 31.24382972717285
    print("temperature_ntc2 : ", msg.temperature_ntc2)  # 0.6494534611701965
    print("power_v : ", msg.power_v)  # 38
    print("power_a : ", msg.power_a)  # 34
    print("fan_frequency : ", msg.fan_frequency)  # [0, 0, 0, 0]
    print("reserve : ", msg.reserve)  # 0
    print("crc : ", msg.crc)  # 150977541


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
