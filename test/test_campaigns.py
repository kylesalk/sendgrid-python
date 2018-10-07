# -*- coding: utf-8 -*-

from datetime import datetime
from sendgrid.helpers.campaigns import *
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestCampaignObject(unittest.TestCase):

    def test_set_title(self):
        c_name = "Test Campaign"
        camp = Campaign(title=c_name)
        self.assertEqual(camp.title, "Test Campaign")


class TestScheduleObject(unittest.TestCase):

    def test_components_to_timestamp(self):
        schedule = Schedule(year=2018, month=12, day=1, hour=8, minute=23)
        unix_timestamp = int((datetime(2018, 12, 1, 8, 23) - datetime(1970, 1, 1)).seconds)
        self.assertEqual(schedule.timestamp, unix_timestamp)

    def test_timestamp_to_dt(self):
        schedule = Schedule(send_at=int((datetime(2018, 12, 1, 8, 23) - datetime(1970, 1, 1)).seconds))
        self.assertEqual(schedule.year, 2018)
        self.assertEqual(schedule.month, 12)
        self.assertEqual(schedule.day, 1)
        self.assertEqual(schedule.hour, 8)
        self.assertEqual(schedule.minute, 23)

    def test_dt_to_timestamp(self):
        schedule = Schedule(datetime(2018, 12, 1, 8, 23))
        unix_timestamp = (datetime(2018, 12, 1, 8, 23) - datetime(1970, 1, 1)).total_seconds()
        self.assertEqual(schedule.timestamp, unix_timestamp)


if __name__ == "__main__":
    unittest.main()