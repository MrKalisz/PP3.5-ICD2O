import os.path
import sys
import PP3_5

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	input_values = ['4']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_5.input = mock_input

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 1\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "12\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "123\n"

def test_q1_4(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "1234\n"

def test_q1_5(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	input_values = ['3']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_5.input = mock_input

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 1\n"

def test_q1_6(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "12\n"

def test_q1_7(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "123\n"

def test_q1_8(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	input_values = ['9']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_5.input = mock_input

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 1\n"

def test_q1_9(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "12\n"

def test_q1_10(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "123\n"

def test_q1_11(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "1234\n"

def test_q1_12(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "12345\n"

def test_q1_13(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "123456\n"

def test_q1_14(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "1234567\n"

def test_q1_15(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "12345678\n"

def test_q1_16(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "123456789\n"

def test_q1_17(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	input_values = ['7']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_5.input = mock_input

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 1\n"

def test_q1_18(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "12\n"

def test_q1_19(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "123\n"

def test_q1_20(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "1234\n"

def test_q1_21(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "12345\n"

def test_q1_22(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "123456\n"

def test_q1_23(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "1234567\n"

def test_q1_24(capsys):

	try:
		exists = os.path.exists("PP3_5.py")
		assert exists
	except:
		sys.exit()

	input_values = ['1']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_5.input = mock_input

	PP3_5.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 1\n"

