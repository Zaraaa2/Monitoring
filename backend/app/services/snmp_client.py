def get_router_stats():
    return {
        "status": "online",
        "cpu_usage": "13%",
        "memory_usage": "42%",
        "uptime": "3 days 5 hours",
        "interfaces": [
            {"name": "ether1", "rx": "2.3 Mbps", "tx": "1.1 Mbps"},
            {"name": "ether2", "rx": "1.8 Mbps", "tx": "0.5 Mbps"},
        ],
    }
