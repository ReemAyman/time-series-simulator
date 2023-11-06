# class KafkaSerializer:
#     def __init__(self, generated_data, generator_id, feature_id):
#         self.generated_data = generated_data
#         self.generator_id = generator_id
#         self.feature_id = feature_id
#
#     def serialize(self):
#         serialized_data = []
#         for _, data_instance in self.generated_data.iterrows():
#             serialized_data.append(
#                 {
#                     'attributeId': self.feature_id,
#                     'value': data_instance['value'],
#                     'timestamp': data_instance['timestamp'],
#                     'assetId': self.generator_id
#                 }
#             )
#         return serialized_data
