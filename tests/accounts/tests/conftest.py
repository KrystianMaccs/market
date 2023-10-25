import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture(autouse=True)
def user():
    return User.objects.create(
        username="testuser",
        first_name="John",
        last_name="Doe",
        email="testuser@gmail.com",
        is_staff=False,
        is_active=True,
    )

