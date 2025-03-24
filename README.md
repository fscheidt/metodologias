# Metodologias de Desenvolvimento de Software

<details>
<summary>DISCIPLINA</summary>

- **[AVA](https://ava.ifpr.edu.br/course/view.php?id=13094)**
- Curso: TADS
- Período: 5°
- Horário: segunda, 19:00 às 22:20 (Lab 1)
- Período letivo: 2025/1
- Período aulas: 10/03/25 à jul/25
- **[Repositório](https://github.com/fscheidt/metodologias)**

</details>

---

## Aula 3 - Teste parametrizado

### (1) Teste básico

#### Função alvo do teste

> **`generate_passwd.py`**

```python
import hashlib

def encrypt_password(password):
    password_bytes = password.encode('utf-8')
    sha1_hash = hashlib.sha1(password_bytes)
    encrypted_password = sha1_hash.hexdigest()
    return encrypted_password
```

#### Teste

> **`test_password.py`**

```python
data = [
    ("password123", "cbfdac6008f9cab4083784cbd1874f76618d2a97"),
    ("1234", "7110eda4d09e062aa5e4a390b0a572ac0d2c0220"),
]
class TestPassword:

    def test_sha1_item(self):        
        password = "1234"
        encrypted = "7110eda4d09e062aa5e4a390b0a572ac0d2c0220"
        result = encrypt_password(password)
        assert result == encrypted

```


### (2) Teste parametrizado

Usando: `@pytest.mark.parametrize()`

#### `passwords.csv`

Atenção ao segundo password:

```
password,encrypted
1234,7110eda4d09e062aa5e4a390b0a572ac0d2c0220
password124,cbfdac6008f9cab4083784cbd1874f76618d2a97
admin123,f865b53623b121fd34ee5426c792e5c33af8c227
qwerty,b1b3773a05c0ed0176787a4f1574ff0075f7521e
abc123,6367c48dd193d56ea7b0baad25b19455e529f5ee
111111,3d4f2bf07dc1be38b20cd6e46949a1071f9d0e3d
football,2d27b62c597ec858f6e7b54e7e58525e6a95e6d8
monkey,ab87d24bdc7452e55738deb5f868e1f16dea5ace
123456,7c4a8d09ca3762af61e59520943dc26494f8941b
admin,d033e22ae348aeb5660fc2140aec35850c4da997
user,12dea96fec20593566ab75692c9949596833adc9
login,2736fab291f04e69b62d490c3c09361f5b82461a
access,0f12541afcce175fb34bb05a79c95b76e765488b
root,dc76e9f0c0006e8f919e0c515c66dbba3982f785
god,21298df8a3277357ee55b01df9530b535cf08ec1
master,4f26aeafdb2367620a393c973eddbe8f8b846ebd
superuser,8e67bb26b358e2ed20fe552ed6fb832f397a507d
guest,35675e68f4b5af7b995d9205ad0fc43842f16450
changeme,fa9beb99e4029ad5a6615399e7bbae21356086b3
```

#### Teste

> **`test_csv_passwd.py`**

```python
def csv_data():
    """ helper function """
    data = []
    file_name = "passwords.csv"
    file_path = Path(__file__).parent / file_name
    with Path.open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append((row['password'], row['encrypted']))
        return data
```

> pytest **decorator:**

```python
@pytest.mark.parametrize("password,encrypted",csv_data())
```

---

## Aula 2 - Teste unitário
- assert
- execução de testes com pytest

Configuração do ambiente virtual:
```bash
python3 -m venv env
source env/bin/activate
pip install pytest
```

Executar teste usando pytest:

```console
pytest -v
```

