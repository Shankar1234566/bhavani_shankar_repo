import pytest
from modules.enterprise_module_22 import EnterpriseService22

def test_enterprise_service_22():
    service = EnterpriseService22()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
