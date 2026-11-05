import pytest
from modules.enterprise_module_104 import EnterpriseService104

def test_enterprise_service_104():
    service = EnterpriseService104()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
