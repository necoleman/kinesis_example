from amazon_kclpy import kcl
import json, base64

class RecordProcessor(kcl.RecordProcessorBase):

    def initialize(self, initialization_input):
        pass

    def process_records(self, process_records_input):
        pass

    def lease_lost(self, lease_lost_input):
        pass

    def shard_ended(self, shard_ended_input):
        pass

    def shutdown_requested(self, shutdown_requested_input):
        pass

if __name__ == "__main__":
    kclprocess = kcl.KCLProcess(RecordProcessor())
    kclprocess.run()
