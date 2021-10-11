# Chaining Hash Table Class
# Handles hash collisions by storing a bucket_list in each bucket and
# appends hash collisions to the end of each bucket_list
class ChainingHashTable:
    # Chaining Hash Table Constructor; optional bucket number parameter(default 10 buckets).
    # On init, initialize bucket_number buckets with an empty list.
    def __init__(self, bucket_number=10):
        # Init hash_table as empty list, append empty list to each bucket
        self.hash_table = []
        for i in range(bucket_number):
            self.hash_table.append([])

    # Probes the Hash Table; If key found, value is updated; If key not found, key and value are inserted
    # Bucket determined by a hash of the key modulo the length of the hash_table
    # space complexity: O(n)    time complexity: O(n)
    def insert(self, key, value):
        # Get the list of [key, value] pairs in the desired bucket and store in bucket_list
        # As a Chaining Hash Table implementation, if a collision occurs (i.e. two different
        # [key, value] pairs being stored in the same bucket), the provided [key, value] pair
        # is appended to the end of the bucket_list stored in the bucket
        bucket = hash(key) % len(self.hash_table)
        bucket_list = self.hash_table[bucket]

        # Search for [key, value] pair in bucket list; If key present, update value
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = value
                return True

        # If [key, value] not present in determined bucket_list, append [key, value] to bucket_list
        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Searches Hash Table for a value with an associated key
    # If found, the value is returned; if not, Empty is returned
    # space complexity: O(n)    time complexity O(n)
    def lookup(self, key):
        # Get the bucket_list where the key would be stored, if present
        bucket = hash(key) % len(self.hash_table)
        bucket_list = self.hash_table[bucket]

        # Copy the bucket list to prevent unintended synchronization errors
        copy_list = bucket_list[:]

        # Search for the key in the copied list; if present, return value
        for key_value in copy_list:
            if key_value[0] == key:
                return key_value[1]

        # Key not found, return none
        return None

    # Remove from the Hash Table a [key, value] pair matching the provided key
    # space complexity: O(n)    time complexity: O(n)
    def remove(self, key):
        # Get the bucket_list for the [key, value] associated to the provided key
        bucket = hash(key) % len(self.hash_table)
        bucket_list = self.hash_table[bucket]

        # Search for the key in the associated list; if present, remove the [key, value]
        # pair from the list
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
