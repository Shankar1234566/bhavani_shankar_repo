import pytest
from modules.enterprise_module_18 import EnterpriseService18

def test_enterprise_service_18():
    service = EnterpriseService18()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
