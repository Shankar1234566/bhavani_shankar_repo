import pytest
from modules.enterprise_module_27 import EnterpriseService27

def test_enterprise_service_27():
    service = EnterpriseService27()
    res = service.execute_handler_1({'test': 'data'})
    assert res['status'] == 'processed'
    assert res['handler'] == 1
