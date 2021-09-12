# HashTable class using chaining.
class HashTable:
    """Constructor with optional initial capacity parameter."""

    def __init__(self, initial_capacity=10):
        """initialize the hash table with empty bucket list entries.

        Space Complexity O(1)
        Time Complexity O(1)
        :param initial_capacity: number of buckets
        """
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        """insert and update item

        Space Complexity O(N)
        Time Complexity O(N)
        :param key: item index
        :param item: item
        :return: True
        """
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def get(self, key):
        """lookup function for a given key

        Space Complexity O(N)
        Time Complexity O(N)
        :param key: item index
        :return: None
        """
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # value
        return None

    def remove(self, key):
        """remove item from hash table for a given key

        :param key: item index
        """
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])