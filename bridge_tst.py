# ruff: noqa: T201

"""Test file for HuaweiSolarBridge."""

import asyncio
import logging

from huawei_solar import HuaweiSUN2000Bridge, create_tcp_bridge
from typing import Any 
from huawei_solar import register_names as rn
from huawei_solar import register_values as rv

loop = asyncio.new_event_loop()

logging.basicConfig(level=logging.DEBUG)


async def test():
    """Run test."""
    bridge = await create_tcp_bridge(host="192.168.0.2", port=502, slave_id=100)
    # await bridge.has_write_permission()

    # assert isinstance(bridge, HuaweiSUN2000Bridge)
    # print(await bridge.has_write_permission())
    # await bridge.login("Installer", "SPCVeCPC123")
    # await bridge.batch_update(
    #     [
    #         # rn.MODEL_NAME,
    #         rn.SDONGLE_TYPE,
    #         rn.SDONGLE_MAXIMUM_DEVICES_ALLOWED,
    #         rn.SDONGLE_TOTAL_INPUT_POWER,
    # #         # rn.MODEL_NAME,
    # #         # rn.SDONGLE_DEVICE_CHANGE_SEQUENCE_NUMBER,
    # #         # rn.ACTIVE_POWER_PERCENTAGE_DERATING,
    # #         # rn.STORAGE_CAPACITY_CONTROL_MODE,
    # #         # rn.STORAGE_CAPACITY_CONTROL_SOC_PEAK_SHAVING,
    # #         # rn.STORAGE_CAPACITY_CONTROL_PERIODS,
    #     ]
    # )
    print(await bridge.client.get(rn.SDONGLE_TYPE))
    # print(await bridge.client.get(rn.MODEL_NAME))
    print(await bridge.client.get(rn.SDONGLE_MAXIMUM_DEVICES_ALLOWED))
    print(await bridge.client.get(rn.SDONGLE_TOTAL_INPUT_POWER))
    print(await bridge.client.get(rn.SDONGLE_LOAD_POWER))
    print(await bridge.client.get(rn.SDONGLE_GRID_POWER))
    print(await bridge.client.get(rn.SDONGLE_TOTAL_ACTIVE_POWER))
    print(await bridge.client.get(rn.SDONGLE_PORT_MODE))
    print(await bridge.client.get(rn.SDONGLE_NTP_TIME_SYNCHRONIZATION))
    # print(await bridge.client.get(rn.me))
    # result: dict[str, Any] = {
    #         "model_name": bridge.model_name,
    #         "serial_number": bridge.serial_number,
    #     }
    # if True:
            # Check if we have write access. If this is not the case, we will
            # need to login (and request the username/password from the user to be
            # able to do this).
        # result["has_write_permission"] = await bridge.has_write_permission()

    device_infos = await bridge.client.get_device_infos()
    print(device_infos)
    # print(await bridge.client.get(rn.SDONGLE_DEVICE_CHANGE_SEQUENCE_NUMBER))
    # print(await bridge.client.get(rn.SDONGLE_TOTAL_ACTIVE_POWER,2))
    # print(await bridge.client.get(rn.ACTIVE_POWER_PERCENTAGE_DERATING))

    # print(await bridge.client.get(rn.STORAGE_CAPACITY_CONTROL_MODE))
    # print(await bridge.client.get(rn.STORAGE_CAPACITY_CONTROL_SOC_PEAK_SHAVING))
    # print(await bridge.client.get(rn.STORAGE_CAPACITY_CONTROL_PERIODS))

    # i = 0
    # while i < 100:

    #     try:
    #         print(await bridge.update())
    #     except Exception as e:
    #         print("Updating failed: ", e)

    #     await asyncio.sleep(2.5)
    #     i = i+1
    # print(await bridge.get_optimizer_system_information_data())
    # print(await bridge.get_latest_optimizer_history_data())

    await bridge.stop()


loop.run_until_complete(test())
