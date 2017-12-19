class ANSIcolor:
	END = '\033[0m'
	def add_attributes(self, args):
		ret = ''
		for item in args:
			ret += '\033[' + str(item) + 'm'
		return ret

	def __init__(self, color='Default', background='Default',
		bold=False, dim=False, italic=False, underline=False, slow_blink=False,
		fast_blink=False, conceal=False, strikethrough=False, font='10', fraktur=False,
		framed=False, encircled=False, overlined=False, ideogram_underline=False, 
		ideogram_double_underline=False, ideogram_overline=False, ideogram_double_overline=False,
		ideogram_stress_marking=False, bright_color=False, bright_background=False):

		self.colors = {'Black' : '30', 'Red' : '31', 'Green' : '32', 'Yellow' : '33', 
		'Blue' : '34', 'Purple' : '35', 'Cyan' : '36', 'White' : '37', 'Default' : '39'}

		self.bright_colors = {'Black' : '90', 'Red' : '91', 'Green' : '92', 'Yellow' : '93', 
		'Blue' : '94', 'Purple' : '95', 'Cyan' : '96', 'White' : '97', 'Default' : '99'}

		self.background_colors = {'Black' : '40', 'Red' : '41', 'Green' : '42', 'Yellow' : '43', 
		'Blue' : '44', 'Purple' : '45', 'Cyan' : '46', 'White' : '47', 'Default' : '49'}

		self.background_bright_colors = {'Black' : '100', 'Red' : '101', 'Green' : '102', 'Yellow' : '103', 
		'Blue' : '104', 'Purple' : '105', 'Cyan' : '106', 'White' : '107', 'Default' : '109'}

		if bright_color:
			colors = self.bright_colors
		else:
			colors = self.colors

		if bright_background:
			background_colors = self.background_colors
		else:
			background_colors = self.background_bright_colors

		args = []

		args.append(colors[color])
		args.append(background_colors[background])
		args.append(font)

		init_args = ['bold', 'dim', 'italic', 'underline', 'slow_blink', 'fast_blink',
			'conceal', 'strikethrough', 'fraktur', 'framed', 'encircled', 'overlined',
			'ideogram_underline', 'ideogram_double_underline', 'ideogram_overline',
			'ideogram_double_overline', 'ideogram_stress_marking']
		init_args_ANSI_codes = [1, 2, 3, 4, 5, 6, 8, 9, 20, 51, 52, 53, 60, 61, 62, 63, 64]
		for arg, code in zip(init_args, init_args_ANSI_codes):
			if vars()[arg]:
				args.append(str(code))

		self.ret = self.add_attributes(args)

	def get(self):
		return self.ret

	def print(self, text):
		print(self.ret + text + self.END)

def colorprint(*text, color='Default', background='Default',
			bold=False, dim=False, italic=False, underline=False, slow_blink=False,
			fast_blink=False, conceal=False, strikethrough=False, font='10', fraktur=False,
			framed=False, encircled=False, overlined=False, ideogram_underline=False, 
			ideogram_double_underline=False, ideogram_overline=False, ideogram_double_overline=False,
			ideogram_stress_marking=False, bright_color=False, bright_background=False):
	print_color = ANSIcolor(color, background, bold, dim, italic, underline, slow_blink, fast_blink,
			conceal, strikethrough, font, fraktur, framed, encircled, overlined, ideogram_underline, 
			ideogram_double_underline, ideogram_overline, ideogram_double_overline,
			ideogram_stress_marking, bright_color, bright_background)
	
	string = ''
	for arg in text:
		string += str(arg) + ' '

	print(print_color.get() + string + print_color.END)

def colorinput(*text, color='Default', background='Default',
			bold=False, dim=False, italic=False, underline=False, slow_blink=False,
			fast_blink=False, conceal=False, strikethrough=False, font='10', fraktur=False,
			framed=False, encircled=False, overlined=False, ideogram_underline=False, 
			ideogram_double_underline=False, ideogram_overline=False, ideogram_double_overline=False,
			ideogram_stress_marking=False, bright_color=False, bright_background=False):
	print_color = ANSIcolor(color, background, bold, dim, italic, underline, slow_blink, fast_blink,
			conceal, strikethrough, font, fraktur, framed, encircled, overlined, ideogram_underline, 
			ideogram_double_underline, ideogram_overline, ideogram_double_overline,
			ideogram_stress_marking, bright_color, bright_background)
	
	string = ''
	for arg in text:
		string += str(arg) + ' '

	return input(print_color.get() + string + print_color.END)