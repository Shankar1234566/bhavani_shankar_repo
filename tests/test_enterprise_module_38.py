import pytest
from modules.enterprise_module_38 import EnterpriseService38

def test_enterprise_service_38():
    service = EnterpriseService38()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
