from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    avaible_permissions = {
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_ vendedor': True
    }

class Vendedor (AbstractUserRole):
    avaible_permissions = {
        'realizar_vendas': True
    }