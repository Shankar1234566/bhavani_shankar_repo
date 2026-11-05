import pytest
from modules.enterprise_module_100 import EnterpriseService100

def test_enterprise_service_100():
    service = EnterpriseService100()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
