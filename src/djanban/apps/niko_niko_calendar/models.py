# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# Each one of the mood measurements for each member
class DailyMemberMood(models.Model):

    MOOD_CHOICES = (
        ("normal", ":-|"),
        ("happy", ":-)"),
        ("sad", ":-(")
    )

    member = models.ForeignKey("members.Member", verbose_name=u"Member", related_name="daily_member_moods")

    date = models.DateField(verbose_name="Date of mood measurement")

    mood = models.CharField(verbose_name=u"Mood of a member after one particular day", max_length=16,
                            choices=MOOD_CHOICES, default="normal")

    @property
    def mood_value(self):
        if self.mood == "normal":
            return 0
        if self.mood == "happy":
            return 1
        if self.mood == "sad":
            return -1
        raise ValueError(u"This choice does not exist")
