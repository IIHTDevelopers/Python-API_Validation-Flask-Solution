import unittest
import sys
import os

# Adjust path for Yaksha framework and app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.TestUtils import TestUtils
from app import app

class TestFlaskAPIWithValidation(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.test_obj = TestUtils()

    def test_status_without_job_id_returns_400(self):
        try:
            response = self.client.get("/status")
            result = response.status_code == 400
            self.test_obj.yakshaAssert("TestStatusMissingJobIdReturns400", result, "functional")
            print("TestStatusMissingJobIdReturns400 =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestStatusMissingJobIdReturns400", False, "functional")
            print(f"TestStatusMissingJobIdReturns400 = Failed | Exception: {e}")

    def test_status_invalid_job_id_returns_400(self):
        try:
            response = self.client.get("/status?job_id=unknown")
            result = response.status_code == 400
            self.test_obj.yakshaAssert("TestStatusInvalidJobIdReturns400", result, "functional")
            print("TestStatusInvalidJobIdReturns400 =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestStatusInvalidJobIdReturns400", False, "functional")
            print(f"TestStatusInvalidJobIdReturns400 = Failed | Exception: {e}")

    def test_submit_missing_json_body_returns_400(self):
        try:
            response = self.client.post("/submit", data="non-json", content_type="text/plain")
            result = response.status_code == 400
            self.test_obj.yakshaAssert("TestSubmitMissingJsonBodyReturns400", result, "functional")
            print("TestSubmitMissingJsonBodyReturns400 =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSubmitMissingJsonBodyReturns400", False, "functional")
            print(f"TestSubmitMissingJsonBodyReturns400 = Failed | Exception: {e}")

    def test_submit_missing_job_id_key_returns_400(self):
        try:
            response = self.client.post("/submit", json={})
            result = response.status_code == 400
            self.test_obj.yakshaAssert("TestSubmitMissingJobIdKeyReturns400", result, "functional")
            print("TestSubmitMissingJobIdKeyReturns400 =", "Passed" if result else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSubmitMissingJobIdKeyReturns400", False, "functional")
            print(f"TestSubmitMissingJobIdKeyReturns400 = Failed | Exception: {e}")

if __name__ == '__main__':
    unittest.main()
