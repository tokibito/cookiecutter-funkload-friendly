from funkload_friendly.test import TestCase, description


class {{ cookiecutter.class_name }}(TestCase):
    @description("Top page")
    def test_top_page(self):
        response = self.get(self.site_url + "/"){% if cookiecutter.example_login == 'yes' %}

    @description("Login to admin site")
    def test_login(self):
        self.get(self.site_url + '/admin/login/')
        response = self.post(self.site_url + '/admin/login/',
            params=[
                ['username', 'example_username'],
                ['password', 'example_password'],
                ['csrfmiddlewaretoken', self.cookie['csrftoken']],
                ['next', '/admin/'],
            ]){% endif %}
