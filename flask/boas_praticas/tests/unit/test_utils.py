from unittest.mock import patch
import pytest
from src.utils import eleva_quadrado, requires_role, HTTPStatus


@pytest.mark.parametrize("test_input,expected", [(2, 4), (10, 100), (3, 9)])
def test_eleva_quadrado_sucesso(test_input, expected):
    resultado = eleva_quadrado(test_input)
    assert resultado == expected


# def test_eleva_quadrado_falha():
#    resultado = eleva_quadrado("a")
#    assert resultado == "aa"


def test_requires_role(mocker):
    mock_user = mocker.Mock()
    mock_user.role.name = "admin"

    mocker.patch("src.utils.get_jwt_identity") 
    mocker.patch("src.utils.db.get_or_404", return_value=mock_user) 

    decorated_function = requires_role("admin")(lambda: "success")
    result = decorated_function()

    assert result == "success"


'''   def test_requires_role_fail(mocker):
        mock_user = mocker.Mock()
        mock_user.role.name = "normal"

        mocker.patch("src.utils.get_jwt_identity") 
        mocker.patch("src.utils.db.get_or_404", return_value=mock_user)

        decorated_function = requires_role("admin")(lambda: "success")
        result = decorated_function()

        assert result == ({"messege": "User dont have access"}, HTTPStatus.FORBIDDEN) '''
