from apps.users.application.use_cases import LoginUser

class FakeUser:
    def __init__(self, email, password=None, username=None):
        self.email = email
        self.password = password
        self.username = username
        self.is_authenticated = True

class FakeUserRepo:
    def __init__(self):
        self.users = {}
        
    def create_user(self, email, password, username):
        user = FakeUser(email, password, username)
        self.users[email] = user
        return user
        
    def authenticate_user(self, email, password):
        user = self.users.get(email)
        if user and user.password == password:
            return user
        return None

def test_login_user():
    # Initial test setup
    repo = FakeUserRepo()
    use_case = LoginUser(repo)
    
    # Create a test user
    test_email = "test@example.com"
    test_password = "secure123"
    repo.create_user(test_email, test_password, "testuser")
    
    # Test successful login
    result = use_case.execute(test_email, test_password)
    assert result.success is True
    assert result.user.email == test_email
    
    # Test failed login - wrong password
    result = use_case.execute(test_email, "wrongpassword")
    assert result.success is False
    assert result.error == "Invalid credentials"
    
    # Test failed login - user not found
    result = use_case.execute("nonexistent@example.com", test_password)
    assert result.success is False
    assert result.error == "Invalid credentials"

def test_authenticate_user():
    # Initial setup
    repo = FakeUserRepo()
    
    # Create test users
    test_email = "test@example.com"
    test_password = "secure123"
    test_username = "testuser"
    
    user = repo.create_user(test_email, test_password, test_username)
    
    # Test successful authentication
    authenticated_user = repo.authenticate_user(test_email, test_password)
    assert authenticated_user is not None
    assert authenticated_user.email == test_email
    assert authenticated_user.username == test_username
    
    # Test failed authentication - wrong password
    wrong_password_result = repo.authenticate_user(test_email, "wrongpassword")
    assert wrong_password_result is None
    
    # Test failed authentication - user not found
    non_existent_user_result = repo.authenticate_user("nonexistent@example.com", test_password)
    assert non_existent_user_result is None
