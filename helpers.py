from uuid import uuid4


def generate_user_data():
    unique_value = uuid4().hex
    return {
        'email': f'ui-bun-tester-{unique_value}@example.com',
        'password': f'password-{unique_value}',
        'name': f'user-{unique_value}',
    }

