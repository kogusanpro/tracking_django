from django.test import TestCase
from trackapp.models import Tracks


# 必要なテストケース
"""
: DBの中身確認
: URLに紐づくHTMLファイルが正しくレンダリングされているか
: 入力項目のフォーマットチェック
: 参考文献　https://nwpct1.hatenablog.com/entry/how-to-write-unittest-on-django
"""

# Create your tests here.
class ScraypingTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_db_confirmation(self) -> None:
        """
        デフォルトではDBが空の確認
        :return:
        """
        saved_tracks = Tracks.objects.all()
        self.assertEqual(saved_tracks.count(), 0)

    def test_form_invalid_format(self):
        """
         URL入力項目にて、http形式でない入力を行えばエラーになることを検証
        :return
        """
        pass
    
    def test_form_correct_format(self):
        """
         正常な入力を行えばエラーにならないことを検証
        :return
        """
