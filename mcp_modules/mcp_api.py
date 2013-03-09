import glob, json, sys, time
from subsystem import subsystem

class mcp_api(subsystem):
    actions = "start"

    def __init__(self, MCP_dir):
        subsystem.__init__(self, MCP_dir)
        self.state = { 'resource':self.__class__.__name__,
                       'date':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                       'status':'online'
                     }
        self.apidir = self.parser.get('mcp_api', 'dir') + "/" + self.parser.get('mcp_api', 'version')
        self.services = self.parser.get('global', 'services')

    def start(self):
        files = glob.glob(self.apidir+"/*")
        if len(files) != 0:
            sys.stderr.write("ERROR: Cannot initialize mcp_api because API directory (" + self.apidir + ") is not empty\n")
            return 0

        for service in self.services.split(','):
            service = service.strip();
            module = __import__(service)
            myclass = getattr(module, service)
            myservice = myclass(self.MCP_dir)

            jstate = json.dumps(myservice.get_state())
            f = open(self.apidir + "/" + service, 'w')
            f.write(jstate)