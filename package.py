class Package:
    # space complexity: O(1)    time complexity: O(1)
    def __init__(self, package_id, address, city, state, zipc, deadline, mass_kilo, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipc = zipc
        self.deadline = deadline
        self.mass_kilo = mass_kilo
        self.special_notes = special_notes
        self.status = "AT_HUB"
        self.delivery_time = "00:00:00"

    # space complexity: O(1)    time complexity: O(1)
    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.state, self.zipc,
            self.deadline, self.mass_kilo, self.special_notes, self.status, self.delivery_time)

