import pytest
from modules.enterprise_module_6 import EnterpriseService6

def test_enterprise_service_6():
    service = EnterpriseService6()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
