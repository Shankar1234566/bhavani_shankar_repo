import pytest
from modules.enterprise_module_40 import EnterpriseService40

def test_enterprise_service_40():
    service = EnterpriseService40()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
