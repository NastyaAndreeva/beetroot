class TVController:
    CHANNELS = ["BBC", "Discovery", "TV1000"]
    
    def __init__(self):
        self.current_channel_idx = 0

    def first_channel(self):
        print(self.CHANNELS[0])

    def last_channel(self):
        print(self.CHANNELS[-1])

    def turn_channel(self, n):
        if self.is_exist(n) == "Yes":
            print(self.CHANNELS[n - 1])
        else:
            print("There is no such a channel")

    def next_channel(self):
        self.current_channel_idx += 1

    def previous_channel(self):
        self.current_channel_idx -= 1

    def current_channel(self):
        return self.current_channel_idx

    def is_exist(self, n):
        if n >= len(self.CHANNELS):
            return "No"

        return "Yes"

controller_1 = TVController()

controller_1.first_channel()
controller_1.last_channel()
controller_1.turn_channel(5)
print(controller_1.current_channel())
controller_1.next_channel()
print(controller_1.current_channel())
controller_1.previous_channel()
print(controller_1.current_channel())