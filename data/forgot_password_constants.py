from faker import Faker

faker = Faker()


class ForgotPasswordConstants:
    FORGOT_PASS_URL = "https://stellarburgers.nomoreparties.site/forgot-password"
    EMAIL = faker.email()
