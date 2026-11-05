import pytest
from modules.enterprise_module_4 import EnterpriseService4

def test_enterprise_service_4():
    service = EnterpriseService4()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
