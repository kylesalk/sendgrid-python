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

    def test_campaign_get(self):
        data = {
            "categories": [
                "summer line"
            ],
            "custom_unsubscribe_url": "test.url",
            "editor": "code",
            "html_content": "<html><head><title></title></head><body><p>Check out our summer line!</p></body></html>",
            "ip_pool": "test_ips",
            "list_ids": [2, 3],
            "plain_content": "Check out our summer line!",
            "segment_ids": [2, 3],
            "sender_id": 4324,
            "subject": "New Products for Summer!",
            "title": "May Newsletter",
            "suppression_group_id": 5123
        }
        camp = Campaign(**data)
        self.assertDictEqual(camp.get(), data)

    def test_campaign_patch(self):
        data = {
            "categories": [
                "summer line"
            ],
            "html_content": "<html><head><title></title></head><body><p>Check out our summer line!</p></body></html>",
            "plain_content": "Check out our summer line!",
            "subject": "New Products for Summer!",
            "title": "May Newsletter"
        }
        camp = Campaign(**data)
        new_data = {
            "categories": [
                "fall line"
            ],
            "html_content": "<html><head><title></title></head><body><p>Check out our summer line!</p></body></html>",
            "plain_content": "Check out our summer line!",
            "subject": "New Products for Fall!",
            "title": "August Newsletter"
        }
        self.assertDictEqual(camp.patch(**new_data), new_data)

    def test_campaign_copy(self):
        data = {
            "plain_content": "Check out our summer line!",
            "subject": "New Products for Summer!",
            "title": "May Newsletter"
        }
        camp = Campaign(**data)
        camp2 = camp.copy("June Newsletter")
        self.assertEqual(camp.subject, camp2.subject)
        self.assertEqual(camp.plain_content, camp2.plain_content)
        self.assertNotEqual(camp.title, camp2.title)


class TestCampaignsObject(unittest.TestCase):

    def test_campaigns_get(self):
        lim = 5
        offset = 20
        camps = Campaigns(offset=offset, limit=lim)
        self.assertEqual(camps.get(), {"offset": offset, "limit": lim})

    def test_campaigns_props(self):
        lim = 5
        offset = 20
        camps = Campaigns(offset=offset, limit=lim)
        self.assertEqual(camps.offset, offset)
        self.assertEqual(camps.limit, lim)


class TestScheduleObject(unittest.TestCase):

    def test_components_to_timestamp(self):
        schedule = Schedule(year=2018, month=12, day=1, hour=8, minute=23)
        t_delta = datetime(2018, 12, 1, 8, 23) - datetime(1970, 1, 1)
        unix_timestamp = t_delta.seconds + t_delta.days * 86400
        self.assertEqual(schedule.timestamp, unix_timestamp)
        self.assertDictEqual(schedule.get(), {"send_at": unix_timestamp})

    def test_timestamp_to_dt(self):
        td = datetime(2018, 12, 1, 8, 23) - datetime(1970, 1, 1)
        timestamp = td.seconds + td.days * 86400
        schedule = Schedule(send_at=timestamp)
        self.assertEqual(schedule.year, 2018)
        self.assertEqual(schedule.month, 12)
        self.assertEqual(schedule.day, 1)
        self.assertEqual(schedule.hour, 8)
        self.assertEqual(schedule.minute, 23)

    def test_dt_to_timestamp(self):
        schedule = Schedule(datetime(2018, 12, 1, 8, 23))
        t_delta = datetime(2018, 12, 1, 8, 23) - datetime(1970, 1, 1)
        unix_timestamp = t_delta.seconds + t_delta.days * 86400
        self.assertEqual(schedule.timestamp, unix_timestamp)


if __name__ == "__main__":
    unittest.main()
