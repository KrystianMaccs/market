import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

@pytest.mark.django_db
def test_user_get_full_name(user):
    full_name = user.get_full_name
    
    assert full_name == "John Doe"