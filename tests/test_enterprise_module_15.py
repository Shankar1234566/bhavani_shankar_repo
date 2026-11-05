import pytest
from modules.enterprise_module_15 import EnterpriseService15

def test_enterprise_service_15():
    service = EnterpriseService15()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
