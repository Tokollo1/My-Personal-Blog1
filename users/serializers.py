from rest_framework import serializers

from .models import *

class UserSerailizer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'