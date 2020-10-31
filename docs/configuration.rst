=============
Configuration
=============

Available settings:


UidModelMixin
=============

UID_FIELD_SALT (="settings.SECRET_KEY")
  Specifies the salt to use for the hashid in the  `uid` field

UID_HASH_MIN_LENGTH (="4")
  Minimum length for the `uid` field

UID_HASH_FORMAT (=['lower', 'upper', 'number'])
  The format to be used for the `uid` field hash alphabet.  Corresponds to equivalent key in the UID_HASH_ALPHABETS setting.

UID_HASH_ALPHABETS (={'lower': 'abcdefghijklmnopqrstuvwxyz','upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','number': '1234567890',})
  Alphabets to be used in the `uid` field format.

UID_HASH_ALPHABET (=UID_HASH_FORMAT)
  The resolved alphabet to be used for the  `uid` field hash.
