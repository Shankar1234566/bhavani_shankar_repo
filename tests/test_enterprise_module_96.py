import pytest
from modules.enterprise_module_96 import EnterpriseService96

def test_enterprise_service_96():
    service = EnterpriseService96()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
