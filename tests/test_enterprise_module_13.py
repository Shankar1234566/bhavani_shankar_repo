import pytest
from modules.enterprise_module_13 import EnterpriseService13

def test_enterprise_service_13():
    service = EnterpriseService13()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
