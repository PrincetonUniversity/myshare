import os
import socket


def get_cluster_name() -> str:
    """Return the name of the HPC cluster."""
    for var in ("SLURM_CLUSTER_NAME", "CLUSTER_NAME"):
        value = os.environ.get(var)
        if value:
            return value
    hostname = socket.getfqdn()
    return hostname.split(".")[0]
