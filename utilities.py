import os
import socket
import config as c


def get_cluster_name() -> str:
    """Return the name of the HPC cluster."""
    for var in ("SLURM_CLUSTER_NAME", "CLUSTER_NAME"):
        value = os.environ.get(var)
        if value:
            return value
    hostname = socket.getfqdn()
    return hostname.split(".")[0]


def title_with_bars(title: str = "My Share") -> str:
    """Return a string containing the title of the output with a bar below and
       above."""
    return f'{"─" * c.WIDTH}\n{title.center(c.WIDTH, "─")}\n{"─" * c.WIDTH}'
