from django.contrib import admin
from challenges.models import Challenge, Challenger, Submission, ChallengeAdmin
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Challenger)
admin.site.register(Submission)
