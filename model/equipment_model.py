class EquipmentModel:
    def __init__(self):
        self.equipment = [] 

    def get_all_equipment(self):
        return self.equipment

    def add_equipment(self, equip_type, number, date):
        new_id = len(self.equipment) + 1
        self.equipment.append({"id": new_id, "type": equip_type, "number": number, "date": date})

    def delete_equipment(self, equip_id):
        self.equipment = [e for e in self.equipment if e["id"] != equip_id]
