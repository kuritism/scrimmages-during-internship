import platform
import psutil
import re
import socket
import uuid
import GPUtil

import requests

final = {}


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "version": response.get("version"),
        "mac address": ":".join(re.findall('..', '%012x' % uuid.getnode())),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "postal": response.get("postal"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "country_population": response.get("country_population")

    }
    return location_data


def get_specs():
    gpu_count = 1
    place_gpu = {}
    gpus = GPUtil.getGPUs()
    spec_data = {
        "platform": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "hostname": socket.gethostname(),
        "processor": platform.processor(),
        "ram": str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
    }
    for gpu in gpus:
        gpu_name = gpu.name

        gpus = {("gpu " + str(gpu_count)): gpu_name}
        gpu_temperature = {"gpu " + str(gpu_count) + " temp": f"{gpu.temperature} °C"}
        spec_data.update(gpus)
        spec_data.update(gpu_temperature)
        gpu_count += 1

    return spec_data


def get_storage():
    partitions = psutil.disk_partitions()
    storage_data = {}
    for partition in partitions:
        mountpoint_data = {f"{partition.device} Mount-point": partition.mountpoint}
        filetype_data = {f"{partition.device} File system type": partition.fstype}
        partition_usage = psutil.disk_usage(partition.mountpoint)
        totalsize_data = {f"{partition.device} storage total": get_size(partition_usage.total)}
        usedsize_data = {f"{partition.device} storage used": get_size(partition_usage.used)}
        freesize_data = {f"{partition.device} storage free": get_size(partition_usage.free)}
        storage_data.update(mountpoint_data)
        storage_data.update(filetype_data)
        storage_data.update(totalsize_data)
        storage_data.update(usedsize_data)
        storage_data.update(freesize_data)
    return storage_data


final.update(get_location())
final.update(get_specs())
final.update(get_storage())

print(final)
