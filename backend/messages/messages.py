from dataclasses import asdict, dataclass


@dataclass
class InfoMessage:
    """
    Собраны все информационные сообщения приложения.
    """

    min_stars: int = 0
    max_stars: int = 0

    def _get_result(self, text_result):
        return text_result.format(**asdict(self))

    @property
    def invalid_min_stars(self):
        text_message = f'Количество звезд не может быть меньше {self.min_stars}'
        return self._get_result(text_message)

    @property
    def invalid_max_stars(self):
        text_message = f'Количество звезд не может быть больше {self.max_stars}'
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
    def invalid_http_method(self):
        text_message = 'Http-метод не используется'
        return self._get_result(text_message)
