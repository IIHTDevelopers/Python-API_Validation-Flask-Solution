import unittest
import sys
import os

# Adjust path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.TestUtils import TestUtils
from app import app  

class TestFlaskAPIWithoutValidation(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.test_obj = TestUtils()

    def test_status_without_job_id_returns_500(self):
        try:
            response = self.client.get("/status")
            result = response.status_code == 500
            self.test_obj.yakshaAssert("TestStatusMissingJobIdReturns500", result, "functional")
            print("TestStatusMissingJobIdReturns500 =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestStatusMissingJobIdReturns500", False, "functional")
            print(f"TestStatusMissingJobIdReturns500 = Failed | Exception: {e}")

    def test_submit_without_json_returns_500(self):
        try:
            response = self.client.post("/submit", data="not-json", content_type="text/plain")
            result = response.status_code == 500
            self.test_obj.yakshaAssert("TestSubmitWithInvalidJsonReturns500", result, "functional")
            print("TestSubmitWithInvalidJsonReturns500 =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSubmitWithInvalidJsonReturns500", False, "functional")
            print(f"TestSubmitWithInvalidJsonReturns500 = Failed | Exception: {e}")

    def test_submit_without_job_id_returns_500(self):
        try:
            response = self.client.post("/submit", json={})
            result = response.status_code == 500
            self.test_obj.yakshaAssert("TestSubmitMissingJobIdReturns500", result, "functional")
            print("TestSubmitMissingJobIdReturns500 =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSubmitMissingJobIdReturns500", False, "functional")
            print(f"TestSubmitMissingJobIdReturns500 = Failed | Exception: {e}")
    def test_submit_with_invalid_json_returns_500(self):
        try:
            response = self.client.post("/submit", data="not-json", content_type="text/plain")
            result = response.status_code == 500
            self.test_obj.yakshaAssert("TestSubmitWithInvalidJsonReturns500", result, "functional")
            print("TestSubmitWithInvalidJsonReturns500 =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSubmitWithInvalidJsonReturns500", False, "functional")
            print(f"TestSubmitWithInvalidJsonReturns500 = Failed | Exception: {e}")
