from django.test import TestCase

# Create your tests here.
import json

from django.test import Client


class TestViews(TestCase):
    def setUp(self):
        print('setup')
        c = Client()
        self.user = []
        fp = open('media/test.jpg', 'rb')
        # create 4 users
        response = c.post('/create_user/', {'digits_id': 1, 'name': 'Sampat Laal', 'phone': '9911111111', 'photo': fp,
                                            'email': 'yederese@storyboard.co'})
        self.user.append(response.json()['data'])

        response = c.post('/create_user/', {'digits_id': 2, 'name': 'Sarweshwar Dayal Saxena', 'phone': '9922222222', 'photo': fp,
                                            'email': 'ramdhari_singh_dinkar@storyboard.co'})
        self.user.append(response.json()['data'])

        response = c.post('/create_user/', {'digits_id': 3, 'name': 'Badshaah', 'phone': '9933333333', 'photo': fp,
                                            'email': 'don_kabir_khan@storyboard.co'})
        self.user.append(response.json()['data'])

        response = c.post('/create_user/', {'digits_id': 4, 'name': 'Rekha Mishra', 'phone': '9944444444', 'photo': fp,
                                            'email': 'rekha_bindu@storyboard.co'})
        self.user.append(response.json()['data'])

        c.post('/create_hifi/', {
            'lat': '28.0198', 'lng': "-82.739817", 'location': "rr", 'post': 'hello all',
            'hf_userids': self.user[0]['userid']
        })

        response = c.post('/create_hifi/', {
            'lat': '28.0198', 'lng': "-82.739817", 'location': "rr",
            'post': 'hello all', 'hf_userids': ",".join([str(k['userid']) for k in self.user])
        })
        fp.close()
        r = response.json()
        self.post = r['data']

    def test_request_methods(self):
        print('test request methods')
        c = Client()
        response = c.get('/verify_user/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/create_user/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/home/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/create_hifi/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/sent_hifi/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/delete_hifi/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/delete_sent_hifi/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/block_user/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/unblock_user/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/report_hifi/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/update_user_profile/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.post('/logout/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be GET')
        response = c.get('/contact_sync/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')
        response = c.get('/update_user_location/')
        self.assertEqual(response.json()['message'], 'Incorrect request method, should be POST')

    def test_create_user(self):
        print('test_create_user')

        c = Client()
        digid = "b"
        name = "test name"
        phone = "9423094803"
        fp = open('media/test.jpg', 'rb')
        response = c.post('/create_user/', {'digits_id': digid, 'name': name, 'phone': phone, 'photo': fp,
                                            'email': 'anshuman@storyboard.co'})
        fp.close()
        self.assertEqual(response.status_code, 200)
        r = json.loads(response.content.decode())
        self.assertEqual(r.get('message'), "User created")
        self.assertEqual(r.get('status'), True)
        self.assertEqual(r.get('code'), 200)

        user = r.get('data')
        self.assertEqual(user.get('phone'), phone)
        self.assertEqual(user.get('digits_id'), digid)
        self.assertEqual(user.get('name'), name)
        self.assertIsNotNone(user.get('avatar'))

