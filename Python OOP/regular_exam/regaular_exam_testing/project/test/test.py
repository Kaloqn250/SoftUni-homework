from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.social_media = SocialMedia('SomeName', 'Instagram',
                                         100, 'SomeContent')

    def test_correct__init__(self):
        self.assertEqual('SomeName', self.social_media._username)
        self.assertEqual('Instagram', self.social_media._platform)
        self.assertEqual(100, self.social_media.followers)
        self.assertEqual('SomeContent', self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_followers_when_they_are_less_then_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -1

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_validate_and_set_platform_with_wrong_platform_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = 'BTV'

        expected_message = "Platform should be one of ['Instagram', 'YouTube', 'Twitter']"
        self.assertEqual(expected_message, str(ve.exception))

    def test_create_post_expects_new_post_in_posts_and_correct_message(self):
        result = self.social_media.create_post('SomeContent')

        self.assertEqual("New SomeContent post created by SomeName on Instagram.", result)
        self.assertEqual([{'content': 'SomeContent', 'likes': 0, 'comments': []}], self.social_media._posts)

    def test_like_post_with_invalid_index(self):
        result = self.social_media.like_post(10)

        self.assertEqual("Invalid post index.", result)

    def test_like_post_with_correct_index_and_the_likes_are_below_10(self):
        self.social_media._posts = [{'content': 'SomeContent', 'likes': 0, 'comments': []}]
        result = self.social_media.like_post(0)

        self.assertEqual("Post liked by SomeName.", result)
        self.assertEqual([{'content': 'SomeContent', 'likes': 1, 'comments': []}], self.social_media._posts)

    def test_like_post_with_correct_index_but_likes_has_reached_their_maximum(self):
        self.social_media._posts = [{'content': 'SomeContent', 'likes': 10, 'comments': []}]
        result = self.social_media.like_post(0)

        self.assertEqual("Post has reached the maximum number of likes.", result)
        self.assertEqual([{'content': 'SomeContent', 'likes': 10, 'comments': []}], self.social_media._posts)

    def test_comment_on_post_with_correct_comment(self):
        self.social_media._posts = [{'content': 'SomeContent', 'likes': 0, 'comments': []}]
        result = self.social_media.comment_on_post(0, 'SomeComment')

        self.assertEqual(f"Comment added by SomeName on the post.", result)
        expected_post = [{'content': 'SomeContent', 'likes': 0, 'comments': [{'user': 'SomeName',
                                                                              'comment': 'SomeComment'}]}]
        self.assertEqual(expected_post, self.social_media._posts)

    def test_comment_on_post_with_too_short_comment(self):
        self.social_media._posts = [{'content': 'SomeContent', 'likes': 0, 'comments': []}]
        result = self.social_media.comment_on_post(0, 'SomeComet')

        self.assertEqual("Comment should be more than 10 characters.", result)
        self.assertEqual([{'content': 'SomeContent', 'likes': 0, 'comments': []}], self.social_media._posts)


if __name__ == '__main__':
    main()
