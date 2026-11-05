import pytest
from modules.enterprise_module_95 import EnterpriseService95

def test_enterprise_service_95():
    service = EnterpriseService95()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
