from django.test import TestCase, Client

# Create your tests here.

from .models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='test',
            sex=1,
            email='333@dd.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='test1',
            sex=1,
            email='333@dd.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟展示不一致！')

    def test_filter(self):
        student = Student.objects.create(
            name='test2',
            sex=1,
            email='333@dd.com',
            profession='主任',
            qq='3333',
            phone='32222',
        )
        name = 'test'  # 前面setUp()创建过
        students = Student.objects.filte::r(name=name)
        self.assertEqual(students.count(), 1, '存在一个名为{}的记录'.format(name))

    def test_get_index(self):
        client = Client()  # 创建一个客户端
        response = client.get('/')   #模拟客户端访问首页
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='333@dd.com',
            profession='副主任',
            qq='3333',
            phone='32222',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        # 不是精确匹配，test_for_post的一部分也可以通过测试
        self.assertTrue(b'test_for' in response.content, 'response content must contain `test_for_post`')