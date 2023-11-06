class TimeSeriesKafkaMessage:
    def __init__(self, attributeId, value, timestamp, assetId):
        self.attributeId = attributeId
        self.value = value
        self.timestamp = timestamp
        self.assetId = assetId

    def __dict__(self):
        return {
            'attributeId': self.attributeId,
            'value': str(self.value),
            'timestamp': str(self.timestamp),
            'assetId': self.assetId
        }
