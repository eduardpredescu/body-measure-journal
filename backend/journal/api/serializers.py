from rest_framework import serializers
from . import models

class MeasurementSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model = models.Measurement
    fields = ('date', 'weight', 'height', 'weight', 'waist_m', 'bust_m', 'owner',)


class AccountSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=True)
  confirm_password = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = models.Account
    fields = ('email', 'password', 'confirm_password', 'username', 'is_admin',)

  def create(self, validated_data):
    return models.Account.objects.create_user(**validated_data)

  def update(self, instance, validated_data):
    password = validated_data.get('password', None)
    confirm_password = validated_data.get('confirm_password', None)

    if password and password == confirm_password:
      instance.set_password(password)
    for attr, value in validated_data.items():
      if attr == 'password':
        pass
      else:
        setattr(instance, attr, value)
    instance.save()
    return instance


  def validate(self, data):
    '''
    Ensure the passwords are the same
    '''
    if data['password']:
      if data['password'] != data['confirm_password']:
        raise serializers.ValidationError("The passwords have to be the same")
    return data