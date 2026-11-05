import pytest
from modules.enterprise_module_8 import EnterpriseService8

def test_enterprise_service_8():
    service = EnterpriseService8()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
