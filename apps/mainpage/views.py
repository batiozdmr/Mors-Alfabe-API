from django.shortcuts import render

from apps.common.api.api import api
from apps.common.covert_size.convert import convert_size
from apps.common.mors.mors import *


def index(request):
    # CPU
    cpu = api("CPU")
    checksum_cpu_decrypt = mors_decrypt(cpu['checksum'].upper())
    data_cpu = cpu['data']
    new_data_cpu = []
    new_data_cpu_count = 0
    for data in data_cpu:
        new_data_cpu_count = new_data_cpu_count + 1
        new_data_cpu.append(
            {
                'model': mors_decrypt(data['model'].upper()),
                'speed': mors_decrypt(data['speed'].upper()),
                'times_user': mors_decrypt(data['times']['user'].upper()),
                'times_sys': mors_decrypt(data['times']['sys'].upper()),
                'times_idle': mors_decrypt(data['times']['idle'].upper()),
                'times_irq': mors_decrypt(data['times']['irq'].upper()),
            }
        )
    # CPU

    # ARCH
    arch = api("ARCH")
    checksum_arch_decrypt = mors_decrypt(arch['checksum'].upper())
    data_arch_decrypt = mors_decrypt(arch['data'].upper())
    # ARCH

    # FREEMEM
    freemem = api("FREEMEM")
    checksum_freemem_decrypt = mors_decrypt(freemem['checksum'].upper())
    data_freemem_decrypt = convert_size(int(mors_decrypt(freemem['data'].upper())))
    # FREEMEM

    # HOSTNAME
    hostname = api("HOSTNAME")
    checksum_hostname_decrypt = mors_decrypt(hostname['checksum'].upper())
    data_hostname_decrypt = mors_decrypt(hostname['data'].upper())
    # HOSTNAME

    # PLATFORM
    platform = api("PLATFORM")
    checksum_platform_decrypt = mors_decrypt(platform['checksum'].upper())
    data_platform_decrypt = mors_decrypt(platform['data'].upper())
    # PLATFORM

    # TOTALMEM
    totalmem = api("TOTALMEM")
    checksum_totalmem_decrypt = mors_decrypt(totalmem['checksum'].upper())
    data_totalmem_decrypt = convert_size(int(mors_decrypt(totalmem['data'].upper())))
    # TOTALMEM

    # TYPE
    type_str = api("TYPE")
    checksum_type_str_decrypt = mors_decrypt(type_str['checksum'].upper())
    data_type_str_decrypt = mors_decrypt(type_str['data'].upper())
    # TYPE

    # UPTIME
    uptime = api("UPTIME")
    checksum_uptime_decrypt = mors_decrypt(uptime['checksum'].upper())
    data_uptime_decrypt = mors_decrypt(uptime['data'].upper())
    # UPTIME

    context = {
        'new_data_cpu': new_data_cpu,
        'new_data_cpu_count': new_data_cpu_count,
        'checksum_cpu_decrypt': checksum_cpu_decrypt,

        'checksum_arch_decrypt': checksum_arch_decrypt,
        'data_arch_decrypt': data_arch_decrypt,

        'checksum_freemem_decrypt': checksum_freemem_decrypt,
        'data_freemem_decrypt': data_freemem_decrypt,

        'checksum_hostname_decrypt': checksum_hostname_decrypt,
        'data_hostname_decrypt': data_hostname_decrypt,

        'checksum_platform_decrypt': checksum_platform_decrypt,
        'data_platform_decrypt': data_platform_decrypt,

        'checksum_totalmem_decrypt': checksum_totalmem_decrypt,
        'data_totalmem_decrypt': data_totalmem_decrypt,

        'checksum_type_str_decrypt': checksum_type_str_decrypt,
        'data_type_str_decrypt': data_type_str_decrypt,

        'checksum_uptime_decrypt': checksum_uptime_decrypt,
        'data_uptime_decrypt': data_uptime_decrypt,

    }
    return render(request, "index.html", context)


def notFound(request):
    return render(request, "404.html", {})
