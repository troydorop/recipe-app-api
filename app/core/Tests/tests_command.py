""" 
Test custom Django managemnt commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from Django.db.utils import OperationalError
from Django.test import SimpleTestCase


@patch('core.managment.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self):
        """Test waiting for database if ready."""