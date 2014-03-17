def what_is_my_sign(day, month):
	d_m = month * 40 + day
	if d_m >= 141 and d_m <= 180:
		return "aries"
	if d_m >= 181 and d_m <= 221:
		return "Taurus"
	if d_m >= 222 and d_m <= 261:
		return "Gemini"
	if d_m >= 262 and d_m <= 302:
		return "Cancer"
	if d_m >= 303 and d_m <= 342:
		return "Leo"
	if d_m >= 343 and d_m <= 383:
		return "Virgo"
	if d_m >= 389 and d_m <= 423:
		return "Libra"
	if d_m >= 424 and d_m <= 462:
		return "Scorpio"
	if d_m >= 463 and d_m <= 501:
		return "Sigittarius"
	if (d_m >= 502 and d_m <= 511) or (d_m >= 0 and d_m <= 60):
		return "Capricorn"
	if d_m >= 61 and d_m <= 99:
		return "Aquarius"
	if d_m >= 100 and d_m <= 140:
		return "Pisces"

