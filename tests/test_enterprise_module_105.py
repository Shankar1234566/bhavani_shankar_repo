import pytest
from modules.enterprise_module_105 import EnterpriseService105

def test_enterprise_service_105():
    service = EnterpriseService105()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
