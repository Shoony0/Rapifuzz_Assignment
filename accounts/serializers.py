import datetime
import random
from accounts.models import LOGIN_TYPE, Incident, User, INCIDENT_PRIORITY, INCIDENT_STATUS
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'email', 
            'password', 
            'login_type',
            'address',
            'country',
            'state',
            'city',
            'pincode',
            'mobile_number_code',
            'mobile_number',
            'fax',
            'phone',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data["username"]=validated_data["email"]
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class RegisterIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('name', 'priority', 'details',)
    
    def create(self, validated_data):
        validated_data["id"]=f"RMG{random.randint(10000, 99999)}{datetime.date.today().year}"
        validated_data['user'] = self.context['request'].user
        incident = Incident(**validated_data)
        incident.save()
        return incident

class ViewIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('name', 'priority', 'details',)
    
    def create(self, validated_data):
        validated_data["id"]=f"RMG{random.randint(10000, 99999)}{datetime.date.today().year}"
        validated_data['user'] = self.context['request'].user
        incident = Incident(**validated_data)
        incident.save()
        return incident

class ViewIncidentSerializer(serializers.ModelSerializer):
    login_type = serializers.SerializerMethodField()
    priority = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    reporter_user = serializers.SerializerMethodField()
    class Meta:
        model = Incident
        fields = ('id', 'name', 'login_type', 'priority', 'reporter_user', 'details', 'status', 'created_at', 'updated_at',)  # adjust fields as needed

    def get_login_type(self, instance):
        return dict(LOGIN_TYPE)[instance.user.login_type]
    
    def get_priority(self, instance):
        return dict(INCIDENT_PRIORITY)[instance.priority]
    
    def get_status(self, instance):
        return dict(INCIDENT_STATUS)[instance.status]
    
    def get_reporter_user(self, instance):
        return instance.user.get_full_name()

class GetIncidentSerializer(serializers.ModelSerializer):
    login_type = serializers.SerializerMethodField()
    priority = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    reporter_user = serializers.SerializerMethodField()
    class Meta:
        model = Incident
        fields = ('id', 'name', 'priority', 'reporter_user', 'login_type','details', 'status', 'created_at', 'updated_at',)  # adjust fields as needed
    

    def get_login_type(self, instance):
        return dict(LOGIN_TYPE)[instance.user.login_type]
    
    def get_priority(self, instance):
        return dict(INCIDENT_PRIORITY)[instance.priority]
    
    def get_status(self, instance):
        return dict(INCIDENT_STATUS)[instance.status]
    
    def get_reporter_user(self, instance):
        return instance.user.get_full_name()
    
class UpdateIncidentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ('status',)  # adjust fields as needed

    def validate(self, data):
        pk = self.context["request"].parser_context["kwargs"]["pk"]
        user = self.context['request'].user  # get the authenticated user
        # Custom validation logic
        if Incident.objects.filter(id=pk, status=2, user=user).exists() and "status" in data.keys():
            raise serializers.ValidationError("This Incident Already Closed. / It cannot be editable.")
        return data
    
class ForgotPasswordSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('password', 'message',)  # adjust fields as needed
        extra_kwargs = {'password': {'write_only': True}}

    def get_message(self, instance):
        return "Password Updated Sucessfully."

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance

    
