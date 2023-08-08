import med_system
import unittest
from unittest.mock import Mock

class TestMedSystem(unittest.TestCase):
    def setUp(self):
        self.med_system = med_system.MedicalSystem()
        self.patient_1 = med_system.Patient("John", 30, "male", ["cold", "diabet"])
        self.patient_1.add_new_appointment("Monday, 8-30am")

    def test_add_new_appointment(self):
        mock_appointments = Mock()
        mock_appointments.return_value = ["Monday, 8-30am", "Tuesday, 6-30pm"]
        self.patient_1.add_new_appointment("Tuesday, 6-30pm")
        self.assertEqual(mock_appointments(), self.patient_1.appointments )

    def test_remove_appointment(self):
        mock_appointment = Mock()
        mock_appointment.return_value = []
        self.patient_1.remove_appointment("Monday, 8-30am")
        self.assertEqual(mock_appointment(), self.patient_1.appointments)


unittest.main()