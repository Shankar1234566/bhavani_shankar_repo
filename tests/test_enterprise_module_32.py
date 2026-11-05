import pytest
from modules.enterprise_module_32 import EnterpriseService32

def test_enterprise_service_32():
    service = EnterpriseService32()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
