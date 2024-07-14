from dataclasses import asdict, dataclass


@dataclass
class InfoMessage:
    """
    Собраны все информационные сообщения приложения.
    """

    min_cook_time: int = 0
    max_cook_time: int = 0
    min_amount: int = 0
    max_amount: int = 0
    recipe_name: str = ''
    tag: str = ''

    def _get_result(self, text_result):
        return text_result.format(**asdict(self))

    @property
    def invalid_hex_code(self):
        text_message = 'Введите валидный шестнадцатеричный цветовой код'
        return self._get_result(text_message)

    @property
    def invalid_min_cook_time(self):
        text_message = f'Время приготовления не может быть меньше {self.min_cook_time}'
        return self._get_result(text_message)

    @property
    def invalid_max_cook_time(self):
        text_message = f'Время приготовления не может быть больше {self.max_cook_time}'
        return self._get_result(text_message)

    @property
    def invalid_min_amount(self):
        text_message = f'Количество не может быть меньше {self.min_amount}'
        return self._get_result(text_message)

    @property
    def invalid_max_amount(self):
        text_message = f'Количество не может быть больше {self.max_amount}'
        return self._get_result(text_message)

    @property
    def invalid_username(self):
        text_message = 'Имя пользователя содержит недопустимые символы'
        return self._get_result(text_message)

    @property
    def invalid_email(self):
        text_message = 'Email должен быть уникальным'
        return self._get_result(text_message)

    @property
    def invalid_username_me(self):
        text_message = 'Использовать имя "me" в качестве username запрещено'
        return self._get_result(text_message)

    @property
    def recipe_whithout_ingredients(self):
        text_message = 'В рецепте должен быть хотя бы один ингредиент'
        return self._get_result(text_message)

    @property
    def recipe_have_identical_ingredients(self):
        text_message = 'В рецепте не может иметь двух одинаковых ингредиентов'
        return self._get_result(text_message)

    @property
    def recipe_exist(self):
        text_message = f'Данный рецепт "{self.recipe_name}" уже существует'
        return self._get_result(text_message)

    @property
    def recipe_have_not_one_tag(self):
        text_message = 'Рецепт должен иметь хотя бы 1 tag'
        return self._get_result(text_message)

    @property
    def tag_not_exist(self):
        text_message = f'Данный tag {self.tag} отсутствует в списке'
        return self._get_result(text_message)

    @property
    def recipe_not_exist(self):
        text_message = f'Данный рецепт "{self.recipe_name}" отсутствует в списке'
        return self._get_result(text_message)

    @property
    def user_selffollow(self):
        text_message = 'Пользователь не может подписаться сам на себя'
        return self._get_result(text_message)

    @property
    def follow_exist(self):
        text_message = 'Нельзя дважды подписаться на одного пользователя'
        return self._get_result(text_message)

    @property
    def follow_not_exist(self):
        text_message = 'Подписка уже удалена, либо не была ранее создана'
        return self._get_result(text_message)

    @property
    def invalid_http_method(self):
        text_message = 'Http-метод не используется'
        return self._get_result(text_message)
