import time
from opcua import Server
from led import CurrentState

class LedServer(object):
    """
    Creates an OPCUA Server. This server can be notified about changes
    calling the `notify` method.
    """
    def __init__(self, url, name, led_block):
        self.led_block = led_block
        self.server = Server()
        self.server.set_endpoint(url)
        addspace = self.server.register_namespace(name)
        node = self.server.get_objects_node()

        param = node.add_object(addspace, "Parameters")
        # Subparam = Param.add_object(addspace,"Subparam")

        self.time = param.add_variable(addspace, "Time", 0.0)
        self.leds = [
            param.add_variable(addspace, "LED1", 0),
            param.add_variable(addspace, "LED2", 0),
            param.add_variable(addspace, "LED3", 0),
            param.add_variable(addspace, "LED4", 0),
        ]
        # Set leds writeable for the clients
        for led in self.leds:
            led.set_writable()
        self.server.start()

    def notify_clients(self, new_val):
        """
        Notify clients about change.
        """
        i = 0
        for value in new_val:
            self.leds[i].set_value(value)
            i += 1
        self.time.set_value(time.time())

    def start_server(self):
        """
        Initialize the server. It is a blocking operation,
        so it should be started in its own thread.
        """
        try:
            print("Server started...")
            while True:
                values = list(map(lambda x: x.get_value(),self.leds))
                self.led_block.set_state(CurrentState(values[0], values[1], values[2], values[3]))
                print(str(values))
                time.sleep(5)


        finally:
            self.server.stop()
