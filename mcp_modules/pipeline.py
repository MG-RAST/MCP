from subsystem import subsystem

class pipeline(subsystem):
    def __init__(self, MCP_dir, json_conf_file_path):
        subsystem.__init__(self, MCP_dir, json_conf_file_path)
