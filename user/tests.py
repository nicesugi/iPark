from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from user.models import Region as RegionModel


# 회원가입 테스트
class UserRegistrationTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.region = RegionModel.objects.bulk_create([RegionModel(region_name="강남구"),
                                                      RegionModel(region_name="강동구"),
                                                      RegionModel(region_name="강북구")])

    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "username" : "user10",
            "password" : "1010abc!",
            "fullname" : "user10",
            "email" : "user10@gmail.com",
            "phone" : "010-1010-1010",
            "birthday" : "2022-07-13",
            "region" : 2
        }
        
        response = self.client.post(url, user_data)

        self.assertEqual(response.status_code, 200)