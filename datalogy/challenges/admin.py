from django.contrib import admin
from challenges.models import Challenge, Challenger, Submission
admin.site.register(Challenge)
admin.site.register(Challenger)
admin.site.register(Submission)
