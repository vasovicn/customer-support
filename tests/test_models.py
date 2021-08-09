from django.test import TestCase
from CustomerSupport.models import Ticket


class TicketModeltest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Ticket.objects.create(name='John Doe', email='test@test.com', subject='Test subject', problem='Test problem')

    def test_ticket_subject(self):
        ticket = Ticket.objects.get(id=1)
        expected_subject = f'{ticket.subject}'
        self.assertEqual(str(ticket), expected_subject)