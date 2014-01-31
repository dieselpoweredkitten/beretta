import beretta
import unittest


class EncodeTestCase(unittest.TestCase):

  def test_encode_tuple(self):
    bytes = beretta.encode((":call", "Module", "function", [True]))
    self.assertEqual(bytes, b'\x83h\x04d\x00\x04callm\x00\x00\x00'
                            b'\x06Modulem\x00\x00\x00\x08functionl'
                            b'\x00\x00\x00\x01h\x02d\x00\x04bertd'
                            b'\x00\x04truej')

  def test_encode_list(self):
    bytes = beretta.encode([1, 2, False])
    self.assertEqual(bytes, b'\x83l\x00\x00\x00\x03h\x02d\x00\x04'
                            b'bertd\x00\x04truea\x02h\x02d\x00\x04'
                            b'bertd\x00\x05falsej')

  def test_encode_empty_list(self):
    bytes = beretta.encode([])
    self.assertEqual(bytes, b'\x83h\x02d\x00\x04bertd\x00\x03nil')

  def test_encode_true(self):
    bytes = beretta.encode(True)
    self.assertEqual(bytes, b'\x83h\x02d\x00\x04bertd\x00\x04true')

  def test_encode_false(self):
    bytes = beretta.encode(False)
    self.assertEqual(bytes, b'\x83h\x02d\x00\x04bertd\x00\x05false')

  def test_encode_none(self):
    bytes = beretta.encode(None)
    self.assertEqual(bytes, b'\x83h\x02d\x00\x04bertd\x00\tundefined')

  def test_encode_dict(self):
    bytes = beretta.encode({'key': 'value'})
    self.assertEqual(bytes, b'\x83h\x03d\x00\x04bertd\x00\x04dictl'
                            b'\x00\x00\x00\x01h\x02m\x00\x00\x00\x03'
                            b'keym\x00\x00\x00\x05valuej')

  def test_encode_empty_dict(self):
    bytes = beretta.encode({})
    self.assertEqual(bytes, b'\x83h\x03d\x00\x04bertd\x00\x04dictj')
