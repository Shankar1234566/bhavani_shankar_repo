import pytest
from modules.enterprise_module_23 import EnterpriseService23

def test_enterprise_service_23():
    service = EnterpriseService23()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
