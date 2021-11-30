from google.cloud import datastore

datastore_client = datastore.Client()


class Properties:

    @staticmethod
    def get(key, default=None):
        key = datastore_client.key('Property', key)
        retrieved_property = datastore_client.get(key)

        return retrieved_property['value'] or default
