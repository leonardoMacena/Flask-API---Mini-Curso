
class Service:

  def get_key_from_dict(self, key, data_dict, value_else):
    return data_dict[key] if data_dict[key] else value_else
