# -*- coding: utf-8 -*-
# users/tokens.py
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six    ## IF USING django 3.0 OR > THEN: "import six" ONLY
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()
