from django.db import models


class EquipmentType(models.Model):
    name = models.CharField(max_length=128)
    sn_mask = models.CharField(max_length=10)

class Equipment(models.Model):
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    serial_number = models.CharField(unique=True, max_length=10)
    note = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()

