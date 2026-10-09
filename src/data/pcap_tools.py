import shutil

class PacketTools:
    def __init__(self, *names: str) -> None:
        self.names = names

    def get_packet_tools(self) -> dict[str, str]:
        tools = {name: shutil.which(name) for name in self.names}
        missing = [name for name, path in tools.items() if path is None]

        if missing:
            raise RuntimeError(f"Missing PCAP tools: {missing}")

        return tools